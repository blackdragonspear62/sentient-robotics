#!/bin/bash
# Sentient Robotics — Full Installation Script
set -e

echo "=========================================="
echo "  Sentient Robotics Installation"
echo "=========================================="

# Check Python version
python3 -c "import sys; assert sys.version_info >= (3, 8), 'Python 3.8+ required'"

# Install Python package
echo "[1/3] Installing Python package..."
pip install -e ".[dev,deploy,teleop]"

# Install external dependencies
echo "[2/3] Installing external dependencies..."
bash external_dependencies/install_deps.sh

# Build C++ deployment stack
echo "[3/3] Building C++ deployment stack..."
cd sentient_sonic_deploy
mkdir -p build && cd build
cmake .. -DONNXRUNTIME_ROOT=/opt/onnxruntime
make -j$(nproc)
cd ../..

echo ""
echo "=========================================="
echo "  Installation Complete!"
echo "=========================================="
echo ""
echo "Verify: python -c \"import sentient_sonic; print(sentient_sonic.__version__)\""
echo "Help:   make help"
