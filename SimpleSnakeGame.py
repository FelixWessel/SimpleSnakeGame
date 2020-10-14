# This is a work in progress - not finished and not working yet

import pygame
import sys
from random import randint

pygame.init()

#Definition of variables for the game
run = True                                  # As long as run equals true the game runs
screen_width = 600                          # Setting the width of the game window
screen_height = 600                         # Setting the height of the game window
square_x_pos = 60                           # The initial x-position of the snake head at start of the game
square_y_pos = 60                           # The initial y-position of the snake head at start of the game
square_dimension_w_h = 20                   # Setting the hight and width of snake's building blocks
rows = ((screen_height - square_dimension_w_h) / square_dimension_w_h) # Rows on the screen
columns = ((screen_width - square_dimension_w_h) / square_dimension_w_h) # Colums on the screen
snake_head = [square_x_pos, square_y_pos]   # The initial position of our snake's head at start of the game
snake_body = [[square_x_pos, square_y_pos], [(square_x_pos + square_dimension_w_h), square_y_pos], [(square_x_pos + (2 * square_dimension_w_h)), square_y_pos]]
                                            # The initial position of our snake's body at start of the game
food_x_pos = (randint(0, columns) * square_dimension_w_h) # Setting the x position of food
food_y_pos  = (randint(0, rows) * square_dimension_w_h) # Setting the y position of food
food = [food_x_pos, food_y_pos]

direction = "LEFT"                          # The initial direction the snake is going to at the start of the game
clock = pygame.time.Clock()                 # Definition of a timer to control the game's speed
fps = 5                                     # Speed of the game (used by clock) 
step = square_dimension_w_h                 # Defines how far the snake moves with each step
turns = 0                                   # Counting the number of turns our snake made
score = 0                                   # Counting the number of food the snake has eaten
RED = (255, 0, 0)                           # Variable that stores the red color for snake body
GREEN = (0, 255, 0)                         # Variable that stores the green color for food
ORANGE = (255, 69, 0)                       # Orange color for snake head



# Defining our game window
game_window = pygame.display.set_mode((screen_width, screen_height))

# This is the main loop of our SimpleSnakeGame
while run:
    # Here we check for inputs and exit the game if we close the game window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Check which key has been pressed and setting the direction variable
    # We also check the current direction and make sure that snake is not running into itself
    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_UP] and direction != "DOWN":
        direction = "UP"
        turns += 1
    if pressed_key[pygame.K_DOWN] and direction != "UP":
        direction = "DOWN"
        turns += 1
    if pressed_key[pygame.K_LEFT] and direction != "RIGHT":
        direction = "LEFT"
        turns += 1
    if pressed_key[pygame.K_RIGHT] and direction != "LEFT":
        direction = "RIGHT" 
        turns += 1

    # Change the movement of the snake depending on the "direction" variable
    if direction == "LEFT" and snake_head[0] < 0:
        snake_head[0] = screen_width
        snake_head[0] -= step
    elif direction == "LEFT": 
        snake_head[0] -= step

    if direction == "RIGHT" and snake_head[0] == (screen_width - square_dimension_w_h):
        snake_head[0] = (0 - square_dimension_w_h)
        snake_head[0] += step
    elif direction == "RIGHT":
        snake_head[0] += step    

    if direction == "UP" and snake_head[1] < 0:
        snake_head[1] = screen_height
        snake_head[1] -= step
    elif direction == "UP":
        snake_head[1] -= step
        
    if direction == "DOWN" and snake_head[1] > (screen_height - square_dimension_w_h):
        snake_head[1] = 0
        snake_head[1] += step
    elif direction == "DOWN":
        snake_head[1] += step

    pygame.draw.rect(game_window, GREEN, (food[0], food[1], square_dimension_w_h, square_dimension_w_h))

    snake_body.insert(0, list(snake_head))
    if snake_head != food:
        snake_body.pop()
    else:
        score += 1
        food[0] = (randint(0, columns)) * square_dimension_w_h
        food[1] = (randint(0, rows)) * square_dimension_w_h
        fps += 0.5



    pygame.draw.rect(game_window, ORANGE, (snake_head[0], snake_head[1], square_dimension_w_h, square_dimension_w_h))
    for segment in snake_body[1:]:
        pygame.draw.rect(game_window, RED, (segment[0], segment[1], square_dimension_w_h, square_dimension_w_h))
    



    pygame.display.update()
    game_window.fill((0, 0, 0))
    
    # Setting the game of the speed
    clock.tick(fps)
    
    
    print (turns)
    print (snake_head[0])

pygame.quit()


