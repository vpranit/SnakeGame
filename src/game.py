import pygame
from src.screen import Screen

class Game:
    def __init__(self):
        pygame.init()
        self.screen = Screen()
        self.screen.draw_rectangle

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_x:
                    running = False 
            # Add game rendering here
            self.screen.update_screen()
        # Properly quit Pygame when the loop ends
        pygame.quit()

    


