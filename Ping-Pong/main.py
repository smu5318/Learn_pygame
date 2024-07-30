import pygame
import constants as cons
from ball import Ball

pygame.init()


# Window
window = pygame.display.set_mode((cons.WINDOW_WIDTH, cons.WINDOW_HEIGHT))
pygame.display.set_caption(cons.WINDOW_NAME)

clock = pygame.time.Clock()

# Text
font = pygame.font.Font(cons.TEXT_FONT, cons.TEXT_SIZE)

# Objects
ball = Ball()

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
            if event.type == pygame.K_DOWN:
                right_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                left_up = False
            if event.key == pygame.K_s:
                left_down = False
            if event.key == pygame.K_UP:
                right_up = False
            if event.type == pygame.K_DOWN:
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
    if ball.rect.right >= cons.WINDOW_WIDTH:
        collition_e = True
    if ball.rect.left <= 0:
        collition_w = True
    
    print("n", collition_n, "\n", "s", collition_s, "\n", "w", collition_w, "\n", "e", collition_e)
    ball.move(collition_n, collition_s, collition_e, collition_w)

    # Points
    textpoint_left = font.render(str(left_point), True, cons.TEXT_COLOR)
    textleft_rect = textpoint_left.get_rect(center = (int(cons.WINDOW_WIDTH/4), int(cons.WINDOW_HEIGHT/6)))
        
    textpoint_right = font.render(str(right_point), True, cons.TEXT_COLOR)
    textright_rect = textpoint_right.get_rect(center = (int(cons.GAMEZONE_XCENTER + cons.WINDOW_WIDTH/4), int(cons.WINDOW_HEIGHT/6)))

    # Draw

     #window
    window.blit(textpoint_left, textleft_rect)
    window.blit(textpoint_right, textright_rect)  
    
     #ball
    ball.draw(window)


    pygame.display.flip()


pygame.quit()