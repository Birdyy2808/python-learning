# "Break" will stop the code execution once the condition is met
for i in range(1,100):
    if i==50:
        break
    print(i)

# "Continue" will skip the condition and continue the code execution
for i in range(1,100):
    if i==50:
        continue
    print(i)

# "Pass" inside a loop means "Do nothing"
for i in range(5):
    pass # Not adding pass will throw error