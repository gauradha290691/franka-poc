from isaacsim import SimulationApp

simulation_app = SimulationApp({
    "headless": False
})

from isaacsim.core.api import World

world = World()

print("Franka simulation environment initialized")

# Franka robot will be added here.
# We will use the Isaac Sim Franka asset on the NVIDIA machine.

world.reset()

while simulation_app.is_running():
    world.step(render=True)

simulation_app.close()
