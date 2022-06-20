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
        '''
        Check if a player won
        '''
        pass
        

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
        pass

    

if __name__ == "__main__":

    print("\n\n\nWelcome to CONNECT 4\n")
    
    while True:
        g = Game(int(input('Select number of players: ')))
        while True:
            g.player_turn()
        
        new_game = input("Play again? ").lower()
        if new_game == 'yes':
            print("\n-------------------------\nNEW GAME")
            continue
        elif new_game == 'no':
            print("\n-------------------------\n\nTHANKS FOR PLAYING\n")
            break
