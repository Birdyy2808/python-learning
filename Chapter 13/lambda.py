# Functions created using an expression using "lambda" keyword

# Simple method
def square(n):
    return n*n
print(square(5))

# Lambda method
# This will take x and return x*x
lambda_square = lambda x:x*x
print(lambda_square(5))

# lambda sum
sum = lambda a,b,c:a+b+c
print(sum(1,2,3))