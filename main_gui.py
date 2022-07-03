## main_gui.py

# main script to play with GUI

# MIT License
# 
# Copyright (c) 2022 Simon Urban, Robert Bernasconi, Casper Kirch, Jose Marques, Akshit Gupta
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

import argparse
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
    screen: A UI screen for the users to interact upon
    __container: a hidden parameter that contains the up to date values of the game.
    turn: it's an int (0)
    myfont: defines UI font and font size
    game_over: initialy set to False
    num_players: number of players (1 or 2)
    bot_difficulty: if in single player mode, it is the both difficulty level (easy,medium,hard)
    
    Methods
    ----------
    draw_board()
        visualizes empty board
    check_move_allowed()
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
    def __init__(self,num_players: int,bot_difficulty: str = None) -> None:
        '''
        Initialization function
            num_players: number of players (1 or 2)
            bot_difficulty: if in single player mode, it is the both difficulty level (easy,medium,hard)
            pygame: initiate game with a title "CONNECT 4"
            return: None
        '''
        pygame.init()
        pygame.display.set_caption('CONNECT 4')
        self.screen = pygame.display.set_mode(size)
        self.__container = np.zeros((6, 7))
        self.turn = 0
        self.myfont = pygame.font.SysFont("comicsansms", 75)
        self.game_over = False
        self.num_players = num_players
        self.bot_difficulty = bot_difficulty

    def draw_board(self):
        '''
        Draws empty board using rectangles and circles
        '''
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

    def check_move_allowed(self, column: int) -> bool:
        '''
        This hidden function checks if the move is allowed, i.e. the column is not full
            column: an int from 0 to 5 representing the column where to check if is not full
            returns: True if the move is allowed
        '''
        return self.__container[0, column] == 0

    def place_coin(self, column: int, player: int) -> bool:
        '''
        This function checks if a move is allowed and place the coin in the selected column.
        In the selected column it checks from the bottom which is the first empty place to place it.
            column: an int from 0 to 5 representing the column where to place the coin
            player: an int (0 or 1) representing the current player making the move
            returns: True if the move was allowed and the board is updated
        '''
        res = self.check_move_allowed(column)
        if res:
            for row in reversed(range(len(self.__container[:, column]))):
                if self.__container[row, column] == 0:
                    break
            self.__container[row, column] = player  # Here the coin is inserted
            return res

    def check_win(self, player: int) -> int:
        '''
        This function evaluates whether a move ends the game (either winning/draw)
        '''
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
                        self.__container[r + 3][c] == player:
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

    def event_handler(self):
        '''
        This function handles the UI by iterating through every event in pygame window
        MOUSEMOTION - handles the coin hovering above the board before being played
        MOUSEBUTTONDOWN - handles playing the coin on the board
        Checks for winning move using check_win
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEMOTION:
                self.draw_coin(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(self.screen, BLACK, (0, 0, width, SQUARESIZE))
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
                
                # if 2 players change turn, if 1 make the bot move
                if self.num_players==2: # Change turn if 2 players
                    self.turn += 1
                    self.turn = self.turn % 2
                else:
                    if not self.game_over: 
                        # Bot input
                        bot = Bot(self.bot_difficulty) #instantiate bot object
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
            self.draw_board()
            if self.game_over: 
                pygame.time.wait(3000)

    def draw_coin(self, event):
        ''' 
        Creates a new coin for the next player to use. 
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
        '''
        A loop that lets the players continue to make their next move and updates the board until the game is over.
        '''
        while not self.game_over:
            self.event_handler()
            pygame.display.update()

