#######################################-------------Handling Missing Keys: defaultdict------------------##################################################

"""A common problem you'll face when you're working with dictionaries in Python is how to handle missing keys. 
If you try to access a key that doesn't exist in a given dictionary, then you get a KeyError:"""

favorites = {"pet": "dog", "color": "blue", "language": "Python"}

""" favorites["fruit"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'fruit'

There are a few approaches to work around this issue. For example, you can use .setdefault(). This method takes a key as an argument. 
If the key exists in the dictionary, then it returns the corresponding value. Otherwise, the method inserts the key, assigns it a default value, 
and returns that value: """

favorites = {"pet": "dog", "color": "blue", "language": "Python"}
print(favorites.setdefault("fruit", "apple"))          #'apple'
print(favorites)                                       #{'pet': 'dog', 'color': 'blue', 'language': 'Python', 'fruit': 'apple'}
print(favorites.setdefault("pet", "cat"))              #'dog'
print(favorites)                                       #{'pet': 'dog', 'color': 'blue', 'language': 'Python', 'fruit': 'apple'}

""" In this example, you use .setdefault() to generate a default value for fruit. Since this key doesn't exist in favorites, .setdefault() 
creates it and assigns it the value of apple. If you call .setdefault() with an existent key, then the call won't affect the dictionary and 
your key will hold the original value instead of the default value.
You can also use .get() to return a suitable default value if a given key is missing: """

favorites = {"pet": "dog", "color": "blue", "language": "Python"}
print(favorites.get("fruit", "apple"))                #'apple'
print(favorites)                                      #{'pet': 'dog', 'color': 'blue', 'language': 'Python'}

"""Here, .get() returns apple because the key is missing in the underlying dictionary. However, .get() doesn't create the new key for you."""

""" The constructor of defaultdict takes a function object as its first argument. When you access a key that doesn't exist, defaultdict automatically 
calls that function without arguments to create a suitable default value for the key at hand. To provide its functionality, defaultdict stores the 
input function in .default_factory and then overrides .__missing__() to automatically call the function and generate a default value when you access 
any missing keys.
You can use any callable to initialize your defaultdict objects. For example, with int() you can create a suitable counter to count different objects: """


from collections import defaultdict

counter = defaultdict(int)
print(counter)              #defaultdict(<class 'int'>, {})
counter["dogs"]             #0
print(counter)              #defaultdict(<class 'int'>, {'dogs': 0})
counter["dogs"] += 1
counter["dogs"] += 1
counter["dogs"] += 1
counter["cats"] += 1
counter["cats"] += 1
print(counter)              #defaultdict(<class 'int'>, {'dogs': 3, 'cats': 2})

# In this example, you create an empty defaultdict with int() as its first argument. When you access a key that doesn't exist, 
# the dictionary automatically calls int(), which returns 0 as the default value for the key at hand.


# Another common use case of defaultdict is to group things. In this case, the handy factory function is list():

pets = [("dog", "Affenpinscher"), ("dog", "Terrier"), ("dog", "Boxer"), ("cat", "Abyssinian") , ("cat", "Birman")]
group_pets = defaultdict(list)

for pet, breed in pets:
    group_pets[pet].append(breed)

for pet, breeds in group_pets.items():
    print(pet, "->", breeds)
    
# dog -> ['Affenpinscher', 'Terrier', 'Boxer']
# cat -> ['Abyssinian', 'Birman']