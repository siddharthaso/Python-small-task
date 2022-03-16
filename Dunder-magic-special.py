#dunder(surrounded by double underscore) and __repr__ and __int__, operator overloading---------------------magic method-----------------------__len__---
class A:
    def __init__(self, fname,  lname, pay) :
        self.fname=fname
        self.lname=lname
        self.pay =pay

    def __repr__(self):
        return " {} , {}".format(self.fname, self.lname)

    def __str__(self) -> str:
        return "{}----------{}".format(self.fname, self.lname)

    def __add__(self,other):
        return " {} , {}".format(self.fname, other.fname)
        return self.fname , other.fname
        # return self.pay+ other.pay

a = A("siddharth", "Asodariya", 33000)
b= A("keval", "Goyani", 30000)
print(a)
print(repr(a))              #a.__repr__()
print(str(a))               #a.__str__()
print(a + b)

print(int.__add__(3,4))
print(str.__add__('a','b'))