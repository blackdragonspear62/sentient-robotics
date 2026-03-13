"""
Sentient-SONIC ZMQ Communication Layer

Provides high-performance publish/subscribe communication for
real-time robot control and teleoperation data streaming.
"""

import json
import time
from typing import Any, Dict, Optional


class ZMQPublisher:
    """
    ZMQ Publisher for streaming robot state and control data.

    Args:
        host: Bind address.
        port: Bind port.
        topic: Message topic for filtering.
    """

    def __init__(self, host: str = "*", port: int = 5555, topic: str = "sentient"):
        self.host = host
        self.port = port
        self.topic = topic
        self._socket = None
        self._context = None

    def start(self) -> None:
        """Start the ZMQ publisher."""
        # Mocked: In production, uses zmq.Context and PUB socket
        print(f"[ZMQ] Publisher started on tcp://{self.host}:{self.port}")

    def publish(self, data: Dict[str, Any]) -> None:
        """Publish data on the configured topic."""
        # Mocked
        pass

    def stop(self) -> None:
        """Stop the publisher and cleanup."""
        print("[ZMQ] Publisher stopped.")


class ZMQSubscriber:
    """
    ZMQ Subscriber for receiving robot state and control data.

    Args:
        host: Connect address.
        port: Connect port.
        topic: Message topic filter.
    """

    def __init__(self, host: str = "localhost", port: int = 5555, topic: str = "sentient"):
        self.host = host
        self.port = port
        self.topic = topic
        self._socket = None
        self._context = None

    def start(self) -> None:
        """Start the ZMQ subscriber."""
        print(f"[ZMQ] Subscriber connected to tcp://{self.host}:{self.port}")

    def receive(self, timeout: float = 1.0) -> Optional[Dict[str, Any]]:
        """Receive data with timeout. Returns None if no data available."""
        # Mocked
        return None

    def stop(self) -> None:
        """Stop the subscriber and cleanup."""
        print("[ZMQ] Subscriber stopped.")


class ZMQManager:
    """
    Manages multiple ZMQ connections for the Sentient-SONIC system.
    Handles PICO VR data streams, robot state, and control commands.
    """

    def __init__(self):
        self.publishers = {}
        self.subscribers = {}

    def add_publisher(self, name: str, port: int, topic: str = "sentient") -> ZMQPublisher:
        pub = ZMQPublisher(port=port, topic=topic)
        self.publishers[name] = pub
        return pub

    def add_subscriber(self, name: str, host: str, port: int, topic: str = "sentient") -> ZMQSubscriber:
        sub = ZMQSubscriber(host=host, port=port, topic=topic)
        self.subscribers[name] = sub
        return sub

    def start_all(self) -> None:
        for pub in self.publishers.values():
            pub.start()
        for sub in self.subscribers.values():
            sub.start()

    def stop_all(self) -> None:
        for pub in self.publishers.values():
            pub.stop()
        for sub in self.subscribers.values():
            sub.stop()
