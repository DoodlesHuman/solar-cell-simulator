from src.simulation import SolarCellSim
from src.field import ElectricField
from src.light_model import generate_carriers
import src.utils
import os

os.makedirs("data/output", exist_ok = True)

def main():
    carriers = generate_carriers(10, 0.0, 1.0)
    field = ElectricField(1.0)
    sim = SolarCellSim(carriers, field, dt = 0.01, steps = 50)
    sim.run()

    print("[INFO] Simulation complete. Trajectory length:", len(sim.trajectory))
    print("[INFO] Check data/output/simulation.log for logs.")

if __name__ == "__main__":
    main()