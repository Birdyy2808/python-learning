l = [10,20,30,60]

index=0
for item in l:
    print(f"The item at {index} is {item}")
    index+=1

# This process can be made easy by enumerate
for index,item in enumerate(l):
    print(f"The item at {index} is {item}")