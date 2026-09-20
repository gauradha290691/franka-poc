from isaacsim import SimulationApp

simulation_app = SimulationApp({
    "headless": False
})

from isaacsim.core.api import World

world = World()

print("Physics test initialized")

# Later we will test:
#
# 1. Gravity
# 2. Object collision
# 3. Franka movement
# 4. Gripper contact
# 5. Object movement
#
# These must work before PPO training.

world.reset()

for i in range(1000):
    if not simulation_app.is_running():
        break

    world.step(render=True)

print("Physics test finished")

simulation_app.close()
