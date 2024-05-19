import random

def get_computer_choice():
    return random.choice(['P', 'S', 'R'])

def get_result(user, computer):
    if user == computer:
        return 0
    elif (user == 'R' and computer == 'S') or (user == 'S' and computer == 'P') or (user == 'P' and computer == 'R'):
        return 1
    else:
        return -1

options = {'P': 'Paper', 'S': 'Scissors', 'R': 'Rock'}
user_wins = 0
computer_wins = 0

while computer_wins < 3 and user_wins < 3:
    user_input = input("Choose (P)aper, (S)cissors, or (R)ock: ").upper()
    
    computer_choice = get_computer_choice()
    print(f"You chose {options[user_input]}, Computer chose {options[computer_choice]}")
    
    result = get_result(user_input, computer_choice)
    if result == 1:
        user_wins += 1
        print("You win this round!")
    elif result == -1:
        computer_wins += 1
        print("Computer wins this round!")
    else:
        print("It's a tie! No points.")
    print(f"Score: You = {user_wins}, Computer = {computer_wins}")

print(f"Final score: You won {user_wins} times. Computer won {computer_wins} times.")
if user_wins > computer_wins:
    print("You are the overall winner!")
else:
    print("Computer is the overall winner!")
