import random

number_to_guess = random.randint(1, 10)  # Generate a random number between 1 and 10
print("I have picked a number between 1 and 10. Try to guess it!")

attempts = 0
guessed = False
while not guessed:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < number_to_guess:
        print("Too low, try again.")
    elif guess > number_to_guess:
        print("Too high, try again.")
    else:
        print(f"Congratulations! You've guessed the right number in {attempts} attempts.")
        guessed = True
    