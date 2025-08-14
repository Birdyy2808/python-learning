# Question 1 -> Function to find greatest of 3 numbers
# Function definition
def greatest():
    num1 = int(input("Enter first num: "))
    num2 = int(input("Enter second num: "))
    num3 = int(input("Enter third num: "))

    if num1>num2 and num1>num3:
        print(f"num1 {num1} is greatest")
    elif num2>num1 and num2>num3:
        print(f"num2 {num2} is greatest")
    else:
         print(f"num3 {num3} is greatest")
# Function call
greatest()

# Question 2 -> function to convert celsius to Fahrenheit
# Function definition with function parameter
def convert_temp(temp):
    converted_temp= (temp*(9/5))+32
    return converted_temp

temp = int(input("Enter the temperature: "))
# Function call with arguement
print(f"The temperature in Fahrenheit is {convert_temp(temp)}F")

# Question 3 -> How to you prevent print() from printing new line
# Answer -> We use print("Hello",end="")

# Question 4 -> Recurssive function to calculate sum of first n number
def recursive_sum(n):
    if n == 1:
        return 1
    return n + recursive_sum(n-1)

num = int(input("Enter the number: "))
print(f"The sum of {num} natural number is {recursive_sum(num)}")

# Question 5 -> Function to print the pattern
# ***
# **
# *
def star_pattern(n):
    for i in range(n,0,-1):
        print("*" * i, end="")
        print("")

num = int(input("Enter the num: "))
star_pattern(num)

# Using recursion
def star(n):
    if n == 0:
        return
    print("*" * n)
    star(n-1)

num = int(input("Enter the num: "))
star(num)

# Question 6 -> Python function to convert inches to cm
def convert_cm(inch):
    inch_to_cm =  inch*2.54
    return inch_to_cm

inch = int(input("Enter the length in centimeter: "))
print(f"The inch {inch} in cenimeter is {convert_cm(inch)} ")

# Question 7 -> Remove a word from the list and strip it at the same time
def rem(my_list,word):
    l = []
    for item in my_list:
        if item!=word:
            l.append(item.strip(word))
    return l

my_list=["vaibhav","geeta","mummy","av"]
print(rem(my_list,"av"))

# Question 8 -> Function to print multiplication table
def table(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")

n = int(input("Enter the number: "))
table(n)