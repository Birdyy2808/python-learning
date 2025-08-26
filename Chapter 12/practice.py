# Question 1 -> Write a program to open three files. If any of these files, not present, promt "File missing"

# try:
#      with open("enumerate.py","r") as file1, open("name_main.py") as file2, open("global.py") as file3:
#         print(file1.read())
#         print(file2.read())
#         print(file3.read())

# except FileNotFoundError:
#     print("file not found")

# except Exception as e:
#     print(e)

# print("Thank you") # To show program did not crash

# Question 2 -> Write a program to print the 3rd, 5th and 7th eleemnt from the list using enumerate function
# my_list = [1,2,3,4,5,6,7,8,9]

# for index,l in enumerate(my_list):
#     if index==2 or index==4 or index==6:
#         print(f"The element at index {index} is {l}")

# Question 3 -> Write a list comprehension to print a list which contains the multiplication table of a user entered number
# user = int(input("Enter the user input num: "))

# my_list = [user*i for i in range(1,11)]

# print(my_list)

# Question 4 -> Writ a program to display a/b where a and b are integers. If b = 0, display infinite by handling the "Zerodivisionerror"
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))

# try:
#     print(int(a/b))
# except ZeroDivisionError:
#     print("Infinite")

# Question 5 -> Store the multiplication table in prob 3 in a file names tables.txt
user = int(input("Enter the user input num: "))

my_list = [user*i for i in range(1,11)]

with open("C:\\Users\\Vaibhav Singh\\Downloads\\tables.txt","a") as file:
    file.write(str(my_list) + "\n")