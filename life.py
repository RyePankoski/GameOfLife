import random
from util import *

from draw import Draw


class Life:
    def __init__(self, screen):
        size = screen.get_size()

        self.draw = Draw(screen)

        self.cells = {}
        self.cells_to_add = set()
        self.columns = size[0] // GRID_SIZE
        self.rows = size[1] // GRID_SIZE
        self.pause = True

        self.can_click = True
        self.click_cooldown = 8
        self.click_timer = 0

        self.can_key = True
        self.key_cooldown = 10
        self.key_timer = 0

        GOSPER_GUN = [
            (1, 5), (1, 6), (2, 5), (2, 6),  # left block
            (11, 5), (11, 6), (11, 7), (12, 4), (12, 8), (13, 3), (13, 9),
            (14, 3), (14, 9), (15, 6), (16, 4), (16, 8),
            (17, 5), (17, 6), (17, 7), (18, 6),  # left "queen bee" section
            (21, 3), (21, 4), (21, 5), (22, 3), (22, 4), (22, 5),
            (23, 2), (23, 6), (25, 1), (25, 2), (25, 6), (25, 7),  # right section
            (35, 3), (35, 4), (36, 3), (36, 4),  # right block
        ]

        ox, oy = 5, 5
        for x, y in GOSPER_GUN:
            self.cells[(GRID_SIZE * (x + ox), GRID_SIZE * (y + oy))] = 1

    def run(self):
        self.timers()

        if self.can_click:
            self.handle_clicking()
        if self.can_key:
            self.handle_keys()
        if not self.pause:
            self.handle_cells()

        self.draw.run(self.cells, self.pause)

    def handle_cells(self):
        cells_to_remove = set()
        for cell in self.cells:
            self.dead_neighbors(cell)

            neighbors = self.find_no_of_neighbors(cell)
            if neighbors < 2 or neighbors > 3:
                cells_to_remove.add(cell)
            else:
                continue

        for cell in cells_to_remove:
            del self.cells[cell]

        for cell in self.cells_to_add:
            self.cells[cell] = 1

        self.cells_to_add.clear()

    def dead_neighbors(self, cell):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for direction in directions:
            dead_cell = cell[0] + direction[0] * GRID_SIZE, cell[1] + direction[1] * GRID_SIZE

            if dead_cell in self.cells:
                continue

            neighbors = self.find_no_of_neighbors(dead_cell)

            if neighbors == 3:
                self.cells_to_add.add(dead_cell)

    def find_no_of_neighbors(self, cell):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        neighbors = 0

        for direction in directions:
            x = cell[0] + direction[0] * GRID_SIZE
            y = cell[1] + direction[1] * GRID_SIZE
            if (x, y) in self.cells:
                neighbors += 1
        return neighbors

    def timers(self):
        if not self.can_click:

            self.click_timer += 1
            if self.click_timer >= self.click_cooldown:
                self.can_click = True
                self.click_timer = 0

        if not self.can_key:
            self.key_timer += 1
            if self.key_timer >= self.key_cooldown:
                self.can_key = True
                self.key_timer = 0

    def handle_clicking(self):
        if pygame.mouse.get_pressed()[0]:
            self.can_click = False
            x, y = pygame.mouse.get_pos()
            x_mod = x % GRID_SIZE
            y_mod = y % GRID_SIZE

            if x_mod >= GRID_SIZE / 2:
                x += GRID_SIZE - x_mod
            else:
                x -= x_mod

            if y_mod >= GRID_SIZE / 2:
                y += GRID_SIZE - y_mod
            else:
                y -= y_mod

            if (x, y) in self.cells:
                del self.cells[(x, y)]
            else:
                self.cells[(x, y)] = 1

    def handle_keys(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.can_key = False
            self.pause = not self.pause


