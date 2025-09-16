import random

# Generate a random number
number = random.randint(1, 100)
# Loop
while True:
    # Ask the user to make a guess
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        #   If guess < number
        if guess < number:
            #   Print too low
            print("Too low!")
        # If guess > number
        elif guess > number:
            #   Print too high
            print("Too high!")
        # Else
        else:
            #   Print well done
            print("Congratulations! You guessed the number.")
            break
    # If not a valid number
    except ValueError:
        # Print an error
        print("Please enter a valid number.")
