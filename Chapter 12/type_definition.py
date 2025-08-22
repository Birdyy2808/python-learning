#  This defines the type we want to use for a variable
a : int = 5
# Here we are telling "a" is an integer and we can get int methods

name : str = "Vaibhav"
# So we defined the string here

# In practical scenario, in functions we can define, what type the function will take and what it will return

def add(num1:int,num2:int) -> int:
    return num1 + num2

a = add(10,20)
print(a)
