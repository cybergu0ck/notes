
- Using OOP in Python, we can restrict access to methods and variables. This prevents data from direct modification which is called encapsulation.
- The basic idea of Encapsulation is to wrap up both data and methods into one single unit.
- Encapsulation in other programming languages have public, private and protected members.

	| Data | Access from Class |  Access from Derived Class | Access from Object |
	|---|---|---|---|
	|Private member      |       Yes        |         No                  |        No          |
	|Protected member    |       Yes        |         Yes                 |        No          |
	|Public member       |       Yes        |         Yes                 |        Yes         |


- “Private” instance variables that cannot be accessed except from inside an object don’t exist in Python.
- However, there is a convention that is followed by most Python code: a name prefixed with an underscore (e.g. `_spam`) should be treated as a non-public part of the API (whether it is a function, a method or a data member).

<br/>

```python
# _attr is just a convention and It can be accessed and modified anywhere in the code.

class Product:
    def __init__(self, price):
        self._price = price   # Just a convention
    
    def sell(self):
        print(f'Product sold for {self._price}')
    
    def setPrice(self, newPrice):
        self._price = newPrice

computer = Product(1000)
computer._price = 2000
print(computer._price)      

#>2000
```

<br/>

```python
#Cannot access, modify __attr anywhere other than inside the class (Technically incorrect as we ca nuse name mangling)

class Product:
    def __init__(self, price):
        self.__price = price   # Just a convention
    
    def sell(self):
        print(f'Product sold for {self.__price}')
    
    def setPrice(self, newPrice):
        self.__price = newPrice

computer = Product(1000)
print(computer.__price)      

#>AttributeError: 'Product' object has no attribute '__price'
```

<br/>
<br/>

### Name Mangling

- Since there is a valid use-case for class-private members (namely to avoid name clashes of names with names defined by subclasses), there is limited support for such a mechanism, called _name mangling_. Any identifier of the form `__spam` (at least two leading underscores, at most one trailing underscore) is textually replaced with `_classname__spam`, where `classname` is the current class name with leading underscore(s) stripped. This mangling is done without regard to the syntactic position of the identifier, as long as it occurs within the definition of a class.
- The name mangling is created on an identifier by `_classname__datamember`

```python
class Product:
    def __init__(self, price):
        self.__price = price   # Just a convention
    
    def sell(self):
        print(f'Product sold for {self.__price}')
    
    def setPrice(self, newPrice):
        self.__price = newPrice

computer = Product(1000)
print(computer._Product__price)  #Name Mangling    

#>1000
```




<br/>
<br/>
<br/>


# Polymorphism

- Polymorphism is the ability of a variable, function, or object to take on multiple forms. 
- It refers to the use of a single type entity (method, operator or object) to represent different types in different scenarios.

<br/>

## 2.a Polymorphisim of Operators 

Another kind of built-in polymorphism in Python is the ability to override an operator in Python depending upon the operands used.

- '+' is used for arithmetic addition when used with numbers and as concatination when used with strings.

<br/>

## 2.b Polymorphism of Functions (Overloading Functions)

Overloading Built in functions :
- len() can be used with different data types like list, tuple, string  


Overloading User Defined Functions :
- Python doesn't support conventional C++ function overloading, it considers the latest function signatures.
	1. the workaround for that is to use default arguments with "None".
		```python
		class Student:
		    def hello(self, name=None):
		        if name is not None:
		            print('Hey ' + name)
		        else:
		            print('Hey ')
		
		
		std = Student()
		
		std.hello()
		
		std.hello('Nicholas')  #same function but diff behaviour

		#>Hey 
		#Hey Nicholas
		```

	2. function overloading using different classes (Illusration 2)
		```python
		class Dog:
		    def speak(self):
		        print('Woof Roof')
		
		class Cat:
		    def speak(self):
		        print('Meow')
		
		myDog = Dog()
		myCat = Cat()
		
		for animal in (myDog, myCat):
		    animal.speak()
		    
		#>Woof Roof
		#>Meow
		```

	3. method overloading using inheritence (Illustration 3)
		```python
		class Parent:
		    def foo(self):
		        print ('Coming hot from Parent Class')
		
		class Child(Parent):
		    def foo(self):
		        print('coming hot from Child class')
		
		parentObj = Parent()
		parentObj.foo()
		
		childObj = Child()
		childObj.foo()

		#Coming hot from Parent Class
		#coming hot from Child class
		```