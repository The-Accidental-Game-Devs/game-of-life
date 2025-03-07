
import pygame
import matrix
import random
import settings

class Game:
    def __init__(self) -> None:
        self.matrix = [[0] * settings.COL_SIZE for _ in range(settings.ROW_SIZE)]  # Create a matrix with row and col sizes
    
    def clear(self) -> None:
        self.matrix = [[0] * settings.COL_SIZE for _ in range(settings.ROW_SIZE)]  # Create a matrix with row and col sizes

    def handle_draw_input(self):
        mouse_input = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        row = int(mouse_pos[1] / settings.CELL_SIZE)
        col = int(mouse_pos[0] / settings.CELL_SIZE)

        if not matrix.is_index_out_of_range(row, col, settings.ROW_SIZE, settings.COL_SIZE):

            if mouse_input[0]:
                self.matrix[row][col] = 1

            if mouse_input[2]:
                self.matrix[row][col] = 0

    def draw(self, surface: pygame.Surface) -> None:
        for (y, row) in enumerate(self.matrix):
            for (x, value) in enumerate(row):

                pos_x = x * settings.CELL_SIZE
                pos_y = y * settings.CELL_SIZE
                rect = pygame.FRect(pos_x, pos_y, settings.CELL_SIZE, settings.CELL_SIZE)

                if value == 1:
                    pygame.draw.rect(surface, settings.CELL_COLOR, rect)

                pygame.draw.rect(surface, settings.GRID_COLOR, rect, 1)

    def update(self):

        new_matrix = [row[:] for row in self.matrix]  # Create a copy to store updates

        for (y, row) in enumerate(self.matrix):
            for (x, value) in enumerate(row):
                sum_of_neighbours = sum(matrix.get_neighbouring_cell(self.matrix, y, x))
                if value == 1:
                    # Live cell dies unless it has 2 or 3 neighbors
                    if sum_of_neighbours not in [2, 3]:
                        new_matrix[y][x] = 0
                elif value == 0:
                    # Dead cell becomes alive if exactly 3 neighbors
                    if sum_of_neighbours == 3:
                        new_matrix[y][x] = 1

        self.matrix = new_matrix

def random_color():
    return (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
