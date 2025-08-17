# Question 1 -> Create class "Programmer" for storing information of few programmers working at microsoft
class Programmer:
    company  = "Microsot"

    def __init__(self,name,emp_id,salary):
        self.name=name
        self.emp_id=emp_id
        self.salary=salary

p = Programmer("Vaibhav","25056",1300000)
print(p.name,p.salary,p.company,p.emp_id)
v= Programmer("Geeta","25057",4700000)
print(v.name,v.company,v.emp_id,v.salary)

# Question 2 -> Create a class "Calculator" capable of finsing square, cube, square root of a number.
class Calculator:
    def __init__(self,num):
        self.num = num
    def sq(self):
        print(f"The square is {self.num*self.num}")
    def cube(self):
        print(f"The cube is {self.num*self.num*self.num}")
    def sq_root(self):
        print(f"The square root is {self.num**0.5}")
    
calc=Calculator(4)
calc.sq()
calc.cube()
calc.sq_root()

# Question 3 -> Create class attribute a; create an object from it and set a directly using object.a=0. Does this change the class attribute?
class Attribute:
    name = "vaibhav"

attr = Attribute()
# # Prints "Vaibhav" since instance attribute is not present, so it prints Class attribute
print(attr.name)
# # Prints Geet, because now Instance attribute is set, so it is setting that
attr.name = "Geeta"
print(attr.name)
# # But, class attribute is not changed, it is same only, hence prints "Vaibhav"
print(Attribute.name)
# # Answer -> No, class Attribute is not changes

# Question 4 -> Add a static methid in problem 2, to gree user with "hello"
class Calculator:
    def __init__(self,num):
        self.num = num
    @staticmethod
    def hello():
        print("hello")
    def sq(self):
        print(f"The square is {self.num*self.num}")
    def cube(self):
        print(f"The cube is {self.num*self.num*self.num}")
    def sq_root(self):
        print(f"The square root is {self.num**0.5}")
    
calc=Calculator(4)
calc.hello()
calc.sq()
calc.cube()
calc.sq_root()

# Question 5 ->Write a class Train which has methods to book a ticket, get status and get fare info. of running train under
# Indian railway
from random import randint
class Train:
    def __init__(self,train_no):
        self.train_no=train_no
    def book(self,fro,to):
        print(f"Ticket is booked in train number {self.train_no} from {fro} to {to}")
    def get_status(self):
        print(f"{self.train_no} is running on time")
    def get_fare(self, fro, to):
        print(f"Ticket fare in train number {self.train_no} from {fro} to {to} is {randint(500,1000)}")

train = Train(25056)
train.book("kanpur","lucknow")
train.get_status()
train.get_fare("kanpur","lucknow")

# Question 6 -> Can you change self parameter inside a class to soemthing else?
class demo:
    def __init__(slf,name):
        slf.name=name
    
    def hello(slf):
        print(f"Hello there {slf.name}")

d = demo("Vaibhav")
d.hello()
# Answer -> The code will work if we change self to slf