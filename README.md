# Franka PPO Pick-and-Place POC

## Goal

Train a Franka robot in NVIDIA Isaac Sim using PPO reinforcement learning.

## Scenario

- Franka robot arm
- Conveyor belt
- Triangular object
- Target cube
- Physics simulation
- RGB-D camera
- PPO reinforcement learning

## Architecture

Camera
→ Object Detection
→ 3D Object Position
→ Robot Coordinate
→ PPO Policy
→ Franka Action
→ Physics
→ Reward
→ PPO Update

## Training

The initial PPO environment will use numerical observations
such as robot position, object position and target position.

Camera perception will be added after the basic RL environment
is working.

## Project Structure

- `assets/` - USD assets and simulation scenes
- `scripts/` - Python simulation and training code
- `checkpoints/` - trained PPO models
- `configs/` - training configuration

