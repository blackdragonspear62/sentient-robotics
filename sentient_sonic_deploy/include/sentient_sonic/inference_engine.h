/**
 * @file inference_engine.h
 * @brief Sentient-SONIC ONNX Inference Engine
 *
 * High-performance inference engine for real-time humanoid control
 * using ONNX Runtime with optimized execution providers.
 *
 * Copyright (c) 2026 Sentient Robotics
 * Licensed under Apache License 2.0
 */

#pragma once

#include <Eigen/Dense>
#include <memory>
#include <string>
#include <vector>

namespace sentient {
namespace sonic {

struct InferenceConfig {
    std::string model_path;
    std::string device = "cpu";  // "cpu" or "cuda"
    int num_threads = 4;
    bool enable_profiling = false;
    float control_dt = 0.02f;  // 50 Hz
};

struct PolicyInput {
    Eigen::VectorXf joint_positions;    // (N_joints,)
    Eigen::VectorXf joint_velocities;   // (N_joints,)
    Eigen::Vector4f base_orientation;   // quaternion (w, x, y, z)
    Eigen::Vector3f base_angular_vel;   // (3,)
    Eigen::Vector3f base_linear_vel;    // (3,)
    Eigen::Vector3f projected_gravity;  // (3,)
    Eigen::VectorXf target_joint_pos;   // (N_joints,)
};

struct PolicyOutput {
    Eigen::VectorXf target_positions;   // (N_joints,)
    Eigen::VectorXf target_velocities;  // (N_joints,)
    float confidence = 1.0f;
    float inference_time_ms = 0.0f;
};

class InferenceEngine {
public:
    explicit InferenceEngine(const InferenceConfig& config);
    ~InferenceEngine();

    bool initialize();
    PolicyOutput infer(const PolicyInput& input);
    void reset();

    bool is_initialized() const { return initialized_; }
    float get_avg_inference_time() const { return avg_inference_time_ms_; }

private:
    InferenceConfig config_;
    bool initialized_ = false;
    float avg_inference_time_ms_ = 0.0f;

    struct Impl;
    std::unique_ptr<Impl> impl_;
};

}  // namespace sonic
}  // namespace sentient
