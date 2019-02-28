import random



class Player():

class ComputerPlayer():
    """ Represents the Player inside of the game console """

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




class HumanPlayer:
    """ Represents the Player outside of the game console """

    def __init__(self, name, action, score):
        """
        Parameters:
        - name -- the player's name
        - action -- the action taken during the players turn
        - score -- 
        """
        self.name = name
        self.action = action
        self.score = score
    
    def take_turn(self, roll_die, hold_turn):
        




    def roll_die(self):
        # generates # between 1-6
        for x in range():
            print random.randint(1,7)
            #if num >1 add num to current_score
            #if number = 1, turn is over, total_score doesn't change, next player


    def hold_turn(self, action, score):


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

###! Reference from stix:

if __name__ == "__main__":
    
    # Need to randomize first player
    p1 = ComputerPlayer()
    p2 = HumanPlayer()

    game = Game(p1, p2)
    game.play_game()
    