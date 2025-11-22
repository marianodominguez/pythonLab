import argparse
from simulation import Simulation

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Particle Simulation")
    parser.add_argument("--width", type=int, default=800, help="Window width")
    parser.add_argument("--height", type=int, default=600, help="Window height")
    parser.add_argument("--count", type=int, default=50, help="Number of particles")
    
    args = parser.parse_args()
    
    sim = Simulation(width=args.width, height=args.height, num_particles=args.count)
    sim.run()
