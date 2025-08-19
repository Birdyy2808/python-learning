# @classmethod decorator is used to call the class attribute and not the instance/object attribute
# "self" means the object on which the method is running
# "cls" means the object of class on which the method is running
class parent:
    name="Vaibhav"
    @classmethod
    def demo(cls):
        print(f"This method will call class attribute {cls.name}")

p = parent()
p.name="Geeta"
p.demo()