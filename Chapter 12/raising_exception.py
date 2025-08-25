# raising error will crash the program, it is necessary for developer to stop the dev and tell him to fix the error

# This will keep running the program and throw exception
try:
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    print(f"The result is {a/b}")
except ZeroDivisionError:
    print("Divided by 0")
except Exception as e:
    print(e)

# This will raise the exception and stop the program if not in try catch block
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

if b==0:
    raise ZeroDivisionError("Please enter a number greater than 0")
else:
    print(f"The result is {a/b}")