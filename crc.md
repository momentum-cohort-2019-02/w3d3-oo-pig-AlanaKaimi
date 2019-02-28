Classes


HumanPlayer:

    Responsibilities:
        - Take turn(s) <-- turn_loop
            - roll or hold? <-- input
        - keep turn_score
        - reset turn_score 
        - update total-score += turn_score


    Collaborators:
        - Game
        - Dice

ComputerPlayer:

    Responsibilities:
        - Take turn(s) <-- turn_loop
            - roll or hold? <-- random 
        - keep turn_score
        - reset turn_score
        - update total-score

    Collaborators:
        - Game
        - Dice

Dice:

    Responsibilities:
        - Generate random number between 1-6

    Collaborators:
        - Game
        - HumanPlayer
        - ComputerPlayer
Game:

    Responsibilities:
        game_start
            - Welcome players
            - display instructions
            - select random 1st player

        game_play
            - display player scores (total_score)
            - alternate player turns

        game_over
            - declare winner
            - play again?

    Collaborators:
        - HumanPlayer
        - ComputerPlayer
        - Dice
