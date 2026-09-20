"""
Evaluate the trained Franka PPO policy.

The trained model will be loaded from:

checkpoints/franka_ppo.pth
"""

print("Evaluation script")

MODEL_PATH = "checkpoints/franka_ppo.pth"

print("Loading model:", MODEL_PATH)

# Later:
#
# Load Isaac Sim
# Load Franka environment
# Load trained PPO checkpoint
# Run the policy
# Observe the robot picking and placing the object

print("Evaluation configuration ready")
