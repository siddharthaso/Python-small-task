# content of test_sample.py
def func(x):
    print("func is called")
    return x + 1


def test_func1(x):
    print("func1 is called")
    return x + 1

def test_answer():
    assert func(3) == 4
