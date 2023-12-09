## sound_source.py
from typing import Tuple

class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def add(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x + other.x, self.y + other.y)

    def multiply(self, scalar: float) -> 'Vector2D':
        return Vector2D(self.x * scalar, self.y * scalar)

class SoundSource:
    def __init__(self, x: float, y: float, frequency: int = 440, amplitude: int = 100):
        self.x = x
        self.y = y
        self.frequency = frequency
        self.amplitude = amplitude

    def emit_sound(self) -> Tuple[int, int]:
        """
        Emit sound from the sound source. This function would be called by the simulation
        to trigger the sound wave emission.

        :return: A tuple containing the frequency and amplitude of the emitted sound wave.
        """
        return (self.frequency, self.amplitude)
