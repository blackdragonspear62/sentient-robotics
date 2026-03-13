# Training Guide

## Prerequisites

- NVIDIA GPU with 24+ GB VRAM (RTX 4090 or A100 recommended)
- Isaac Gym or Isaac Lab installed
- Large-scale motion dataset (AMASS format)

## Training Pipeline

1. **Data Preparation**: Preprocess motion data
2. **Environment Setup**: Configure simulation
3. **Policy Training**: PPO with motion tracking reward
4. **Evaluation**: Test on held-out motions
5. **Export**: Convert to ONNX for deployment

## Launch Training

```bash
python -m sentient_sonic.core.trainer \
    --config sentient_sonic/configs/train_sonic_base.yaml
```

## Hyperparameters

| Parameter | Base | Large |
|-----------|------|-------|
| Num Envs | 4096 | 8192 |
| Hidden Dims | [512, 256, 128] | [1024, 512, 256] |
| Learning Rate | 3e-4 | 1e-4 |
| Total Steps | 100M | 500M |
| History Length | 10 | 15 |
