# class is an example of encapsulation -> Keeping everything inside
# This is also abstraction where we are not showing the internal methods and implementations

class parent:
    num=1
    @classmethod
    def demo(cls):
        print(f"This method will call class attribute {cls.num}")

    # This is an example of Getters and Setters also
    @property
    def full_name(self):
        return f"{self.fname} {self.lname}"
    
    @full_name.setter
    def full_name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


p = parent()
p.num=10
# p.demo()

p.full_name = "vaibhav Singh"
print(p.fname,p.lname)
