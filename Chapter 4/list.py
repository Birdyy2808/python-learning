# List is used to store different types of data -> [string,int,float,string]
my_list=[0,1,"vaibhav",0.05,100]

print(my_list[4])

# Append a value
my_list.append("hello")
print(my_list)

l1=[1,50,3,4,100,5,101]

l1.sort()
print(l1)

l1.reverse()
print(l1)

# Insert to add item at a another index
l1.insert(3,10000)
print(l1)

# pop to delete a index and return a value
# Print the value that will be deleted
print(l1.pop(3))
# print
print(l1)

# remove
l1.remove(4)
print(l1)

# # Can modify a list but not strings, hence List are mutable
my_list[0]="1 lakh"
print(my_list)

for l in l1:
    print(l)
