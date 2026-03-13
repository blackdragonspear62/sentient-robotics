"""
Sentient-SONIC Motion Data Loader

Loads and preprocesses large-scale human motion capture data for
training the SONIC behavior foundation model.
"""

import os
from typing import Dict, List, Optional, Tuple

import numpy as np


class MotionClip:
    """Represents a single motion capture clip."""

    def __init__(self, joint_positions: np.ndarray, joint_velocities: np.ndarray,
                 root_positions: np.ndarray, root_orientations: np.ndarray,
                 fps: float = 30.0, metadata: Optional[Dict] = None):
        self.joint_positions = joint_positions  # (T, N_joints)
        self.joint_velocities = joint_velocities  # (T, N_joints)
        self.root_positions = root_positions  # (T, 3)
        self.root_orientations = root_orientations  # (T, 4)
        self.fps = fps
        self.metadata = metadata or {}

    @property
    def num_frames(self) -> int:
        return self.joint_positions.shape[0]

    @property
    def duration(self) -> float:
        return self.num_frames / self.fps

    def get_frame(self, idx: int) -> Dict[str, np.ndarray]:
        return {
            "joint_pos": self.joint_positions[idx],
            "joint_vel": self.joint_velocities[idx],
            "root_pos": self.root_positions[idx],
            "root_quat": self.root_orientations[idx],
        }

    def subsample(self, target_fps: float) -> "MotionClip":
        ratio = int(self.fps / target_fps)
        return MotionClip(
            joint_positions=self.joint_positions[::ratio],
            joint_velocities=self.joint_velocities[::ratio],
            root_positions=self.root_positions[::ratio],
            root_orientations=self.root_orientations[::ratio],
            fps=target_fps,
            metadata=self.metadata,
        )


class MotionDataset:
    """Dataset of motion capture clips for training."""

    def __init__(self, data_dir: str, robot_name: str = "unitree_g1"):
        self.data_dir = data_dir
        self.robot_name = robot_name
        self.clips: List[MotionClip] = []
        self._index = []

    def load(self) -> int:
        """Load all motion clips from data directory. Returns number of clips loaded."""
        # Mocked: In production, loads .npz or .pkl files
        print(f"[MotionDataset] Loading from {self.data_dir} for {self.robot_name}")
        print(f"[MotionDataset] (Mocked) Would load motion clips here.")
        return len(self.clips)

    def get_random_clip(self) -> Optional[MotionClip]:
        if not self.clips:
            return None
        idx = np.random.randint(len(self.clips))
        return self.clips[idx]

    def __len__(self) -> int:
        return len(self.clips)

    def __getitem__(self, idx: int) -> MotionClip:
        return self.clips[idx]
