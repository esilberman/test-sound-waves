## web_interface.py
from flask import Flask, jsonify, request
from simulation import Simulation
from interface import Interface

app = Flask(__name__)

# Initialize the simulation with default values
simulation = Simulation(frequency=440, amplitude=100)
interface = Interface(simulation)

@app.route('/simulate', methods=['GET'])
def get_simulation_state():
    """
    Endpoint to retrieve the current state of the simulation.
    Returns a JSON object containing the current state of the simulation.
    """
    # Construct the simulation state data structure
    simulation_state = {
        'particles': [
            {'x': particle.x, 'y': particle.y, 'velocity': {'x': particle.velocity.x, 'y': particle.velocity.y}}
            for particle in simulation.particles
        ],
        'soundSource': {
            'x': simulation.sound_source.x,
            'y': simulation.sound_source.y,
            'frequency': simulation.sound_source.frequency,
            'amplitude': simulation.sound_source.amplitude
        },
        'isPlaying': simulation.is_playing
    }
    return jsonify(simulation_state)

@app.route('/control', methods=['POST'])
def control_simulation():
    """
    Endpoint to control the simulation (start, stop, adjust parameters).
    Expects a JSON object with the control command and parameters.
    """
    control_data = request.get_json()
    action = control_data.get('action')

    if action == 'start':
        simulation.is_playing = True
    elif action == 'stop':
        simulation.is_playing = False
    elif action == 'adjust':
        frequency = control_data.get('frequency', simulation.frequency)
        amplitude = control_data.get('amplitude', simulation.amplitude)
        simulation.frequency = frequency
        simulation.amplitude = amplitude

    return jsonify({'status': 'success', 'action': action})

if __name__ == '__main__':
    app.run(debug=True)
