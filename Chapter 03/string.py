# String is a sequence of character enclosed in ""
# String is immutable -> Cannot be changed
name="Vaibhav"

print(len(name)) #To get the length

for char in name:
    print(char)

print(name[0:4]) # For slicing a string -> Exclude 4th index

# Skip string
a="bahhshajkaalsllsa"
print(a[1:8:3])
