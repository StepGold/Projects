from Constants import *
import pygame

class Field:
    def __init__(self):
        self.current_brick = None
        self.borrow = [[0 for i in range(W_COUNT)] + [1] for j in range(H_COUNT)] + [[1 for i in range(W_COUNT + 1)]] + [[0 for i in range(W_COUNT + 1)]]

    def rows_fall(self, y):
        for height in range(y, 0, -1):
            self.borrow[height] = self.borrow[height-1]
        self.borrow[0] = [0 for i in range(W_COUNT)] + [1]

    def full_row(self):
        for height in range(H_COUNT):
            if all(self.borrow[height]):
                self.rows_fall(height)

    def draw(self, screen):
        width = WIDTH
        height = HEIGHT
        cell_size = CELL_SIZE

        pygame.draw.rect(
            screen,
            GRAY,
            (0, 0, width, height)
        )

        for x in range(width // cell_size + 1):
            pygame.draw.line(
                screen,
                WHITE,
                (x * cell_size, 0),
                (x * cell_size, height)
            )
        
        for y in range(height // cell_size):
            pygame.draw.line(
                screen,
                WHITE,
                (0, y * cell_size),
                (width, y * cell_size)
            )
        
        for height in range(H_COUNT):
            for width in range(W_COUNT):
                color_index = self.borrow[height][width]
                if color_index:
                    pygame.draw.rect(
                        screen,
                        COLORS[color_index],
                        (width * CELL_SIZE + 1, height * CELL_SIZE + 1, CELL_SIZE - 1, CELL_SIZE - 1)
                    )

        self.current_brick.draw(screen)

