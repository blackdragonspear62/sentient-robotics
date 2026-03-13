"""
Sentient-SONIC Teleoperation CLI

Command-line interface for launching teleoperation sessions.
"""

import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(
        description="Sentient-SONIC Teleoperation CLI"
    )
    parser.add_argument(
        "--mode",
        type=str,
        default="keyboard",
        choices=["vr", "keyboard", "gamepad"],
        help="Teleoperation mode (default: keyboard)",
    )
    parser.add_argument(
        "--robot",
        type=str,
        default="unitree_g1",
        help="Robot type (default: unitree_g1)",
    )
    parser.add_argument(
        "--style",
        type=str,
        default="walk",
        help="Movement style (default: walk)",
    )
    parser.add_argument(
        "--zmq-host",
        type=str,
        default="localhost",
        help="ZMQ host for VR mode (default: localhost)",
    )
    parser.add_argument(
        "--zmq-port",
        type=int,
        default=5555,
        help="ZMQ port for VR mode (default: 5555)",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    print("=" * 60)
    print("Sentient-SONIC Teleoperation System")
    print("=" * 60)
    print(f"Mode: {args.mode}")
    print(f"Robot: {args.robot}")

    if args.mode == "vr":
        from sentient_sonic.teleop.vr_controller import VRController
        from sentient_sonic.core.config import TeleopConfig

        config = TeleopConfig(zmq_host=args.zmq_host, zmq_port=args.zmq_port)
        controller = VRController(config=config)
        controller.connect()
        print("[INFO] VR teleoperation session started. Press Ctrl+C to stop.")

    elif args.mode == "keyboard":
        from sentient_sonic.teleop.keyboard_controller import KeyboardController

        controller = KeyboardController(style=args.style)
        controller.start()
        print("[INFO] Keyboard control session started. Press Ctrl+C to stop.")

    elif args.mode == "gamepad":
        from sentient_sonic.teleop.gamepad_controller import GamepadController

        controller = GamepadController()
        controller.connect()
        print("[INFO] Gamepad control session started. Press Ctrl+C to stop.")

    # Mocked: In production, this would enter the main control loop
    print("[INFO] (Mocked) Control loop would run here.")


if __name__ == "__main__":
    main()
