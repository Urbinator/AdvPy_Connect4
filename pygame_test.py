import pygame
import numpy as np
import sys

BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

num_columns = 7
num_rows = 6

board = np.zeros((6,7))


def draw_board(board):
    pygame.init()
    
    # Initiating play square
    SQUARESIZE = 100
    width = 7 * SQUARESIZE
    height = 7 * SQUARESIZE
    size = (width, height)
    screen = pygame.display.set_mode(size)
    
    for c in range(num_columns):
        for r in range(num_rows):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE, SQUARESIZE, SQUARESIZE)) # (board, color, position, size)
            
            
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            ## Ask for input >> column = event.type
            print('hello')

draw_board(board)


