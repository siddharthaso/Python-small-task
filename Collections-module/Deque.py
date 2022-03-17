############################################################-------------DEQUE------------------##################################################

""" The deque initializer takes two optional arguments:
        iterable holds an iterable that serves as an initializer.
        maxlen holds an integer number that specifies the maximum length of the deque.
If you don't provide an iterable, then you get an empty deque. If you supply a value to maxlen, then your deque will only store up to maxlen items. """


from collections import deque
my_queue = deque()
my_queue.append(1)
my_queue.append(2)
my_queue.append(3)
my_queue.append(4)
my_queue.append(5)
print(my_queue)             #deque([1, 2, 3, 4, 5])
print(type(my_queue))       #<class 'collections.deque'>
my_queue.popleft()
print(my_queue)             #deque([2, 3, 4, 5])

print('-------------------------------------------------------------------------------------------------')
mq = deque([1,2,3], maxlen=3)
mq.append(4)
print(mq)   #deque([2, 3, 4], maxlen=3)
# Once the deque reaches its maximum size (three files in this case), adding a new file on an end of the deque automatically discards the file at 
# the opposite end. If you don't supply a value to maxlen, then the deque can grow to an arbitrary number of items.

""" 
>>> from collections import deque

>>> # Use different iterables to create deques
>>> deque((1, 2, 3, 4))
deque([1, 2, 3, 4])

>>> deque([1, 2, 3, 4])
deque([1, 2, 3, 4])

>>> deque("abcd")
deque(['a', 'b', 'c', 'd'])

>>> # Unlike lists, deque doesn't support .pop() with arbitrary indices
>>> deque("abcd").pop(2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: pop() takes no arguments (1 given)

>>> # Extend an existing deque
>>> numbers = deque([1, 2])
>>> numbers.extend([3, 4, 5])
>>> numbers
deque([1, 2, 3, 4, 5])

>>> numbers.extendleft([-1, -2, -3, -4, -5])
>>> numbers
deque([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])

>>> # Insert an item at a given position
>>> numbers.insert(5, 0)
>>> numbers
deque([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])

Deques also support sequence operations:

Method	Description
.clear()	Remove all the elements from a deque
.copy()	Create a shallow copy of a deque
.count(x)	Count the number of deque elements equal to x
.remove(value)	Remove the first occurrence of value

>>> from collections import deque

>>> ordinals = deque(["first", "second", "third"])
>>> ordinals.rotate()
>>> ordinals
deque(['third', 'first', 'second'])

>>> ordinals.rotate(2)
>>> ordinals
deque(['first', 'second', 'third'])

>>> ordinals.rotate(-2)
>>> ordinals
deque(['third', 'first', 'second'])

>>> ordinals.rotate(-1)
>>> ordinals
deque(['first', 'second', 'third'])
This method rotates the deque n steps to the right. The default value of n is 1. If you provide a negative value to n, then the rotation is to the left.

Finally, you can use indices to access the elements in a deque, but you can't slice a deque:

>>> from collections import deque

>>> ordinals = deque(["first", "second", "third"])
>>> ordinals[1]
'second'

>>> ordinals[0:2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sequence index must be integer, not 'slice' """