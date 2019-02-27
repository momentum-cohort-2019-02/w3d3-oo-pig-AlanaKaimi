import random

class Player():
    """ Represents the Players """

    def __init__(self, action, score):
        """
        Parameters:
        - human -- the player outside
        - computer -- the player inside
        """
        self.action = action
        self.score = score

    def human_player(self, action, score):


    def computer_player(self, action, score):



class Actions():
    """ Defines actions players can take """

    def __init__(self, roll, hold):
        """
        Parameters:
        - roll -- the player rolls a dice resulting in a number between 1-6
        - hold -- the player holds and adds current score to total score
        """
        self.roll = roll
        self.hold = hold

    def roll_die():


    def hold_turn():

    def roll_again():



class Game():
    """ Defines game start, play, and end """

    def __init__(self, player, action):
        """
        Parameters:
        
        """
        self.player = player
        self.action = action
        

    def game_start():


    def game_play():

    
    def game_end():