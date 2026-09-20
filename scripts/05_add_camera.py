from isaacsim import SimulationApp

simulation_app = SimulationApp({
    "headless": False
})

from isaacsim.core.api import World

world = World()

print("Camera environment initialized")

# RGB-D camera will be added here.
#
# Camera output:
# RGB image
# Depth image
#
# Later:
# RGB image -> object detection
# Depth + pixel -> 3D position
# 3D position -> robot coordinates

world.reset()

while simulation_app.is_running():
    world.step(render=True)

simulation_app.close()
