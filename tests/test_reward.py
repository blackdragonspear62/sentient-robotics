"""Tests for reward functions."""

import numpy as np
import pytest

from sentient_sonic.core.reward import MotionTrackingReward


class TestMotionTrackingReward:
    def test_perfect_tracking(self):
        reward_fn = MotionTrackingReward()
        obs = {"joint_pos": np.zeros(23), "joint_vel": np.zeros(23)}
        target = {"joint_pos": np.zeros(23), "joint_vel": np.zeros(23)}
        action = np.zeros(23)
        prev_action = np.zeros(23)

        result = reward_fn.compute(obs, target, action, prev_action)
        assert result["position_tracking"] == pytest.approx(1.0, abs=1e-5)
        assert result["velocity_tracking"] == pytest.approx(1.0, abs=1e-5)

    def test_large_error(self):
        reward_fn = MotionTrackingReward()
        obs = {"joint_pos": np.ones(23) * 10, "joint_vel": np.zeros(23)}
        target = {"joint_pos": np.zeros(23), "joint_vel": np.zeros(23)}
        action = np.zeros(23)
        prev_action = np.zeros(23)

        result
 = reward_fn.compute(obs, target, action, prev_action)
        assert result["position_tracking"] < 0.1  # Should be near zero

    def test_energy_penalty(self):
        reward_fn = MotionTrackingReward(w_energy=-0.01)
        obs = {"joint_pos": np.zeros(23), "joint_vel": np.zeros(23)}
        target = {"joint_pos": np.zeros(23), "joint_vel": np.zeros(23)}
        action = np.ones(23) * 5.0
        prev_action = np.zeros(23)

        result = reward_fn.compute(obs, target, action, prev_action)
        assert result["total"] < reward_fn.compute(obs, target, np.zeros(23), np.zeros(23))["total"]
