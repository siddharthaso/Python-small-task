"""classs"""

class Demo:
    def __new__(self):
        
        # import pdb; pdb.set_trace()
        self.__init__(self)       #Derived_Demo's __init__() invoked
        print("Demo's __new__() invoked")
        # return super(Demo, self).__new__(self)

    def __init__(self):
        print("Demo's __init__() invoked")

class Derived_Demo(Demo):
    def __new__(self):
        print("Derived_Demo's __new__() invoked")
        # return super(Derived_Demo, self).__new__(self)  #Demo's __new__() invoked  <__main__.Derived_Demo object at 0x7fd5522a2be0>



    def __init__(self):
        print("Derived_Demo's __init__() invoked")


def main():
    obj1 = Derived_Demo()
    obj2 = Demo()

main()