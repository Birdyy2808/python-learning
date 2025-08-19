class Number:
    
    def __init__(self,n):
        self.n =n

    def __add__(self,num):
        return self.n + num.n

num = Number(1)
num2 = Number(2)

print(num+num2)