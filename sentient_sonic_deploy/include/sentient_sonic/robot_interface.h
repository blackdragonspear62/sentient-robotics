/**
 * @file robot_interface.h
 * @brief Sentient-SONIC Robot Hardware Interface
 *
 * Abstract interface for communicating with humanoid robot hardware.
 * Supports Unitree G1 and extensible to other platforms.
 *
 * Copyright (c) 2026 Sentient Robotics
 * Licensed under Apache License 2.0
 */

#pragma once

#include <Eigen/Dense>
#include <memory>
#include <string>

namespace sentient {
namespace sonic {

struct RobotState {
    Eigen::VectorXf joint_positions;
    Eigen::VectorXf joint_velocities;
    Eigen::VectorXf joint_torques;
    Eigen::Vector4f base_orientation;
    Eigen::Vector3f base_angular_velocity;
    Eigen::Vector3f base_linear_velocity;
    Eigen::Vector3f base_position;
    double timestamp = 0.0;
    bool is_valid = false;
};

struct RobotCommand {
    Eigen::VectorXf target_positions;
    Eigen::VectorXf target_velocities;
    Eigen::VectorXf kp_gains;
    Eigen::VectorXf kd_gains;
    double timestamp = 0.0;
};

class RobotInterface {
public:
    virtual ~RobotInterface() = default;

    virtual bool connect(const std::string& ip, int port) = 0;
    virtual void disconnect() = 0;
    virtual bool is_connected() const = 0;

    virtual RobotState get_state() = 0;
    virtual bool send_command(const RobotCommand& cmd) = 0;

    virtual int num_joints() const = 0;
    virtual std::string robot_name() const = 0;
};

class UnitreeG1Interface : public RobotInterface {
public:
    UnitreeG1Interface();
    ~UnitreeG1Interface() override;

    bool connect(const std::string& ip, int port) override;
    void disconnect() override;
    bool is_connected() const override;

    RobotState get_state() override;
    bool send_command(const RobotCommand& cmd) override;

    int num_joints() const override { return 23; }
    std::string robot_name() const override { return "unitree_g1"; }

private:
    struct Impl;
    std::unique_ptr<Impl> impl_;
    bool connected_ = false;
};

}  // namespace sonic
}  // namespace sentient
