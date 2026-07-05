import pygame
import random

pygame.init()

GRAY = (150, 150, 150)
WHITE = (215, 215, 215)
RED = (235, 20, 20)
GREEN = (20, 215, 20)
BLUE = (20, 20, 225)
CYAN = (0, 235, 235)
YELLOW = (235, 235, 20)
PURPLE = (235, 20, 235)
BLACK = (40, 40, 40)
BROWN = (150, 30, 30)
ORANGE = (235, 150, 20)
PINK = (235, 150, 150)

H_COUNT = 15
W_COUNT = 9
CELL_SIZE = 60
WIDTH = CELL_SIZE * W_COUNT
HEIGHT = CELL_SIZE * H_COUNT
COLORS = [RED, GREEN, BLUE, YELLOW, CYAN, ORANGE, PURPLE]

FPS = 10

class Field:
    def __init__(self):
        self.bricks = []
        self.borrow = [[0 for i in range(W_COUNT)] + [1] for j in range(H_COUNT)] + [[1 for i in range(W_COUNT)] + [[0 for i in range(W_COUNT)]]]
        #print(self.borrow)

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



class Brick:
    def __init__(self):
        self.static = False
        self.pos = 0

        self.borrow = []
        self.color = WHITE
        self.rotate_left_matrix = []
    
    def block_field(self, field):
        for (x, y) in self.borrow:
            field.borrow[y][x] = 1
            
    def check_free(self, field, direction=None):
        if direction is None:
            x_shape, y_shape = 0, 1
        elif direction == 0:
            x_shape, y_shape = -1, 0
        elif direction == 1:
            x_shape, y_shape = 1, 0
            
        for (x, y) in self.borrow:
            if field.borrow[y + y_shape][x + x_shape]:
                return False

        return True
    
    def fall(self, field):
        if self.check_free(field):
            for i in range(len(self.borrow)):
                self.borrow[i][1] += 1
        else:
            self.static = True

    def move(self, field, direction):
        if self.check_free(field, direction):
            if direction == 0:
                x_shape, y_shape = -1, 0
            else:
                x_shape, y_shape = 1, 0

            for i in range(len(self.borrow)):
                self.borrow[i][0] += x_shape
                self.borrow[i][1] += y_shape
    
    def draw(self, screen):
        for x, y in self.borrow:
            pygame.draw.rect(
                screen,
                self.color,
                (x * CELL_SIZE + 1, y * CELL_SIZE + 1, CELL_SIZE - 1, CELL_SIZE - 1)
            )
    


class Brick_square(Brick):
    def __init__(self, color):
        super().__init__()
        self.borrow = [[4, 0], [4, 1], [3, 0], [3, 1]]
        self.color = color
    
    def rotate(self, field, direction):
        pass
    
class Brick_T(Brick):
    def __init__(self, color):
        super().__init__()
        self.borrow = [[3, 0], [4, 1], [5, 0], [4, 0]]
        self.color = color

        self.rotate_left_matrix = [
            [[1, 1], [1, -1], [-1, -1], [0, 0]],
            [[-1, 1], [1, 1], [1, -1], [0, 0]],
            [[-1, -1], [-1, 1], [1, 1], [0, 0]],
            [[1, -1], [-1, -1], [-1, 1], [0, 0]]
        ]

        self.rotate_right_matrix = [
            [[1, -1], [-1, -1], [-1, 1], [0, 0]],
            [[1, 1], [1, -1], [-1, -1], [0, 0]],
            [[-1, 1], [1, 1], [1, -1], [0, 0]],
            [[-1, -1], [-1, 1], [1, 1], [0, 0]]
        ]
    
    def rotate(self, field, direction):
        if direction:
            translations = self.rotate_right_matrix[self.pos]
            self.pos = (self.pos + 1) % 4
            for index in range(4):
                x, y = self.borrow[index]
                self.borrow[index] = [x + translations[index][0], y + translations[index][1]]
        else:
            translations = self.rotate_left_matrix[self.pos]
            self.pos = (self.pos + 3) % 4
            for index in range(4):
                x, y = self.borrow[index]
                self.borrow[index] = [x + translations[index][0], y + translations[index][1]]


def new_random_brick():
    color_index = random.randint(0, 6)
    color = COLORS[color_index]
    color = [0.8 * i for i in color]

    index = random.randint(0, 1) # 0, 6

    if index == 0:
        brick = Brick_square(color)
    elif index == 1:
        brick = Brick_T(color)
    
    return brick





screen = pygame.display.set_mode((WIDTH + 4 * CELL_SIZE, HEIGHT))
pygame.display.set_caption("TETRIS")
clock = pygame.time.Clock()


field = Field()
current_brick = new_random_brick()
field.add_brick(current_brick)

user_move_left = False
user_move_right = False
user_rotate_left = False
user_rotate_right = False
tick = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                user_move_left = True
            elif event.key == pygame.K_d:
                user_move_right = True
            elif event.key == pygame.K_q:
                user_rotate_left = True
            elif event.key == pygame.K_e:
                user_rotate_right = True





    if current_brick.static:
        current_brick.block_field(field)
        current_brick = new_random_brick()
        field.add_brick(current_brick)
    else:

        if user_move_left:
            current_brick.move(field, 0)
            user_move_left = False
        elif user_move_right:
            current_brick.move(field, 1)
            user_move_right = False
        elif user_rotate_left:
            current_brick.rotate(field, 0)
            user_rotate_left = False
        elif user_rotate_right:
            current_brick.rotate(field, 1)
            user_rotate_right = False

        if tick:
            current_brick.fall(field)





    tick = (tick + 1) % 2
    field.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
