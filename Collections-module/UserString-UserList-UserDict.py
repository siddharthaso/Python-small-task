###################################-------------Customizing Built-Ins: UserString, UserList, and UserDict------------------##############################

""" Sometimes you need to customize built-in types, such as strings, lists, and dictionaries to add and modify certain behavior. Since Python 2.2, 
you can do that by subclassing those types directly. However, you could face some issues with this approach, as you'll see in a minute.

Python's collections provides three convenient wrapper classes that mimic the behavior of the built-in data types:
    UserString
    UserList
    UserDict
With a combination of regular and special methods, you can use these classes to mimic and customize the behavior of strings, lists, and dictionaries.

Nowadays, developers often ask themselves if there's a reason to use UserString, UserList, and UserDict when they need to customize the behavior of 
built-in types. The answer is yes.

Built-in types were designed and implemented with the open-closed principle in mind. This means that they're open for extension but closed for modification.
 Allowing modifications on the core features of these classes can potentially break their invariants. So, Python core developers decided to protect them 
 from modifications.

For example, say you need a dictionary that automatically lowercases the keys when you insert them. You could subclass dict and override .__setitem__() 
so every time you insert a key, the dictionary lowercases the key name: """


class LowerDict(dict):
    def __setitem__(self, key, value):
        key = key.lower()
        super().__setitem__(key, value)


ordinals = LowerDict({"FIRST": 1, "SECOND": 2})
ordinals["THIRD"] = 3
ordinals.update({"FOURTH": 4})
print(ordinals)                         #{'FIRST': 1, 'SECOND': 2, 'third': 3, 'FOURTH': 4}
print(isinstance(ordinals, dict))       #True


""" This dictionary works correctly when you insert new keys using dictionary-style assignment with square brackets ([]). However, it doesn't work 
when you pass an initial dictionary to the class constructor or when you use .update(). This means that you would need to 
override .__init__(), .update(), and probably some other methods for your custom dictionary to work correctly.

Now take a look at the same dictionary but using UserDict as a base class: """


from collections import UserDict

class LowerDict(UserDict):
    def __setitem__(self, key, value):
        key = key.lower()
        super().__setitem__(key, value)

ordinals = LowerDict({"FIRST": 1, "SECOND": 2})
ordinals["THIRD"] = 3
ordinals.update({"FOURTH": 4})
print(ordinals)                        #{'first': 1, 'second': 2, 'third': 3, 'fourth': 4}
print(isinstance(ordinals, dict))      #False

""" 
It works! Your custom dictionary now converts all the new keys into lowercase letters before inserting them into the dictionary. Note that since you 
don't inherit from dict directly, your class doesn't return instances of dict as in the example above.

UserDict stores a regular dictionary in an instance attribute called .data. Then it implements all its methods around that dictionary. UserList and 
UserString work the same way, but their .data attribute holds a list and a str object, respectively.

If you need to customize either of these classes, then you just need to override the appropriate methods and change what they do as required.

In general, you should use UserDict, UserList, and UserString when you need a class that acts almost identically to the underlying wrapped built-in 
class and you want to customize some part of its standard functionalities.

Another reason to use these classes rather than the built-in equivalent classes is to access the underlying .data attribute to manipulate it directly.

The ability to inherit from built-in types directly has largely superseded the use of UserDict, UserList, and UserString. However, the internal 
implementation of built-in types makes it hard to safely inherit from them without rewriting a significant amount of code. In most cases, it's safer 
to use the appropriate class from collections. It'll save you from several issues and weird behaviors. """