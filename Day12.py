import random

# Define the number of attempts
TOTAL_ATTEMPTS = 10

def check_guess(guess, answer, attempts):
    """Checks the player's guess against the answer."""
    if guess > answer:
        print("Too high.")
        return attempts - 1
    elif guess < answer:
        print("Too low.")
        return attempts - 1
    else:
        print(f"You got it! The answer was {answer}.")
        return 0


def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    answer = random.randint(1, 100)
    print(f"Psst, the correct answer is {answer}")  # Debugging aid; remove for real gameplay.
    
    attempts = TOTAL_ATTEMPTS
    guess = 0  # Initialize with a value outside the valid range.
    
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
        attempts = check_guess(guess, answer, attempts)
        if guess == answer:
            break
        
        if attempts == 0:
            print(f"You've run out of guesses. The correct answer was {answer}.")
        elif attempts > 0:
            print("Guess again.")


while input("Do you want to play the Number Guessing Game? Type 'yes' or 'no': ").lower() == "yes":
    play_game()
print("Goodbye!")
