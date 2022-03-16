#class, attr, and object---------------------------------------------------------------------------------------------------

#class method as constructor
from datetime import datetime
class Emp:
    def __init__(self,first, last) -> None:         
        self.fname= first
        self.lname= last
    def full_name(self):        
        print("Name : "+self.fname +" "+ self.lname)

    @classmethod
    def date_cmethod_constructor(cls,a,b):
        print(datetime.now())
        return Emp(a,b)

emp1= Emp("sidd", "patel")
emp2= Emp.date_cmethod_constructor("krishna", "god")
print(emp1)
print(emp2)



#class and instance method and static method
import datetime
class Emp:
    Emp_count=0
    #raise_amt= 1.04
    def __init__(self,first, last) -> None:         #means return None
        self.fname= first
        self.lname= last
        Emp.Emp_count +=1  # if self. then Only count that instance's value to 1
        # Emp_count +=1     local variable 'Emp_count' referenced before assignment

    def full_name(self):        
        print("Name : "+self.fname +" "+ self.lname)

    @classmethod
    def class_method(cls,text,num):
        print(cls)
        print("This runs in class method: "+text)
        cls.Emp_count=num

    @staticmethod
    def isWorkday(my_day):         #don't take any cls or self and don't use any property of it
        # return my_day.isoweekday()
        if my_day.isoweekday() ==5 or my_day.isoweekday() ==6:  
            return False
        else: 
            return True

emp1= Emp("sidd", "patel")
emp2= Emp("krishna", "god")
print(Emp.Emp_count)    #2
print(emp1.Emp_count)   #2
print(emp1.__dict__)    #{'fname': 'sidd', 'lname': 'patel'}

emp1.Emp_count=0
print(Emp.Emp_count)    #2
print(emp1.Emp_count)   #0
print(emp1.__dict__)    #{'fname': 'sidd', 'lname': 'patel', 'Emp_count': 0}

#if emp1.Emp_count=0 is not happens then ./below
Emp.class_method("Hello class",3) #<class '__main__.Emp'>     This runs in class method: Hello class
print(Emp.Emp_count)    #3
print(emp1.Emp_count)   #3
emp1.class_method("run from instance object",4)
print(Emp.Emp_count)    #4
print(emp1.Emp_count)   #4

my_day=datetime.date(2022,3,13)
print(my_day.weekday())
print(Emp.isWorkday(my_day))


#Constructor and method
class Emp:
    class_var=3
    def __init__(self,first, last) -> None:         #means return None
        self.fname= first
        self.lname= last
        #print(self)            # <__main__.Emp object at 0x7fa6d4040ee0> same as print(object_name)

    def full_name(self):        #if not put self here then at time of method call full_name() takes 0 positional arguments but 1 was given
        print("Name : "+self.fname +" "+ self.lname)    #if put only fname then name 'fname' is not defined
        print(Emp.class_var)    #or self.class_var

emp1= Emp("sidd", "patel")
print(emp1.fname)
print(emp1.full_name())         #also print None at last because of return None
print(emp1.full_name)           #<bound method Emp.full_name of <__main__.Emp object at 0x7fc490627ee0>>
print(Emp.__dict__)  
#{'__module__': '__main__', 'class_var': 3, '__init__': <function Emp.__init__ at 0x7f78e0611280>, 'full_name': <function Emp.full_name at 0x7f78e06113a0>, 
# '__dict__': <attribute '__dict__' of 'Emp' objects>, '__weakref__': <attribute '__weakref__' of 'Emp' objects>, '__doc__': None}


#class variable but if given value to instance then it create that attr in that instance's space      Searching value order--instance scope-> Class scope
class Emp:
    name=None
    pass
emp1= Emp()  # create object <__main__.Emp object at 0x7f668d787ee0>
emp1.name ="sidd"
print(emp1.name) #sidd
print(Emp.name)    #None
print(emp1.__dict__)  #{'name': 'sidd'}

#only refernce will be passed if change in emp1 then also change in Emp
emp1= Emp
emp1.name ="sidd"
print(emp1)            #<class '__main__.Emp'>
print(emp1.__dict__)     
#{'__module__': '__main__', '__dict__': <attribute '__dict__' of 'Emp' objects>, '__weakref__': <attribute '__weakref__' of 'Emp' objects>, '__doc__': None,
# 'name': 'sidd'}
print(Emp.__dict__)