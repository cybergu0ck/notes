

# `dir()`
---
Without arguments, return the list of *names in the current local scope*. With an argument, attempt to return a list of valid attributes for that object. (i.e. returns all attributes and methods of the specified object, without the values)

The default [`dir()`](https://docs.python.org/3/library/functions.html#dir "dir") mechanism behaves differently with different types of objects, as it attempts to produce the most relevant, rather than complete, information:

-   If the object is a module object, the list contains the names of the module’s attributes.
-   If the object is a type or class object, the list contains the names of its attributes, and recursively of the attributes of its bases.
-   Otherwise, the list contains the object’s attributes’ names, the names of its class’s attributes, and recursively of the attributes of its class’s base classes.

```python
class Butterfly:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def fly(self):
        print('butterfly is flying.')

my_butterfly = Butterfly('Purple', 'Huge')

print(dir(my_butterfly))

#> ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'color', 'fly', 'size']

# We can see that the data attributes 'color', 'size' and method 'fly' are present in output of dir()
```

<br/>

# `ord()`

ord() returns the ASCII value of the parameter

```python
ord('A')

#>65
```

<br/>

# `chr()`

chr() returns the character for the given ASCII number

```python
chr(65)

#>'A'
```

