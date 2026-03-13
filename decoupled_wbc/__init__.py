"""
Decoupled Whole-Body Controller

The decoupled controller used in Sentient Robotics N1.5 and N1.6 models.
Uses RL for lower body locomotion and IK for upper body manipulation.
"""

__version__ = "0.1.0"

from decoupled_wbc.controller import DecoupledWBController
from decoupled_wbc.lower_body import LowerBodyPolicy
from decoupled_wbc.upper_body import UpperBodyIK

__all__ = ["DecoupledWBController", "LowerBodyPolicy", "UpperBodyIK"]
