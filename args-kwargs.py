class Random:
    # can put any name instead of args and kargs but * represent tuple and ** represent dict
    def __init__(self, *args, **kargs):
        print(kargs)
        self.a = kargs.get('positional_first', 1)
        self.b = kargs.get('positional_second', 2)

    @classmethod
    def named_const_1_param(cls, positional_second):
        cls(positional_second=positional_second).addition()

    @classmethod
    def named_const_2_param(cls, positional_first):
        cls(positional_first=positional_first).addition()

    #don't require any class or instance variable
    @staticmethod
    def greet(text):
        print(text)

    def addition(self):
        print(self.a + self.b)

if __name__ == '__main__':
    class_obj = Random
    class_obj.named_const_1_param(2)
    class_obj.named_const_2_param(1)
    Random.greet("Hello")