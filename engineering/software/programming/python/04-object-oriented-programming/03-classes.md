- classes and types are same in Python3.

<br/>

## Class definition syntax

```python
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```

When a class definition is entered, a new namespace is created, and used as the local scope — thus, all assignments to local variables go into this new namespace. In particular, function definitions bind the name of the new function here.

<br/>

## Class Objects

Class objects support two kinds of operations: attribute references and instantiation.

1. **_Attribute references_** use the standard syntax used for all attribute references in Python: `obj.name`. Valid attribute names are all the names that were in the class’s namespace when the class object was created.

   ```python
   class MyClass:
       """A simple example class"""
       i = 12345
       def f(self):
           return 'hello world'
   ```

   - For the above class definition, `MyClass.i` and `MyClass.f` are valid **_attribute references_**, returning an integer and a function object, respectively.

   - Class attributes can also be assigned to, so you can change the value of MyClass.i by assignment.

   - `__doc__` is also a valid attribute, returning the docstring belonging to the class: "A simple example class".

2. **_Class instantiation_** uses function notation.

   ```python
   x = MyClass()
   ```

   - creates a new instance of the class and assigns this object to the local variable x.

   - When a class defines an `__init__()` method (Note that `__init__()` is not mandatory; i.e. a class can be created without it), class instantiation automatically invokes `__init__()` for the newly created class instance.

     ```python
     def __init__(self):
         self.data = []

     ```

<br/>

## Instance Objects

The only operations understood by **_instance objects_** are **_attribute references_**. There are two kinds of valid attribute names: **_data attributes_** and **_methods_**.

1. **_data attributes_** need not be declared; like local variables, they spring into existence when they are first assigned to. For illustration:

   ```python
   class Demo:
       pass

   obj = Demo()

   obj.data_attr = 10
   print(obj.data_attr)

   #>10
   ```

2. A **_method_** is a function that “belongs to” an object. (In Python, the term method is not unique to class instances: other object types can have methods as well. For example, list objects have methods called append, insert, remove, sort, and so on.

   - Valid method names of an instance object depend on its class. By definition, all attributes of a class that are function objects define corresponding methods of its instances.

   - So in our example, `x.f` is a valid method reference, since `MyClass.f` is a function, but `x.i` is not, since `MyClass.i` is not.

     > But `x.f` is not the same thing as `MyClass.f` — it is a method object, not a function object.

<br/>

NOTE:

Data attributes are prioritised over methods. If you have a data attribute and a method with the same name, then it'll give an error when the method is called.

```python
class Heat:
    def __init__(self):
        self.temperature = 96

    def temperature(self):
        return self.temp

pan = Heat()
print(pan.temperature)  #No trouble in accessing data attribute.

#>96
```

```python
class Heat:
    def __init__(self):
        self.temperature = 96

    def temperature(self):
        return self.temp

pan = Heat()
print(pan.temperature())  # error

#>TypeError: 'int' object is not callable
```

<br/>

## Method Objects

```python
class Demo:
    def foo(self):
        print("printing foo")

obj = Demo()
obj.foo()  # This is exactly equvivalent to Demo.foo(obj)

#>printing foo
```

- the special thing about methods is that the instance object is passed as the first argument of the function.

- In our example, the call `obj.foo()` is exactly equivalent to `Demo.foo(obj)`.

- When a non-data attribute of an instance is referenced, the instance’s class is searched. If the name denotes a valid class attribute that is a function object, a method object is created by packing (pointers to) the instance object and the function object just found together in an abstract object: this is the method object.

- When the method object is called with an argument list, a new argument list is constructed from the instance object and the argument list, and the function object is called with this new argument list.

<br/>

## Class and Instance Variables

Instance variables are for data unique to each instance and are declared in the constructor.

Class variables are for attributes and methods shared by all instances of the class, hence remain the same for all instances of the class and are declared at the top-level of a class.

```python
class Dog:
    kind = "Canine"          # Class variable shared by all instances

    def __init__(self, name):
        self.name = name    # Instance variable unique to each instance

ramu = Dog('Ramu')
tommy = Dog("Tommy")

print('{} is a {}'.format(ramu.name, ramu.kind))
print('{0} is a {1}'.format(tommy.name, tommy.kind))

#>Ramu is a Canine
#>Tommy is a Canine
```

<br/>
<br/>
<br/>

# Class methods, Instance methods and Static methods

### 1. Instance Methods

Instance Method enables to access data and properties unique to each instance.

- Instance method are methods which require an object of its class to be created before it can be called.
- Instance methods are bound to the Object itself.
- They are referenced by Reference to the Object itself (self)

<br/>
<br/>

### 2. Class Methods

A Class Method is used to access or modify the state of the class.

- Class methods are the methods that can be called without creating an object of class.
- Class method is a method that is bound to a class rather than its object.
- They are referenced by the class name itself (cls, as the first parameter)

```python
class Pet:
    total_pets = 0
    def __init__(self, name):
        self.name = name
        Pet.total_pets += 1

    @classmethod
    def get_pet_count(cls):
        return Pet.total_pets

class Dog(Pet):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

my_pet = Pet("Scoobie")
his_pet = Dog("Brownie", "Pom")
print(Pet.get_pet_count())  #Note that here we are calling get_pet_count method on the class itself.

#>2
```

<br/>
<br/>

### 3. Static Methods

---

A static method is a general utility method that performs a task in isolation.

- Static methods are the methods that can be called without creating an object of class (much like class methods).
- Static methods (much like class methods) are methods that are bound to a class rather than its object.
- They are referenced by the class name itself or reference to the Object of that class.

```python
class Math:

    @staticmethod
    def doubler(num):      #No need for "self" nor "cls" parameter.
        return num*2

    @staticmethod
    def printSomethhing():
        print("Bla Bla Bla")


print(Math.doubler(5))  #No need to create an object to access static methods.
Math.printSomethhing()


#>10
#>Bla Bla Bla
```

<br/>
<br/>

### Difference between Static Method and Class Method

The difference between a static method and a class method is:

- Static method knows nothing about the class and just deals with the parameters that are passed to it.
- Class method works with the class since its parameter is always the class itself.

<br>
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
