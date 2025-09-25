import random

total = 0

# Loop  
while True:
    # Ask: roll the dice?
    answer = input("Roll the dice? (y/n): ")

    # If user enter y
    if answer in ("y", "Y"):
        while True:
            try:
                number = int(input("How many dice?: "))
                if number <= 0:
                    print("Please enter a valid number.")
                    continue
                break                
            except ValueError:
                print("Please enter a valid number.")

        dice = "" 
        # Generate random numbers 
        for i in range(number): 
            each_dice = random.randint(1,6) 
            dice += str(each_dice)  
        print(f'({", ".join(dice)})')

        total += 1
        print(f'Number of times dice are rolled: {total}')

    # If user enter n
    elif answer in ("n", "N"):
        #   Print thank you message
        print("Thanks for playing!")
        #   Terminate
        break

    # Else
    else: 
        #   Print invalide choice
        print("Invalid choice!")