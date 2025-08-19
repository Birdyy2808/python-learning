# An example of multiple inheritence
# we can give 2 parents name to the inherited child like
# Eg: inherited_class(Parent1,Parent2)

class Employee:
    company  = "ITC Infotech"
    def show(self):
        print(f"The Company name is {self.company}")

class another_parent:

    language = "Python"
    def fav_lang(self):
        print(f"The language used is {self.language}")

class Programmer(Employee,another_parent):

    def final_show(self):
        print(f"The company name is {self.company} and the language name is {self.language}")

a = Programmer()
print(a.show(),a.fav_lang(),a.final_show())