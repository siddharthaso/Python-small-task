class GovtSingleton:  
    __instance__ = None  
    
    def __init__(self):  
        # This is a Constructor  
        if GovtSingleton.__instance__ is None:  
            GovtSingleton.__instance__ = self  
        else:  
            pass
            print("breakpoint")
            # raise Exception("We can not creat another class")  
    
    @staticmethod  
    def get_instance():  
        # We define the static method to fetch instance  
        if not GovtSingleton.__instance__:  
            GovtSingleton()  
        return GovtSingleton.__instance__  
    
# Creating an object of above defined class.  
gover = GovtSingleton()  
print(gover)  
    
same_gover = GovtSingleton.get_instance()  
print(same_gover)  
    
another_gover = GovtSingleton.get_instance()  
print(another_gover)  
    
new_gover = GovtSingleton()  
print(new_gover)  

""""
<__main__.GovtSingleton object at 0x0000026FDDAC8160>
<__main__.GovtSingleton object at 0x0000026FDDAC8160>
<__main__.GovtSingleton object at 0x0000026FDDAC8160>
File "C:/Users/DEVANSH SHARMA/PycharmProjects/MyPythonProject/pillow_image.py", line 119, in __init__
    raise Exception("We cannot creat another class")
Exception: We cannot create another class

Explanation -
In the above code, we have instantiated an object and stored it in a variable. We have also defined construction, 
which checks if there is another existing class; otherwise, it will raise an exception. We have then defined the 
static method named get_instance(), which returns the existing instance; if it is not available, then create it and return.

When we execute the script, the one GovInstance object is stored at a single point in the memory. When we create another object, it raises an exception.
"""


""" 
Method - 2: Double Checked Locking Singleton Design Pattern
The synchronization of the threading is no longer in use because the object never is equal to the None. Let's understand the following example.
Example - """

# Double Checked Locking singleton pattern   
import threading   
class Single_Checked(object):   
    
    # resources shared by each and every   
    # instance   
    
    __single_acq_lock = threading.Lock()   
    __singleton_instance = None  
    
    # define the classmethod   
    @classmethod  
    def instance(cls):   
    
        # check for the singleton instance   
        if not cls.__singleton_instance:   
            with cls.__single_acq_lock:   
                if not cls.__singleton_instance:   
                    cls.__singleton_instance = cls()   
    
        # return the singleton instance   
        return cls.__singleton_instance   
    
# main method   
if __name__ == '__main__':   
    
    # create class A   
    class A(Single_Checked):   
        pass  
    
    # create class B  
    class B(Single_Checked):   
        pass  
    
    X1, X2 = A.instance(), A.instance()   
    Y1, Y2 = B.instance(), B.instance()   
    
    assert X1 is not Y1   
    assert X1 is X2   
    assert Y1 is Y2   
    
    print('X1 : ', X1)   
    print('X2 : ', X2)   
    print('Y1 : ', Y1)   
    print('Y2 : ', Y2)  

""" Output -
X1 :  <__main__.A object at 0x7f2920a23df0>
X2 :  <__main__.A object at 0x7f2920a23df0>
Y1 :  <__main__.B object at 0x7f2920a23f70>
Y2 :  <__main__.B object at 0x7f2920a23f70> """



""" 
Classic implementation of Singleton Design Pattern
In the classic implementation of the Singleton Design pattern, we simply use the static method for creating the getInstance 
method which has the ability to return the shared resource. We also make use of so-called Virtual private Constructor to raise 
the exception against it although which is not much required. """

# classic implementation of Singleton Design pattern
class Singleton:
    __shared_instance = 'Siddharth'
 
    @staticmethod
    def getInstance():
 
        """Static Access Method"""
        if Singleton.__shared_instance == 'Siddharth':
            Singleton()
        return Singleton.__shared_instance
 
    def __init__(self):
 
        """virtual private constructor"""
        if Singleton.__shared_instance != 'Siddharth':
            raise Exception ("This class is a singleton class !")
        else:
            Singleton.__shared_instance = self
 
# main method
if __name__ == "__main__":
 
    # create object of Singleton Class
    obj = Singleton()
    print(obj)
  
    # pick the instance of the class
    obj = Singleton.getInstance()
    print(obj)


""" Output:  
 __main__.Singleton object at 0x014FFE90
 __main__.Singleton object at 0x014FFE90 """



"""
Advantages and Disadvantages of Singleton Patterns

    A class created using the singleton pattern violates the Single Responsibility Principle, which means it can solve two problems simultaneously.
    Single Pattern is difficult to implement in the multithreading environment because we need to ensure that the multithreading environment wouldn't create singleton objects several times.
    It makes the unit testing very hard because they follow the global state to an application.

Applicability of Design Pattern
We define the applicability of singleton design pattern as follows. 
    In the project, where we need a firm control over the global variables, we must use the Singleton Method.
    Singleton patterns solves the most occurring problems such as logging, caching, thread pools, and configuration setting and often used in conjunction with the Factory design pattern.

"""