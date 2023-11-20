import pygame
import random
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
pygame.mixer.init()

snake = [(100, 100), (90, 100), (80, 100)]
food = (200, 200)
snake_direction = "right"  # Initialize snake_direction

def draw_board():
    for i in range(0, 640, 20):
        for j in range(0, 480, 20):
            if (i, j) in snake:
                pygame.draw.rect(screen, (0, 255, 0), (i, j, 20, 20))
            elif (i, j) == food:
                pygame.draw.rect(screen, (255, 0, 0), (i, j, 20, 20))
            else:
                pygame.draw.rect(screen, (0, 0, 0), (i, j, 20, 20))

def handle_input():
    global snake_direction  # Add global keyword to modify the global variable
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_direction = "up"
            elif event.key == pygame.K_DOWN:
                snake_direction = "down"
            elif event.key == pygame.K_LEFT:
                snake_direction = "left"
            elif event.key == pygame.K_RIGHT:
                snake_direction = "right"

def update_game_state():
    global snake, food
    # Move the snake
    if snake_direction == "up":
        snake.insert(0, (snake[0][0], snake[0][1] - 20))
    elif snake_direction == "down":
        snake.insert(0, (snake[0][0], snake[0][1] + 20))
    elif snake_direction == "left":
        snake.insert(0, (snake[0][0] - 20, snake[0][1]))
    elif snake_direction == "right":
        snake.insert(0, (snake[0][0] + 20, snake[0][1]))
    # Check for collisions
    if snake[0] == food:
        # Eat the food and generate new food
        snake.append((food[0], food[1]))
        food = (random.randint(0, 31) * 20, random.randint(0, 23) * 20)
    elif snake[0] in snake[1:]:
        # The snake collided with itself
        game_over = True
    # Remove the tail of the snake if it is too long
    if len(snake) > 100:
        snake.pop()

def draw_game_screen():
    screen.fill((0, 0, 0))
    for i in range(0, 640, 20):
        pygame.draw.line(screen, (255, 255, 255), (i, 0), (i, 480), 1)
    for j in range(0, 480, 20):
        pygame.draw.line(screen, (255, 255, 255), (0, j), (640, j), 1)
    for (i, j) in snake:
        pygame.draw.rect(screen, (0, 255, 0), (i, j, 20, 20))
    pygame.draw.rect(screen, (255, 0, 0), (food[0], food[1], 20, 20))
    pygame.display.update()

game_over = False
while not game_over:
    handle_input()
    update_game_state()
    draw_game_screen()
    clock.tick(10)
pygame.quit()
sys.exit()
