class A:
    def __init__(self) -> None:
        self.lst = []

    def get_list(self):
        self.lst.append("python")
        self.lst.extend(["golang", "java"])
        return self.lst
    
a = A()
print(a.get_list())
