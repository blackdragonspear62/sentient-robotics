# ZMQ Communication Protocol

Sentient-SONIC uses ZeroMQ for high-performance inter-process communication.

## Architecture

```
┌──────────┐     ZMQ PUB     ┌──────────────┐
│ VR App   │ ──────────────> │ Control PC   │
│ (PICO)   │     Port 5555   │              │
└──────────┘                  │  ┌─────────┐ │
                              │  │ Policy  │ │
┌──────────┐     ZMQ SUB     │  │ Infer   │ │
│ Robot    │ <────────────── │  └─────────┘ │
│ (G1)     │     Port 5556   │              │
└──────────┘                  └──────────────┘
```

## Message Format

Messages are serialized as JSON with the following structure:

```json
{
    "topic": "sentient/state",
    "timestamp": 1234567890.123,
    "data": {
        "joint_pos": [0.0, ...],
        "joint_vel": [0.0, ...],
        "base_quat": [1.0, 0.0, 0.0, 0.0]
    }
}
```

## Topics

| Topic | Direction | Description |
|-------|-----------|-------------|
| sentient/state | Robot → PC | Robot state at 200 Hz |
| sentient/command | PC → Robot | Control commands at 50 Hz |
| sentient/vr | VR → PC | VR tracking data at 72 Hz |
| sentient/safety | PC → Robot | Safety status updates |
