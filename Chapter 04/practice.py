# Question 1 -> Store seven fruit in a list entered by user
fruits = input("Enter fruits seperated by spaces: ").split()

for fruit in fruits:
    print(fruit)

# Question 2 -> Accept marks of 6 students and display them in sorted
marks=[]
m1=int(input("enter m1: "))
marks.append(m1)

m2=int(input("enter m2: "))
marks.append(m2)

m3=int(input("enter m3: "))
marks.append(m3)

marks.sort()
print(marks)

# Question 3 -> Show tuple cannot be changed
a=("Vaibhav",'Singh')
a[1]="hello"
print(a)

# Question 4 -> Add numbers in a list
list=[10,20,30,50]
sum=0
for i in list:
    sum+=i
print(sum)

# Question 5 -> Code to find number of 0 in tuple
tuple=(1,4,5,0,1,0,0,0)
print(tuple.count(0))

# Question 2 -> Improvement
marks=[]
for i in range(6):
    mark = int(input(f"Enter the marks {i+1}: "))
    marks.append(mark)

marks.sort()
print(marks)