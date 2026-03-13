"""
Sentient-SONIC Keyboard Controller

Provides keyboard-based locomotion control for the kinematic planner.
Choose a movement style, steer with keyboard, and adjust speed/height.
"""

from typing import Dict, Optional

import numpy as np


class KeyboardController:
    """
    Keyboard-based locomotion controller for Sentient-SONIC.

    Supports movement styles: walk, run, stealth, happy, injured,
    kneeling, hand crawling, elbow crawling, boxing.

    Usage:
        controller = KeyboardController()
        controller.start()
        while running:
            command = controller.get_command()
            # Send command to policy
    """

    MOVEMENT_STYLES = [
        "walk", "run", "stealth", "happy", "injured",
        "kneeling", "hand_crawling", "elbow_crawling", "boxing",
    ]

    KEY_BINDINGS = {
        "w": "forward",
        "s": "backward",
        "a": "left",
        "d": "right",
        "q": "turn_left",
        "e": "turn_right",
        "space": "stop",
        "up": "speed_up",
        "down": "speed_down",
        "1-9": "select_style",
    }

    def __init__(self, style: str = "walk", speed: float = 1.0):
        self.style = style
        self.speed = speed
        self._running = False

    def start(self) -> None:
        """Start the keyboard controller."""
        self._running = True
        print("[Sentient-SONIC] Keyboard controller started.")
        print(f"[Sentient-SONIC] Style: {self.style}, Speed: {self.speed}")

    def stop(self) -> None:
        """Stop the keyboard controller."""
        self._running = False
        print("[Sentient-SONIC] Keyboard controller stopped.")

    def get_command(self) -> Dict[str, float]:
        """Get current locomotion command from keyboard input."""
        # Mocked: returns zero command
        return {
            "linear_x": 0.0,
            "linear_y": 0.0,
            "angular_z": 0.0,
            "height": 0.0,
            "style": self.style,
        }

    def set_style(self, style: str) -> None:
        """Set the movement style."""
        if style not in self.MOVEMENT_STYLES:
            raise ValueError(f"Unknown style: {style}. Available: {self.MOVEMENT_STYLES}")
        self.style = style
        print(f"[Sentient-SONIC] Movement style set to: {style}")
