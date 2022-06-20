# connect4.py

import numpy as np

class Board:
    def __init__(self) -> None:
        self.__container = np.zeros((6,7))
        

    def __is_full(self, location: int) -> bool:
        '''
        check if the move is allowed
        '''
        pass

    def check_win(self, player: int) -> int:
        # Check horizontal locations for win
        for c in range(7-3):
            for r in range(6):
                if self.__container[r][c] == self.__container[r][c+1] == self.__container[r][c+2] == self.__container[r][c+3] == player
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
        

    def position_coin(self, location: int, player: int) -> bool:
        pass
       
        
class Game:
    def __init__(self, num_player: int):
        self.b = Board()
        self.num_player = num_player
        self.__player = 1
    
    def player_turn(self) -> int:
        pass

            

    

if __name__ == "__main__":

    x = Board()
    x.show_self.__container()



   
    '''    while True:
            g = Game('input')
            while True:
                g.make_a_move()
        
            new_game = input("Play again? ").lower()
            if new_game == 'yes':
                print("\n-------------------------\nNEW GAME")
                continue
            elif new_game == 'no':
                print("\n-------------------------\n\nTHANKS FOR PLAYING\n")
                break'''
