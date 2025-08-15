# Read lines in a file and add in the dictionary
dict  = []
f = open("C:\\Users\\Vaibhav Singh\\Downloads\\new_file.txt")
data = f.readlines()
for line in data:
    dict.append(line)
print(dict)

f.close()

# Append function
str = "This is appended line"
f = open("C:\\Users\\Vaibhav Singh\\Downloads\\new_file.txt","a")
f.write(str)
f.close()