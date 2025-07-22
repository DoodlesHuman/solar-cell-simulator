from src.utils import timeit, log_step

class SolarCellSim:
    def __init__(self, carriers, field, dt = 0.01, steps = 100):
        self.carriers = carriers
        self.field = field
        self.dt = dt
        self.steps = steps
        self.trajectory = []

@timeit
def run(self):
    for _ in range(self.steps):
        self.run_step()

@log_step
def run_step(self):
    positions = []
    for c in self.carriers:
        c.move(self.field, self.dt)
        positions.append((c.charge_type, c.position))
    self.trajectory.append(positions)

"""
    def run(self):
        for _ in range(self.steps):
            step_data = []
            for c in self.carriers:
                c.move(self.field, self.dt)
                step_data.append(c.position)
            self.trajectory.append(step_data)
"""