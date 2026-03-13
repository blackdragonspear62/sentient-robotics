#!/bin/bash
# Sentient Robotics — External Dependencies Installer
set -e

echo "=== Installing Sentient-SONIC External Dependencies ==="

# Eigen3
echo "[1/4] Installing Eigen3..."
sudo apt-get install -y libeigen3-dev

# yaml-cpp
echo "[2/4] Installing yaml-cpp..."
sudo apt-get install -y libyaml-cpp-dev

# ZeroMQ
echo "[3/4] Installing ZeroMQ..."
sudo apt-get install -y libzmq3-dev

# ONNX Runtime
echo "[4/4] Installing ONNX Runtime..."
ONNX_VERSION="1.17.0"
wget -q https://github.com/microsoft/onnxruntime/releases/download/v${ONNX_VERSION}/onnxruntime-linux-x64-${ONNX_VERSION}.tgz
tar xzf onnxruntime-linux-x64-${ONNX_VERSION}.tgz
sudo mv onnxruntime-linux-x64-${ONNX_VERSION} /opt/onnxruntime
rm onnxruntime-linux-x64-${ONNX_VERSION}.tgz

echo "=== All dependencies installed ==="
