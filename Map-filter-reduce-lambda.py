""" A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.

Every anonymous function you define in Python will have 3 essential parts:
    The lambda keyword.
    The parameters (or bound variables), and
    The function body.
 """


#What a lambda returns
from numpy import square

string="some kind of a useless lambda"
print(lambda string : print(string))

# Output:<function <lambda> at 0x7efeac226f70>
# This is because the lambda itself returns a function object. In this example, the lambda is not being called by the print function but simply returning the function object and the memory location where it is stored.


#What a lambda returns #2
x="some kind of a useless lambda"
(lambda x : print(x))(x)            #some kind of a useless lambda
print((lambda x: x + x)(2))         #4

""" we are defining a lambda and calling it immediately by passing the string as an argument. This is something called an IIFE
An #####IIFE####### (Immediately Invoked Function Expression) is a JavaScript function that runs as soon as it is defined. The name IIFE is promoted by Ben Alman in his blog
You can use IIFEs to prevent global variables' definition issues, alias variables, protect private data, and avoid conflicts of using many libraries that export the same object name """


#A REGULAR FUNCTION
def sidd( funct, *args ):
    funct( *args )
def printer_one( arg ):
    return print (arg)
def printer_two( arg ):
    print(arg)

#CALL A REGULAR FUNCTION 
sidd( printer_one, 'printer 1 REGULAR CALL' )
sidd( printer_two, 'printer 2 REGULAR CALL \n' )

#CALL A REGULAR FUNCTION THRU A LAMBDA
sidd(lambda: printer_one('printer 1 LAMBDA CALL'))
sidd(lambda: printer_two('printer 2 LAMBDA CALL'))

""" printer 1 REGULAR CALL
printer 2 REGULAR CALL 

printer 1 LAMBDA CALL
printer 2 LAMBDA CALL """



def addition(x,y):
    return x+y
print(addition(4,5))

#Usimg lambda--
add_fun = lambda x,y : x+y



print(add_fun(4,5))

def factorial(n):
    if n==1: return 1
    else: return n* factorial(n-1)
print(factorial(5))

#Usimg lambda-
factorial = lambda n: 1 if n==1 else n * factorial(n-1)
print(factorial(5))

fact = lambda x: x == 0 and 1 or x * fact(x-1)
fact = lambda x: x == 0 or x * fact(x-1)
fact = lambda x: x==1 or x * fact(x-1)
print(fact(5))

# fact = lambda x: 1 or x * fact(x-1)     #fact(5)=>1
# fact = lambda x: x==-1 or x * fact(x-1) #fact(5)=>0



# Something Out of the blue--------
print("----------------------------------------------------------------------------------")
x= lambda x:x==1 and 2
print(x(-1))           #False
print(x(0))            #False
print(x(1))            #2
print(x(2))            #False
print(x('fff'))        #False

x= lambda x:x==1 and 2 or x+x       #if "and x+x" then,,,False,False,2,False
print(x(-1))           #-2
print(x(0))            #0
print(x(1))            #2
print(x(2))            #4


# The power of lambda is better shown when you use them as an anonymous function inside another function.
print("----------------------------------------------------------------------------------")
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))
mytripler = myfunc(3)
print(mytripler(11))

#Use lambda functions when an anonymous function is required for a short period of time.




####################################-------------Map----------#############################
""" This function is used to map a particular function onto the sequence of elements. After applying, this returns a new set of values.
Syntax: map(function, sequence) 
the map function is used to apply a particular operation to every element in a sequence. Like filter(), it also takes 2 parameters:
    A function that defines the op to perform on the elements
    One or more sequences
"""
print("-------------------------------------------MAP---------------------------------------\n")

without_gst_cost = [100, 200, 300, 400]

with_gst_cost = map(lambda x: x+10, without_gst_cost)
print(with_gst_cost)                                        #<map object at 0x7fe379043220>
x=list(with_gst_cost)
print("Without GST items costs: ",without_gst_cost)
print("With GST items costs: ",x)

#--------------------Two list
a=[1,2,3]
b=[4,5,6]
x= map(lambda c,d:c+d , a, b)
print(list(x))                          #[5, 7, 9]


#map different way
n=[4,3,2,1]
print(list(map(lambda x:x**2, n)))

print(list(map(square,n)))
print([x**2 for x in  n])



####################################-------------Filter----------#############################
""" This function is used to filter values from a sequence of values. The syntax is:
Syntax: filter(function, sequence) 
The filter function is used to select some particular elements from a sequence of elements. The sequence can be any iterator like lists, sets, tuples, etc.
The elements which will be selected is based on some pre-defined constraint. It takes 2 parameters:

    A function that defines the filtering constraint
    A sequence (any iterator like lists, tuples, etc.)
"""
print("--------------------------------------Filter--------------------------------------------\n")

# The filter function will filter the elements in the sequence based on the condition in the function. Let’s understand it through the example.

items_cost = [999, 888, 1100, 1200, 1300, 777]
gt_thousand = filter(lambda x : x>1000, items_cost)
x=list(gt_thousand)
print("Eligible for discount: ",x)

#using List Comprehension
print([x for x in items_cost if x>1000])





####################################--------------Reduce---------#############################
""" This function reduces the sequence of elements into a single element by applying a specific condition or logic. To use the reduce 
function we need to import the functools module.
Syntax: reduce(function, sequence) 
The reduce function, like map(), is used to apply an operation to every element in a sequence. However, it differs from the map in its working. 
These are the steps followed by the reduce() function to compute an output:
Step 1) Perform the defined operation on the first 2 elements of the sequence.
Step 2) Save this result
Step 3) Perform the operation with the saved result and the next element in the sequence.
Step 4) Repeat until no more elements are left.

It also takes two parameters:

    A function that defines the operation to be performed
    A sequence (any iterator like lists, tuples, etc.)
"""
print("------------------------------------Reduce---------------------------------------------\n")

""""Applies same operation to items of a sequence
Uses result of operation as 1St param of next operation
Return an item, not a list
"""


from functools import reduce

n=[4,3,2,1]
print(reduce(lambda x,y:x*y, n))        #24 =4*3*2*1


each_items_costs = [111, 222, 333, 444]
total_cost = reduce(lambda x, y: x+y, each_items_costs)
print(total_cost)




""" 
When should you not use Lambda?

You should never write complicated lambda functions in a production environment. It will be very difficult for coders who 
maintain your code to decrypt it. If you find yourself making complex one-liner expressions, it would be a much superior 
practice to define a proper function. As a best practice, you need to remember that simple code is always better than complex code.

Lambda functions can only have one expression in their body.
Regular functions can have multiple expressions and statements in their body.
Lambdas do not have a name associated with them. That’s why they are also known as anonymous functions.
Regular functions must have a name and signature.
Lambdas do not contain a return statement because the body is automatically returned.
Functions which need to return value should include a return statement. """