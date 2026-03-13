# VR Whole-Body Teleoperation

Sentient-SONIC supports real-time whole-body teleoperation via PICO VR headset.

## Requirements

- PICO 4 or PICO Neo 3 VR headset
- Wi-Fi connection (same network as control PC)
- ZMQ communication stack

## Setup

1. Install the Sentient-SONIC VR app on your PICO headset
2. Connect headset and PC to the same network
3. Start the ZMQ bridge on the control PC:

```bash
sentient-teleop --mode vr --zmq-host 0.0.0.0 --zmq-port 5555
```

4. Launch the VR app and connect to the control PC IP

## Tracking Modes

| Mode | Description | Tracked Points |
|------|-------------|----------------|
| Full Body | Head + hands + estimated lower body | 6 DOF |
| Upper Body | Head + hands only | 3 points |
| Hands Only | Hand tracking for manipulation | 2 points |

## Data Recording

Enable recording to save teleoperation demonstrations:

```yaml
recording:
  enable_recording: true
  output_dir: data/teleop_recordings/
  save_format: npz
```
