"""
Sentient-SONIC Configuration Module

Defines configuration dataclasses for the Sentient-SONIC policy,
deployment, and teleoperation systems.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class SonicConfig:
    """
    Configuration for the Sentient-SONIC whole-body control policy.

    Attributes:
        model_name: Name of the model variant.
        num_joints: Number of controllable joints.
        control_freq: Control frequency in Hz.
        action_space: Type of action space ('position', 'velocity', 'torque').
        observation_keys: List of observation keys expected by the policy.
        checkpoint_path: Path to the pretrained model checkpoint.
        device: Compute device for inference.
    """

    model_name: str = "sentient-sonic-base"
    num_joints: int = 23
    control_freq: float = 50.0
    action_space: str = "position"
    observation_keys: List[str] = field(
        default_factory=lambda: [
            "joint_pos",
            "joint_vel",
            "base_quat",
            "base_ang_vel",
            "base_lin_vel",
            "projected_gravity",
        ]
    )
    checkpoint_path: Optional[str] = None
    device: str = "cpu"

    # Motion tracking parameters
    tracking_weight_pos: float = 1.0
    tracking_weight_vel: float = 0.1
    tracking_weight_root: float = 0.5

    # Safety limits
    max_joint_velocity: float = 10.0  # rad/s
    max_joint_torque: float = 100.0  # Nm
    max_base_velocity: float = 2.0  # m/s

    def validate(self) -> bool:
        """Validate configuration parameters."""
        assert self.num_joints > 0, "num_joints must be positive"
        assert self.control_freq > 0, "control_freq must be positive"
        assert self.action_space in ("position", "velocity", "torque"), (
            f"Invalid action_space: {self.action_space}"
        )
        return True


@dataclass
class DeployConfig:
    """Configuration for deploying Sentient-SONIC on real hardware."""

    robot_type: str = "unitree_g1"
    ip_address: str = "192.168.1.100"
    port: int = 8080
    use_onnx: bool = True
    onnx_model_path: Optional[str] = None
    enable_safety_controller: bool = True
    safety_margin: float = 0.9


@dataclass
class TeleopConfig:
    """Configuration for VR teleoperation with Sentient-SONIC."""

    vr_device: str = "pico"
    tracking_mode: str = "full_body"
    retargeting_method: str = "optimization"
    zmq_host: str = "localhost"
    zmq_port: int = 5555
    control_freq: float = 50.0
    enable_haptic_feedback: bool = True
