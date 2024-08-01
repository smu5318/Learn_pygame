import pygame
import constants as cons

class Ball():
    def __init__(self):
        self.rect = pygame.rect.Rect(cons.BALL_INITPOSITION[0], cons.BALL_INITPOSITION[1], cons.BALL_WIDTH, cons.BALL_HEIGHT)
        self.move_to = "nw"

        # INCREASE-SPEED
        self.speed_movement = cons.BALL_SPEED

        self.increase = False
        self.increase_count = 1
        self.speed_increase = 1

        # TIME
        self.count_time = 0

    def move(self, n :bool, s :bool, e :bool, w :bool):

        if self.count_time >= cons.BALL_INCREASETIME * self.increase_count:

            self.increase = True
            self.speed_increase = self.speed_movement + self.increase_count
            
            self.increase_count += 1
            self.count_time = 0

        if self.increase:
            if self.speed_movement <= cons.BALL_MAXSPEED:
                if self.speed_movement < self.speed_increase:
                    self.speed_movement = round(self.speed_movement + cons.BALL_INCREASESPEED, 4)
                else:
                    self.increase = False

        if n:
            self.move_to = "s" + self.move_to[1]
        if s:
            self.move_to = "n" + self.move_to[1]
        if e:
            self.move_to = self.move_to[0] + "w"
        if w:
            self.move_to = self.move_to[0] + "e"

        if self.move_to[0] == "n":
            self.rect.y += -self.speed_movement
        elif self.move_to[0] == "s":
            self.rect.y += self.speed_movement
        if self.move_to[1] == "e":
            self.rect.x += self.speed_movement
        elif self.move_to[1] == "w":
            self.rect.x += -self.speed_movement 

        # print(self.rect.center, "-", self.move_to)
    
    def draw(self, window):
        pygame.draw.rect(window, cons.BALL_COLOR, self.rect)
        
        self.count_time += 1