from second import second_function

def first_function():
    print("first function called")

first_function()
second_function()

# >>> hasattr(3,'int')
# False
# >>> hasattr([],'len')
# False
# >>> hasattr({"D":3},'keys')
# True
# >>> hasattr({"D":3},'values')
# True
# >>> hasattr({"D":3},'len')
# False
# >>> 
# >>> 
# >>> isinstance({"D":3},dict)
# True
# >>> isinstance([],list)
# True
# >>> isinstance(3,int)
# True
