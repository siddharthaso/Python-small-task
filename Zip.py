# The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.
# The syntax of the zip() function is:
# zip(*iterables)
""""
zip() Parameters
iterables: 	can be built-in iterables (like: list, string, dict), or user-defined iterables

zip() Return Value:
The zip() function returns an iterator of tuples based on the iterable objects.
    If we do not pass any parameter, zip() returns an empty iterator
    If a single iterable is passed, zip() returns an iterator of tuples with each tuple having only one element.
    If multiple iterables are passed, zip() returns an iterator of tuples with each tuple having elements from all the iterables.

    Suppose, two iterables are passed to zip(); one iterable containing three and other containing five elements. Then, the returned iterator will contain three tuples. It's because the iterator stops when the shortest iterable is exhausted.

"""
# ----------------------------------------------------------------------------
print(list(zip([4,5,2])))           #series of 1-item tuples

# print(list(zip(1,[4,5,2])))       #'int' object is not iterable
print(list(zip((1,),[4,5,2])))
print(list(zip([1],[4,5,2])))
print(list(zip((1,2),[4,5,2])))             #take only shortest number of iterator
print(list(zip([1,2],[4,5,2])))
print(list(zip([1,2,3,4],[4,5,2])))
print(list(zip([4,5,2])))
print(list(zip([4,5,2])))
print(list(zip('ABC','abc')))

print(list(zip()))          #[]

s={2,3,1}
s2={'c','a','b'}
print(list(zip(s,s2)))           #[(1, 'b'), (2, 'c'), (3, 'a')] 
# tuples returned by zip() will have elements that are paired up randomly. 

print(list(zip(range(5), range(100))))      #[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]   


print("---------------------------------------------------------------------------")
# ----------------------------------------------------------------------------

languages = ['Java', 'Python', 'JavaScript']
versions = [14, 3, 6]

result = zip(languages, versions)
print(result)               #<zip object at 0x7fd459cd6ec0>
print(type(result))         #<class 'zip'>
print(list(result))

print(result)               #<zip object at 0x7fd459cd6ec0>

# Building Dictionaries
print(dict(result))                 #??????????????????????????????
print(dict(zip(languages, versions)))
#  dict13.update(zip(field, new_job))

# print(next(result))
print()

#<zip object at 0x7f7e6835ae80>
# [('Java', 14), ('Python', 3), ('JavaScript', 6)]
# {}


# Example 1: Python zip()------------------------------------------------------------------------------

number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']

# No iterables are passed
result = zip()

# Converting iterator to list
result_list = list(result)
print(result_list)

# Two iterables are passed
result = zip(number_list, str_list)

# Converting iterator to set
result_set = set(result)
print(result_set)

# Output

# []
# {(2, 'two'), (3, 'three'), (1, 'one')}



# Example 2: Different number of iterable elements------------------------------------------------------------------------------

numbersList = [1, 2, 3]
str_list = ['one', 'two']
numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR')

# Notice, the size of numbersList and numbers_tuple is different
result = zip(numbersList, numbers_tuple)

# Converting to set
result_set = set(result)
print(result_set)

result = zip(numbersList, str_list, numbers_tuple)

# Converting to set
result_set = set(result)
print(result_set)

# Output
# {(2, 'TWO'), (3, 'THREE'), (1, 'ONE')}
# {(2, 'two', 'TWO'), (1, 'one', 'ONE')}

# The * operator can be used in conjunction with zip() to unzip the list.
# zip(*zippedList)



# Example 3: Unzipping the Value Using zip()------------------------------------------------------------------------------

coordinate = ['x', 'y', 'z']
value = [3, 4, 5]

result = zip(coordinate, value)
result_list = list(result)      
print(result_list)       

c, v =  zip(*result_list)

print('c =', c)
print('v =', v)

# Output
# [('x', 3), ('y', 4), ('z', 5)]
# c = ('x', 'y', 'z')
# v = (3, 4, 5)


# Example ------------------------------------------------------------------------------
print("------------------------------------------------------------------------------")

from itertools import zip_longest
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
longest = range(5)
zipped = zip_longest(numbers, letters, longest, fillvalue='?')
print(list(zipped))
# [(1, 'a', 0), (2, 'b', 1), (3, 'c', 2), ('?', '?', 3), ('?', '?', 4)]

""" 
Looping Over Multiple Iterables

Traversing Lists in Parallel: for l, n in zip(letters, numbers):
Traversing Dictionaries in Parallel: for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()): """


"""
Python's zip() function creates an iterator that will aggregate elements from two or more iterables. You can use the resulting 
iterator to quickly and consistently solve common programming problems, like creating dictionaries.

zip() is available in the built-in namespace. If you use dir() to inspect __builtins__, then you'll see zip() at the end of the list:

Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. 
The iterator stops when the shortest input iterable is exhausted. With a single iterable argument, it returns an iterator of 1-tuples.
With no arguments, it returns an empty iterator. 

The function takes in iterables as arguments and returns an iterator. This iterator generates a series of tuples containing elements 
from each iterable. zip() can accept any type of iterable, such as files, lists, tuples, dictionaries, sets, and so on.
"""