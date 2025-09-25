import random

best_score = 0

def number_range(value):
    while True:
        try:
            return int(input(value))
        except ValueError:
            print("Please enter a valid number.")

minimum = number_range("What is the minimum value of the number range? ")
# Loop
while True:
    maximum = number_range("What is the maximum value of the number range? ")
    if maximum <= minimum:
        print("Please enter a valid number.")
    else: 
        break     

while True:
    # Generate a random number
    number = random.randint(minimum, maximum)
    for i in range(10):        
        while True:
            try:
                # Ask the user to make a guess
                guess = int(input("Guess a number: "))
                break
            except ValueError:
                print("Please enter a valid number.")
        # If guess < number
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
            if i == 0: 
                print("Congratulations! You guessed the number in the first attempt.")
            else: 
                print(f'Congratulations! You guessed the number in {i + 1} attempts.')

            if best_score == 0 or i + 1 < best_score:
                best_score = i + 1
                print(f'New best score: {best_score}')
            else:
                print(f'Best score: {best_score}')
            break
    else:
        print(f'You ran out of attempts. The correct number is {number}')
    
    while True:
        choice = input("Play again with the same range? (y/n): ").lower()
        if choice == 'y':
            break
        elif choice == 'n':
            print("Thanks for playing!")
            exit()
        else: 
            print("Invalid choice.")