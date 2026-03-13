/**
 * @file state_estimator.cpp
 * @brief Sentient-SONIC State Estimator Implementation
 *
 * Kalman filter-based state estimation fusing IMU and contact data.
 *
 * Copyright (c) 2026 Sentient Robotics
 * Licensed under Apache License 2.0
 */

#include "sentient_sonic/state_estimator.h"

#include <cmath>

namespace sentient {
namespace sonic {

StateEstimator::StateEstimator() {
    reset();
}

void StateEstimator::update(const IMUData& imu, const ContactState& contacts,
                            const Eigen::VectorXf& joint_pos,
                            const Eigen::VectorXf& joint_vel) {
    base_orientation_ = imu.orientation;
    base_angular_vel_ = imu.angular_velocity;

    // Simple complementary filter for velocity estimation
    // In production, this would be a full EKF
    Eigen::Matrix3f R = Eigen::Quaternionf(
        base_orientation_[0], base_orientation_[1],
        base_orientation_[2], base_orientation_[3]
    ).toRotationMatrix();

    gravity_projected_ = R.transpose() * Eigen::Vector3f(0, 0, -9.81);

    // Integrate acceleration for velocity (simplified)
    Eigen::Vector3f acc_world = R * (imu.acceleration - gravity_projected_);
    base_linear_vel_ += acc_world * 0.002f;  // dt = 2ms

    // Contact-based velocity correction
    if (contacts.left_foot || contacts.right_foot) {
        base_linear_vel_ *= 0.99f;  // Damping when in contact
    }

    base_position_ += base_linear_vel_ * 0.002f;
}

Eigen::Vector3f StateEstimator::get_base_position() const { return base_position_; }
Eigen::Vector4f StateEstimator::get_base_orientation() const { return base_orientation_; }
Eigen::Vector3f StateEstimator::get_base_linear_velocity() const { return base_linear_vel_; }
Eigen::Vector3f StateEstimator::get_base_angular_velocity() const { return base_angular_vel_; }
Eigen::Vector3f StateEstimator::get_projected_gravity() const { return gravity_projected_; }

void StateEstimator::reset() {
    base_position_ = Eigen::Vector3f(0, 0, 1.05);
    base_orientation_ = Eigen::Vector4f(1, 0, 0, 0);
    base_linear_vel_ = Eigen::Vector3f::Zero();
    base_angular_vel_ = Eigen::Vector3f::Zero();
    gravity_projected_ = Eigen::Vector3f(0, 0, -9.81);

    // Initialize Kalman filter matrices
    P_ = Eigen::MatrixXf::Identity(6, 6) * 0.1f;
    Q_ = Eigen::MatrixXf::Identity(6, 6) * 0.01f;
    R_ = Eigen::MatrixXf::Identity(3, 3) * 0.1f;
}

}  // namespace sonic
}  // namespace sentient
