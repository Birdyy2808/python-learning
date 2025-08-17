# Tuple is immutabe
my_tuple=(1,2,4,6,10)
print(type(my_tuple))

# make a tuple with only 1 element then add ",", else it will consder it as a int
my_new_tuple=(1,)
print(type(my_new_tuple))

# functions on tuples
my_tuple=(1,2,4,6,4,4,4,10)

# No functions in tuple that modify the tuple, hence immutable

# But there are few methods that help in counting or returning the index

# Count
no_of_occurance=my_tuple.count(4)
print(no_of_occurance)

# Return index of first occurance
print(my_tuple.index(4))
