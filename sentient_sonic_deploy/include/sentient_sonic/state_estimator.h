/**
 * @file state_estimator.h
 * @brief Sentient-SONIC State Estimator
 *
 * Fuses IMU, joint encoder, and contact sensor data for
 * robust base state estimation during locomotion.
 *
 * Copyright (c) 2026 Sentient Robotics
 * Licensed under Apache License 2.0
 */

#pragma once

#include <Eigen/Dense>

namespace sentient {
namespace sonic {

struct IMUData {
    Eigen::Vector3f acceleration;
    Eigen::Vector3f angular_velocity;
    Eigen::Vector4f orientation;
    double timestamp;
};

struct ContactState {
    bool left_foot = false;
    bool right_foot = false;
    float left_force = 0.0f;
    float right_force = 0.0f;
};

class StateEstimator {
public:
    StateEstimator();
    ~StateEstimator() = default;

    void update(const IMUData& imu, const ContactState& contacts,
                const Eigen::VectorXf& joint_pos, const Eigen::VectorXf& joint_vel);

    Eigen::Vector3f get_base_position() const;
    Eigen::Vector4f get_base_orientation() const;
    Eigen::Vector3f get_base_linear_velocity() const;
    Eigen::Vector3f get_base_angular_velocity() const;
    Eigen::Vector3f get_projected_gravity() const;

    void reset();

private:
    Eigen::Vector3f base_position_;
    Eigen::Vector4f base_orientation_;
    Eigen::Vector3f base_linear_vel_;
    Eigen::Vector3f base_angular_vel_;
    Eigen::Vector3f gravity_projected_;

    // Kalman filter state
    Eigen::MatrixXf P_;  // Covariance
    Eigen::MatrixXf Q_;  // Process noise
    Eigen::MatrixXf R_;  // Measurement noise
};

}  // namespace sonic
}  // namespace sentient
