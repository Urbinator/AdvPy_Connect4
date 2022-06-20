# connect4.py

print("test")
import numpy as np

print('something')
print('hello world')
print('hello world 2')

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
        '''function moderates the turns each player takes & checks winning condition after each turn'''
        if self.num_player == 2:
            self.b.show_board
            column = input("In which column do you want to place your coin?")

            
            if self.b.place_coin(column = column, player = self.__player) == True:
                if self.b.check_win(player = self.__player) == True:
                    break
                else:
                    self.__player = 2


        elif self.num_player == 1:
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
