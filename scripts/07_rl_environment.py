"""
Franka Pick-and-Place RL Environment

This file defines:

Observation:
    What the robot/PPO can see

Action:
    What PPO can command

Reward:
    How we tell PPO whether the action was good
"""


class FrankaPickPlaceEnv:

    def __init__(self):

        # What PPO observes
        self.observation = {
            "franka_position": [0, 0, 0],
            "object_position": [0, 0, 0],
            "target_position": [0, 0, 0]
        }

        # What PPO can control
        self.action = {
            "move_x": 0,
            "move_y": 0,
            "move_z": 0,
            "gripper": 0
        }

    def reset(self):

        print("Environment reset")

        # Later:
        # Reset Franka
        # Reset object
        # Reset conveyor

    def step(self, action):

        print("Action:", action)

        # Later:
        # 1. Send action to Franka
        # 2. Run physics
        # 3. Observe new state
        # 4. Calculate reward

        reward = 0

        return self.observation, reward
