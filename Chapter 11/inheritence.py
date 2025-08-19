class Employee:
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and salary is {self.salary} show method")

# class Programmer:
#     company = "ITC Infotech"

#     def show(self):
#         print(f"The name is {self.name} and salary is {self.salary} show method")

#     def show_language(self):
#         print(f"The name is {self.name} and he is good with {self.language}")
# Instead of repeating the same methods again and again in classes,
# use INHERITENCE

# Inheritence is a way of creating a new class from an existing class
# EMployee is Base class
# inherited_class is the inherited class

# Below is the example of Single Level Inheritence

class inherited_class(Employee):
    pass

a =  Employee()
b = inherited_class()
a.name = "Vaibhav"
a.salary = 13333333333
print(a.show())
b.name = "Geeta"
b.salary = 15555555555
print(b.show())