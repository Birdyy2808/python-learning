# Question 1 -> Write multiplication table of a number using for loop
i= int(input("Enter the number you want table of: "))
for a in range(1,11):
    print(f"{i} * {a} = {i*a}")

# Question 2 -> Program to greet all person whose name starts with "G"
my_list = ["Geeta","Geetanjali","Harry","Vaibhav","Geetu"]

for i in my_list:
    if i.startswith("G"):
        print(f"Greeting {i}")

# Question 3 -> Attemp 1 using while
i=1
num = int(input("Enter the number you want table of: "))
while i<11:
    print(f"{num} X {i} = {num*i}")
    i+=1

# Question 4 -> Check if a numbe ris prime or not
num  = int(input("Enter the number to check: "))

for i in range(2,num):
    if num%i==0:
        print("Not prime")
        break
else:
    print("prime")

# Question 5 -> To find sum of first n natural number
# Using for loop
num = int(input('Enter the number: '))
total=0
for i in range(1,num+1):
    total+=i
print(total)

# Using while loop
num = int(input('Enter the number: '))
i=1
total_new=0
while i<=num:
    total_new+=i
    i+=1
print(total_new)

# Question 6 -> Program to calculate the factorial
num = int(input("Enter the number: "))
fact=1
for i in range(1,num+1):
    fact*=i
print(fact)

# Question 7 -> Print star pattern
#   *
#  ***
# *****
n = int(input("Enter the number: "))
for i in range(1,n+1):
    print(" " * (n-i),end="")
    print("*" * (2*i-1),end="")
    print("")

# Question 8 -> Print another star pattern
# *
# **
# ***
n = int(input("Enter the number: "))

for i in range(1,n+1):
    print("*" * i,end="")
    print("")

# Question 9 -> Print the star pattern
# ***
# * *
# ***
n = int(input("Enter the number: "))

for i in range(1,n+1):
    if i==1 or i==n:
        print("*" * n)
    else:
        print("*",end="")
        print(" " * (n-2),end="")
        print("*",end="")
        print("")

# Question 10 -> Table in reverse order
n = int(input("Enter the number: "))

for i in range(10,0,-1):
    print(f"{n} * {i} = {n*i}")
