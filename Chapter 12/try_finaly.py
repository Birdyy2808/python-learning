# Unlike try-else, which will exceute "else" only when "try" is successful.
# "Finally" will be executed irresepective of "try" or "except", for both case it will execute.

# "Finally" is important in "Functions", if we return a value, then still "finally" will always run
def main():
    try:
        a = int(input("Please enter a number: "))
        return a
    
    except Exception as e:
        return e
    
    finally:
        print(f"Thank you")

print(main())
