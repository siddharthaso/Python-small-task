# -------------order matter
def parent():
    print("Printing from the parent() function")
    # second_child()              #Exception has occurred: UnboundLocalError local variable 'second_child' referenced before assignment
    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")
    second_child()
    first_child()
parent()

# the inner functions are not defined until the parent function is called. 
# They are locally scoped to parent(): they only exist inside the parent() function as local variables. 