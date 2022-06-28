# MIT License
# 
# Copyright (c) 2022 Simon Urban, Robert Bernasconi, Casper Kirch, Jose Marques, Akshit XXX
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import numpy as np
import pygame
from time import sleep
import math

#GLOBAL VARIABLES
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
#GLOBAL VARIABLES END

class Connect4:
    '''Main Connect 4 class with all functionalities needed
    Attributes
    -----------
    Player: int
        Which player is currently playing (0 or 1)
    column: int
        Int from 0 to 5 representing the column where to place the coin
    
    Methods
    ----------
    create_board()
        creates empty Connect 4 matrix
    draw_board()
        visualizes empty board
    print_current_board()
        prints current status of the board
    __check_move_allowed()
        checks if the desired move is allowed/ possible
    place_coin()
        places the coin in the desired column, after the desired move is checked regarding feasibility
    check_win()
        checks the winning conditions
    event_handler()
        inputs users interactions into the place_coin() function for each player and checks for winning condition via the check_win() function
    draw_coin()
        creates a new coin at the beginning of each player's turn
    gameloop()
        loops through event_handler() until winning condition is met

    '''
    def __init__(self,num_players):
        '''
        Initialization function
            pygame: with a title "CONEECT 4"
            screen: A UI screen for the users to interact upon
            __container: a hidden parameter that contains the up to date values of the game.
            turn: it's an int (0)
            myfont: defines UI font and font size
            game_over: initialy set to False
            
            return: None
        '''
        pygame.init()
        pygame.display.set_caption('CONNECT 4')
        self.screen = pygame.display.set_mode(size)
        self.__container = self.create_board()
        self.turn = 0
        self.myfont = pygame.font.SysFont("comicsansms", 75)
        self.game_over = False
        self.num_players = num_players

    def create_board(self):
        '''This function creates an empty Connect 4 matrix with zeros.'''
        # board = np.zeros((ROWS, COLLUMNS))
        self.__container = np.zeros((6, 7))

        return self.__container

    def draw_board(self):
        '''Draws empty board using rectangles and circles'''
        for c in range(num_columns):
            for r in range(num_rows):
                pygame.draw.rect(self.screen, BLUE,
                                 (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pygame.draw.circle(self.screen, BLACK, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

        for c in range(num_columns):
            for r in range(num_rows):
                if self.__container[r][c] == 1:
                    pygame.draw.circle(self.screen, RED, (
                        int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)),
                                       RADIUS)
                elif self.__container[r][c] == 2:
                    pygame.draw.circle(self.screen, YELLOW, (
                        int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)),
                                       RADIUS)
        pygame.display.update()
 
    #FIXME: is function print_current_board() still needed, if pygame visualizes and updates baord via draw_board() ?
    def print_current_board(self):
        '''
        This function prints the current state of the board
        '''
        print(self.__container)
        # print('  0 1  2  3  4  5  6')

    def __check_move_allowed(self, column: int) -> bool:
        '''
        This hidden function checks if the move is allowed, i.e. the column is not full
            column: an int from 0 to 5 representing the column where to check if is not full
            returns: True if the move is allowed
        '''
        if self.__container[0, column] == 0:
            return True

    def place_coin(self, column: int, player: int) -> bool:
        '''
        This function checks if a move is allowed and place the coin in the selected column.
        In the selected column it checks from the bottom which is the first empty place to place it.
            column: an int from 0 to 5 representing the column where to place the coin
            player: an int (0 or 1) representing the current player making the move
            returns: True if the move was allowed and the board is updated, False if the move was not allowed
        '''
        res = self.__check_move_allowed(column)
        if res:
            for row in reversed(range(len(self.__container[:, column]))):
                if self.__container[row, column] == 0:
                    break
            self.__container[row, column] = player  ## Here the coin is inserted
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
        '''handles the UI by iterating through every event in pygame window
        MOUSEMOTION - handles the coin hovering above the board before being played
        MOUSEBUTTONDOWN - handles playing the coin on the board
        Checks for winning move using check_win'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEMOTION:
                self.draw_coin(event)
            print('pre eevent type')
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(self.screen, BLACK, (0, 0, width, SQUARESIZE))
                print('before player move')
                if self.turn == 0:
                # Ask for Player 1 Input 
                    posx = event.pos[0]
                    col = int(math.floor(posx / SQUARESIZE)) 
                    if self.place_coin(col, 1):
                        if self.check_win(1) == 1:
                            label = self.myfont.render("Player 1 wins!!", 1, RED)
                            self.screen.blit(label, (110,0))
                            self.game_over = True
                        if self.check_win(1) == 3:
                            label = self.myfont.render("It's a Draw!!", 1, BLUE)
                            self.screen.blit(label, (110,0))
                            self.game_over = True
                    else:
                        break
                else:
                    # Ask for Player 2 Input
                    posx = event.pos[0]
                    col = int(math.floor(posx / SQUARESIZE))
                    if self.place_coin(col, 2):
                        if self.check_win(2) == 2:
                            label = self.myfont.render("Player 2 wins!!", 1, YELLOW)
                            self.screen.blit(label, (110,0))
                            self.game_over = True
                        if self.check_win(1) == 3:
                            label = self.myfont.render("It's a Draw!!", 1, RED)
                            self.screen.blit(label, (110,0))
                            self.game_over = True
                    else:
                        break
                    
                self.print_current_board()
                
                if self.num_players==2:
                    self.turn += 1
                    self.turn = self.turn % 2
                else:
                    if not self.game_over: 
                        print('before bot move')
                        # Bot input
                        bot = Bot()
                        bot.set_difficulty('moderate')
                        col = bot.bot_move(self.__container)
                        if self.place_coin(col,2):
                            if self.check_win(2) == 2:
                                label = self.myfont.render("Player 2 wins!!", 1, YELLOW)
                                self.screen.blit(label, (110,0))
                                self.game_over = True
                            if self.check_win(1) == 3:
                                label = self.myfont.render("It's a Draw!!", 1, RED)
                                self.screen.blit(label, (110,0))
                                self.game_over = True
            print('end of turn')            
            self.draw_board()
            if self.game_over: 
                pygame.time.wait(3000)

    def draw_coin(self, event):
        ''' Creates a new coin for the next player to use. 
        Player 1 receives a red coin. Player 2 receives a yellow coin. 
        '''
        pygame.draw.rect(self.screen, BLACK, (0, 0, width, SQUARESIZE))
        posx = event.pos[0]
        if self.turn == 0:
            pygame.draw.circle(self.screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
        else:
            pygame.draw.circle(self.screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)
        pygame.display.update()

    def gameloop(self):
        '''A loop that lets the players continue to make their next move and updates the board until the game is over.'''
        while not self.game_over:
            self.event_handler()
            pygame.display.update()

class Bot(Connect4):
    def __init__(self):
        self.diff = None
        super().__init__(1)

    def set_difficulty(self,difficulty: str):
        '''
        This function set the difficulty of the bot player
            difficulty: a str can be equal to: easy,moderate,hard,extreme
        '''
        self.diff = difficulty.lower()

    def set_current_board(self, curr_board: object):
        '''
        This function set the board state to be evaluated by the bot
            board: the matrix containing the current state of the board
        '''
        self._Connect4__container = curr_board.copy()
    
    def random_move(self,curr_board: object) -> int:
        '''
        This function picks a random column and place a coin.
            board: the matrix containing the current state of the board
            Return: an int representing the column
        '''
        self.set_current_board(curr_board)
        while True:
            col = np.random.randint(0,7)
            if self.place_coin(col,2):
                return col

    def place_4th_coin(self,curr_board: object) -> int:
        '''
        This function check if there is a winning move for either player and place the coin in that position.
        It prioritize a winning move over stopping the win of the other player.
            board: the matrix containing the current state of the board
            Return: an int representing the column 
        '''
        for player in reversed(range(1,3)):
            for col in range(7):
                if self.place_coin(col,player):
                    if self.check_win(player) == player:
                        return col
                    self.set_current_board(curr_board)
                    
    def bot_move(self,curr_board: object):
        '''
        This function uses the current state of the board and the difficulty level selected to make a move for the Bot player
            board: the matrix containing the current state of the board
        '''
        if self.diff == 'easy': #random move
            return self.random_move(curr_board)
        elif self.diff == 'moderate': #identify 3 in a row and place it (priority to winning move)
            res = self.place_4th_coin(curr_board)
            if res != None:
                print('Bot move: ',res)
                return res
            else:
                print('RANDOM bot move: ')
                return self.random_move(curr_board)
        elif self.diff == 'hard': #Trained with Reinforcement learning
            pass


if __name__ == "__main__":
    game = Connect4(1)
    game.gameloop()
