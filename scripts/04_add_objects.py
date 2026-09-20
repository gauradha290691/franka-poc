from isaacsim import SimulationApp

simulation_app = SimulationApp({
    "headless": False
})

from isaacsim.core.api import World

world = World()

print("Object environment initialized")

# Triangle object will be added here.
# Target cube will be added here.

world.reset()

while simulation_app.is_running():
    world.step(render=True)

simulation_app.close()
