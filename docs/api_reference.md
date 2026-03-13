# API Reference

## sentient_sonic

### Core

- `SonicPolicy` — Main policy class for inference
- `SonicConfig` — Policy configuration
- `SonicPolicyNetwork` — Neural network architecture
- `MotionTrackingReward` — Reward function
- `SonicTrainer` — PPO training pipeline
- `SonicEnvWrapper` — Environment wrapper

### Teleoperation

- `VRController` — PICO VR teleoperation
- `KeyboardController` — Keyboard locomotion control
- `GamepadController` — Gamepad locomotion control

### Utilities

- `quat_to_rot` — Quaternion to rotation matrix
- `rot_to_quat` — Rotation matrix to quaternion
- `euler_to_quat` — Euler angles to quaternion
- `ZMQPublisher` — ZMQ data publisher
- `ZMQSubscriber` — ZMQ data subscriber
- `MotionDataset` — Motion capture dataset loader
- `MotionRetargeter` — Cross-embodiment retargeting

## decoupled_wbc

- `DecoupledWBController` — Main decoupled controller
- `LowerBodyPolicy` — RL locomotion policy
- `UpperBodyIK` — IK manipulation solver

## sentient_sonic_deploy (C++)

- `InferenceEngine` — ONNX Runtime inference
- `SafetyController` — Real-time safety monitoring
- `RobotInterface` / `UnitreeG1Interface` — Hardware communication
- `StateEstimator` — IMU + contact state estimation
