# A RAM is volatile in nature, meaning any code you write or any variable you create is lost once program terminates
# In order to persist data we use FILES.
# A FILE is data stored in storage device.
# A python program can talk to the files by reading it and writing contents to it.

# 2 ways we can use open() function
# 1
f = open("file.txt")
data = f.read()
print(data)
f.close()
# 2
with open("file.txt","r") as f:
    data = f.read()
    print(data)