# If I run this code using "pyhon module.py". the __name__==__main__
# if I run from name_main.py, where I have imported this module, it will show __name__=module
def add(a:int,b:int) -> int:
    return a+b

if __name__=="__main__":
    # If this code is directly executed by running the file it is present in
    print(add(5,10))
    print(__name__)