### Game-enstein

import random

class Dice:

    def roll_dice(self):

        return random.randint(1, 6)



class ComputerPlayer:
    """ Represents the Player inside of the game console """

    def __init__(self, name, action, score):
        """
        Parameters:
        - name -- the player's name
        - action -- the action taken during the players turn
        - score -- turn-score and total_score
        """
        self.name = name
        self.action = action
        self.score = score


    def take_turn(self):
        #randomly chooses to roll or hold
            
        #if roll:
        # generates # between 1-6
            #if num >1 add num to turn_score
            #if number = 1, turn is over, total_score doesn't change, next player

            # else hold: ends turn, and adds current_score to total_score




class HumanPlayer:
    """ Represents the Player outside of the game console """

    def __init__(self, name, action, score):
        """
        Parameters:
        - name -- the player's name
        - action -- the action taken during the players turn
        - score -- turn-score and total_score
        """
        self.name = name
        self.action = action
        self.score = score
    
    def take_turn(self):
        #input choice to roll or hold
        #if roll:
        # generates # between 1-6
            #if num >1 add num to turn_score
            #if number = 1, turn is over, total_score doesn't change, next player

            # else hold: ends turn, and adds current_score to total_score 


class Game():
    """ Defines game start, play, and end """

    def __init__(self, player1, player2):
        """
        Parameters:
        
        """
        self.player = player
        self.action = action
        

    def game_start():
        # Welcomes player, asks for name
        # Generates 1st player randomly
        

    def game_play():
        # Alternate player turns
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
    