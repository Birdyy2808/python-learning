from functools import reduce

# Map example: Map is used if we want to run lambda function on each item of a list
l = [1,4,6,7,8]
squared = lambda x:x*x

result = map(squared,l)
print(list(result))

# Filter example: Used to filter
def even(n):
    if n%2==0:
        return True
    return False
only_even = filter(even,l)
print(list(only_even))

# Reduce example: Use to reduce the function, in my case sum, where it runs in pais
sum = lambda a,b:a+b
mul = lambda a,b:a*b
print(reduce(sum,l), reduce(mul,l))

