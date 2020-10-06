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
snake_head = [square_x_pos, square_y_pos]   # The initial position of our snake's head at start of the game
snake_body = [[square_x_pos, square_y_pos], [(square_x_pos + square_dimension_w_h), square_y_pos], [(square_x_pos + (2 * square_dimension_w_h)), square_y_pos]]
                                            # The initial position of our snake's body at start of the game
direction = "LEFT"                          # The initial direction the snake is going to at the start of the game

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
    if pressed_key[pygame.K_DOWN] and direction != "UP":
        direction = "DOWN"
    if pressed_key[pygame.K_LEFT] and direction != "RIGHT":
        direction = "LEFT"
    if pressed_key[pygame.K_RIGHT] and direction != "LEFT":
        direction = "RIGHT" 


    pygame.draw.rect(game_window, (255, 0, 0), (square_x_pos, square_y_pos, square_dimension_w_h, square_dimension_w_h))

    pygame.display.update()
    game_window.fill((0, 0, 0))

    print (direction)

pygame.quit()


