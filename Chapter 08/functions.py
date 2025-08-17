# A function is a group of statements that perform an operation and can be called again without repeating the code again
# Function definition
def avg():
    a = int(input("Enter number 1: "))
    b =int(input("Enter number 2: "))
    c = int(input("Enter number 3: "))
    avg = (a+b+c)/3
    return avg

# Function call
avg = avg()
print(avg)

# Quiz -> Create a function to say hello
def goodday(name):
    print(f"Hello {name}")

name = input("Enter your name: ")
goodday(name)
