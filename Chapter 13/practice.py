# Question 1 -> Write a program to input name, marks and ph number of a student and format it using format function
name = input("Enter your name: ")
marks = int(input("Enter your marks: "))
number = int(input("Enter your phone number: "))

print("The name of the student is {}, his marks are {}, and phone number is {}".format(name,marks,number))

# Question 2 -> A list contains table of 7, write a program to convert it into string of same numbers
table = [str(7*i) for i in range(1,11)]
print("\n".join(table))

# Question 3 -> Program to filter a list of number which are divisble by 5
my_list = [6,10,5,565,554,3001,5000]

result  = lambda x:x%5==0

final_result = filter(result,my_list)
print(list(final_result))

# Question 4 -> Write a program to find the maximum of the number in a list using reduce function
from functools import reduce

my_list = [6,10,5,565,5000,554,3001]

greater = lambda a,b:a if a>b else b

final_result  = reduce(greater,my_list)
print(final_result)

# Question 5 -> Explore "Flask" module and create a web server using Flask and python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()


