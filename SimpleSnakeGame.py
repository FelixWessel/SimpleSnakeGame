# This is a work in progress - not finished and not working yet

import pygame
import sys
from random import randint

pygame.init()

#Definition of variables for the game
run = True                  # As long as run equals true the game runs
screen_width = 600          # Setting the width of the game window
screen_height = 600         # Setting the height of the game window
square_x_pos = 60           # The initial x-position of the snake head at start of the game
square_y_pos = 60           # The initial y-position of the snake head at start of the game
square_dimension_w_h = 20   # Setting the hight and width of snake's building blocks


# Defining our game window
game_window = pygame.display.set_mode((screen_width, screen_height))

# This is the main loop of our SimpleSnakeGame
while run:
    # Here we check for inputs and exit the game if we close the game window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.rect(game_window, (255, 0, 0), (square_x_pos, square_y_pos, square_dimension_w_h, square_dimension_w_h))

    pygame.display.update()
    game_window.fill((0, 0, 0))

pygame.quit()


