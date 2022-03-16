# Abstract Base Class using abc module of python----------------------------------------------------------------
# import abc
# class shape(metaclass=abc.ABCMeta):
#    @abc.abstractmethod
# A helper class that has ABCMeta as its metaclass.

from abc import ABC, abstractmethod
# import abc

class shape(ABC):
    PI = 3.14

    @abstractmethod
    def perimeter(self): pass

    @abstractmethod
    def area(self): pass

    def print_all(self):
        print( "Given {}'s perimeter is : {} and area is {}".format(self.__class__.__name__, self.perimeter(), self.area()))

# Instead of subclassing from abstract base class, it can be registered as abstract base by register class decorator.
# @shape.register
# You may also provide class methods and static methods in abstract base class by decorators 
# @abstractclassmethod and @abstractstatic method decorators respectively. @abstractproperty

class squre(shape):

    def __init__(self, side):
        self.side = side
    
    def perimeter(self):
        return self.side * 4
    
    def area(self):
        return self.side * self.side
#if this code put at the end then name 'rect' is not defined
class rect(shape):
    
    def __init__(self, h, w):
        self.h = h
        self.w = w 
    
    def perimeter(self):
        return self.h * 2 + self.w * 2
    
    def area(self):
        return self.h *self.w

if __name__=='__main__':
    
    # pass
    # sh = shape()                #Can't instantiate abstract class shape with abstract methods area, perimeter
    # print(sh)
    o1 = squre(5)
    print(o1.perimeter())
    print(o1.area())
    o1.print_all()
    o2 = rect(5,9)
    o2.print_all()
    print(o1.PI)

# Note
# Unlike Java abstract methods, these abstract methods may have an implementation. 
# This implementation can be called via the super() mechanism from the class that overrides it. 
# This could be useful as an end-point for a super-call in a framework that uses cooperative multiple-inheritance. 