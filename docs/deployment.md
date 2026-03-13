# Deployment Guide

## Supported Platforms

| Platform | Interface | Status |
|----------|-----------|--------|
| Unitree G1 | Unitree SDK 2.0 | Supported |
| Fourier GR1 | Fourier SDK | Experimental |
| Simulation | Isaac Gym / MuJoCo | Supported |

## C++ Deployment

The `sentient_sonic_deploy` module provides a high-performance C++ runtime:

```bash
cd sentient_sonic_deploy
mkdir build && cd build
cmake .. -DONNXRUNTIME_ROOT=/opt/onnxruntime-1.17.0
make -j$(nproc)

# Run deployment
./sentient_deploy checkpoints/policy.onnx 192.168.1.100 8080
```

## Safety System

The deployment includes a multi-level safety controller:

| Level | Status | Action |
|-------|--------|--------|
| 0 | NOMINAL | Normal operation |
| 1 | WARNING | Reduced velocity limits |
| 2 | CRITICAL | Minimal movement only |
| 3 | EMERGENCY_STOP | All joints locked |
