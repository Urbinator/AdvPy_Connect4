# connect4.py

import numpy as np
<<<<<<< HEAD
print('something')
=======
print('hello world')
>>>>>>> 59a7f897538ac7aba1339c905de3015fbbf5caf0
class Board:
    def __init__(self) -> None:
        self.__container = np.zeros(2,6,7)
        

    def __is_full(self, location: int) -> bool:
        '''
        check if the move is allowed
        '''
        pass

    def check_win(self, player: int) -> int:
        '''
        Check if a player won
        '''
        pass
        

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
    x.show_board()



   
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
