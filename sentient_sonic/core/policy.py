"""
Sentient-SONIC Policy Module

Implements the core SONIC policy for whole-body humanoid control.
SONIC is a humanoid behavior foundation model that provides a core set of
motor skills learned from large-scale human motion data.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

import numpy as np


@dataclass
class PolicyOutput:
    """Output from the Sentient-SONIC policy inference."""

    joint_positions: np.ndarray  # Target joint positions (N_joints,)
    joint_velocities: np.ndarray  # Target joint velocities (N_joints,)
    base_position: np.ndarray  # Base position (3,)
    base_orientation: np.ndarray  # Base orientation quaternion (4,)
    confidence: float = 1.0  # Policy confidence score


class SonicPolicy:
    """
    Sentient-SONIC Whole-Body Control Policy.

    This policy uses motion tracking as a scalable training task, enabling
    a single unified policy to produce natural, whole-body movement and
    support a wide range of behaviors — from walking and crawling to
    teleoperation and multi-modal control.

    Args:
        config: Policy configuration object.
        checkpoint_path: Path to the pretrained model checkpoint.
        device: Compute device ('cpu', 'cuda:0', etc.).
    """

    def __init__(
        self,
        config: Optional["SonicConfig"] = None,
        checkpoint_path: Optional[str] = None,
        device: str = "cpu",
    ):
        self.config = config
        self.checkpoint_path = checkpoint_path
        self.device = device
        self._model = None
        self._is_loaded = False

    def load(self) -> None:
        """Load the policy model from checkpoint."""
        if self.checkpoint_path is None:
            raise ValueError(
                "No checkpoint path specified. Use download_from_hf.py to download "
                "pretrained Sentient-SONIC checkpoints."
            )
        # Mocked: In production, this loads the actual model
        print(f"[Sentient-SONIC] Loading policy from {self.checkpoint_path}")
        print(f"[Sentient-SONIC] Device: {self.device}")
        self._is_loaded = True
        print("[Sentient-SONIC] Policy loaded successfully.")

    def reset(self) -> None:
        """Reset the policy state for a new episode."""
        if not self._is_loaded:
            raise RuntimeError("Policy not loaded. Call load() first.")
        # Mocked: Reset internal state
        print("[Sentient-SONIC] Policy state reset.")

    def infer(
        self,
        observation: Dict[str, np.ndarray],
        target_motion: Optional[np.ndarray] = None,
    ) -> PolicyOutput:
        """
        Run policy inference given current observation.

        Args:
            observation: Dictionary containing sensor observations.
                Expected keys: 'joint_pos', 'joint_vel', 'base_quat', 'base_ang_vel'
            target_motion: Optional target motion reference for tracking.

        Returns:
            PolicyOutput with target joint positions and velocities.
        """
        if not self._is_loaded:
            raise RuntimeError("Policy not loaded. Call load() first.")

        n_joints = observation.get("joint_pos", np.zeros(23)).shape[0]

        # Mocked inference output
        return PolicyOutput(
            joint_positions=np.zeros(n_joints),
            joint_velocities=np.zeros(n_joints),
            base_position=np.zeros(3),
            base_orientation=np.array([1.0, 0.0, 0.0, 0.0]),
            confidence=0.95,
        )

    @property
    def is_loaded(self) -> bool:
        """Whether the policy model is loaded."""
        return self._is_loaded

    def __repr__(self) -> str:
        status = "loaded" if self._is_loaded else "not loaded"
        return f"SonicPolicy(device={self.device}, status={status})"
