"""Tests for Sentient-SONIC configuration module."""

import pytest

from sentient_sonic.core.config import SonicConfig, DeployConfig, TeleopConfig


class TestSonicConfig:
    def test_defaults(self):
        config = SonicConfig()
        assert config.model_name == "sentient-sonic-base"
        assert config.num_joints == 23
        assert config.control_freq == 50.0
        assert config.action_space == "position"

    def test_validate(self):
        config = SonicConfig()
        assert config.validate()

    def test_invalid_action_space(self):
        config = SonicConfig(action_space="invalid")
        with pytest.raises(AssertionError):
            config.validate()

    def test_invalid_num_joints(self):
        config = SonicConfig(num_joints=-1)
        with pytest.raises(AssertionError):
            config.validate()


class TestDeployConfig:
    def test_defaults(self):
        config = DeployConfig()
        assert config.robot_type == "unitree_g1"
        assert config.use_onnx is True
        assert config.enable_safety_controller is True


class TestTeleopConfig:
    def test_defaults(self):
        config = TeleopConfig()
        assert config.vr_device == "pico"
        assert config.zmq_port == 5555
