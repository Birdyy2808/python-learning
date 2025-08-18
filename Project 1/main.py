import random

# 1. Create a list
my_list = ["snake","water","gun"]


while True:

    # 2. Ask computer to choose an item from list.
    comp_choice = random.choice(my_list)

    # 3. Ask user to input the value
    user_choice = input("Enter the choice between \"snake\",\"water\",\"gun\": ").lower()
    
    if user_choice not in my_list:
        print("Invalid input, Please choose from snake, water, or gun.")
        continue
    
    print(f"You chose {user_choice}")
    print(f"Computer chose {comp_choice}")

    # 4. Compare the values and decide who wins
    if comp_choice == user_choice:
        print("Draw")
    elif ((comp_choice == "snake" and user_choice == "water")
    or (comp_choice == "water" and user_choice == "gun") 
    or (comp_choice == "gun" and user_choice == "snake")):
        print("Computer won")
    else:
        print("You won")

    play_continue = input("Do you wish to continue? (Yes or No): ").lower()

    if play_continue != "yes":
        print("Thanks for playing")
        break