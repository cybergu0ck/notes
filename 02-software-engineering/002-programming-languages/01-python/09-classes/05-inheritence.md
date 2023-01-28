
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
    def __init__(self,name, environment):
        self.name = name
        self.environment = environment
    
    def getenvironment(self):
        print(f'{self.name} likes {self.environment} environment.')

class Dog(Animal):
    def __init__(self, name, environment, breed):
        super().__init__(name,environment)      #Initialising environment attribute from super class, No need for "self" and ":"
        self.breed = breed

class Bird(Animal):
    def __init__(self,name):
        super().__init__(name, 'Air')   #'Air' is passed into environment parameter in init of super class!


myDog = Dog('Cooper','Land', "Pom")
myBird = Bird('Rio')      # This may look like Bird class has only 1 data attribute but that's not the case.
myDog.getenvironment()
myBird.getenvironment()

'''
See how we can skip the parameter from the parameter list of the child-class.
We can create a data attribute by directly initailising it from the parent class.
Since all birds (excluding exclusions) are air based, we can directly pass that in the super().__init__()
'''

#>Cooper likes Land environment.
#>Rio likes Air environment.
```



- When the class object is constructed, the base class is remembered. This is used for resolving attribute references: if a requested attribute (data attribute or method) is not found in the class, the search proceeds to look in the base class. This rule is applied recursively if the base class itself is derived from some other class.

- attributes (data attribute or method) may override attributes of their base class.

<br/>
<br/>

### Understanding super() 

The super() builtin returns a proxy object (temporary object of the superclass) that allows us to access methods of the base class.

```python
class Parent:
    def __init__(self):
        pass

    def parentFunc(self):
        print ('Tis a parent func')

class Child(Parent):
    def trynaAccessParent(self):
        super().parentFunc()    #Here super() returns a temporary Parent object which then is used to access parentFunc.
    
me = Child()
me.trynaAccessParent()

'''same can be obtained by simply using me.parentFunc() but the above is done to demo super()'''

#>Tis a parent func

```

<br/>
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

- For most purposes, in the simplest cases, you can think of ***the search for attributes inherited from a parent class as depth-first, left-to-right, not searching twice in the same class where there is an overlap in the hierarchy.*** Thus, if an attribute is not found in DerivedClassName, it is searched for in Base1, then (recursively) in the base classes of Base1, and if it was not found there, it was searched for in Base2, and so on.

- In fact, it is slightly more complex than that; the method resolution order changes dynamically to support cooperative calls to [`super()`](https://docs.python.org/3/library/functions.html#super "super")

<br/>

```python
'''Explanation can be found on https://www.programiz.com/python-programming/methods/built-in/super'''

class Animal:
  def __init__(self, Animal):
    print(Animal, 'is an animal.');

class Mammal(Animal):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
    super().__init__(mammalName)
    
class NonWingedMammal(Mammal):
  def __init__(self, NonWingedMammal):
    print(NonWingedMammal, "can't fly.")
    super().__init__(NonWingedMammal)

class NonMarineMammal(Mammal):
  def __init__(self, NonMarineMammal):
    print(NonMarineMammal, "can't swim.")
    super().__init__(NonMarineMammal)

class Dog(NonMarineMammal, NonWingedMammal):
  def __init__(self):
    print('Dog has 4 legs.');
    super().__init__('Dog')
    
d = Dog()
print('')
bat = NonMarineMammal('Bat')


#>Dog has 4 legs.
#>Dog can't swim.
#>Dog can't fly.
#>Dog is a warm-blooded animal.
#>Dog is an animal.
#>
#>Bat can't swim.
#>Bat is a warm-blooded animal.
#>Bat is an animal.
```

<br/>
<br/>

### Method Resolution Order (MRO)


Method Resolution Order (MRO) is the order in which methods should be inherited in the presence of multiple inheritance. You can view the MRO by using the __mro__ attribute.

- A method in the derived calls is always called before the method of the base class. In our example, Dog class is called before NonMarineMammal or NoneWingedMammal. These two classes are called before Mammal, which is called before Animal, and Animal class is called before the object.
- If there are multiple parents like Dog(NonMarineMammal, NonWingedMammal), methods of NonMarineMammal is invoked first because it appears first.

```python
class Animal:
  def __init__(self, Animal):
    print(Animal, 'is an animal.');

class Mammal(Animal):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
    super().__init__(mammalName)
    
class NonWingedMammal(Mammal):
  def __init__(self, NonWingedMammal):
    print(NonWingedMammal, "can't fly.")
    super().__init__(NonWingedMammal)

class NonMarineMammal(Mammal):
  def __init__(self, NonMarineMammal):
    print(NonMarineMammal, "can't swim.")
    super().__init__(NonMarineMammal)

class Dog(NonMarineMammal, NonWingedMammal):
  def __init__(self):
    print('Dog has 4 legs.');
    super().__init__('Dog')

print(Dog.__mro__)


#>(__main__.Dog, __main__.NonMarineMammal,__main__.NonWingedMammal,__main__.Mammal,__main__.Animal,object)
```