import pygame
import constants as cons

class Right_Player():
    def __init__(self):
        self.rect = pygame.rect.Rect(cons.RPLAYER_INITPOSITION[0], cons.RPLAYER_INITPOSITION[1], cons.PLAYER_WIDTH, cons.PLAYER_HEIGHT)

    def move(self, deltaY):
        self.rect.y += deltaY

    def draw(self, window):
        pygame.draw.rect(window, cons.PLAYER_COLOR, self.rect)