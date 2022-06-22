import numpy as np
import pygame
from time import sleep
import math

BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

num_columns = 7
num_rows = 6
SQUARESIZE = 100
RADIUS = int(SQUARESIZE / 2 - 5)

width = num_columns * SQUARESIZE
height = (num_rows + 1) * SQUARESIZE

size = (width, height)

class Connect4:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('CONNECT4')
        self.screen = pygame.display.set_mode(size)
        self.__container = self.create_board()
        self.turn = 0
        self.myfont = pygame.font.SysFont("monospace", 75)
        self.game_over = False
    def create_board(self):
        # board = np.zeros((ROWS, COLLUMNS))
        self.__container = np.zeros((6, 7))
 
        return self.__container
    
    def draw_board(self):
        for c in range(num_columns):
            for r in range(num_rows):
                pygame.draw.rect(self.screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pygame.draw.circle(self.screen, BLACK, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

        for c in range(num_columns):
            for r in range(num_rows):
                if self.__container[r][c] == 1:
                    pygame.draw.circle(self.screen, RED, (
                        int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)
                elif self.__container[r][c] == 2:
                    pygame.draw.circle(self.screen, YELLOW, (
                        int(c * SQUARESIZE + SQUARESIZE / 2),  int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)
        pygame.display.update()
    def print_board(self):
        '''
        This function prints the current state of the board
        '''
        print(self.__container)
        #print('  0 1  2  3  4  5  6')
    def __is_not_full(self, column: int) -> bool:
        '''
        This function checks if the move is allowed, i.e. the column is not full
            column: an int from 0 to 5 representing the column where to check if is not full
            returns: True if the move is allowed
        '''
        if self.__container[0, column] == 0:
            return True

    def position_coin(self, column: int, player: int) -> bool:
        '''
        This function check if a move is allowed and place the coin in the selected column.
        In the selected column it check from the bottom which is the first empty place to place it.
            column: an int from 0 to 5 representing the column where to place the coin
            player: an int (0 or 1) representing the current player making the move
            returns: True if the move was allowed and the board is updated, False if the move was not allowed
        '''
        res = self.__is_not_full(column)
        if res:
            for row in reversed(range(len(self.__container[:,column]))):
                if self.__container[row,column] == 0:
                    break
            self.__container[row,column] = player ## Here the coin is inserted
            return res
        else:
            print('The column is full -> Select another one')
            return False

    def check_win(self, player: int) -> int:
        '''This function evaluates whether a move ends the game (either winning/draw)'''
        # Check horizontal locations for win
        for c in range(7 - 3):
            for r in range(6):
                if self.__container[r][c] == self.__container[r][c + 1] == self.__container[r][c + 2] == \
                        self.__container[r][c + 3] == player:
                    return player

                    # Check for vertical win
        for c in range(7):
            for r in range(6 - 3):
                if self.__container[r][c] == self.__container[r + 1][c] == self.__container[r + 2][c] == \
                        self.__container[r + 3][c] == player:  ## self.__container==self.__container==player
                    return player

        # Check for decreasing diagonal win (slope <0)
        for c in range(7 - 3):
            for r in range(6 - 3):
                if self.__container[r][c] == self.__container[r + 1][c + 1] == self.__container[r + 2][c + 2] == \
                        self.__container[r + 3][c + 3] == player:
                    return player

        # Check for increasing diagonal win (slope >0)
        for c in range(7 - 3):
            for r in range(3, 6):
                if self.__container[r][c] == self.__container[r - 1][c + 1] == self.__container[r - 2][c + 2] == \
                        self.__container[r - 3][c + 3] == player:
                    return player

        # Check if draw
        if np.all(self.__container):
            return 3

        return 0

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEMOTION:
                self.update_board(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(self.screen, BLACK, (0, 0, width, SQUARESIZE))
                # print(event.pos)
                # Ask for Player 1 Input
                if self.turn == 0:
                    posx = event.pos[0]
                    col = int(math.floor(posx / SQUARESIZE))

                    if self.position_coin(col,1):

                        if self.check_win(1) == 1:
                            label = self.myfont.render("Player 1 wins!!", 1, RED)
                            self.screen.blit(label, (40, 10))
                            self.game_over = True
                else:
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))
                    if self.position_coin(col,2):
                        if self.check_win(2) == 2:
                            label = self.myfont.render("Player 2 wins!!", 1, RED)
                            self.screen.blit(label, (40, 10))
                            self.game_over = True
                self.print_board()

                self.turn += 1
                self.turn = self.turn % 2
            self.draw_board()
            if self.game_over:
                pygame.time.wait(3000)


    def update_board(self,event):
        pygame.draw.rect(self.screen, BLACK, (0, 0, width, SQUARESIZE))
        posx = event.pos[0]
        if self.turn == 0:
            pygame.draw.circle(self.screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
        else:
            pygame.draw.circle(self.screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)
        pygame.display.update()

    def gameloop(self):
        while not self.game_over:
            self.event_handler()
            pygame.display.update()


if __name__ == "__main__":
    game = Connect4()
    game.gameloop()
