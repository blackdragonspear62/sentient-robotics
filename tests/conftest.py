"""Shared test fixtures for Sentient Robotics test suite."""

import numpy as np
import pytest


@pytest.fixture
def sample_observation():
    """Create a sample robot observation for testing."""
    return {
        "joint_pos": np.random.randn(23) * 0.1,
        "joint_vel": np.random.randn(23) * 0.5,
        "base_quat": np.array([1.0, 0.0, 0.0, 0.0]),
        "base_ang_vel": np.random.randn(3) * 0.1,
        "base_lin_vel": np.random.randn(3) * 0.1,
        "projected_gravity": np.array([0.0, 0.0, -9.81]),
    }


@pytest.fixture
def sample_locomotion_command():
    """Create a sample locomotion command."""
    return {
        "linear_x": 0.5,
        "linear_y": 0.0,
        "angular_z": 0.1,
    }
