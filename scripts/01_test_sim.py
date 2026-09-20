from isaacsim import SimulationApp

simulation_app = SimulationApp({
    "headless": False
})

print("Isaac Sim started successfully!")

simulation_app.update()

input("Press Enter to close...")

simulation_app.close()
