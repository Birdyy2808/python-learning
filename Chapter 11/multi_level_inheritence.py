# Example of multi level inheritence

class Employee:
    a=1

class Manager(Employee):
    b=2

class Programmer(Manager):
    c=3

o = Programmer()
print(o.a,o.b,o.c)