# connect4.py

from secrets import randbelow
import numpy as np
from torch import rand

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
        

    def get_board(self):
        '''
        This function returns the current state of the board
        '''
        return self.__container
        

    def position_coin(self, column: int, player: int) -> bool:
        '''
        This function check if a move is allowed and place the coin in the selected column.
        In the selected column it check from the bottom which is the first empty place to place it.
            column: an int from 0 to 6 representing the column where to place the coin
            player: an int (1 or 2) representing the current player making the move
            returns: True if the move was allowed and the board is updated, False if the move was not allowed
        '''
        res = self.__is_not_full(column)
        if res:
            for row in reversed(range(len(self.__container[:,column]))):
                if self.__container[row,column] == 0:
                    break
            self.__container[row,column] = player
            return res
        else:
            print('The column is full -> Select another one')
            return False

class Bot(Board):
    def __init__(self):
        self.diff = None
        super().__init__()

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
        self._Board__container = curr_board.copy()
    
    def random_move(self,curr_board: object) -> int:
        '''
        This function picks a random column and place a coin.
            board: the matrix containing the current state of the board
            Return: an int representing the column
        '''
        self.set_current_board(curr_board)
        while True:
            col = np.random.randint(0,7)
            if self.position_coin(col,2):
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
                if self.position_coin(col,player):
                    print(self.get_board())
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

class Game:
    def __init__(self, num_player: int):
        self.b = Board()
        self.num_player = num_player
        self.__player = 1
        self.bot = Bot()

    def player_turn(self) -> int:
        '''function moderates the turns each player takes & checks winning condition after each turn'''
        if self.num_player == 2:
            print(self.b.get_board())
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
            print(self.b.get_board())
            column = int(input("\nIn which column do you want to place your coin? "))
            res = self.b.position_coin(column,self.__player)
            if res == True:
                if self.b.check_win(self.__player) == self.__player:
                    print('\nCONGRATS! You won\n')
                    print(self.b.get_board())
                    return True
                elif self.b.check_win(self.__player) == 3:
                    print('\nDRAW\n')
                    print(self.b.get_board())
                    return True
                else:
                    res = self.b.position_coin(self.bot.bot_move(self.b.get_board()),2)
                    if res == True:
                        if self.b.check_win(2) == 2:
                           print('\nYou lost\n')
                           print(self.b.get_board())
                           return True
                        elif self.b.check_win(2) == 3:
                            print('\nDRAW\n')
                            print(self.b.get_board())
                            return True

    

if __name__ == "__main__":

    #FIXME create new class bot in the execution, not inside game
    
    print("\n\n\nWelcome to CONNECT 4\n")
    
    while True:
        n_players = int(input('Select number of players: '))
        g = Game(n_players)
        if n_players == 1:
            g.bot.set_difficulty(input('Select the difficulty: (easy,moderate,hard) '))
        while True:
            if g.player_turn():
                break
        
        new_game = input("\nPlay again? (yes,no)").lower()
        if new_game == 'yes':
            print("\n-------------------------\nNEW GAME")
            continue
        elif new_game == 'no':
            print("\n-------------------------\n\nTHANKS FOR PLAYING\n")
            break