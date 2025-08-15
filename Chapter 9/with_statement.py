# With is used so that we can ignore the manual way of saying f.close()
# Reading a file
with open("C:\\Users\\Vaibhav Singh\\Downloads\\new_file.txt") as file:
    print(file.read())

# Writing to a new file
str = "Hello Vaibhav SIngh"
with open("C:\\Users\\Vaibhav Singh\\Downloads\\new_write_file.txt","w") as file:
    file.write(str)

