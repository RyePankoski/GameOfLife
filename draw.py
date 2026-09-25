import pygame
from util import *


class Draw:
    def __init__(self, screen):
        self.screen = screen
        self.size = self.screen.get_size()

    def run(self, cells, pause):
        start_blit(self.screen)
        self.draw_cells(cells)
        self.draw_pause(pause)
        end_blit()

    def draw_cells(self, cells):
        for cell in cells:
            pygame.draw.circle(self.screen, (255, 255, 255), (cell[0], cell[1]), DOT_SIZE)

    def draw_pause(self, state):
        if state:
            pygame.draw.rect(self.screen, (255, 50, 50), (0, 0, self.size[0], self.size[1]), 2)
