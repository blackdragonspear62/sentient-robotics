# Installation Guide

## Prerequisites

- Python 3.8+
- CUDA 11.8+ (for GPU training)
- Git LFS

## Clone Repository

```bash
git clone https://github.com/SentientRobotics/sentient-robotics.git
cd sentient-robotics
git lfs pull
```

## Install Package

```bash
# Basic installation
pip install -e .

# With development tools
pip install -e ".[dev]"

# With deployment dependencies
pip install -e ".[deploy]"

# With teleoperation dependencies
pip install -e ".[teleop]"
```

## C++ Deployment Stack

```bash
cd sentient_sonic_deploy
mkdir build && cd build
cmake .. -DONNXRUNTIME_ROOT=/path/to/onnxruntime
make -j$(nproc)
```

## Verify Installation

```python
import sentient_sonic
print(sentient_sonic.__version__)  # 0.1.0
```
