#######################################-------------Chaining Dictionaries Together: ChainMap------------------########################################

"""     
        Python's ChainMap groups multiple dictionaries and other mappings together to create a single object that works pretty much like a regular dictionary. 
In other words, it takes several mappings and makes them logically appear as one.
        ChainMap objects are updateable views, which means that changes in any of the chained mappings affect the ChainMap object as a whole. This is because 
ChainMap doesn't merge the input mappings together. It keeps a list of mappings and reimplements common dictionary operations on top of that list. For example,
a key lookup searches the list of mappings successively until it finds the key.

Note: Check out Python's ChainMap: Manage Multiple Contexts Effectively for a deeper dive into using ChainMap in your Python code.
When you're working with ChainMap objects, you can have several dictionaries with either unique or repeated keys.

In either case, ChainMap allows you to treat all your dictionaries as one. If you have unique keys across your dictionaries, 
you can access and update the keys as if you were working with a single dictionary.

If you have repeated keys across your dictionaries, besides managing your dictionaries as one, you can also take advantage of the internal list of 
mappings to define some sort of access priority. Because of this feature, ChainMap objects are great for handling multiple contexts.

For example, say you're working on a command-line interface (CLI) application. The application allows the user to use a proxy service for connecting to 
the Internet. The settings priorities are:

Command-line options (--proxy, -p)
Local configuration files in the user's home directory
Global proxy configuration
If the user supplies a proxy at the command line, then the application must use that proxy. Otherwise, the application should use the proxy provided in 
the next configuration object, and so on. This is one of the most common use cases of ChainMap. In this situation, you can do the following: """

from collections import ChainMap

cmd_proxy = {}                                  # The user doesn't provide a proxy
local_proxy = {"proxy": "proxy.local.com"}
global_proxy = {"proxy": "proxy.global.com"}

config = ChainMap(cmd_proxy, local_proxy, global_proxy)
print(config["proxy"])                          #'proxy.local.com'


""" ChainMap allows you to define the appropriate priority for the application's proxy configuration. A key lookup searches cmd_proxy, then local_proxy, 
and finally global_proxy, returning the first instance of the key at hand. In this example, the user doesn't provide a proxy at the command line, 
so your application uses the proxy in local_proxy.

In general, ChainMap objects behave similarly to regular dict objects. However, they have some additional features. For example, they have a .maps 
public attribute that holds the internal list of mappings: """

numbers = {"one": 1, "two": 2}
letters = {"a": "A", "b": "B"}
alpha_nums = ChainMap(numbers, letters)
print(alpha_nums.maps)                      #[{'one': 1, 'two': 2}, {'a': 'A', 'b': 'B'}]


""" The instance attribute .maps gives you access to the internal list of mappings. This list is updatable. You can add and remove mappings manually, 
iterate through the list, and more.
Additionally, ChainMap provides a .new_child() method and a .parents property: """

dad = {"name": "John", "age": 35}
mom = {"name": "Jane", "age": 31}

family = ChainMap(mom, dad)
print(family)                       #ChainMap({'name': 'Jane', 'age': 31}, {'name': 'John', 'age': 35})

son = {"name": "Mike", "age": 0}
family = family.new_child(son)

for person in family.maps:
    print(person)

# {'name': 'Mike', 'age': 0}
# {'name': 'Jane', 'age': 31}
# {'name': 'John', 'age': 35}

print(family.parents)               #ChainMap({'name': 'Jane', 'age': 31}, {'name': 'John', 'age': 35})

""" With .new_child(), you create a new ChainMap object containing a new map (son) followed by all the maps in the current instance. The map passed as a 
first argument becomes the first map in the list of maps. If you don't pass a map, then the method uses an empty dictionary.
The parents property returns a new ChainMap objects containing all the maps in the current instance except for the first one. This is useful when you 
need to skip the first map in a key lookup.

A final feature to highlight in ChainMap is that mutating operations, such as updating keys, adding new keys, deleting existing keys, popping keys, 
and clearing the dictionary, act on the first mapping in the internal list of mappings: """

numbers = {"one": 1, "two": 2}
letters = {"a": "A", "b": "B"}

alpha_nums = ChainMap(numbers, letters)
print(alpha_nums)                       #ChainMap({'one': 1, 'two': 2}, {'a': 'A', 'b': 'B'})

# Add a new key-value pair
alpha_nums["c"] = "C"
print(alpha_nums)                       #ChainMap({'one': 1, 'two': 2, 'c': 'C'}, {'a': 'A', 'b': 'B'})

# Pop a key that exists in the first dictionary
print(alpha_nums.pop("two"))            #2

print(alpha_nums)                       #ChainMap({'one': 1, 'c': 'C'}, {'a': 'A', 'b': 'B'})

# Delete keys that don't exist in the first dict but do in others

# del alpha_nums["a"]
# Traceback (most recent call last):
#   ...
# KeyError: "Key not found in the first mapping: 'a'"

# Clear the dictionary
alpha_nums.clear()
print(alpha_nums)                       #ChainMap({}, {'a': 'A', 'b': 'B'})


""" These examples show that mutating operations on a ChainMap object only affect the first mapping in the internal list. This is an important detail to
 consider when you're working with ChainMap.
The tricky part is that, at first glance, it could look like it's possible to mutate any existing key-value pair in a given ChainMap. However, 
you can only mutate the key-value pairs in the first mapping unless you use .maps to access and mutate other mappings in the list directly. """