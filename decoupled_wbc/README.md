# Decoupled Whole-Body Controller

The **Decoupled WBC** is the controller architecture used in Sentient Robotics N1.5 and N1.6 models. It splits humanoid control into two independent subsystems:

- **Lower Body**: RL-based locomotion policy trained with PPO
- **Upper Body**: Optimization-based IK solver for manipulation

## Architecture

```
                    ┌─────────────────────┐
                    │   Task Planner      │
                    │  (Locomotion Cmd +  │
                    │   EE Targets)       │
                    └─────────┬───────────┘
                              │
                    ┌─────────▼───────────┐
                    │  Decoupled WBC      │
                    │  Controller         │
                    └──┬──────────────┬───┘
                       │              │
              ┌────────▼─────┐  ┌─────▼────────┐
              │ Lower Body   │  │ Upper Body   │
              │ RL Policy    │  │ IK Solver    │
              │ (12 joints)  │  │ (11 joints)  │
              └────────┬─────┘  └─────┬────────┘
                       │              │
                    ┌──▼──────────────▼───┐
                    │   Joint Merger      │
                    │   (23 joints)       │
                    └─────────┬───────────┘
                              │
                    ┌─────────▼───────────┐
                    │   Robot Hardware    │
                    └─────────────────────┘
```

## Quick Start

```python
from decoupled_wbc import DecoupledWBController

controller = DecoupledWBController(robot_name="unitree_g1")
controller.setup()

action = controller.compute(
    observation=obs,
    locomotion_command={"linear_x": 0.5, "linear_y": 0.0, "angular_z": 0.0},
    ee_targets={"left_hand": target_pos},
)
```

For detailed documentation, see the [Decoupled WBC Guide](../docs/decoupled_wbc.md).
