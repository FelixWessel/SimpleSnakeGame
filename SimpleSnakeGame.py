import pygame
import sys
from random import randint

pygame.init()

run = True

screen_width = 600
screen_height = 600

square_x_pos = 60
square_y_pos = 60
square_dimension_w_h = 20

game_window = pygame.display.set_mode((screen_width, screen_height))

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.rect(game_window, (255, 0, 0), (square_x_pos, square_y_pos, square_dimension_w_h, square_dimension_w_h))

    pygame.display.update()
    game_window.fill((0, 0, 0))

pygame.quit()


