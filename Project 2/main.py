# Project 2 -> The Perfect Guess

import random

# 1. Create a random number that comp generates
rand_num = random.randint(1,100)
guess = 0
while True:
    # 2. Increase count for guess
    guess+=1

    # 3. Create a user guess number
    user_num = int(input("Please Guess a number between 1 and 100: "))

    # 4. Print message based on user guessed num is greater or lower than random num
    if(user_num<rand_num):
        print(f"Higher number please: {user_num}")
    elif(user_num>rand_num):
        print(f"Lower number please: {user_num}")
    else:
        print(f"You guessed the number in {guess} no. of tries and the number is {rand_num}")
        break