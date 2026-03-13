"""
Sentient-SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control

This module provides the teleoperation stack for collecting demonstration data
and controlling humanoid robots via VR, keyboard, and gamepad interfaces.
"""

__version__ = "0.1.0"
__project__ = "Sentient Robotics"

from sentient_sonic.core.policy import SonicPolicy
from sentient_sonic.core.config import SonicConfig

__all__ = [
    "SonicPolicy",
    "SonicConfig",
    "__version__",
    "__project__",
]
