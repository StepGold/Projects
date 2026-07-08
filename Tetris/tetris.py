import pygame
import random

from Constants import *
from Field import Field
from Brick import Brick_T, Brick_square 

pygame.init()

def new_random_brick(field):
    color_index = random.randint(1, 6)
    color = COLORS[color_index]

    index = random.randint(0, 1) # 0, 6

    if index == 0:
        brick = Brick_square(color, color_index)
    elif index == 1:
        brick = Brick_T(color, color_index)

    field.current_brick = brick
    
    return brick


def printer(a):
    for row in a:
        print(row)
    print("\n\n\n\n\n")


screen = pygame.display.set_mode((WIDTH + 4 * CELL_SIZE, HEIGHT))
pygame.display.set_caption("TETRIS")
clock = pygame.time.Clock()


field = Field()
current_brick = new_random_brick(field)

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
        current_brick = new_random_brick(field)
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
            field.full_row()
            #printer(field.borrow)





    tick = (tick + 1) % 2
    field.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
