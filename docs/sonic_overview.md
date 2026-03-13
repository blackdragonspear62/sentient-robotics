# Sentient-SONIC Overview

**Sentient-SONIC** is a humanoid behavior foundation model that gives robots a core set of motor skills learned from large-scale human motion data.

## Key Features

- **Motion Tracking**: Uses motion tracking as a scalable training task
- **Unified Policy**: Single policy for walking, crawling, teleoperation, and more
- **Generalization**: Generalizes beyond training motions
- **Foundation Model**: Serves as foundation for higher-level planning

## Supported Behaviors

| Category | Behaviors |
|----------|-----------|
| Locomotion | Walking, Running, Sideways, Turning |
| Ground | Kneeling, Hand Crawling, Elbow Crawling |
| Recovery | Getting Up (prone/supine) |
| Athletic | Jumping, Boxing |
| Manipulation | Bimanual, Object Hand-off |
| Expressive | Happy, Stealth, Injured |

## Architecture

The SONIC policy uses a temporal encoder followed by an MLP actor-critic:

1. **Observation Encoding**: Joint states, base IMU, projected gravity
2. **Temporal Encoder**: 1D convolutions over motion history
3. **Latent Space**: 256-dim representation
4. **Actor Head**: Outputs target joint positions
5. **Critic Head**: Estimates value function

Training uses PPO with motion tracking reward on 4096+ parallel environments.
