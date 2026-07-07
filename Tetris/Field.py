from Constants import *
import pygame

class Field:
    def __init__(self):
        self.bricks = []
        self.borrow = [[0 for i in range(W_COUNT)] + [1] for j in range(H_COUNT)] + [[1 for i in range(W_COUNT)] + [[0 for i in range(W_COUNT)]]]
        print(self.borrow)

    def add_brick(self, brick):
        self.bricks.append(brick)



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
        
        for brick in self.bricks:
            brick.draw(screen)

