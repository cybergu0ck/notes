# Python Data Types

Everything in python is an object, important core data types are as follows:

| Object Type                  | Examples                                         |
| ---------------------------- | ------------------------------------------------ |
| Numbers                      | 1234, 3.1415, 3+4j, 0b111, Decimal(), Fraction() |
| Strings                      | 'spam', "Bob's", b'a\x01c', u'sp\xc4m'           |
| Lists                        | [1, [2, 'three'], 4.5], list(range(10))          |
| Dictionaries                 | {'food': 'spam', 'taste': 'yum'}, dict(hours=10) |
| Tuples                       | (1, 'spam', 4, 'U'), tuple('spam'), namedtuple   |
| Files                        | open('eggs.txt'), open(r'C:\ham.bin', 'wb')      |
| Sets                         | set('abc'), {'a', 'b', 'c'}                      |
| Other core types             | Booleans, types, None                            |
| Program unit types           | Functions, modules, classes                      |
| Implementation-related types | Compiled code, stack tracebacks                  |

<br>
<br>

## Getting Help

<br>

### dir function

_The `dir` function in Python is a built-in function that returns a list of valid attributes for an object._

- `dir` without any parameter will return the list of names in the current local scope.

  ```py
  print(dir())

  # ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'traceback']
  ```

- `dir` with parameters:

  ```py
  class Sample:
      def __init__(self):
          self.x = 10
          self.y = 20

      def greet(self):
          print("Hello")

  sample = Sample()
  print(dir(sample))

  # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__','__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__','__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__','__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'greet', 'x', 'y']
  ```

  ```py
  num = 15
  print(dir(num))

  # ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
  ```

<br>

## help function
