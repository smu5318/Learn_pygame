import pygame
import constants as cons

class Ball():
    def __init__(self):
        self.rect = pygame.rect.Rect((int(cons.GAMEZONE_XCENTER - cons.BALL_WIDTH), int(cons.GAMEZONE_YCENTER - cons.BALL_HEIGHT), cons.BALL_WIDTH, cons.BALL_HEIGHT))
        self.move_to = "ne"

    def move(self, n :bool, s :bool, e :bool, w :bool):
        if n:
            self.move_to = "s" + self.move_to[1]
        if s:
            self.move_to = "n" + self.move_to[1]
        if e:
            self.move_to = self.move_to[0] + "w"
        if w:
            self.move_to = self.move_to[0] + "e"

        if self.move_to[0] == "n":
            self.rect.y += -cons.BALL_SPEED
        elif self.move_to[0] == "s":
            self.rect.y += cons.BALL_SPEED
        if self.move_to[1] == "e":
            self.rect.x += cons.BALL_SPEED
        elif self.move_to[1] == "w":
            self.rect.x += -cons.BALL_SPEED 

        print(self.rect.center, "-", self.move_to)
    
    def draw(self, window):
        pygame.draw.rect(window, cons.BALL_COLOR, self.rect)