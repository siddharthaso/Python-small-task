""" You’ll look at the following Python stack implementations:

list
collections.deque
queue.LifoQueue """

my_stack =[]
my_stack.append('sidd')     #append() takes exactly one argument (3 given)
my_stack.append(67)
my_stack.append('fg')
my_stack.append(True)
print(my_stack)
print("popping: ", my_stack.pop())
print(my_stack)

from collections import deque
from re import M
my_stack = deque()
my_stack.append('sidd')
print(my_stack)             #deque(['sidd'])
print(type(my_stack))       #<class 'collections.deque'>
my_stack.pop()
print(my_stack)

# my_stack.popleft()
# my_stack.appendleft('fdfdf')

from queue import LifoQueue
my_stack = LifoQueue()
my_stack.put('siddharth')
my_stack.put('asd')
print(my_stack)             #<queue.LifoQueue object at 0x7f66b04b3bb0>
print(type(my_stack))       #<class 'queue.LifoQueue'>
print(my_stack.get())       #asd
print(my_stack.get())
# print(my_stack.get())       #wait_ forever stuck at this line empty
# print(my_stack.get_nowait())    #Empty exception: no description
my_stack.put('rfsfs')

""" There are various functions available in this module: 
    maxsize – Number of items allowed in the queue.
    empty() – Return True if the queue is empty, False otherwise.
    full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
    get() – Remove and return an item from the queue. If the queue is empty, wait until an item is available.
    get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
    put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
    put_nowait(item) – Put an item into the queue without blocking.
    qsize() – Return the number of items in the queue. If no free slot is immediately available, raise QueueFull. """