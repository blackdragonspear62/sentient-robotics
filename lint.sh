#!/bin/bash
# Sentient Robotics — Lint Script
# Runs code quality checks across the project

set -e

echo "=== Sentient Robotics Lint Suite ==="
echo ""

echo "[1/3] Running ruff..."
ruff check sentient_sonic/ decoupled_wbc/ --fix

echo "[2/3] Running black..."
black --check sentient_sonic/ decoupled_wbc/

echo "[3/3] Running isort..."
isort --check sentient_sonic/ decoupled_wbc/

echo ""
echo "=== All checks passed ==="
