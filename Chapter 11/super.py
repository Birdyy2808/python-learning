# Example of super
# Used to call the constructor of parent

class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a=1

class Manager(Employee):
    def __init__(self):
        print("Constructor of Manager")
    b=2

class Programmer(Manager):
    def __init__(self):
        super().__init__()
        print("Constructor of Programmer")
    c=3

# e = Employee()
# m = Manager()
p = Programmer()
