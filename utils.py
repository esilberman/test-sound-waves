## utils.py
from typing import Tuple

class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def add(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x + other.x, self.y + other.y)

    def multiply(self, scalar: float) -> 'Vector2D':
        return Vector2D(self.x * scalar, self.y * scalar)

class Utils:
    @staticmethod
    def calculate_wave_impact(particle_position: Tuple[float, float], 
                              sound_source_position: Tuple[float, float], 
                              frequency: int, amplitude: int) -> Vector2D:
        """
        Calculate the impact of the sound wave on a particle given the particle's position
        and the sound source's properties.

        :param particle_position: A tuple representing the (x, y) position of the particle.
        :param sound_source_position: A tuple representing the (x, y) position of the sound source.
        :param frequency: The frequency of the sound wave emitted by the sound source.
        :param amplitude: The amplitude of the sound wave emitted by the sound source.
        :return: A Vector2D object representing the velocity change of the particle due to the sound wave.
        """
        # Placeholder for actual wave impact calculation logic
        # This should be replaced with a scientifically accurate model
        distance_x = particle_position[0] - sound_source_position[0]
        distance_y = particle_position[1] - sound_source_position[1]
        distance = (distance_x**2 + distance_y**2)**0.5

        # Simple model: wave impact decreases with distance and is influenced by frequency and amplitude
        impact_strength = amplitude / (distance + 1) * frequency
        impact_x = impact_strength * (distance_x / distance)
        impact_y = impact_strength * (distance_y / distance)

        return Vector2D(impact_x, impact_y)
