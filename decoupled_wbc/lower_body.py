"""
Decoupled WBC — Lower Body RL Policy

Reinforcement learning policy for lower body locomotion control.
Handles walking, running, turning, and balance recovery.
"""

from typing import Dict, Optional

import numpy as np


class LowerBodyPolicy:
    """RL policy for lower body locomotion."""

    LOWER_BODY_JOINTS = [
        "left_hip_yaw", "left_hip_roll", "left_hip_pitch",
        "left_knee", "left_ankle_pitch", "left_ankle_roll",
        "right_hip_yaw", "right_hip_roll", "right_hip_pitch",
        "right_knee", "right_ankle_pitch", "right_ankle_roll",
    ]

    def __init__(self, robot_name: str = "unitree_g1",
                 checkpoint_path: Optional[str] = None):
        self.robot_name = robot_name
        self.checkpoint_path = checkpoint_path
        self.num_joints = len(self.LOWER_BODY_JOINTS)

    def infer(self, observation: Dict[str, np.ndarray],
              command: Dict[str, float]) -> np.ndarray:
        """Compute lower body joint targets from locomotion command."""
        # Mocked
        return np.zeros(self.num_joints)