class Bot(Connect4):
    '''
    Bot class with all functionalities needed to play against the computer in single player mode.
    Inheritance from the class Connect4 is needed to use the main methods
    Attributes
    -----------
    All the ones of inherithed from Connect4 class (only _Connect4__container and bot_difficulty are used)
    
    Methods
    ----------
    All the ones of inherithed from Connect4 class (only place_coin,check_win and check_move_allowed are used)
    set_current_board: creates copy of the board state to be evaluated by the bot for its moves
    random_move: picks a random column and place a coin
    place_4th_coin: check if there is a winning move for either player and place the coin in that position (priority to own winning move)
    check_mistake: check if a move would create a new winning opportunity for the opponent
    bot_move: uses the current state of the board and the difficulty level selected to return a column which represent the move for the Bot player
    '''

    def __init__(self,difficulty: str) -> None:
        '''
        Initialization function
        Inherits attributes and methods from Connect4 class
        Also allow to set the bot_difficulty (which is none by default in the parent class)
        '''
        super().__init__(1,difficulty)

    def set_current_board(self, curr_board: object):
        '''
        This function set the copy of the board state to be evaluated by the bot for its moves
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
        self.set_current_board(curr_board)
        for player in reversed(range(1,3)):
            for col in range(7):
                if self.place_coin(col,player):
                    if self.check_win(player) == player:
                        return col
                    self.set_current_board(curr_board)

    def check_mistake(self,column: int,curr_board: object) -> bool:
        '''This function check if a move would create a new winning opportunity for the opponent
            column: int representing the column of the move to check
            board: the matrix containing the current state of the board
            Return: an bool indicating if the move is a mistake 
        '''
        self.set_current_board(curr_board)
        if self.place_coin(column,2):
            updated_board = self._Connect4__container #current_board updated with the potential move/mistake
            for col in range(7):
                if self.place_coin(col,1):
                    if self.check_win(1) == 1:
                        return True
                    self.set_current_board(updated_board)
                    
    def bot_move(self,curr_board: object):
        '''
        This function uses the current state of the board and the difficulty level selected to make a move for the Bot player
            board: the matrix containing the current state of the board
        '''
        if self.bot_difficulty == 'easy': #random move
            return self.random_move(curr_board)
        elif self.bot_difficulty == 'moderate': #identify 3 in a row and place coin in the forth space (priority to winning move, then to stop the other's win), otherwise random move
            res = self.place_4th_coin(curr_board)
            if res != None:
                return res
            else:
                return self.random_move(curr_board)
        elif self.bot_difficulty == 'hard': #same as 'moderate' but it also check if a move is a mistake (mistake: the move creat a new winning opportunity for the other player)
            res = self.place_4th_coin(curr_board)
            if res != None:
                return res
            else:
                # Check if there are moves that are not mistakes
                available_moves = 0
                for col in range(7):
                    if self.check_move_allowed(col):
                        if not self.check_mistake(col,curr_board):
                            available_moves += 1
                # If there are: select randomly
                if available_moves > 0:
                    while True:
                        rand_move = self.random_move(curr_board)
                        if not self.check_mistake(rand_move,curr_board):
                            return rand_move
                # If there aren't moves  that are not mistakes: place the mistake anyway (to avoid entering an infinite loop and halt the game)
                else:
                    return self.random_move(curr_board)


if __name__ == "__main__":
    #Arguments to pass
    parser = argparse.ArgumentParser(
        description="This program takes 2 arguments:\n1)Number of Players\n2)The bot level (only required for single player)")
    parser.add_argument('-number_of_players','-num', type=int, required=True, help='Select number of Players: 1 or 2')
    parser.add_argument('-bot_difficulty','-diff', choices=['easy', 'moderate', 'hard'], required=False, help='Select bot difficulty in single player')
    argument_list = parser.parse_args()
    # Make the -bot_difficulty argument necessary only if 2 players are selected
    if argument_list.number_of_players == 1 and argument_list.bot_difficulty is None:
        parser.error("-number_of_players = 1 requires -bot_difficulty/-diff")
    
    # Start Game
    game = Connect4(argument_list.number_of_players,argument_list.bot_difficulty)
    game.gameloop()
