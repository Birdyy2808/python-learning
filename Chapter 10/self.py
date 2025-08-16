class Employee:
    language = "Python"
    salary = 1200000

    def get_salary(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    # If don't want to add "self" the use @staticmethod
    @staticmethod
    def greet():
        print("Good morning")

vaib = Employee()

vaib.greet()
# Converted to Employee.greet(vaibhav)
vaib.get_salary()
# converted to Employee.get_salary(vaibhav)


# Always need to give self in the method, even if use it or not use it. Becuase when we call the method it takes like
# Empoyee.get_salary(vaibhav)
# And in get_salary if we don't pass anything, we get error that it expects one value