import pygame
import constants as cons

class Snake():
    def __init__(self):

        self.direction = "e"    #n, e, s, w

        self.snake: list = [cons.SNAKE_INITPOSITION, 
            (cons.SNAKE_INITPOSITION[0] -1, cons.SNAKE_INITPOSITION[1]),
            (cons.SNAKE_INITPOSITION[0] -2, cons.SNAKE_INITPOSITION[1])]

        self.move_up = False
        self.move_left = False
        self.move_down = False
        self.move_right = False

    def move(self, up_move, left_move, down_move, right_move):
        
        self.move_up == up_move
        self.move_left == left_move
        self.move_down == down_move
        self.move_right == right_move

        if self.move_up and self.direction != "n" and self.direction != "s":
            self.direction = "n"
            print("up")
 
        elif self.move_left and self.direction != "w" and self.direction != "e":
            self.direction = "w"

        elif self.move_down and self.direction != "s" and self.direction != "n":
            self.direction = "s"
        
        elif self.move_right and self.direction != "e" and self.direction != "w":
            self.direction = "e"

        pygame.time.wait(cons.SNAKE_WAITMOVEMENT)

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

            print(new_snake, "\n", index)
            
            index += 1
        
        print("old snake: ", self.snake)
        
        self.snake.clear()
        self.snake = new_snake
        
        print("new snake: ", self.snake)
        print("DIRECTION: ", self.direction)
        print("Up: ", self.move_up)
        print("Down: ", self.move_down)
        print("Left: ", self.move_left)
        print("Right: ", self.move_right)

    def draw(self, window):
        
        for part in self.snake:
            if part == self.snake[0]:
                head = pygame.rect.Rect((part[0] * cons.GRID_CELLSIZE) - cons.WINDOW_BORDER, (part[1] * cons.GRID_CELLSIZE) - cons.WINDOW_BORDER, cons.SNAKE_WIDTH, cons.SNAKE_HEIGHT)
                pygame.draw.rect(window, cons.SNAKE_HEADCOLOR, head)
            else:
                rect = pygame.rect.Rect((part[0] * cons.GRID_CELLSIZE) - cons.WINDOW_BORDER, (part[1] * cons.GRID_CELLSIZE) - cons.WINDOW_BORDER, cons.SNAKE_WIDTH, cons.SNAKE_HEIGHT)

                pygame.draw.rect(window, cons.SNAKE_COLOR, rect)
