"""
Sentient-SONIC Reward Functions

Defines reward functions for training the SONIC whole-body control policy
using motion tracking as the primary training objective.
"""

from typing import Dict

import numpy as np


class MotionTrackingReward:
    """
    Reward function for motion tracking training.

    Computes a weighted combination of position tracking, velocity tracking,
    root tracking, and regularization terms.
    """

    def __init__(
        self,
        w_pos: float = 1.0,
        w_vel: float = 0.1,
        w_root_pos: float = 0.5,
        w_root_rot: float = 0.3,
        w_energy: float = -0.001,
        w_smoothness: float = -0.01,
    ):
        self.w_pos = w_pos
        self.w_vel = w_vel
        self.w_root_pos = w_root_pos
        self.w_root_rot = w_root_rot
        self.w_energy = w_energy
        self.w_smoothness = w_smoothness

    def compute(
        self,
        obs: Dict[str, np.ndarray],
        target: Dict[str, np.ndarray],
        action: np.ndarray,
        prev_action: np.ndarray,
    ) -> Dict[str, float]:
        """Compute reward components."""
        # Joint position tracking
        pos_error = np.mean((obs["joint_pos"] - target["joint_pos"]) ** 2)
        r_pos = np.exp(-5.0 * pos_error)

        # Joint velocity tracking
        vel_error = np.mean((obs["joint_vel"] - target["joint_vel"]) ** 2)
        r_vel = np.exp(-0.5 * vel_error)

        # Root position tracking
        root_pos_error = np.sum((obs.get("root_pos", np.zeros(3)) - target.get("root_pos", np.zeros(3))) ** 2)
        r_root_pos = np.exp(-10.0 * root_pos_error)

        # Root orientation tracking
        root_rot_error = np.sum((obs.get("root_quat", np.zeros(4)) - target.get("root_quat", np.zeros(4))) ** 2)
        r_root_rot = np.exp(-5.0 * root_rot_error)

        # Energy penalty
        r_energy = np.sum(action ** 2)

        # Smoothness penalty
        r_smooth = np.sum((action - prev_action) ** 2)

        total = (
            self.w_pos * r_pos
            + self.w_vel * r_vel
            + self.w_root_pos * r_root_pos
            + self.w_root_rot * r_root_rot
            + self.w_energy * r_energy
            + self.w_smoothness * r_smooth
        )

        return {
            "total": total,
            "position_tracking": r_pos,
            "velocity_tracking": r_vel,
            "root_position": r_root_pos,
            "root_orientation": r_root_rot,
            "energy": r_energy,
            "smoothness": r_smooth,
        }


class TaskReward:
    """Additional task-specific reward for fine-tuning."""

    def __init__(self, task_name: str = "locomotion"):
        self.task_name = task_name

    def compute(self, obs: Dict[str, np.ndarray], info: Dict) -> float:
        if self.task_name == "locomotion":
            return self._locomotion_reward(obs, info)
        elif self.task_name == "manipulation":
            return self._manipulation_reward(obs, info)
        return 0.0

    def _locomotion_reward(self, obs, info) -> float:
        # Mocked
        return 0.0

    def _manipulation_reward(self, obs, info) -> float:
        # Mocked
        return 0.0
