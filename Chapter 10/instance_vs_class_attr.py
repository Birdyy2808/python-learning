class Employee:
    language = "Python" # This is a class attribute
    salary = 120000



obj1 = Employee
obj1.language = "Django" # This is an object/instance attribute
print(obj1.salary,obj1.language)

# Instance attribute take precedence over class attribute