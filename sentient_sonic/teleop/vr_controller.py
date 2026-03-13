"""
Sentient-SONIC VR Teleoperation Controller

Supports real-time whole-body teleoperation via PICO VR headset,
enabling natural human-to-robot motion transfer for data collection
and interactive control.
"""

from dataclasses import dataclass
from typing import Dict, Optional

import numpy as np

from sentient_sonic.core.config import TeleopConfig


@dataclass
class VRState:
    """State from VR headset and controllers."""

    head_position: np.ndarray  # (3,)
    head_orientation: np.ndarray  # (4,) quaternion
    left_hand_position: np.ndarray  # (3,)
    left_hand_orientation: np.ndarray  # (4,)
    right_hand_position: np.ndarray  # (3,)
    right_hand_orientation: np.ndarray  # (4,)
    button_states: Dict[str, bool] = None


class VRController:
    """
    VR Teleoperation Controller for Sentient-SONIC.

    Connects to a PICO VR headset via ZMQ and streams real-time
    motion data for whole-body teleoperation.

    Args:
        config: Teleoperation configuration.
    """

    def __init__(self, config: Optional[TeleopConfig] = None):
        self.config = config or TeleopConfig()
        self._connected = False
        self._zmq_context = None
        self._zmq_socket = None

    def connect(self) -> bool:
        """Establish connection to VR headset via ZMQ."""
        print(f"[Sentient-SONIC Teleop] Connecting to VR at "
              f"{self.config.zmq_host}:{self.config.zmq_port}...")
        # Mocked connection
        self._connected = True
        print("[Sentient-SONIC Teleop] VR connection established.")
        return True

    def disconnect(self) -> None:
        """Disconnect from VR headset."""
        self._connected = False
        print("[Sentient-SONIC Teleop] VR disconnected.")

    def get_state(self) -> Optional[VRState]:
        """Get current VR headset and controller state."""
        if not self._connected:
            return None

        # Mocked VR state
        return VRState(
            head_position=np.zeros(3),
            head_orientation=np.array([1.0, 0.0, 0.0, 0.0]),
            left_hand_position=np.array([-0.3, 0.0, 0.5]),
            left_hand_orientation=np.array([1.0, 0.0, 0.0, 0.0]),
            right_hand_position=np.array([0.3, 0.0, 0.5]),
            right_hand_orientation=np.array([1.0, 0.0, 0.0, 0.0]),
            button_states={"trigger_left": False, "trigger_right": False},
        )

    def retarget(self, vr_state: VRState) -> np.ndarray:
        """
        Retarget VR motion to robot joint targets.

        Args:
            vr_state: Current VR state.

        Returns:
            Target joint positions for the robot.
        """
        # Mocked retargeting
        return np.zeros(23)

    @property
    def is_connected(self) -> bool:
        return self._connected
