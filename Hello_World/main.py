import pygame
import constants as cons

pygame.init()

# Window
screen = pygame.display.set_mode((cons.WINDOW_WIDTH, cons.WINDOW_HEIGHT))
pygame.display.set_caption(cons.WINDOW_NAME)

# Clock
clock = pygame.time.Clock()

# Font
font = pygame.font.Font(cons.TEXT_FONT, cons.TEXT_SIZE)

# Render text
text = font.render(cons.TEXT_TEXT, True, cons.TEXT_COLOR)
text_rect = text.get_rect(center = (int(cons.WINDOW_WIDTH/2), int(cons.WINDOW_HEIGHT/2)))

screen.blit(text, text_rect)

# Vars
left_bool = False
right_bool = False
up_bool = False
down_bool = False

running = True
while running:

    # Update Screen
    clock.tick(cons.TIME_FPS)
    screen.fill(cons.WINDOW_COLOR)
    
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_bool = True
            if event.key == pygame.K_RIGHT:
                right_bool = True
            if event.key == pygame.K_UP:
                up_bool = True
            if event.key == pygame.K_DOWN:
                down_bool = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_bool = False
            if event.key == pygame.K_RIGHT:
                right_bool = False
            if event.key == pygame.K_UP:
                up_bool = False
            if event.key == pygame.K_DOWN:
                down_bool = False
    # Movement
    if left_bool:
        text_rect = (text_rect[0] -cons.TEXT_SPEED, text_rect[1])
    if right_bool:
        text_rect = (text_rect[0] +cons.TEXT_SPEED, text_rect[1])
    if up_bool:
        text_rect = (text_rect[0], text_rect[1] -cons.TEXT_SPEED)
    if down_bool:
        text_rect = (text_rect[0], text_rect[1] +cons.TEXT_SPEED)
    
    screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()