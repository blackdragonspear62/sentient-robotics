/**
 * @file safety_controller.cpp
 * @brief Sentient-SONIC Safety Controller Implementation
 *
 * Copyright (c) 2026 Sentient Robotics
 * Licensed under Apache License 2.0
 */

#include "sentient_sonic/safety_controller.h"

#include <algorithm>
#include <cmath>
#include <iostream>

namespace sentient {
namespace sonic {

SafetyController::SafetyController(const SafetyLimits& limits)
    : limits_(limits) {}

SafetyStatus SafetyController::check(
    const Eigen::VectorXf& joint_pos,
    const Eigen::VectorXf& joint_vel,
    const Eigen::VectorXf& joint_torque,
    const Eigen::Vector3f& base_vel,
    const Eigen::Vector3f& base_ang_vel) {

    // Check joint velocity limits
    float max_vel = joint_vel.cwiseAbs().maxCoeff();
    if (max_vel > limits_.max_joint_velocity * limits_.emergency_stop_threshold) {
        status_ = SafetyStatus::EMERGENCY_STOP;
        if (callback_) callback_(status_);
        return status_;
    }
    if (max_vel > limits_.max_joint_velocity * limits_.safety_margin) {
        status_ = SafetyStatus::WARNING;
    }

    // Check base velocity
    float base_speed = base_vel.norm();
    if (base_speed > limits_.max_base_velocity * limits_.emergency_stop_threshold) {
        status_ = SafetyStatus::EMERGENCY_STOP;
        if (callback_) callback_(status_);
        return status_;
    }

    // Check torque limits
    float max_torque = joint_torque.cwiseAbs().maxCoeff();
    if (max_torque > limits_.max_joint_torque) {
        status_ = SafetyStatus::CRITICAL;
        if (callback_) callback_(status_);
        return status_;
    }

    if (status_ != SafetyStatus::WARNING) {
        status_ = SafetyStatus::NOMINAL;
    }

    return status_;
}

Eigen::VectorXf SafetyController::clamp_action(const Eigen::VectorXf& action) {
    Eigen::VectorXf clamped = action;
    float limit = limits_.max_joint_velocity * limits_.safety_margin * 0.02f;
    for (int i = 0; i < clamped.size(); ++i) {
        clamped[i] = std::clamp(clamped[i], -limit, limit);
    }
    return clamped;
}

void SafetyController::trigger_emergency_stop() {
    status_ = SafetyStatus::EMERGENCY_STOP;
    std::cerr << "[SAFETY] EMERGENCY STOP TRIGGERED" << std::endl;
    if (callback_) callback_(status_);
}

void SafetyController::reset() {
    status_ = SafetyStatus::NOMINAL;
}

void SafetyController::set_callback(std::function<void(SafetyStatus)> callback) {
    callback_ = std::move(callback);
}

}  // namespace sonic
}  // namespace sentient
