#Method resolution order----------------------------------------------------------------------------------------------------
class A:
    pass  
class B(A):
    pass
print(help(B))


# class B(A)
#  |  Method resolution order:
#  |      B
#  |      A
#  |      builtins.object
#  |  
#  |  Data descriptors inherited from A:
#  |  
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |  
#  |  __weakref__
#  |      list of weak references to the object (if defined)


""" Python MRO (Method Resolution Order)

When we search for an attribute in a class that is involved in python multiple inheritance, an order is followed.

First, it is searched in the current class. If not found, the search moves to parent classes. This is left-to-right, depth-first.

So, in the above class, the search order will be – Child, Mother, Father, Object.

This order is called linearization of class Child, and the set of rules applied are called MRO (Method Resolution Order).

To get the MRO of a class, you can use either the __mro__ attribute or the mro() method.
>>> Child.__mro__

Output
(<class ‘__main__.Child’>, <class ‘__main__.Mother’>, <class ‘__main__.Father’>, <class ‘object’>)

The __mro__ attribute returns a tuple, but the mro() method returns a python list.
>>> Child.mro()

Output
[<class ‘__main__.Child’>, <class ‘__main__.Mother’>, <class ‘__main__.Father’>, <class ‘object’>]

To take a more complex example that also demonstrates depth-first search, we take 6 classes.
>>> class X:pass
>>> class Y: pass
>>> class Z:pass
>>> class A(X,Y):pass
>>> class B(Y,Z):pass
>>> class M(B,A,Z):pass
>>> M.mro()

Output
[<class ‘__main__.M’>, <class ‘__main__.B’>, <class ‘__main__.A’>, <class ‘__main__.X’>, <class ‘__main__.Y’>, <class ‘__main__.Z’>, <class ‘object’>]



First, the interpreter scans M. Then, it scans B, and then A-B first because of the order of arguments at the time of inheritance.

It scans Z later, after X and Y. The order is- X, then Y, then Z. This is because due to depth-first search, X comes first to A.

Finally, it scans the class object. Hence, the order. """