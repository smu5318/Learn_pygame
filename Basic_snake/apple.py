import pygame
import constants as cons
import random

class Apple():
    def __init__(self):
        self.position = cons.APPLE_INITPOSITION
        self.rect = pygame.rect.Rect((self.position[0] * cons.GRID_CELLSIZE) - cons.WINDOW_BORDER, (self.position[1] * cons.GRID_CELLSIZE) - cons.WINDOW_BORDER, cons.APPLE_WIDTH, cons.APPLE_HEIGHT)

    def generate(self):

        rand = random.Random()

        self.position = (rand.randint(1, cons.GRID_NUMCELLSX), rand.randint(1, cons.GRID_NUMCELLSY))
        
    def eliminate(self):
        self.position = (-1, -1)        

    def retry(self):
        self.position = cons.APPLE_INITPOSITION

    def draw(self, window):

        self.rect.topleft = ((self.position[0] * cons.GRID_CELLSIZE) - cons.WINDOW_BORDER, (self.position[1] * cons.GRID_CELLSIZE) - cons.WINDOW_BORDER)

        pygame.draw.rect(window, cons.APPLE_COLOR, self.rect)