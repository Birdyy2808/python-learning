my_list = [1,4,5,6,11,19]

squred_list=[]

for item in my_list:
    squred_list.append(item*item)

print(squred_list)

# The above can be made easy using list comprehensions
squred_list_new = [i*i for i in my_list]
print(squred_list_new)