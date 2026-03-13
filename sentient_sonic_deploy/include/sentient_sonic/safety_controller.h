/**
 * @file safety_controller.h
 * @brief Sentient-SONIC Safety Controller
 *
 * Real-time safety monitoring and emergency stop system for
 * humanoid robot deployment.
 *
 * Copyright (c) 2026 Sentient Robotics
 * Licensed under Apache License 2.0
 */

#pragma once

#include <Eigen/Dense>
#include <functional>
#include <string>

namespace sentient {
namespace sonic {

struct SafetyLimits {
    float max_joint_velocity = 10.0f;    // rad/s
    float max_joint_torque = 100.0f;     // Nm
    float max_base_velocity = 2.0f;      // m/s
    float max_base_angular_vel = 5.0f;   // rad/s
    float max_joint_deviation = 0.5f;    // rad from nominal
    float emergency_stop_threshold = 2.0f;
    float safety_margin = 0.9f;
};

enum class SafetyStatus {
    NOMINAL,
    WARNING,
    CRITICAL,
    EMERGENCY_STOP
};

class SafetyController {
public:
    explicit SafetyController(const SafetyLimits& limits);
    ~SafetyController() = default;

    SafetyStatus check(
        const Eigen::VectorXf& joint_pos,
        const Eigen::VectorXf& joint_vel,
        const Eigen::VectorXf& joint_torque,
        const Eigen::Vector3f& base_vel,
        const Eigen::Vector3f& base_ang_vel
    );

    Eigen::VectorXf clamp_action(const Eigen::VectorXf& action);
    void trigger_emergency_stop();
    void reset();

    SafetyStatus get_status() const { return status_; }
    void set_callback(std::function<void(SafetyStatus)> callback);

private:
    SafetyLimits limits_;
    SafetyStatus status_ = SafetyStatus::NOMINAL;
    std::function<void(SafetyStatus)> callback_;
};

}  // namespace sonic
}  // namespace sentient
