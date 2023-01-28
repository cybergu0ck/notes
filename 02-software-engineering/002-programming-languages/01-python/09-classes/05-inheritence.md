
- Inheritance allows one class (aka child class / subclass / derivedclass) to inherit the attributes and behaviour from another class (aka parentclass/s superclass /baseclass).
- This powerful language feature helps us avoid writing a lot of the same code twice. It allows us to ***DRY (don't repeat yourself)*** up our code.

- The syntax for a derived class definition looks like this:

    ```python
    class DerivedClassName(BaseClassName):
        # class body
    ```
- The name BaseClassName must be defined in a scope containing the derived class definition. 

- In place of a base class name, other arbitrary expressions are also allowed. This can be useful, for example, when the base class is defined in another module:

    ```python
    class DerivedClassName(modname.BaseClassName):
        #class body
    ```

Example of a code using Inheritance:

```python
class Animal:
    def __init__(self, environment):
        self.environment = environment
    
    def getenvironment(self):
        print(f'The animal likes {self.environment} environment.')

class Dog(Animal):
    def __init__(self, environment, breed):
        super().__init__(environment)      #Initialising environment attribute from super class, No need for "self" and ":"
        self.breed = breed

class Bird(Animal):
    def __init__(self):
        super().__init__('Air')   #'Air' is passed into environment parameter in init of super class!


myDog = Dog('Land', "Pom")
myBird = Bird()
myDog.getenvironment()
myBird.getenvironment()
```



> When the class object is constructed, the base class is remembered. This is used for resolving attribute references: if a requested attribute (data attribute or method) is not found in the class, the search proceeds to look in the base class. This rule is applied recursively if the base class itself is derived from some other class.

> attributes (data attribute or method) may override attributes of their base class.

<br/>

NOTE:  Because methods have no special privileges when calling other methods of the same object, a method of a base class that calls another method defined in the same base class may end up calling a method of a derived class that overrides it.

<br/>

Python has two built-in functions that work with inheritance:

* Use `isinstance()` to check an instance’s type: `isinstance(obj, int)` will be True only if `obj.__class__` is `int` or some class derived from `int`.

* Use `issubclass()` to check class inheritance: `issubclass(bool, int)` is `True` since `bool` is a subclass of `int`. However, `issubclass(float, int)` is `False` since `float` is not a subclass of `int`.

<br/>

## Multiple Inheritance
---
A class definition with multiple base classes looks like this:
```python
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

For most purposes, in the simplest cases, you can think of ***the search for attributes inherited from a parent class as depth-first, left-to-right, not searching twice in the same class where there is an overlap in the hierarchy.*** Thus, if an attribute is not found in DerivedClassName, it is searched for in Base1, then (recursively) in the base classes of Base1, and if it was not found there, it was searched for in Base2, and so on.
