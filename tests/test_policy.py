"""Tests for Sentient-SONIC policy module."""

import numpy as np
import pytest

from sentient_sonic.core.policy import SonicPolicy, PolicyOutput
from sentient_sonic.core.config import SonicConfig


class TestSonicPolicy:
    """Test suite for SonicPolicy."""

    def test_init(self):
        policy = SonicPolicy()
        assert not policy.is_loaded
        assert policy.device == "cpu"

    def test_load_without_checkpoint(self):
        policy = SonicPolicy()
        with pytest.raises(ValueError, match="No checkpoint path"):
            policy.load()

    def test_load_with_checkpoint(self, tmp_path):
        checkpoint = tmp_path / "model.pt"
        checkpoint.touch()
        policy = SonicPolicy(checkpoint_path=str(checkpoint))
        policy.load()
        assert policy.is_loaded

    def test_infer_without_load(self):
        policy = SonicPolicy()
        with pytest.raises(RuntimeError, match="not loaded"):
            policy.infer({"joint_pos": np.zeros(23)})

    def test_infer(self, tmp_path):
        checkpoint = tmp_path / "model.pt"
        checkpoint.touch()
        policy = SonicPolicy(checkpoint_path=str(checkpoint))
        policy.load()

        obs = {
            "joint_pos": np.zeros(23),
            "joint_vel": np.zeros(23),
            "base_quat": np.array([1.0, 0.0, 0.0, 0.0]),
        }
        output = policy.infer(obs)
        assert isinstance(output, PolicyOutput)
        assert output.joint_positions.shape == (23,)
        assert output.joint_velocities.shape == (23,)
        assert output.confidence > 0

    def test_reset(self, tmp_path):
        checkpoint = tmp_path / "model.pt"
        checkpoint.touch()
        policy = SonicPolicy(checkpoint_path=str(checkpoint))
        policy.load()
        policy.reset()  # Should not raise

    def test_repr(self):
        policy = SonicPolicy(device="cuda:0")
        assert "cuda:0" in repr(policy)
        assert "not loaded" in repr(policy)
