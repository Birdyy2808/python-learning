# Question 1-> Create class 2-D vector and use it to create anther class representing 3-D vector
class Two_D_Vector:
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")


class Three_D_Vector(Two_D_Vector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}")

two = Two_D_Vector(1,2)
two.show()
three = Three_D_Vector(1,2,3)
three.show()

# Question 2 -> Create a class "Pets" from class "Animals" and further create a class "Dog"
# from "Pets". Add a method "Bark" to class "Dog"
class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("The dog barks")

d = Dog()
d.bark()

# Question 3 -> Create a class "Employee" and add salary and increment properties to it
class Employee:
    salary = 234
    increment = 20
    
    @property
    def salary_after_increment(self):
        return (self.salary + self.salary * (self.increment/100)) 
        
    @salary_after_increment.setter
    def salary_after_increment(self,salary):
        self.increment =  ((salary/self.salary)-1)*100



e = Employee()
e.salary_after_increment = 280.888
print(e.increment)

# Question 4 -> Write a class "Complex" to represent complex numbers, along with overloaded operators "+" 
# which adds them
class Complex:
    def __init__(self,i,j):
        self.i=i
        self.j=j
        
    def __add__(self,c2):
        return Complex(self.i + c2.i,self.j + c2.j)
    
    def __str__(self):
        return f"{self.i} + {self.j}i"
    
c1 = Complex(1,2)
c2 = Complex(3,4)
print(c1+c2)




