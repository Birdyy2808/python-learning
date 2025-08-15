# Question 1 -> Read poems.txt and find whether "twinkle" word is present or not
with open("C:\\Users\\Vaibhav Singh\\Downloads\\poems.txt") as file:
    if "Twinkle" in file.read():
        print("Present in file")
    else:
        print("Not present")

# Question 2 -> Create a game function and overwrite the score if score exceeds in the file
import random
def game():
    while True:
        score  = random.randint(1,100)
        with open("C:\\Users\\Vaibhav Singh\\Downloads\\highscore.txt","r") as f:
            high_score = f.read()
            if high_score!="":
                high_score = int(high_score)
            else:
                high_score = 0

        print(f"Your score is {score}")

        if score>high_score:
            with open("C:\\Users\\Vaibhav Singh\\Downloads\\highscore.txt","w") as file:
                file.write(str(score))
        
        user_choice  = input("Do you want to play again? Y or N: ").lower()
        if user_choice != "y":
            break

    return score
    
game()

# Question 3 -> Write a table from 2 to 21 and write in a file
def generate_table(n):

    for i in range(1,11):
        with open(f"C:\\Users\\Vaibhav Singh\\Downloads\\tables\\tables_{n}.txt","a") as file:
            file.write(f"{n} * {i} = {n*i}\n")


for i in range(2,21):
    generate_table(i)

# Question 4 -> A file contain "Donkey" multiple times. Write code to replace the word with ####
def replace_word(str):

    with open("C:\\Users\\Vaibhav Singh\\Downloads\\new_file.txt") as file:
        content = file.read()
    
    new_content = content.replace(str,"#####")

    with open("C:\\Users\\Vaibhav Singh\\Downloads\\new_file.txt","w") as f:
        f.write(new_content)


replace_word("Donkey")

# Question 5 -> For Question 4., list of words are give, censor them
my_list  = ["Donkey","Parrot","Cat"]

with open("C:\\Users\\Vaibhav Singh\\Downloads\\new_file.txt") as file:
    content = file.read()

for i in my_list:
    content = content.replace(i,"#"*len(i))

with open("C:\\Users\\Vaibhav Singh\\Downloads\\new_file.txt","w") as f:
    f.write(content)

# Question 6 -> Check the log file if it contains the Python word in it
with open("C:\\Users\\Vaibhav Singh\\Downloads\\log.txt") as file:
    content = file.read()

if "Python" in content:
    print("Contains Python")
else:
    print("Does not contain python")

# Question 7 -> From Q.6, find in which line Python is present
with open("C:\\Users\\Vaibhav Singh\\Downloads\\log.txt") as file:
    lines = file.readlines()

    line_no = 1
    for line in lines:
        if "Python" in line:
            print(f"Python is present in the line {line_no}")
        else:
            print("Not present")
        line_no+=1

# Question 8 -> Write a program to make a copy of txt file "this.txt"
with open("C:\\Users\\Vaibhav Singh\\Downloads\\log.txt") as file:
    content  = file.read()

with open("C:\\Users\\Vaibhav Singh\\Downloads\\log_copy.txt","w") as f:
    f.write(content)

# Question 9 -> Check if the file is identical and matches the content
with open("C:\\Users\\Vaibhav Singh\\Downloads\\log.txt") as file:
    content = file.readlines()

with open("C:\\Users\\Vaibhav Singh\\Downloads\\log_copy.txt") as f:
    new_content = f.readlines()

if content == new_content:
    print("Identical content")
else:
    print("Not identical")

# Question 10 -> Write a program to wipe out the content of file using python
with open("C:\\Users\\Vaibhav Singh\\Downloads\\log_copy.txt","w") as f:
    f.write("")

# Question 11 -> Write a program to rename a file to "renamed_by_python.txt"
import os

with open("C:\\Users\\Vaibhav Singh\\Downloads\\old.txt") as f:
    content  = f.read()

with open("C:\\Users\\Vaibhav Singh\\Downloads\\renamed_by_python.txt","w") as file:
    file.write(content)

os.remove("C:\\Users\\Vaibhav Singh\\Downloads\\old.txt")