import pygame
import constants as cons
from ball import Ball
from left_player import Left_Player
from right_player import Right_Player
    
pygame.init()


# Window
window = pygame.display.set_mode((cons.WINDOW_WIDTH, cons.WINDOW_HEIGHT))
pygame.display.set_caption(cons.WINDOW_NAME)

clock = pygame.time.Clock()

# Text
font = pygame.font.Font(cons.TEXT_FONT, cons.TEXT_SIZE)
line = font.render("_"*31, True, cons.TEXT_COLOR)

# Objects
ball = Ball()
left_player = Left_Player()
right_player = Right_Player()

# Functions
def init_positions():
    ball.rect.topleft = cons.BALL_INITPOSITION

    left_player.rect.topleft = cons.LPLAYER_INITPOSITION
    right_player.rect.topleft = cons.RPLAYER_INITPOSITION

# Vars
 
 #points
left_point = 0
right_point = 0

 #players movement
left_up = False
left_down = False
right_up = False
right_down = False

running = True
while running:
    
    clock.tick(cons.WINDOW_FPS)
    
    window.fill(cons.WINDOW_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                left_up = True
            if event.key == pygame.K_s:
                left_down = True
            if event.key == pygame.K_UP:
                right_up = True
            if event.key == pygame.K_DOWN:
                right_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                left_up = False
            if event.key == pygame.K_s:
                left_down = False
            if event.key == pygame.K_UP:
                right_up = False
            if event.key == pygame.K_DOWN:
                right_down = False
        
    # Movement
     #ball
    collition_n = False
    collition_s = False
    collition_e = False
    collition_w = False

    if ball.rect.top <= cons.WINDOW_LIMIT:
        collition_n = True
    if ball.rect.bottom >= cons.WINDOW_HEIGHT:
        collition_s = True
    if ball.rect.right >= cons.WINDOW_WIDTH or ball.rect.colliderect(right_player.rect):
        collition_e = True
    if ball.rect.left <= 0 or ball.rect.colliderect(left_player.rect):
        collition_w = True
    
    #print("n", collition_n, "\n", "s", collition_s, "\n", "w", collition_w, "\n", "e", collition_e)
    ball.move(collition_n, collition_s, collition_e, collition_w)

     #players
    left_deltaY = 0
    right_deltaY = 0

    if left_up and left_player.rect.top >= cons.WINDOW_LIMIT:
        left_deltaY = -cons.PLAYER_SPEED
    if left_down and left_player.rect.bottom <= cons.WINDOW_HEIGHT:
        left_deltaY = cons.PLAYER_SPEED
    if right_up and right_player.rect.top >= cons.WINDOW_LIMIT:
        right_deltaY = -cons.PLAYER_SPEED
    if right_down and right_player.rect.bottom <= cons.WINDOW_HEIGHT:
        right_deltaY = cons.PLAYER_SPEED
    
    left_player.move(left_deltaY)
    right_player.move(right_deltaY)

    # Points
    point = False

    if ball.rect.left <= cons.GAMEZONE_POINTZONE - int(cons.PLAYER_WIDTH/2):
        point = True
        right_point += 1
    if ball.rect.right >= (cons.WINDOW_WIDTH - cons.GAMEZONE_POINTZONE) + int(cons.PLAYER_WIDTH/2):
        point = True
        left_point += 1

    if point:
        init_positions()
    
    textpoint_left = font.render(str(left_point), True, cons.TEXT_COLOR)
    textleft_rect = textpoint_left.get_rect(center = (int(cons.WINDOW_WIDTH/4), int(cons.WINDOW_HEIGHT/6)))
        
    textpoint_right = font.render(str(right_point), True, cons.TEXT_COLOR)
    textright_rect = textpoint_right.get_rect(center = (int(cons.GAMEZONE_XCENTER + cons.WINDOW_WIDTH/4), int(cons.WINDOW_HEIGHT/6)))

    # Draw

     #window
    window.blit(textpoint_left, textleft_rect)
    window.blit(textpoint_right, textright_rect)
    window.blit(line, line.get_rect(centerx = cons.GAMEZONE_XCENTER, bottom = cons.WINDOW_LIMIT-2))
    
     #ball
    ball.draw(window)

     #players
    left_player.draw(window)
    right_player.draw(window)

    pygame.display.flip()
    
    if point:
        ball.count_time = 0
        ball.speed_movement = cons.BALL_SPEED
        pygame.time.wait(1000)

pygame.quit()