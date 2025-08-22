# Walrus Operator
#  := allows to assign values to variable as part of an expression
#  Offically called assignement operator

if ( n := len([1,2,3,4,5,6])) > 3:
    print(f"{n} is too long")
else:
    print("Length is fine")