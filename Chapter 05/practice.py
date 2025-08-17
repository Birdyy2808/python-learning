# Question 1 -> Dict of Hindi and English words
dict = {
    "kutta":"dog",
    "billi":"cat",
    "namaste":"hello"
}

word = input("Enter the word you want to search the translation of: ")
print(dict.get(word))

# Question 2 -> Input 4 numbers from users and display all unique number once
my_set = set()

num1=input("Enter the first number: ")
my_set.add(int(num1))

num2=input("Enter the first number: ")
my_set.add(int(num2))

num3=input("Enter the first number: ")
my_set.add(int(num3))

num4=input("Enter the first number: ")
my_set.add(int(num4))

print(my_set)

# Question 3 -> Can we have 18 (int) and '18' (str) in a set
my_set = {18,"18"}
print(my_set)  #Yes we can add str and int of same number as types are different

# Question 4 -> Determine size
s = set()
s.add(20)
s.add(20.0)
s.add("20")

print(s,len(s))

# Question 5 -> Determine type
d = {}
print(type(d))

# Question 6 -> Create dict of frnd names and fav. lang as value
dict = {}

for i in range(4):
    name = input(f"Enter your name {i+1}: ")
    lang = input(f"Enter your lang {i+1}: ")

    dict.update({name:lang})
print(dict)

# Question 7 -? When the names are same, what happens in Question 6?
# Answer -> The last key with the last value will be updated and size will be 3

# Question 8 -> What if the values are same, what happens in Question 6
# Answer -> No issues, size will be 4 and the values will be different for different keys

# Question 9 -> Can you change the values inside a list which is contained in set
s = {8,7,17,"Harry",[1,2]}
# Cannot add list inside set
print(s)



