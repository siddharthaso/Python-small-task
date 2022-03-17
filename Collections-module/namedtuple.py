""" Improving Code Readability: namedtuple()
Python's namedtuple() is a factory function that allows you to create tuple subclasses with named fields. 
These fields give you direct access to the values in a given named tuple using the dot notation, like in obj.attr. """

""" required arguments:

typename is the name of the class you're creating. It must be a string with a valid Python identifier.
field_names is the list of field names you'll use to access the items in the resulting tuple. It can be:
    An iterable of strings, such as ["field1", "field2", ..., "fieldN"]
    A string with whitespace-separated field names, such as "field1 field2 ... fieldN"
    A string with comma-separated field names, such as "field1, field2, ..., fieldN" """

from collections import namedtuple
def custom_divmod(x, y):
    DivMod = namedtuple("DivMod", "quotient remainder")
    return DivMod(*divmod(x, y))

result = custom_divmod(12, 5)
print(result)              #DivMod(quotient=2, remainder=2)
print(result.quotient)     #2
print(result.remainder)    #2

print('-------------------------------------------------------------------------------------------------')
# Use a list of strings as field names
Point = namedtuple("Point", ["x", "y"])
point = Point(2, 4)
print(point)
# Access the coordinates
print(point.x)      #2
print(point.y)      #4
print(point[0])     #2

print('-------------------------------------------------------------------------------------------------')
# Use a generator expression as field names
Point = namedtuple("Point", (field for field in "xy"))
print(Point(2, 4))
# Use a string with comma-separated field names
Point = namedtuple("Point", "x, y")
print(Point(2, 4))
# Use a string with space-separated field names
Point = namedtuple("Point", "x y")
print(Point(2, 4))

print('-------------------------------------------------------------------------------------------------')
# Define default values for fields
Person = namedtuple("Person", "name job", defaults=["Python Developer"])
person = Person("Jane")
print(person)
# Create a dictionary from a named tuple
print(person._asdict())
# Replace the value of a field
person = person._replace(job="Web Developer")
print(person)