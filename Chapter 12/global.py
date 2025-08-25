a = 90 # Global variable

def func():
    global a  #This chnage the global variable from 90 to a
    a=5 # Local Variable
    print(a)
    
func()
print(a)
