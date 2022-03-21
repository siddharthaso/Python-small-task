#######################################-------------Keeping Your Dictionaries Ordered: OrderedDict------------------########################################



""" The new class would remember the order of items based on the moment in which keys were inserted. That was the origin of OrderedDict.
OrderedDict iterates over keys and values in the same order keys were first inserted into the dictionary. If you assign a new value to an existing key, 
then the order of the key-value pair remains unchanged. If an entry is deleted and reinserted, then it'll be moved to the end of the dictionary. """

from collections import OrderedDict
life_stages = OrderedDict()
life_stages["childhood"] = "0-9"
life_stages["adolescence"] = "9-18"
life_stages["adulthood"] = "18-65"
life_stages["old"] = "+65"
for stage, years in life_stages.items():
    print(stage, "->", years)

# childhood -> 0-9
# adolescence -> 9-18
# adulthood -> 18-65
# old -> +65


""" There are some features of OrderedDict that still make it valuable:

    Intent communication: With OrderedDict, your code will make it clear that the order of items in the dictionary is important. 
                            You're clearly communicating that your code needs or relies on the order of items in the underlying dictionary.
    Control over the order of items: With OrderedDict, you have access to .move_to_end(), which is a method that allows you to manipulate 
                            the order of items in your dictionary. You'll also have an enhanced variation of .popitem() that allows removing items 
                            from either end of the underlying dictionary.
    Equality test behavior: With OrderedDict, equality tests between dictionaries take the order of items into account. So, if you have two ordered 
                            dictionaries with the same group of items but in a different order, then your dictionaries will be considered non-equal.

There is at least one more reason for using OrderedDict: backward compatibility. Relying on regular dict objects to preserve the order of items will 
break your code in environments that run versions of Python older than 3.6. """

 
letters = OrderedDict(b=2, d=4, a=1, c=3)
print(letters)                      #OrderedDict([('b', 2), ('d', 4), ('a', 1), ('c', 3)])

# Move b to the right end
letters.move_to_end("b")
print(letters)                      #OrderedDict([('d', 4), ('a', 1), ('c', 3), ('b', 2)])

# Move b to the left end
letters.move_to_end("b", last=False)
print(letters)                      #OrderedDict([('b', 2), ('d', 4), ('a', 1), ('c', 3)])

# Sort letters by key
for key in sorted(letters):letters.move_to_end(key)
print(letters)                      #OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

"""In these examples, you use .move_to_end() to move items around and reorder letters. Note that .move_to_end() accepts an optional argument called last 
that allows you to control which end of the dictionary you want to move the items to. """


# Another important difference between OrderedDict and a regular dictionary is how they compare for equality:
# Regular dictionaries compare the content only
letters_0 = dict(a=1, b=2, c=3, d=4)
letters_1 = dict(b=2, a=1, d=4, c=3)
print(letters_0 == letters_1)          #True

# Ordered dictionaries compare content and order
letters_0 = OrderedDict(a=1, b=2, c=3, d=4)
letters_1 = OrderedDict(b=2, a=1, d=4, c=3)
print(letters_0 == letters_1)           #False

letters_2 = OrderedDict(a=1, b=2, c=3, d=4)
print(letters_0 == letters_2)           #True