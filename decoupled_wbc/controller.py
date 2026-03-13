"""
Decoupled Whole-Body Controller

Combines RL-based lower body locomotion with IK-based upper body
control for versatile humanoid manipulation and navigation.
"""

from typing import Dict, Optional

import numpy as np


class DecoupledWBController:
    """
    Decoupled Whole-Body Controller.

    Splits the humanoid control into:
    - Lower body: RL policy for locomotion (walking, balancing)
    - Upper body: Inverse Kinematics for manipulation tasks

    This architecture enables independent development and testing
    of locomotion and manipulation capabilities.
    """

    def __init__(self, robot_name: str = "unitree_g1",
                 lower_checkpoint: Optional[str] = None,
                 upper_config: Optional[Dict] = None):
        self.robot_name = robot_name
        self.lower_checkpoint = lower_checkpoint
        self.upper_config = upper_config or {}
        self._lower_body = None
        self._upper_body = None

    def setup(self) -> None:
        """Initialize both controllers."""
        from decoupled_wbc.lower_body import LowerBodyPolicy
        from decoupled_wbc.upper_body import UpperBodyIK

        self._lower_body = LowerBodyPolicy(self.robot_name, self.lower_checkpoint)
        self._upper_body = UpperBodyIK(self.robot_name, **self.upper_config)
        print("[DecoupledWBC] Controllers initialized.")

    def compute(self, observation: Dict[str, np.ndarray],
                locomotion_command: Dict[str, float],
                ee_targets: Optional[Dict[str, np.ndarray]] = None) -> np.ndarray:
        """
        Compute full-body joint targets.

        Args:
            observation: Current robot state.
            locomotion_command: Velocity commands {linear_x, linear_y, angular_z}.
            ee_targets: Optional end-effector targets for upper body IK.

        Returns:
            Full joint position targets.
        """
        # Lower body: RL policy
        lower_action = self._lower_body.infer(observation, locomotion_command)

        # Upper body: IK solver
        upper_action = self._upper_body.solve(observation, ee_targets)

        # Merge actions
        full_action = np.concatenate([lower_action, upper_action])
        return full_action
