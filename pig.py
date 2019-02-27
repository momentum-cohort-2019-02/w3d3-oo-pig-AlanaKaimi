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
        # generates # between 1-6
            #if num >1 add num to current_score
            #if number = 1, turn is over, total_score doesn't change, next player

    def hold_turn():
        # ends turn, and adds current_score to total_score





class Game():
    """ Defines game start, play, and end """

    def __init__(self, player, action):
        """
        Parameters:
        
        """
        self.player = player
        self.action = action
        

    def game_start():
        # Welcomes player, asks for name
        # Generates 1st player randomly
        

    def game_play():
        # Gets player action
        # enters turn loop
        # displays player rolls
        # displays current & total scores


    
    def game_end():
        # When player total_score is >=100
            # declare winner
            # ask if player wants to play again