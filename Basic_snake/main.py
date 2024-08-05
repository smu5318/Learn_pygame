import pygame
import constants as cons
from snake import Snake
from apple import Apple

# functions
def draw_grid():
    for x in range(cons.WINDOW_BORDER, cons.WINDOW_WIDTH, cons.GRID_CELLSIZE):
        pygame.draw.line(window, cons.GRID_COLOR, (x, cons.WINDOW_BORDER), (x, cons.GAMEZONE_HEIGHT))
    for y in range(cons.WINDOW_BORDER, cons.WINDOW_HEIGHT, cons.GRID_CELLSIZE):
        pygame.draw.line(window, cons.GRID_COLOR, (cons.WINDOW_BORDER, y), (cons.GAMEZONE_WIDTH, y))

def draw(window, border, snake, apple):
    window.fill(cons.WINDOW_COLOR)
            
    for bord in border:
        pygame.draw.rect(window, cons.WINDOW_BORDERCOLOR, bord)

    draw_grid()

    snake.draw(window)

    apple.draw(window)

def lose_game(window):
    
    lose_text = font.render("You Lose. Press Any Key to Start", True, cons.TEXT_COLOR)
    window.blit(lose_text, lose_text.get_rect(center = (cons.WINDOW_WIDTH //2, cons.WINDOW_HEIGHT //2)))

    snake.dead()
    apple.retry()    
    return False
    

pygame.init()

# Window
window = pygame.display.set_mode((cons.WINDOW_WIDTH, cons.WINDOW_HEIGHT))
pygame.display.set_caption("Snake")

# Text
font = pygame.font.Font(cons.TEXT_FONT, cons.TEXT_SIZE)

# Objects
clock = pygame.time.Clock()

border = [
    pygame.rect.Rect(0, 0, cons.WINDOW_WIDTH, cons.WINDOW_BORDER), 
    pygame.rect.Rect(0, 0, cons.WINDOW_BORDER, cons.WINDOW_HEIGHT),
    pygame.rect.Rect(0, cons.WINDOW_HEIGHT - cons.WINDOW_BORDER, cons.WINDOW_WIDTH, cons.WINDOW_BORDER),
    pygame.rect.Rect(cons.WINDOW_WIDTH - cons.WINDOW_BORDER, 0, cons.WINDOW_BORDER, cons.WINDOW_HEIGHT)]

snake = Snake()
apple = Apple()

# Vars
start_game = False
tick_game = 1
apple_outgame = True
apple_tick = 1

points = 0

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

                draw(window, border, snake, apple)

                start_game = True

                continue

    # Move
     #snake
    if start_game and tick_game != 1:
        snake.move(up_move, left_move, down_move,right_move, tick_game)
        
        up_move = False
        down_move = False
        left_move = False
        right_move = False

    #Collitions

        collition = False
        index = 1
        while index < len(snake.snake) and (not collition):
            if snake.snake[index] == snake.snake[0]:
                collition = True
            index += 1
        
        if cons.GRID_NUMCELLSX < snake.snake[0][0] or snake.snake[0][0] < 1 or cons.GRID_NUMCELLSY < snake.snake[0][1] or snake.snake[0][1] < 1:
            start_game = lose_game(window)
            points = 0
        
        if collition:
            start_game = lose_game(window)
            points = 0

        if apple.position[0] == snake.snake[0][0] and apple.position[1] == snake.snake[0][1]:
            snake.eat()
            points += 1
            apple.eliminate()
            apple_outgame = False


    # Draw
     #window
    if last_start and start_game or tick_game == 1:
        
        draw(window, border, snake, apple)

        point_text = font.render(f"Apples: {points}", True, cons.APPLE_COLOR)
        window.blit(point_text, point_text.get_rect(center = (cons.WINDOW_WIDTH //4, cons.WINDOW_BORDER //2)))
    
    pygame.display.flip()
    
    tick_game += 1
    if not apple_outgame:

        if apple_tick % cons.APPLE_WAITGENERATE == 0:
            
            apple.generate()
            for part in snake.snake:
                if part == apple.position:
                    apple.generate()

            apple_outgame = True
            apple_tick = 1

        else:
            apple_tick += 1
    print(tick_game, "\napple: ", apple_tick)

     # Init game
    if tick_game == 2:
        if not start_game:
            pygame.time.wait(cons.WINDOW_WAIT)
            start_game = True
    
    elif (not last_start) and start_game:
        pygame.time.wait(cons.WINDOW_WAIT)