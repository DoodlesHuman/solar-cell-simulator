class SolarCellSim:
    def __init__(self, carriers, field, dt = 0.01, steps = 100):
        self.carriers = carriers
        self.field = field
        self.dt = dt
        self.steps = steps
        self.trajectory = []

    def run(self):
        for _ in range(self.steps):
            step_data = []
            for c in self.carriers:
                c.move(self.field, self.dt)
                step_data.append(c.position)
            self.trajectory.append(step_data)