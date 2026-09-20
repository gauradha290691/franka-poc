from isaacsim import SimulationApp

simulation_app = SimulationApp({
    "headless": False
})

from isaacsim.core.api import World
from isaacsim.core.api.objects import DynamicCuboid

world = World()

cube = world.scene.add(
    DynamicCuboid(
        prim_path="/World/Cube",
        name="cube",
        position=[0, 0, 1],
        scale=[1, 1, 1],
        color=[1, 0, 0]
    )
)

world.reset()

print("World created successfully!")

while simulation_app.is_running():
    world.step(render=True)

simulation_app.close()

