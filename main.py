## main.py
import sys
from simulation import Simulation
from interface import Interface
from web_interface import app

def main():
    # Initialize the simulation with default values
    simulation = Simulation(frequency=440, amplitude=100)
    
    # Check if the script is run with a 'web' argument to start the web interface
    if len(sys.argv) > 1 and sys.argv[1] == 'web':
        app.run(debug=True)
    else:
        # Initialize the Pygame interface and start the simulation
        interface = Interface(simulation)
        interface.run()

if __name__ == "__main__":
    main()
