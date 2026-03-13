/**
 * @file main_deploy.cpp
 * @brief Sentient-SONIC Main Deployment Entry Point
 *
 * Launches the full deployment pipeline: inference engine,
 * safety controller, robot interface, and ZMQ bridge.
 *
 * Copyright (c) 2026 Sentient Robotics
 * Licensed under Apache License 2.0
 */

#include "sentient_sonic/inference_engine.h"
#include "sentient_sonic/safety_controller.h"
#include "sentient_sonic/robot_interface.h"
#include "sentient_sonic/state_estimator.h"

#include <iostream>
#include <csignal>
#include <atomic>

static std::atomic<bool> g_running{true};

void signal_handler(int sig) {
    std::cout << "\n[Sentient-SONIC] Received signal " << sig << ", shutting down..." << std::endl;
    g_running = false;
}

int main(int argc, char** argv) {
    std::signal(SIGINT, signal_handler);
    std::signal(SIGTERM, signal_handler);

    std::cout << "========================================" << std::endl;
    std::cout << "  Sentient-SONIC Deployment Runtime" << std::endl;
    std::cout << "  Version 0.1.0" << std::endl;
    std::cout << "========================================" << std::endl;

    // Parse arguments
    std::string model_path = "checkpoints/sentient-sonic-base/policy.onnx";
    std::string robot_ip = "192.168.1.100";
    int robot_port = 8080;

    if (argc > 1) model_path = argv[1];
    if (argc > 2) robot_ip = argv[2];
    if (argc > 3) robot_port = std::stoi(argv[3]);

    // Initialize components
    sentient::sonic::InferenceConfig inf_config;
    inf_config.model_path = model_path;
    inf_config.device = "cpu";
    inf_config.num_threads = 4;

    sentient::sonic::InferenceEngine engine(inf_config);
    if (!engine.initialize()) {
        std::cerr << "[ERROR] Failed to initialize inference engine." << std::endl;
        return 1;
    }

    sentient::sonic::SafetyLimits safety_limits;
    sentient::sonic::SafetyController safety(safety_limits);

    sentient::sonic::UnitreeG1Interface robot;
    if (!robot.connect(robot_ip, robot_port)) {
        std::cerr << "[ERROR] Failed to connect to robot." << std::endl;
        return 1;
    }

    sentient::sonic::StateEstimator estimator;

    std::cout << "[Sentient-SONIC] All systems initialized. Starting control loop..." << std::endl;

    // Main control loop
    while (g_running) {
        auto state = robot.get_state();
        if (!state.is_valid) continue;

        sentient::sonic::PolicyInput input;
        input.joint_positions = state.joint_positions;
        input.joint_velocities = state.joint_velocities;
        input.base_orientation = state.base_orientation;
        input.base_angular_vel = state.base_angular_velocity;
        input.base_linear_vel = state.base_linear_velocity;

        auto output = engine.infer(input);
        auto safe_action = safety.clamp_action(output.target_positions);

        sentient::sonic::RobotCommand cmd;
        cmd.target_positions = safe_action;
        robot.send_command(cmd);
    }

    robot.disconnect();
    std::cout << "[Sentient-SONIC] Shutdown complete." << std::endl;
    return 0;
}
