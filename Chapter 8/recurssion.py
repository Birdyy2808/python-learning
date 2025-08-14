# A recurssion is a function that calls itself

def fact(n):
    if n==1 or n==0:
        return 1  # base condition needs to be defined so loop stops
    return n * fact(n-1)

input = int(input("Enter the number: "))
res= fact(input)
print(f"The factorial of {input} is {res}")

