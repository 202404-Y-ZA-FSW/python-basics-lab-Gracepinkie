import random

def guessing_game():
    """A number guessing game where the player tries to guess a randomly generated number between 1 and 100."""

    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1   and 100.")

    while True:
        attempts += 1
        guess = int(input("Enter your guess: "))

        if guess == number_to_guess:
            print(f"Congratulations! You've guessed the correct number in {attempts} attempts.")
            break
        elif guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    guessing_game()