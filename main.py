# connect4.py

import numpy as np

class Board:
    def __init__(self) -> None:
        self.__container = np.array(7,6)

    def __is_full(self, location: int) -> bool:
        '''
        check if the move is allowed
        '''
        if self.__container[location] == 0:
            return True
        else:
            return False

    def check_win(self, player: int) -> int:
        '''
        Check if a player won
        '''
        #FIXME: add the draw option
        for i in range(3):
            if self.__container[0+i] == self.__container[1+i] == self.__container[2+1] == player: # Horizontals (-)
                return player
        for i in range(3):
            if self.__container[0+i] == self.__container[3+i] == self.__container[6+1] == player: # Verticals (|)
                return player
        if self.__container[0] == self.__container[4] == self.__container[8] == player: # Diagonal (\)
            return player
        elif self.__container[2] == self.__container[4] == self.__container[6] == player: # Diagonal (/)
            return player
        else:
            return 0

    def show_board(self) -> list:
        matrix = [ self.__container[i:i+3] for i in range(0,len(self.__container),3)]
        for l in matrix:
            print(l)

    def locate_tile(self, location: int, player: int) -> bool:
        res = self.__check_rules(location,player)
        if res == True:
            self.__container[location] = player
            return res
        else:
            print('\nNO CHEATING!!! <> use available positions')
            return False
        
class Game:
    def __init__(self, num_player: int):
        self.b = Board()
        self.num_player = num_player
        self.__player = 1
    
    def make_a_move(self) -> int:
        #FIXME: add single player
        #FIXME: allow only 0 to 8
        if self.num_player == 2:
            print("-------------------------\nCurrent Player: {}\n".format(self.__player))
            self.b.show_board()
            res = self.b.locate_tile(int(input('\nLocate tile in position:')),self.__player)
            if res == True:
                if self.b.check_win(self.__player):
                    print("\n-------------------------\nPlayer {} has won!!\n".format(self.__player))
                    self.b.show_board()
                    print("\nCONGRATULATIONS!!\n-------------------------\n")
                    return 0
            else:
                return -1
            if self.__player == 1:
                self.__player = 2
            else:
                self.__player = 1
            return 1

            

    

if __name__ == "__main__":

    print("\n\n\nWelcome to Tik-Tak-Toe\n")
    print('\n-------------------------\n\nNotes: You can exit the game anytime by typing "exit"\n')

    while True:
        g = Game(2)
        while True:
            res = g.make_a_move()
            if res == 0:
                break
        new_game = input("Play again? ").lower()
        #FIXME: allow only 'yes' and 'no'
        if new_game == 'yes':
            print("\n-------------------------\nNEW GAME")
            continue
        elif new_game == 'no':
            print("\n-------------------------\n\nTHANKS FOR PLAYING\n")
            break
