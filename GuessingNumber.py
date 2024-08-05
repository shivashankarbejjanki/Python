import random

def number_guessing_game():
    # Define the range for the random number
    lower_bound = 1
    upper_bound = 100

    # Generate a random number
    target_number = random.randint(lower_bound, upper_bound)

    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")

    # Initialize variables
    guess = None
    attempts = 0

    # Game loop
    while guess != target_number:
        try:
            # Get the user's guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Provide feedback
            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    number_guessing_game()
