## particle.py
from typing import Tuple

class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def add(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x + other.x, self.y + other.y)

    def multiply(self, scalar: float) -> 'Vector2D':
        return Vector2D(self.x * scalar, self.y * scalar)

class Particle:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.velocity = Vector2D(0.0, 0.0)

    def update_position(self, delta_time: float = 1.0) -> None:
        """
        Update the particle's position based on its velocity and the time elapsed.

        :param delta_time: The time elapsed since the last update.
        """
        self.x += self.velocity.x * delta_time
        self.y += self.velocity.y * delta_time

    def apply_force(self, force: Vector2D) -> None:
        """
        Apply a force to the particle, changing its velocity.

        :param force: A Vector2D representing the force to be applied.
        """
        self.velocity = self.velocity.add(force)

    def reset_velocity(self) -> None:
        """
        Reset the particle's velocity to zero.
        """
        self.velocity = Vector2D(0.0, 0.0)
