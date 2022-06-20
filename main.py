# connect4.py

import numpy as np

class Board:
    def __init__(self) -> None:
        self.__container = np.zeros((6,7))
        

    def __is_full(self, column: int) -> bool:
        '''
        check if the move is allowed, i.e. the column is not full
        '''
        if self.__container[0,column] == 0:
            return True

    def check_win(self, player: int) -> int:
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
        print(self.__container)
        

    def position_coin(self, column: int, player: int) -> bool:
        res = self.__is_full(column)
        if res:
            for row in reversed(range(len(self.__container[:,column]))):
                if self.__container[row,column] == 0:
                    break
            self.__container[row,column] = player
            return res
        else:
            print('The column is full -> Select another one')
            return False


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


    

if __name__ == "__main__":

    print("\n\n\nWelcome to CONNECT 4\n")
    
    while True:
        g = Game(int(input('Select number of players: ')))
        while True:
            if g.player_turn():
                break
        
        new_game = input("Play again? ").lower()
        if new_game == 'yes':
            print("\n-------------------------\nNEW GAME")
            continue
        elif new_game == 'no':
            print("\n-------------------------\n\nTHANKS FOR PLAYING\n")
            break
