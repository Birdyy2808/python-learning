class Employee:
    language = "Python"
    salary = 1100000


    def __init__(self,name,salary,language): #Dunder method which is called automatically and they start with __
        self.name = name
        self.salary = salary
        self.language = language
        print(f"I am creating a constructor and my fav lang is {self.language} and salary is {self.salary}")


vaib = Employee("Geeta",13000000,"Django")

