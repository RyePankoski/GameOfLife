import pygame


GRID_SIZE = 5
DOT_SIZE = GRID_SIZE/2 + 2

def start_blit(screen):
    screen.fill((0, 0, 0))

def end_blit():
    pygame.display.flip()