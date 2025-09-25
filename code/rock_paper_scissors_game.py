import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
emojis = {ROCK: '🪨', PAPER: '📃', SCISSORS: '✂️'}
choices = tuple(emojis.keys())
win_cases = ((ROCK, SCISSORS), (SCISSORS, PAPER), (PAPER, ROCK))

# Ask the user to make a choice
def get_user_choice():
    while True: 
        user_choice = input("Rock, paper, or scissors? (r,p,s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice!")

    
# Print choices (emojis)    
def print_choices(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')  


# Determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice, computer_choice) in win_cases:
        return "win"
    else: 
        return "lose"

# Ask the user if they want to continue
def play_again():
    while True:
        answer = input("Play again? (y/n): ").lower()
        if answer == 'y':
            return True
        # If not
        elif answer == 'n':
            print("Thanks for playing!")
            #   Terminate
            return False
        else: 
            print("Invalid choice")

def play_game():

    while True:
        user_score = 0
        computer_score = 0
        ties = 0

        while user_score < 2 and computer_score <2:
            user_choice = get_user_choice()

            # Let the computer make a choice
            computer_choice = random.choice(choices) 

            print_choices(user_choice, computer_choice)

            result = determine_winner(user_choice, computer_choice)
            if result == "tie":
                print("Tie!")
                ties += 1
            elif result == "win":
                print("You win this round")
                user_score += 1
            else:
                print("You lose this round")
                computer_score += 1
        
            print(f'Wins: {user_score}, Losses: {computer_score}, Ties: {ties}')

        if user_score == 2:
            print("You won the game")
        else: 
            print("You lose the game")   

        if not play_again():
            break        

play_game()





