import pygame
import constants as cons

class Snake():
    def __init__(self):

        self.direction = cons.SNAKE_DIRECTIONS[1][0]    #n, e, s, w
        self.type_direction = "x" #x, y

        self.snake: list = [cons.SNAKE_INITPOSITION, 
            (cons.SNAKE_INITPOSITION[0] -1, cons.SNAKE_INITPOSITION[1]),
            (cons.SNAKE_INITPOSITION[0] -2, cons.SNAKE_INITPOSITION[1])]

        self.move_up = False
        self.move_left = False
        self.move_down = False
        self.move_right = False

    def move(self, up_move: bool, left_move: bool, down_move: bool, right_move: bool, tick_game: int):
        
        self.move_up = up_move
        self.move_left = left_move
        self.move_down = down_move
        self.move_right = right_move

        if self.type_direction == "x":

            if self.move_up and (not self.direction in cons.SNAKE_DIRECTIONS[0]) :
                self.direction = "n"
            elif self.move_down and (not self.direction in cons.SNAKE_DIRECTIONS[0]):
                self.direction = "s"

        elif self.type_direction == "y":
            
            if self.move_left and (not self.direction in cons.SNAKE_DIRECTIONS[1]):
                self.direction = "w"
            elif self.move_right and (not self.direction in cons.SNAKE_DIRECTIONS[1]):
                self.direction = "e"
        
        if tick_game % cons.SNAKE_WAITMOVEMENT == 0 or tick_game == 1:      
            
            new_snake: list = []  
            index = 0

            while index < len(self.snake):
                
                new_coordinates = None

                if index != 0:
                    new_coordinates = self.snake[index - 1]
                    new_snake.insert(index, new_coordinates)

                else:
                    if self.direction == "e":
                        old_coordinates = self.snake[index]
                        new_coordinates = (old_coordinates[0] + 1, old_coordinates[1])
                        new_snake.insert(index, new_coordinates)

                    elif self.direction == "n":
                        old_coordinates = self.snake[index]
                        new_coordinates = (old_coordinates[0], old_coordinates[1] - 1)
                        new_snake.insert(index, new_coordinates)

                    elif self.direction == "w":
                        old_coordinates = self.snake[index]
                        new_coordinates = (old_coordinates[0] - 1, old_coordinates[1])
                        new_snake.insert(index, new_coordinates)

                    elif self.direction == "s":
                        old_coordinates = self.snake[index]
                        new_coordinates = (old_coordinates[0], old_coordinates[1] + 1)
                        new_snake.insert(index, new_coordinates)
                
                index += 1
        
            #print("old snake: ", self.snake)
            
            self.snake.clear()
            self.snake = new_snake

            if self.direction in cons.SNAKE_DIRECTIONS[0]:
                self.type_direction = "y"
            elif self.direction in cons.SNAKE_DIRECTIONS[1]:
                self.type_direction = "x"
            
            print("new snake: ", self.snake)
            print("DIRECTION: ", self.direction, "\n")

    def eat(self):
        pass

    def draw(self, window):
        
        for part in self.snake:
            if part == self.snake[0]:
                head = pygame.rect.Rect((part[0] * cons.GRID_CELLSIZE) - cons.WINDOW_BORDER, (part[1] * cons.GRID_CELLSIZE) - cons.WINDOW_BORDER, cons.SNAKE_WIDTH, cons.SNAKE_HEIGHT)
                pygame.draw.rect(window, cons.SNAKE_HEADCOLOR, head)
            else:
                rect = pygame.rect.Rect((part[0] * cons.GRID_CELLSIZE) - cons.WINDOW_BORDER, (part[1] * cons.GRID_CELLSIZE) - cons.WINDOW_BORDER, cons.SNAKE_WIDTH, cons.SNAKE_HEIGHT)

                pygame.draw.rect(window, cons.SNAKE_COLOR, rect)
