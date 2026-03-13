"""Tests for Decoupled Whole-Body Controller."""

import numpy as np
import pytest

from decoupled_wbc.controller import DecoupledWBController
from decoupled_wbc.lower_body import LowerBodyPolicy
from decoupled_wbc.upper_body import UpperBodyIK


class TestDecoupledWBC:
    def test_lower_body_joints(self):
        policy = LowerBodyPolicy()
        assert policy.num_joints == 12

    def test_upper_body_joints(self):
        ik = UpperBodyIK()
        assert ik.num_joints == 11

    def test_lower_body_infer(self):
        policy = LowerBodyPolicy()
        obs = {"joint_pos": np.zeros(23), "joint_vel": np.zeros(23)}
        cmd = {"linear_x": 0.5, "linear_y": 0.0, "angular_z": 0.0}
        action = policy.infer(obs, cmd)
        assert action.shape == (12,)

    def test_upper_body_solve(self):
        ik = UpperBodyIK()
        obs = {"joint_pos": np.zeros(23)}
        action = ik.solve(obs)
        assert action.shape == (11,)
