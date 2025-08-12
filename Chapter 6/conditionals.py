# If, else, elif
age  = int(input("Enter you age: "))

# Used relational operator(==,>=,<=) and Logical opertor(and,or,not)
if age<0:
    print("Enter a valid age")
elif age>=18 and age<=25:
    print("You are between 18 and 25")
else:
    print("You are above 25")