from Constants import *
import pygame


class Brick:
    def __init__(self):
        self.static = False
        self.pos = 0

        self.borrow = []
        self.color = WHITE
        self.color_index = 0
        self.rotate_left_matrix = []
    
    def block_field(self, field):
        for (x, y) in self.borrow:
            field.borrow[y][x] = self.color_index
            
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

    def check_free_rotate(self, field, check_list):

        for (x, y) in check_list:
            if field.borrow[y][x]:
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
    
    def drop(self, field):
        while not self.static:
            
            self.fall(field)
    
    def draw(self, screen):
        for x, y in self.borrow:
            pygame.draw.rect(
                screen,
                self.color,
                (x * CELL_SIZE + 1, y * CELL_SIZE + 1, CELL_SIZE - 1, CELL_SIZE - 1)
            )
    


class Brick_square(Brick):
    def __init__(self, color, color_index):
        super().__init__()
        self.borrow = [[4, 0], [4, 1], [3, 0], [3, 1]]
        self.color = color
        self.color_index = color_index
    
    def rotate(self, field, direction):
        pass
    
class Brick_T(Brick):
    def __init__(self, color, color_index):
        super().__init__()
        self.borrow = [[3, 0], [4, 1], [5, 0], [4, 0]]
        self.color = color
        self.color_index = color_index

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

            help_list = []
            for index in range(4):
                x, y = self.borrow[index]
                xx, yy = x + translations[index][0], y + translations[index][1]

                help_list.append([xx, yy])

            if self.check_free_rotate(field, help_list):
                self.borrow = help_list
                self.pos = (self.pos + 1) % 4

        else:
            translations = self.rotate_left_matrix[self.pos]

            help_list = []
            for index in range(4):
                x, y = self.borrow[index]
                xx, yy = x + translations[index][0], y + translations[index][1]

                help_list.append([xx, yy])
            
            if self.check_free_rotate(field, help_list):
                self.borrow = help_list
                self.pos = (self.pos + 3) % 4

class Brick_Line(Brick):
    def __init__(self, color, color_index):
        super().__init__()
        self.borrow = [[3, 0], [4, 0], [5, 0], [6, 0]]
        self.color = color
        self.color_index = color_index

        self.rotate_matrix = [
            [[1, 1], [0, 0], [-1, -1], [-2, -2]],
            [[-1, -1], [0, 0], [1, 1], [2, 2]],
        ]
    
    def rotate(self, field, direction):
        if direction:
            translations = self.rotate_matrix[self.pos]

            help_list = []
            for index in range(4):
                x, y = self.borrow[index]
                xx, yy = x + translations[index][0], y + translations[index][1]

                help_list.append([xx, yy])

            if self.check_free_rotate(field, help_list):
                self.borrow = help_list
                self.pos = (self.pos + 1) % 2

        else:
            translations = self.rotate_matrix[self.pos]

            help_list = []
            for index in range(4):
                x, y = self.borrow[index]
                xx, yy = x + translations[index][0], y + translations[index][1]

                help_list.append([xx, yy])
            
            if self.check_free_rotate(field, help_list):
                self.borrow = help_list
                self.pos = (self.pos + 1) % 2