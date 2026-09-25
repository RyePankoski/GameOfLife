import pygame
import sys
from life import Life


pygame.init()
clock = pygame.time.Clock()
FPS = 40

screen = pygame.display.set_mode(pygame.display.get_desktop_sizes()[0])
life = Life(screen)

def main():
    running = True
    while running:
        events = pygame.event.get()
        dt = clock.tick(FPS) / 1000
        for event in events:
            if event.type == pygame.QUIT:
                return False

        life.run()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
