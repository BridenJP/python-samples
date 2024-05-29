# PAPER, SCISSORS, ROCK - starter code

# Load the random module - used for the computer's choice
import random

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(['P', 'S', 'R'])

# This function takes the user and computer choices ('P', 'S', or 'R') 
# and returns -1 if the computer wins, 0 for a draw, 1 if the player wins
def get_result(user, computer):
    # >>> Write code to check choices and return the approriate value <<<
    # Hint: Consider the game rules...
    # * If they are the same it's a tie.
    # * Rock beats Scissors, Scissors beat Paper, and Paper beats Rock.
    pass # <-- Once you add your code you can remove this line

# MAIN CODE STARTS HERE

# A dictionary that defines our options
options = {'P': 'Paper', 'S': 'Scissors', 'R': 'Rock'} 

# Initialise variables to keep track how many times the player has won
# and how many times the computer has won.
# Make sure you give the variables short, but meaningful names.
# >>> Code to initialise the user's score <<<
# >>> Code to initialise the computer's score <<<

# Use a while loop to repeat the rounds until either the player
# or the computer has won 3 times.
while True: # <-- Replace True with the correct condition
    # Get the user's choice (convert it to upper case for consistency)
    # Note: You don't need to worry about input validation (for now)
    user_input = input("Choose (P)aper, (S)cissors, or (R)ock: ").upper()
    
    # Get the computer's choice
    # >>> Code to get computer choice <<<
    
    # Get the result of the round
    # >>> Call function to compare choices <<<

    # Update the score based on the result
    # >>> Code to update score <<<

    # Output the user and computer choices and who won the round
    # >>> Code to check result and output info <<<

    # Show the current score
    # >>> Code to output current score <<<

# Once there is a winner - announce the final score and overall winner
# >>> Code to output final score <<<
# >>> Code to output who won <<<
