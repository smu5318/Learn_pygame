import pygame
import constants as cons
from snake import Snake

# functions
def draw_grid():
    for x in range(cons.WINDOW_BORDER, cons.WINDOW_WIDTH, cons.GRID_CELLSIZE):
        pygame.draw.line(window, cons.GRID_COLOR, (x, cons.WINDOW_BORDER), (x, cons.GAMEZONE_HEIGHT))
    for y in range(cons.WINDOW_BORDER, cons.WINDOW_HEIGHT, cons.GRID_CELLSIZE):
        pygame.draw.line(window, cons.GRID_COLOR, (cons.WINDOW_BORDER, y), (cons.GAMEZONE_WIDTH, y))

pygame.init()

# Window
window = pygame.display.set_mode((cons.WINDOW_WIDTH, cons.WINDOW_HEIGHT))
pygame.display.set_caption("Snake")

# Text
font = pygame.font.Font(cons.TEXT_FONT, cons.TEXT_SIZE)
init_text = font.render("Press Any Key to Start", True, cons.TEXT_COLOR)

# Objects
clock = pygame.time.Clock()

border = [
    pygame.rect.Rect(0, 0, cons.WINDOW_WIDTH, cons.WINDOW_BORDER), 
    pygame.rect.Rect(0, 0, cons.WINDOW_BORDER, cons.WINDOW_HEIGHT),
    pygame.rect.Rect(0, cons.WINDOW_HEIGHT - cons.WINDOW_BORDER, cons.WINDOW_WIDTH, cons.WINDOW_BORDER),
    pygame.rect.Rect(cons.WINDOW_WIDTH - cons.WINDOW_BORDER, 0, cons.WINDOW_BORDER, cons.WINDOW_HEIGHT)]

snake = Snake()

# Vars
start_game = False
tick_game = 0

up_move = False
down_move = False
left_move = False
right_move = False

running = True
while running:

    last_start = start_game

    # FPS
    clock.tick(cons.WINDOW_FPS)

    # Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                up_move = True

            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                down_move = True

            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                left_move = True

            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                right_move = True

        if event.type == pygame.KEYUP:
            if not start_game:
                start_game = True
                continue

            if event.key == pygame.K_ESCAPE:
                start_game = False
                continue

    # Move
    if start_game:
        snake.move(up_move, left_move, down_move,right_move)
    
        

        print("Up: ", up_move)
        print("Down: ", down_move)
        print("Left: ", left_move)
        print("Right: ", right_move)
        
        up_move = False
        down_move = False
        left_move = False
        right_move = False
    # Draw
     #window
    window.fill(cons.WINDOW_COLOR)
    
    for bord in border:
        pygame.draw.rect(window, cons.WINDOW_BORDERCOLOR, bord)

    draw_grid()

    snake.draw(window)

     # Pause game
    if not start_game:
        window.blit(init_text, init_text.get_rect(center = (cons.WINDOW_WIDTH // 2, cons.WINDOW_HEIGHT // 2)))

    pygame.display.flip()

    # Init
    if (not last_start) and start_game:
        pygame.time.wait(cons.WINDOW_WAIT)