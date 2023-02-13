#decoratro using *args and **kwargs-------------------------------
def decor(func):
    def wrapper(*args, **kwargs):
        print("decorator before function called ")
        func(*args, **kwargs)
    return wrapper
@decor                 #greeting = decor(greeting)
def greeting(text):
    print(text)
greeting("hello")


#function generator ---------------------------------
def add(a):
    def wrapper(b):
        print(a+b)
    return wrapper
add_5 = add(5)
add_5(10)
print(add)
print(add_5)

#decorator using @---------------------------------
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice
@do_twice
def say_whee():
    print("Whee!")

say_whee()


# # -----------------decoretor
def my_decorator(func_name):
    def wrapper():
        print("Start")
        func_name()
        print("End")
    return wrapper

def greeting():
    print("hello")

greeting = my_decorator(greeting)
greeting()
print(greeting)
#wrapper() has a reference to the original greeting() as func, and calls that function between the two calls to print().
# decorators wrap a function, modifying its behavior.

""" By definition, a decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.
decorators wrap a function, modifying its behavior.
---------------
@gfg_decorator
def hello_decorator():
    print("Gfg")

'''Above code is equivalent to -

def hello_decorator():
    print("Gfg")
    
hello_decorator = gfg_decorator(hello_decorator)'''
In the above code, gfg_decorator is a callable function, will add some code on the top of some another callable function, hello_decorator function and return the wrapper function.
Decorator can modify the behaviour:   """