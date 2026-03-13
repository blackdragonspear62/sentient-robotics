"""
Sentient-SONIC Environment Wrapper

Wraps Isaac Gym / Isaac Lab environments for training the SONIC policy
with standardized observation and action spaces.
"""

from typing import Any, Dict, Optional, Tuple

import numpy as np


class SonicEnvWrapper:
    """
    Environment wrapper for Sentient-SONIC training.

    Provides a standardized interface for different simulation backends
    (Isaac Gym, Isaac Lab, MuJoCo) with motion tracking task setup.
    """

    def __init__(
        self,
        env_name: str = "humanoid_motion_tracking",
        num_envs: int = 4096,
        robot_name: str = "unitree_g1",
        sim_dt: float = 0.005,
        control_dt: float = 0.02,
        motion_file: Optional[str] = None,
    ):
        self.env_name = env_name
        self.num_envs = num_envs
        self.robot_name = robot_name
        self.sim_dt = sim_dt
        self.control_dt = control_dt
        self.motion_file = motion_file
        self._step_count = 0

    @property
    def observation_space(self) -> Dict[str, Tuple[int, ...]]:
        return {
            "joint_pos": (23,),
            "joint_vel": (23,),
            "base_quat": (4,),
            "base_ang_vel": (3,),
            "base_lin_vel": (3,),
            "projected_gravity": (3,),
            "target_joint_pos": (23,),
            "target_joint_vel": (23,),
        }

    @property
    def action_space(self) -> Tuple[int, ...]:
        return (23,)

    def reset(self) -> Dict[str, np.ndarray]:
        """Reset all environments."""
        self._step_count = 0
        obs = {k: np.zeros((self.num_envs,) + v) for k, v in self.observation_space.items()}
        return obs

    def step(self, actions: np.ndarray) -> Tuple[Dict[str, np.ndarray], np.ndarray, np.ndarray, Dict]:
        """Step all environments."""
        self._step_count += 1
        obs = {k: np.zeros((self.num_envs,) + v) for k, v in self.observation_space.items()}
        rewards = np.zeros(self.num_envs)
        dones = np.zeros(self.num_envs, dtype=bool)
        infos = {"episode_length": np.full(self.num_envs, self._step_count)}
        return obs, rewards, dones, infos

    def close(self) -> None:
        """Cleanup environments."""
        pass
