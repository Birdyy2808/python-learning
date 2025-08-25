# Sometimes, we want to run a code only whehn "Try" was successful.
# So for that, we use try-else
# If try is successful, "else" will be executed or else except message will be shown
try:
    a = int(input("Enter a number: "))
    print(a)
except Exception as e:
    print(e)
else:
    print("Thank you")