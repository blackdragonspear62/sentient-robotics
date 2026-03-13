"""Tests for Sentient-SONIC transform utilities."""

import numpy as np
import pytest

from sentient_sonic.utils.transforms import (
    quat_to_rot, rot_to_quat, euler_to_quat,
    quat_multiply, quat_inverse, slerp,
)


class TestTransforms:
    def test_identity_quat_to_rot(self):
        q = np.array([1.0, 0.0, 0.0, 0.0])
        R = quat_to_rot(q)
        np.testing.assert_allclose(R, np.eye(3), atol=1e-7)

    def test_rot_to_quat_identity(self):
        R = np.eye(3)
        q = rot_to_quat(R)
        np.testing.assert_allclose(np.abs(q), [1, 0, 0, 0], atol=1e-7)

    def test_roundtrip(self):
        q_orig = np.array([0.7071, 0.7071, 0.0, 0.0])
        q_orig = q_orig / np.linalg.norm(q_orig)
        R = quat_to_rot(q_orig)
        q_back = rot_to_quat(R)
        # Quaternions can differ by sign
        assert np.allclose(q_orig, q_back, atol=1e-5) or np.allclose(q_orig, -q_back, atol=1e-5)

    def test_euler_to_quat_zero(self):
        q = euler_to_quat(0, 0, 0)
        np.testing.assert_allclose(q, [1, 0, 0, 0], atol=1e-7)

    def test_quat_multiply_identity(self):
        q = np.array([0.5, 0.5, 0.5, 0.5])
        identity = np.array([1.0, 0.0, 0.0, 0.0])
        result = quat_multiply(q, identity)
        np.testing.assert_allclose(result, q, atol=1e-7)

    def test_quat_inverse(self):
        q = np.array([0.5, 0.5, 0.5, 0.5])
        q_inv = quat_inverse(q)
        result = quat_multiply(q, q_inv)
        np.testing.assert_allclose(result, [1, 0, 0, 0], atol=1e-7)

    def test_slerp_endpoints(self):
        q1 = np.array([1.0, 0.0, 0.0, 0.0])
        q2 = np.array([0.0, 1.0, 0.0, 0.0])
        np.testing.assert_allclose(slerp(q1, q2, 0.0), q1, atol=1e-5)
        np.testing.assert_allclose(slerp(q1, q2, 1.0), q2, atol=1e-5)
