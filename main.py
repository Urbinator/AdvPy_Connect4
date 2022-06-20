# connect4.py

import numpy as np
print('hello world')
class Board:
    def __init__(self) -> None:
        self.__container = np.array(7,6)
        

    def __is_full(self, location: int) -> bool:
        '''
        check if the move is allowed
        '''
        

    def check_win(self, player: int) -> int:
        '''
        Check if a player won
        '''
        

    def show_board(self) -> list:
        

    def position_coin(self, location: int, player: int) -> bool:
       
        
class Game:
    def __init__(self, num_player: int):
        self.b = Board()
        self.num_player = num_player
        self.__player = 1
    
    def player_turn(self) -> int:
        

            

    

if __name__ == "__main__":

   
    while True:
        g = Game('input')
        while True:
            g.make_a_move()
    
        new_game = input("Play again? ").lower()
        if new_game == 'yes':
            print("\n-------------------------\nNEW GAME")
            continue
        elif new_game == 'no':
            print("\n-------------------------\n\nTHANKS FOR PLAYING\n")
            break
