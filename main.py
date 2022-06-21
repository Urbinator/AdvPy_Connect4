# connect4.py

import numpy as np
import pygame 


class Board:
    def __init__(self) -> None:
        self.__container = np.zeros((6,7))
        

    def __is_not_full(self, column: int) -> bool:
        '''
        This function checks if the move is allowed, i.e. the column is not full
            column: an int from 0 to 5 representing the column where to check if is not full
            returns: True if the move is allowed
        '''
        if self.__container[0,column] == 0:
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
        for c in range(7-3):
            for r in range(6):
                if self.__container[r][c] == self.__container[r][c+1] == self.__container[r][c+2] == self.__container[r][c+3] == player:
                    return player 
                
        # Check for vertical win
        for c in range(7):
            for r in range(6-3):
                if self.__container[r][c] == self.__container[r+1][c] == self.__container[r+2][c] == self.__container[r+3][c] == player:## self.__container==self.__container==player
                    return player
                
        # Check for decreasing diagonal win (slope <0)
        for c in range(7-3):
            for r in range(6-3):
                if self.__container[r][c] == self.__container[r+1][c+1] == self.__container[r+2][c+2] == self.__container[r+3][c+3] == player:
                    return player
                
        # Check for increasing diagonal win (slope >0)
        for c in range(7-3):
            for r in range(3,6):
                if self.__container[r][c] == self.__container[r-1][c+1] == self.__container[r-2][c+2] == self.__container[r-3][c+3] == player:
                    return player
        
        # Check if draw
        if np.all(self.__container):
            return 3
        
        return 0
        

    def show_board(self):
        '''
        This function prints the current state of the board
        '''
        index = [0,1,2,3,4,5,6]
        print(self.__container)
        print('  0 1  2  3  4  5  6')


class Game:
    def __init__(self, num_player: int):
        self.b = Board()
        self.num_player = num_player
        self.__player = 1

    def player_turn(self) -> int:
        '''function moderates the turns each player takes & checks winning condition after each turn'''
        if self.num_player == 2:
            self.b.show_board()
            column = int(input("\nPLAYER {}: In which column do you want to place your coin? ".format(self.__player)))
            res = self.b.position_coin(column,self.__player)
            if res == True:
                if self.b.check_win(self.__player) == self.__player:
                    print('CONGRATS! Player {} won'.format(self.__player))
                    return True
                elif self.b.check_win(self.__player) == 3:
                    print('DRAW')
                    return True
                else:
                    if self.__player == 1:
                        self.__player = 2
                    else:
                        self.__player = 1

        elif self.num_player == 1:
            pass

class Interface:
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)

    ROW_COUNT = 6
    COLUMN_COUNT = 7
    SQUARESIZE = 100

    width = COLUMN_COUNT * SQUARESIZE
    height = (ROW_COUNT + 1) * SQUARESIZE

    size = (width, height)
    

if __name__ == "__main__":

    print("\n\n\nWelcome to CONNECT 4\n")
    
    while True:
        g = Game(int(input('Select number of players: ')))
        while True:
            if g.player_turn():
                break
        
        new_game = input("Play again? (yes,no)").lower()
        if new_game == 'yes':
            print("\n-------------------------\nNEW GAME")
            continue
        elif new_game == 'no':
            print("\n-------------------------\n\nTHANKS FOR PLAYING\n")
            break
