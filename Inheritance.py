#inheritance-----------------------------------------------------------------------------------------------------
class Employee:
    r_amount=1.05
    emp_count=0
    def __init__(self,first_name,last_name, amount):
        self.first_name=first_name
        self.last_name=last_name
        self.amount=amount
        self.email_id="{0}.{1}@{1}.com" .format(first_name,last_name)
        Employee.emp_count +=1

    def fullname(self):
        print ("%s %s"%(self.first_name,self.last_name))

    def print1(self):
        print (self.email)
        print ("Total no of Employee are :%d" %(Employee.emp_count))

    def raise_amount(self):
        self.amount = self.amount * self.r_amount
        return self.amount

class Developer(Employee):
    r_amount = 1.10
    def __init__(self,f,l,a,prog):
        super().__init__(f,l,a)
        self.programming=prog

class Manager(Employee):
    def __init__(self,f,l,a,emp):
        super().__init__(f,l,a)
        if emp is None:
            self.my_employee=[]
        else:
            self.my_employee=emp

    def add_employee(self,emp):
        if emp in self.my_employee:
            print("employee is already exist")
        else:
            self.my_employee.append(emp)

    def remove_employee(self,emp):
        if emp in self.my_employee:
            self.my_employee.remove(emp)

    def print_employee(self):
        for emp in self.my_employee:
            emp.fullname()
    #Why does my Python code print None?
    # Because there are two print statements. First is inside function and second is outside function. 
    # When a function doesn't return anything, it implicitly returns None . Use return statement at end of function to return value.

dev1=Developer("sidd","Asodariya",500000,"Python")
dev2=Developer('keval','Goyani',5688989,'react_native')
emp1=Employee("trump","dump",30000)
mgr1=Manager("lakhan","shah",5000,[dev1])
print(dev1.raise_amount())
dev1.fullname()
emp1.fullname()
mgr1.fullname()
#mgr1.add_employee(dev1)
mgr1.add_employee(emp1)
mgr1.add_employee(dev2)
mgr1.print_employee()
mgr1.remove_employee(dev1)
mgr1.print_employee()
# print(mgr1.__dict__)
# print(help(mgr1))

print("--------------------")
print(isinstance(dev1,Developer))
print(isinstance(dev1,Employee))
print(isinstance(mgr1, Manager))
print(isinstance(mgr1, Employee))
print(isinstance(dev1, Manager))
print(isinstance(mgr1, Developer))
print("--------------------")
print(issubclass(Employee,Developer))
print(issubclass(Developer,Employee))            #issubclass() arg 1 must be a class
print(issubclass(Employee, Manager))
print(issubclass(Manager, Employee))
print(issubclass(Developer, Manager))
print(issubclass(Manager, Developer))