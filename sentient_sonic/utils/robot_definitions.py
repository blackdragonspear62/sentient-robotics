"""
Sentient-SONIC Robot Definitions

Joint configurations, kinematic chains, and hardware specs for
supported humanoid platforms.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Tuple
import numpy as np


@dataclass
class JointDef:
    """Definition of a single robot joint."""
    name: str
    index: int
    lower_limit: float  # radians
    upper_limit: float  # radians
    max_velocity: float  # rad/s
    max_torque: float  # Nm
    damping: float = 0.1
    friction: float = 0.05


@dataclass
class RobotDefinition:
    """Complete robot hardware definition."""
    name: str
    num_joints: int
    joints: List[JointDef]
    base_height: float  # meters
    total_mass: float  # kg
    foot_size: Tuple[float, float]  # (length, width) meters
    imu_link: str = "base_link"
    end_effectors: List[str] = field(default_factory=list)


# Unitree G1 humanoid robot definition
UNITREE_G1 = RobotDefinition(
    name="unitree_g1",
    num_joints=23,
    base_height=1.05,
    total_mass=35.0,
    foot_size=(0.18, 0.10),
    imu_link="base_link",
    end_effectors=["left_hand_link", "right_hand_link", "left_foot_link", "right_foot_link"],
    joints=[
        JointDef("left_hip_yaw", 0, -1.57, 1.57, 10.0, 88.0),
        JointDef("left_hip_roll", 1, -0.52, 2.09, 10.0, 88.0),
        JointDef("left_hip_pitch", 2, -2.79, 0.87, 10.0, 139.0),
        JointDef("left_knee", 3, -0.09, 2.53, 10.0, 139.0),
        JointDef("left_ankle_pitch", 4, -0.87, 0.52, 10.0, 50.0),
        JointDef("left_ankle_roll", 5, -0.26, 0.26, 10.0, 50.0),
        JointDef("right_hip_yaw", 6, -1.57, 1.57, 10.0, 88.0),
        JointDef("right_hip_roll", 7, -2.09, 0.52, 10.0, 88.0),
        JointDef("right_hip_pitch", 8, -2.79, 0.87, 10.0, 139.0),
        JointDef("right_knee", 9, -0.09, 2.53, 10.0, 139.0),
        JointDef("right_ankle_pitch", 10, -0.87, 0.52, 10.0, 50.0),
        JointDef("right_ankle_roll", 11, -0.26, 0.26, 10.0, 50.0),
        JointDef("torso_yaw", 12, -2.62, 2.62, 8.0, 88.0),
        JointDef("left_shoulder_pitch", 13, -3.11, 2.62, 10.0, 50.0),
        JointDef("left_shoulder_roll", 14, -1.57, 2.62, 10.0, 50.0),
        JointDef("left_shoulder_yaw", 15, -2.62, 2.62, 10.0, 50.0),
        JointDef("left_elbow", 16, -1.57, 0.0, 10.0, 50.0),
        JointDef("left_wrist", 17, -1.57, 1.57, 10.0, 20.0),
        JointDef("right_shoulder_pitch", 18, -3.11, 2.62, 10.0, 50.0),
        JointDef("right_shoulder_roll", 19, -2.62, 1.57, 10.0, 50.0),
        JointDef("right_shoulder_yaw", 20, -2.62, 2.62, 10.0, 50.0),
        JointDef("right_elbow", 21, 0.0, 1.57, 10.0, 50.0),
        JointDef("right_wrist", 22, -1.57, 1.57, 10.0, 20.0),
    ],
)

# Fourier GR1 humanoid robot definition
FOURIER_GR1 = RobotDefinition(
    name="fourier_gr1",
    num_joints=32,
    base_height=1.65,
    total_mass=55.0,
    foot_size=(0.25, 0.12),
    imu_link="pelvis",
    end_effectors=["left_hand", "right_hand", "left_foot", "right_foot"],
    joints=[JointDef(f"joint_{i}", i, -3.14, 3.14, 8.0, 100.0) for i in range(32)],
)

SUPPORTED_ROBOTS = {
    "unitree_g1": UNITREE_G1,
    "fourier_gr1": FOURIER_GR1,
}


def get_robot(name: str) -> RobotDefinition:
    """Get robot definition by name."""
    if name not in SUPPORTED_ROBOTS:
        raise ValueError(f"Unknown robot: {name}. Supported: {list(SUPPORTED_ROBOTS.keys())}")
    return SUPPORTED_ROBOTS[name]
