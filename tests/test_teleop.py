"""Tests for teleoperation controllers."""

import pytest

from sentient_sonic.teleop.vr_controller import VRController
from sentient_sonic.teleop.keyboard_controller import KeyboardController
from sentient_sonic.teleop.gamepad_controller import GamepadController
from sentient_sonic.core.config import TeleopConfig


class TestVRController:
    def test_init(self):
        controller = VRController()
        assert not controller.is_connected

    def test_connect(self):
        controller = VRController()
        assert controller.connect()
        assert controller.is_connected

    def test_get_state_disconnected(self):
        controller = VRController()
        assert controller.get_state() is None

    def test_get_state_connected(self):
        controller = VRController()
        controller.connect()
        state = controller.get_state()
        assert state is not None
        assert state.head_position.shape == (3,)

    def test_disconnect(self):
        controller = VRController()
        controller.connect()
        controller.disconnect()
        assert not controller.is_connected


class TestKeyboardController:
    def test_init(self):
        controller = KeyboardController()
        assert controller.style == "walk"

    def test_set_style(self):
        controller = KeyboardController()
        controller.set_style("run")
        assert controller.style == "run"

    def test_invalid_style(self):
        controller = KeyboardController()
        with pytest.raises(ValueError):
            controller.set_style("flying")

    def test_get_command(self):
        controller = KeyboardController()
        cmd = controller.get_command()
        assert "linear_x" in cmd
        assert "style" in cmd


class TestGamepadController:
    def test_init(self):
        controller = GamepadController()
        assert not controller.is_connected

    def test_connect(self):
        controller = GamepadController()
        assert controller.connect()
