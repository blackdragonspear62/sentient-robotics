# External Dependencies

This directory contains build scripts and patches for external dependencies
required by the Sentient-SONIC deployment stack.

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| ONNX Runtime | >= 1.17.0 | Neural network inference |
| Eigen3 | >= 3.3 | Linear algebra |
| yaml-cpp | >= 0.7 | Configuration parsing |
| ZeroMQ | >= 4.3 | Inter-process communication |
| Unitree SDK | >= 2.0 | Robot hardware interface |

## Installation

```bash
bash install_deps.sh
```
