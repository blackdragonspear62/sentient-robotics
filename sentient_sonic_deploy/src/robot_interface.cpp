/**
 * @file robot_interface.cpp
 * @brief Sentient-SONIC Unitree G1 Robot Interface Implementation
 *
 * Copyright (c) 2026 Sentient Robotics
 * Licensed under Apache License 2.0
 */

#include "sentient_sonic/robot_interface.h"

#include <iostream>

namespace sentient {
namespace sonic {

struct UnitreeG1Interface::Impl {
    std::string ip;
    int port;
    // Unitree SDK handles would be here
};

UnitreeG1Interface::UnitreeG1Interface()
    : impl_(std::make_unique<Impl>()) {}

UnitreeG1Interface::~UnitreeG1Interface() {
    if (connected_) disconnect();
}

bool UnitreeG1Interface::connect(const std::string& ip, int port) {
    std::cout << "[G1] Connecting to " << ip << ":" << port << std::endl;
    impl_->ip = ip;
    impl_->port = port;
    // Mocked: In production, connects via Unitree SDK
    connected_ = true;
    std::cout << "[G1] Connected successfully." << std::endl;
    return true;
}

void UnitreeG1Interface::disconnect() {
    std::cout << "[G1] Disconnecting..." << std::endl;
    connected_ = false;
}

bool UnitreeG1Interface::is_connected() const {
    return connected_;
}

RobotState UnitreeG1Interface::get_state() {
    RobotState state;
    state.joint_positions = Eigen::VectorXf::Zero(23);
    state.joint_velocities = Eigen::VectorXf::Zero(23);
    state.joint_torques = Eigen::VectorXf::Zero(23);
    state.base_orientation = Eigen::Vector4f(1, 0, 0, 0);
    state.base_angular_velocity = Eigen::Vector3f::Zero();
    state.base_linear_velocity = Eigen::Vector3f::Zero();
    state.base_position = Eigen::Vector3f(0, 0, 1.05);
    state.is_valid = connected_;
    return state;
}

bool UnitreeG1Interface::send_command(const RobotCommand& cmd) {
    if (!connected_) return false;
    // Mocked: In production, sends via Unitree SDK
    return true;
}

}  // namespace sonic
}  // namespace sentient
