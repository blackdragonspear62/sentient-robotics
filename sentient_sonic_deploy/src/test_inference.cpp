/**
 * @file test_inference.cpp
 * @brief Sentient-SONIC Inference Benchmark
 *
 * Benchmarks the ONNX inference engine for latency and throughput.
 *
 * Copyright (c) 2026 Sentient Robotics
 * Licensed under Apache License 2.0
 */

#include "sentient_sonic/inference_engine.h"

#include <chrono>
#include <iostream>
#include <vector>

int main(int argc, char** argv) {
    std::string model_path = (argc > 1) ? argv[1] : "checkpoints/policy.onnx";
    int num_iterations = (argc > 2) ? std::stoi(argv[2]) : 1000;

    std::cout << "Sentient-SONIC Inference Benchmark" << std::endl;
    std::cout << "==================================" << std::endl;
    std::cout << "Model: " << model_path << std::endl;
    std::cout << "Iterations: " << num_iterations << std::endl;

    sentient::sonic::InferenceConfig config;
    config.model_path = model_path;
    config.device = "cpu";
    config.num_threads = 4;

    sentient::sonic::InferenceEngine engine(config);
    engine.initialize();

    // Prepare dummy input
    sentient::sonic::PolicyInput input;
    input.joint_positions = Eigen::VectorXf::Zero(23);
    input.joint_velocities = Eigen::VectorXf::Zero(23);
    input.base_orientation = Eigen::Vector4f(1, 0, 0, 0);
    input.base_angular_vel = Eigen::Vector3f::Zero();
    input.base_linear_vel = Eigen::Vector3f::Zero();
    input.projected_gravity = Eigen::Vector3f(0, 0, -9.81);

    // Warmup
    for (int i = 0; i < 10; ++i) {
        engine.infer(input);
    }

    // Benchmark
    std::vector<float> latencies;
    auto total_start = std::chrono::high_resolution_clock::now();

    for (int i = 0; i < num_iterations; ++i) {
        auto start = std::chrono::high_resolution_clock::now();
        auto output = engine.infer(input);
        auto end = std::chrono::high_resolution_clock::now();
        float ms = std::chrono::duration<float, std::milli>(end - start).count();
        latencies.push_back(ms);
    }

    auto total_end = std::chrono::high_resolution_clock::now();
    float total_ms = std::chrono::duration<float, std::milli>(total_end - total_start).count();

    // Statistics
    float sum = 0, min_val = 1e9, max_val = 0;
    for (float l : latencies) {
        sum += l;
        min_val = std::min(min_val, l);
        max_val = std::max(max_val, l);
    }
    float mean = sum / latencies.size();

    std::cout << "\nResults:" << std::endl;
    std::cout << "  Mean latency: " << mean << " ms" << std::endl;
    std::cout << "  Min latency:  " << min_val << " ms" << std::endl;
    std::cout << "  Max latency:  " << max_val << " ms" << std::endl;
    std::cout << "  Throughput:   " << (num_iterations / (total_ms / 1000.0f)) << " infer/s" << std::endl;
    std::cout << "  Total time:   " << total_ms << " ms" << std::endl;

    return 0;
}
