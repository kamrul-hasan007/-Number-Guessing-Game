import random

# Number Guessing Game
print("Welcome to the Number Guessing Game!")
print("Try to guess the number between 1 and 100.")

# Generate random number
secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Enter your guess: ")

    # Validate user input
    if not guess.isdigit():
        print("Invalid input! Please enter a numeric value.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Congratulations! You've guessed the number in {attempts} attempts.")
        break
