"""Tests for robot definitions."""

import pytest

from sentient_sonic.utils.robot_definitions import (
    UNITREE_G1, FOURIER_GR1, get_robot, SUPPORTED_ROBOTS,
)


class TestRobotDefinitions:
    def test_unitree_g1(self):
        robot = UNITREE_G1
        assert robot.name == "unitree_g1"
        assert robot.num_joints == 23
        assert len(robot.joints) == 23
        assert robot.base_height > 0

    def test_fourier_gr1(self):
        robot = FOURIER_GR1
        assert robot.name == "fourier_gr1"
        assert robot.num_joints == 32

    def test_get_robot(self):
        robot = get_robot("unitree_g1")
        assert robot.name == "unitree_g1"

    def test_get_robot_unknown(self):
        with pytest.raises(ValueError, match="Unknown robot"):
            get_robot("unknown_robot")

    def test_joint_limits(self):
        for joint in UNITREE_G1.joints:
            assert joint.lower_limit < joint.upper_limit
            assert joint.max_velocity > 0
            assert joint.max_torque > 0
