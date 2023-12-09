import numpy as np
from typing import List
from particle import Particle, Vector2D
from sound_source import SoundSource
from utils import Utils

class Simulation:
    def __init__(self, frequency: int = 440, amplitude: int = 100):
        self.particles: List[Particle] = []
        self.sound_source = SoundSource(x=0.0, y=0.0, frequency=frequency, amplitude=amplitude)
        self.frequency = frequency
        self.amplitude = amplitude
        self.is_playing = False

    def run(self) -> None:
        """
        Start the simulation. This will be the main loop that updates and renders the simulation.
        """
        self.is_playing = True
        while self.is_playing:
            self.update()
            self.render()

    def update(self) -> None:
        """
        Update the simulation state. This includes updating the position of particles and handling
        the sound wave propagation.
        """
        # Emit sound from the sound source
        sound_wave = self.sound_source.emit_sound()

        # Update each particle's position based on the sound wave impact
        for particle in self.particles:
            wave_impact = Utils.calculate_wave_impact(
                particle_position=(particle.x, particle.y),
                sound_source_position=(self.sound_source.x, self.sound_source.y),
                frequency=sound_wave[0],
                amplitude=sound_wave[1]
            )
            particle.apply_force(wave_impact)
            particle.update_position()

    def render(self) -> None:
        """
        Render the simulation state. This function would be responsible for drawing the particles
        and sound waves on the screen.
        """
        # Placeholder for rendering logic
        # This should be implemented using a graphics library like Pygame
        pass

    def add_particle(self, x: float, y: float) -> None:
        """
        Add a new particle to the simulation at the given (x, y) coordinates.

        :param x: The x-coordinate of the new particle.
        :param y: The y-coordinate of the new particle.
        """
        self.particles.append(Particle(x, y))

    def set_sound_source(self, x: float, y: float, frequency: int = None, amplitude: int = None) -> None:
        """
        Set the position and properties of the sound source.

        :param x: The new x-coordinate of the sound source.
        :param y: The new y-coordinate of the sound source.
        :param frequency: The new frequency of the sound source, if provided.
        :param amplitude: The new amplitude of the sound source, if provided.
        """
        self.sound_source.x = x
        self.sound_source.y = y
        if frequency is not None:
            self.sound_source.frequency = frequency
        if amplitude is not None:
            self.sound_source.amplitude = amplitude

    def toggle_playback(self) -> None:
        """
        Toggle the playback state of the simulation (play/pause).
        """
        self.is_playing = not self.is_playing
