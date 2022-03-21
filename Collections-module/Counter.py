#######################################-------------Counting Objects in One Go: Counter------------------########################################

# Counting objects is a common operation in programming. Say you need to count how many times a given item appears in a list or iterable. 
# If your list is short, then counting its items can be straightforward and quick. If you have a long list, then counting the items will be more challenging.

word = "mississippi"
counter = {}
for letter in word:
    if letter not in counter:
        counter[letter] = 0
    counter[letter] += 1

print(counter)          #{'m': 1, 'i': 4, 's': 4, 'p': 2}


from collections import defaultdict
counter = defaultdict(int)
for letter in "mississippi":
    counter[letter] += 1

print(counter)              #defaultdict(<class 'int'>, {'m': 1, 'i': 4, 's': 4, 'p': 2})



from collections import Counter
print(Counter("mississippi"))           #Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})


# You can use lists, tuples, or any iterables with repeated objects. The only restriction is that your objects need to be hashable:
""" Integer numbers are hashable, so Counter works correctly. On the other hand, lists aren't hashable, so Counter fails with a TypeError.
Being hashable means that your objects must have a hash value that never changes during their lifetime. 
This is a requirement because these objects will work as dictionary keys. In Python, immutable objects are also hashable.
 """

from collections import Counter
Counter([1, 1, 2, 3, 3, 3, 4])      #Counter({3: 3, 1: 2, 2: 1, 4: 1})
# Counter(([1], [1]))
# Traceback (most recent call last):
# TypeError: unhashable type: 'list'


""" Since Counter is a subclass of dict, their interfaces are mostly the same. However, there are some subtle differences. 
The first difference is that Counter doesn't implement .fromkeys(). This avoids inconsistencies, such as Counter.fromkeys("abbbc", 2), 
in which every letter would have an initial count of 2 regardless of the real count it has in the input iterable.

The second difference is that .update() doesn't replace the count (value) of an existing object (key) with a new count. It adds both counts together: """

letters = Counter("mississippi")
print(letters)                      #Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

# Update the counts of m and i
letters.update(m=3, i=4)
print(letters)                      #Counter({'i': 8, 'm': 4, 's': 4, 'p': 2})

# Add a new key-count pair
letters.update({"a": 2})
print(letters)                      #Counter({'i': 8, 'm': 4, 's': 4, 'p': 2, 'a': 2})

# Update with another counter
letters.update(Counter(["s", "s", "p"]))
print(letters)                      #Counter({'i': 8, 's': 6, 'm': 4, 'p': 3, 'a': 2})


# Another difference between Counter and dict is that accessing a missing key returns 0 instead of raising a KeyError:
letters = Counter("mississippi")
print(letters["a"])    #0


""" In Python, Counter is also useful to emulate a multiset or bag. Multisets are similar to sets, but they allow multiple instances of a given element. 
The number of instances of an element is known as its multiplicity. For example, you can have a multiset like {1, 1, 2, 3, 3, 3, 4, 4}.
When you use Counter to emulate multisets, the keys represent the elements, and the values represent their respective multiplicity: """

from collections import Counter
multiset = Counter({1, 1, 2, 3, 3, 3, 4, 4})   #become set bcs of {}
print(multiset)                                #Counter({1: 1, 2: 1, 3: 1, 4: 1})
print(multiset.keys() == {1, 2, 3, 4})         #True


""" 
Here, the keys of multiset are equivalent to a Python set. The values hold the multiplicity of each element in the set.
Python' Counter provides a few additional features that help you work with them as multisets. For example, you can initialize your counters 
ith a mapping of elements and their multiplicity. You can also perform math operations on the elements' multiplicity and more.
Say you're working at the local pet shelter. You have a given number of pets, and you need to have a record of how many pets are adopted each day 
and how many pets enter and leave the shelter. In this case, you can use Counter: """

from collections import Counter

inventory = Counter(dogs=23, cats=14, pythons=7)
adopted = Counter(dogs=2, cats=5, pythons=1)

inventory.subtract(adopted)
print(inventory)                                      #Counter({'dogs': 21, 'cats': 9, 'pythons': 6})

new_pets = {"dogs": 4, "cats": 1}
inventory.update(new_pets)
print(inventory)                                      #Counter({'dogs': 25, 'cats': 10, 'pythons': 6})

inventory = inventory - Counter(dogs=2, cats=3, pythons=1)
print(inventory)                                      #Counter({'dogs': 23, 'cats': 7, 'pythons': 5})

new_pets = {"dogs": 4, "pythons": 2}
inventory += new_pets
print(inventory)                                      #Counter({'dogs': 27, 'cats': 7, 'pythons': 7})

# That's neat! Now you can keep a record of your pets using Counter. Note that you can use .subtract() and .update() to subtract 
# and add counts or multiplicities. You can also use the addition (+) and subtraction (-) operators.