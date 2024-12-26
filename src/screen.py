import pygame
from src.constants import SCREEN_BACKGROUND_COLOR

pygame.init()

# Get display information
display_info = pygame.display.Info()

# Extract screen dimensions
display_width = display_info.current_w
display_height = display_info.current_h - 60

class Screen:

    def __init__(self, width=display_width, height=display_height, title="Snake Game"):
        # pygame.init()
        # Initialize the Display
        self.screen = pygame.display.set_mode((width,height), pygame.RESIZABLE)
        pygame.display.set_caption(title)

    def clear_screen(self):
        # Clear the screen with the background color
        screen.fill(SCREEN_BACKGROUND_COLOR)

    def update_screen(self):
        # Update the screen with any changes
        pygame.display.update()

    def draw_rectangle (self):
        # Draw a Rectangle for 
        rectangle = pygame.Rect(50,50,50,50)
