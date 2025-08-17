# We can pass default args in function parameters so that if we don't pass the argument in the function call, the default one is taken
# else the function argument is taken
def hello(name, ending="Thank you"):
    print(f"Hello {name}")
    print(ending)

hello("Vaibhav","Thanks")
hello("Geeta")