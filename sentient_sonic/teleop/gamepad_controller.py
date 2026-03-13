"""
Sentient-SONIC Gamepad Controller

Provides gamepad-based locomotion control for the kinematic planner.
Supports standard USB/Bluetooth gamepads for steering and speed control.
"""

from typing import Dict, Optional

import numpy as np


class GamepadController:
    """
    Gamepad-based locomotion controller for Sentient-SONIC.

    Supports standard gamepad input for controlling humanoid locomotion
    with analog stick steering and trigger-based speed modulation.
    """

    def __init__(self, device_id: int = 0):
        self.device_id = device_id
        self._connected = False

    def connect(self) -> bool:
        """Connect to gamepad device."""
        print(f"[Sentient-SONIC] Connecting to gamepad {self.device_id}...")
        # Mocked connection
        self._connected = True
        print("[Sentient-SONIC] Gamepad connected.")
        return True

    def disconnect(self) -> None:
        """Disconnect gamepad."""
        self._connected = False

    def get_command(self) -> Dict[str, float]:
        """Get locomotion command from gamepad input."""
        if not self._connected:
            return {"linear_x": 0.0, "linear_y": 0.0, "angular_z": 0.0}

        # Mocked: returns zero command
        return {
            "linear_x": 0.0,
            "linear_y": 0.0,
            "angular_z": 0.0,
            "height": 0.0,
        }

    @property
    def is_connected(self) -> bool:
        return self._connected
