# Decoupled Whole-Body Controller

The Decoupled WBC architecture splits control into independent lower body (RL) and upper body (IK) subsystems.

## When to Use

- When you need independent locomotion and manipulation
- When upper body tasks require precise IK solutions
- Compatible with Sentient Robotics N1.5 and N1.6 models

## API

```python
from decoupled_wbc import DecoupledWBController

controller = DecoupledWBController(
    robot_name="unitree_g1",
    lower_checkpoint="checkpoints/lower_body.pt",
)
controller.setup()

# In control loop:
action = controller.compute(
    observation=robot_state,
    locomotion_command={"linear_x": 0.5, "linear_y": 0.0, "angular_z": 0.1},
    ee_targets={"left_hand": np.array([0.3, 0.2, 0.8])},
)
```
