# Question 1 -> Find greatest of 4 number entered by the user
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if num1>num2 and num1>num3 and num1>num4:
    print(num1, " entered by 1st user is greater")
elif num2>num1 and num2>num3 and num2>num4:
    print(num2, " entered by 2nd user is greater")
elif num3>num1 and num3>num2 and num3>num4:
    print(num3, " entered by 3rd user is greater")
else:
    print(num4, " entered by 4th user is greater")

# Question 2 -> Code to check if a student has passed or not. Total 40% to pass and 33% individually to pass.
marks=[]

for i in range(3):
    mark=int(input("Enter your marks: "))
    marks.append(mark)

sum_marks = sum(marks)

if (sum_marks/300)*100>=40 and sum_marks>=99:
    print("Passed")
else:
    print("failed")

# Question 3 -> Write code to detect spam
spam = ["make a lot of money","buy now","subscribe me","click this"]

user_comment = input("Enter the comment: ")

if user_comment in spam:
    print("spam detected: ", user_comment)
else:
    print("free of spam")

# Question 4 -> Check username has less than 10 char
username = input("Enter your username: ")

if len(username)<10:
    print("Username accepted")
else:
    print("Username not accepted")

# Question 5 -> Find whether a name is present in list or not
list = ["Vaibhav","Geeta","Balwant"]
name  = input("Enter a name: ")

if name in list:
    print("Name is Present")
else:
    print("Not present")

# Question 6 -> Grade students
marks = int(input("Enter your marks: "))

if marks>90 and marks<=100:
    print("Ex")
elif marks>80 and marks<=90:
    print("A")
elif marks>70 and marks<=80:
    print("B")
else:
    print("F")

# Question 7 -> Check whether a post talks about Vaibhav
post  = "My name is Vaibhav \nVaibhav is a good boy"
subject = input("Enter keyword: ")

if subject.lower() in post.lower():
    print("This post is about Vaibhav")
else:
    print("Not about Vaibhav")
