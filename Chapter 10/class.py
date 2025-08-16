class Employee:
    language = "Python" # This is a class attribute
    salary = 120000



obj1 = Employee
obj1.name = "vaibhav" # This is an object/instance attribute
print(obj1.salary,obj1.language,obj1.name)

# here name is object/instance attribute and salary and language are class attribute as they are directly belong to the class