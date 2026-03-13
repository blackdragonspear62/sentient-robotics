/**
 * @file g1_deploy_onnx_ref.cpp
 * @brief Unitree G1 ONNX Deployment Reference Implementation
 *
 * Minimal reference implementation for deploying Sentient-SONIC
 * on the Unitree G1 humanoid robot using ONNX Runtime.
 *
 * Copyright (c) 2026 Sentient Robotics
 * Licensed under Apache License 2.0
 */

#include "sentient_sonic/inference_engine.h"
#include "sentient_sonic/robot_interface.h"
#include "sentient_sonic/safety_controller.h"

#include <iostream>
#include <chrono>
#include <thread>

int main(int argc, char** argv) {
    std::cout << "Sentient-SONIC G1 Reference Deployment" << std::endl;
    std::cout << "======================================" << std::endl;

    std::string model_path = (argc > 1) ? argv[1] : "checkpoints/policy.onnx";

    // Setup inference
    sentient::sonic::InferenceConfig config;
    config.model_path = model_path;
    config.device = "cpu";
    config.num_threads = 2;
    config.control_dt = 0.02f;

    sentient::sonic::InferenceEngine engine(config);
    engine.initialize();

    // Setup safety
    sentient::sonic::SafetyLimits limits;
    limits.max_joint_velocity = 8.0f;
    limits.max_joint_torque = 80.0f;
    limits.safety_margin = 0.85f;
    sentient::sonic::SafetyController safety(limits);

    // Setup robot
    sentient::sonic::UnitreeG1Interface robot;
    std::string ip = (argc > 2) ? argv[2] : "192.168.1.100";
    robot.connect(ip, 8080);

    // Heading initialization
    std::cout << "[G1] Initializing heading reference..." << std::endl;
    auto init_state = robot.get_state();
    // Store initial heading for drift compensation

    std::cout << "[G1] Starting control loop at 50 Hz..." << std::endl;

    for (int step = 0; step < 5000; ++step) {
        auto start = std::chrono::high_resolution_clock::now();

        auto state = robot.get_state();

        sentient::sonic::PolicyInput input;
        input.joint_positions = state.joint_positions;
        input.joint_velocities = state.joint_velocities;
        input.base_orientation = state.base_orientation;
        input.base_angular_vel = state.base_angular_velocity;
        input.base_linear_vel = state.base_linear_velocity;

        auto output = engine.infer(input);

        auto status = safety.check(
            state.joint_positions, state.joint_velocities,
            state.joint_torques, state.base_linear_velocity,
            state.base_angular_velocity
        );

        if (status == sentient::sonic::SafetyStatus::EMERGENCY_STOP) {
            std::cerr << "[G1] EMERGENCY STOP at step " << step << std::endl;
            break;
        }

        auto safe_action = safety.clamp_action(output.target_positions);

        sentient::sonic::RobotCommand cmd;
        cmd.target_positions = safe_action;
        robot.send_command(cmd);

        // Maintain 50 Hz
        auto elapsed = std::chrono::high_resolution_clock::now() - start;
        auto sleep_time = std::chrono::milliseconds(20) - elapsed;
        if (sleep_time.count() > 0) {
            std::this_thread::sleep_for(sleep_time);
        }
    }

    robot.disconnect();
    std::cout << "[G1] Deployment complete." << std::endl;
    return 0;
}
