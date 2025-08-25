# exception handling

a =  int(input("Enter a number: "))
print(a)

# The above throws error
# A program should never throw error, it should be handled to throw exception

try:
    a = int(input("Enter a number: "))
    print(a)
except ValueError:
    print("Please enter a valid number")
except Exception as e:
    print(e)