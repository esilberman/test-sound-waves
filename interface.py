## interface.py
import pygame
from simulation import Simulation

class Interface:
    def __init__(self, simulation: Simulation):
        self.simulation = simulation
        self.running = True
        self.screen = None
        self.clock = None
        self.size = (800, 600)  # Default window size

    def run(self) -> None:
        """
        Initialize the interface and start the main event loop.
        """
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Sound Wave Simulator")
        self.clock = pygame.time.Clock()

        while self.running:
            self.handle_events()
            self.update_controls()
            self.simulation.update()
            self.render()
            pygame.display.flip()
            self.clock.tick(60)  # Run at 60 frames per second

    def handle_events(self) -> None:
        """
        Handle user input events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            # Additional event handling can be implemented here

    def update_controls(self) -> None:
        """
        Update the simulation controls based on user input.
        """
        # Placeholder for control update logic
        # This should include handling of sliders, buttons, etc.
        pass

    def render(self) -> None:
        """
        Render the simulation state to the screen.
        """
        self.screen.fill((255, 255, 255))  # Fill the screen with a white background
        # Placeholder for rendering the simulation state
        # This should include drawing particles, sound waves, and UI elements
        pass

    def set_simulation_parameters(self, frequency: int, amplitude: int) -> None:
        """
        Set the simulation parameters such as frequency and amplitude.

        :param frequency: The frequency of the sound wave.
        :param amplitude: The amplitude of the sound wave.
        """
        self.simulation.frequency = frequency
        self.simulation.amplitude = amplitude

    def toggle_simulation_playback(self) -> None:
        """
        Toggle the playback state of the simulation (play/pause).
        """
        self.simulation.toggle_playback()
