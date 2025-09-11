import random
# Loop
a = True 
while a == True:
# Ask: roll the dice?
    answer = input("Roll the dice? (y/n): ")
    # If user enter y
    if answer in ("y", "Y"):
        #   Generate two random numbers
        #   Print them
        print("(",random.randint(1,6),", ",random.randint(1,6),")")
    # If user enter n
    elif answer in ("n", "N"):
        #   Print thank you message
        print("Thanks for playing!")
        #   Terminate
        a = False
    # Else
    else: 
        #   Print invalide choicey
        print("Invalid choice!")
