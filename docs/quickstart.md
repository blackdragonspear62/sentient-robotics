# Quick Start

## Run Keyboard Control Demo

```bash
sentient-teleop --mode keyboard --style walk
```

## Run VR Teleoperation

```bash
sentient-teleop --mode vr --zmq-host localhost --zmq-port 5555
```

## Deploy on Unitree G1

```bash
sentient-deploy --config sentient_sonic/configs/deploy_g1.yaml \
    --checkpoint checkpoints/sentient-sonic-base/policy.onnx \
    --robot-ip 192.168.1.100
```

## Train a Policy

```bash
python -m sentient_sonic.core.trainer \
    --config sentient_sonic/configs/train_sonic_base.yaml
```

## Download Pretrained Checkpoints

```bash
python download_from_hf.py --model sentient-sonic-base
```
