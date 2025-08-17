# Question 1 -> display name
name = input("Enter your name: ")
print("Good Afternoon",name)

# Question 2
# Can do chaining of functions
letter = '''
Dear <|name|> \nYou are selected!\n<|Date|>
'''
print(letter.replace("<|name|>","Vaibhav").replace("<|Date|>","8th August"))

# Question 3 -> Detect double space in string
my_str="My name is  vaibhav"
print(my_str.find("  "))

# Question 4 -> Replace double space in 3 with single space
print(my_str.replace("  ","    "))

# Question 5 -> Write the lines using escape sequence
my_letter="Dear Vaibhav,\n\tThis is python course,\nThanks"
print(my_letter)





#NOTE:  STRINGS ARE IMMUTABLE (CANNOT change them, when we use function, it creates a new string)