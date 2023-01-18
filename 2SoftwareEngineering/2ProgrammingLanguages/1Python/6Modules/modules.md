
## Module
---
* ___A module is a file containing Python definitions and statements.___
* The file name is the module name.
* Within a module, the module’s name (as a string) is available as the value of the global variable ```__name__```.
* It is an object that serves as an organizational unit of Python code.  
* Definitions from a module can be imported into other modules or into the main module

Consider the following myPackage for illustration, Here fibo.py and myCode.py are modules. myCode imports fibo module.
```
myPackage
    │   fibo.py
    │   myCode.py
    │   __init__.py
    
```

```python
#fibo.py
#-----------------------------------------------

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```


Import the entire module and use dot notation to access functions
```python
#myCode.py (import v1)
#-----------------------------------------------

import fibo
fibo.fib(4)

>0 1 1 2 3 
```


Import particular functions from a module.
```python
#myCode.py (import v2)
#-----------------------------------------------

from fibo import fib
fib(4)

>0 1 1 2 3 
```


Import everything from a module. (Not ideal as may result in namespace errors)
```python
#myCode.py (import v3)
#-----------------------------------------------

from fibo import *
fib(4)

>0 1 1 2 3 
```


import the module with an alias.
```python
#myCode.py (import v4)
#-----------------------------------------------

import fibo as Fibonacci
Fibonacci.fib(4)

>0 1 1 2 3 
```


Import a function with alias from a module.
```python
#myCode.py (import v5)
#-----------------------------------------------

from fibo import fib as Fibonacci
Fibonacci(4)

>0 1 1 2 3 
```


>  For efficiency reasons, each module is only imported once per interpreter session. ___Therefore, if you change your modules, you must restart the interpreter___ – or, if it’s just one module you want to test interactively, use importlib.reload(), e.g. import importlib; importlib.reload(modulename).



## Package
---
- Packages are a way of structuring Python’s module namespace by using “dotted module names”. ___Package is essentially a collection of modules.___
- Technically, a package is a Python module with a ```__path__``` attribute.


> _It’s important to keep in mind that all packages are modules, but not all modules are packages._ Or put another way, packages are just a special kind of module. Specifically, any module that contains a ```__path__``` attribute is considered a package.


> * When importing the package, Python searches through the directories on sys.path looking for the package subdirectory.
> * The ```__init__```.py files are required to make Python treat directories containing the file as packages. 
> * In the simplest case, ```__init__```.py can just be an empty file, but it can also execute initialization code for the package or set the ```__all__``` variable



### Regular Package
---
A traditional package, such as a directory containing an ```__init__```.py file.

### Namespace Package
---
- A PEP 420 package which serves only as a container for subpackages. Namespace packages may have no physical representation, and specifically are not like a regular package because they have no ```__init__```.py file.

- Note that names are case sensitive when importing.

> All names in Python are case-sensitive: variable names, function names, class names, module names, exception names. If you can get it, set it, call it, construct it, import it, or raise it, it's case-sensitive.

### Namespaces
---
- The place where a variable is stored. 
- Namespaces are implemented as dictionaries. 
- There are the local, global and built-in namespaces as well as nested namespaces in objects (in methods). 
- Namespaces support modularity by preventing naming conflicts. For instance, the functions ```__builtins.open__``` and ```__os.open()__``` are distinguished by their namespaces. Namespaces also aid readability and maintainability by making it clear which module implements a function. For instance, writing random.seed() or itertools.islice() makes it clear that those functions are implemented by the random and itertools modules, respectively.

Consider myPackage for illustration, myPackage is a package containing modules fibo, myCode and subpackages calc and greet.

```
myPackage
    │   __init__.py                     #Initialise myPackage
    │   fibo.py                         #Module
    │   myCode.py                       #Module
    │
    ├───calc                                #Subpackage
    │   │   functions.py
    │   │   __init__.py
    │   
    │
    ├───greet                               #Subpackage
        │   functions.py
        │   __init__.py
       
```


```python
#functions module present in calc subpackage
#-----------------------------------------------

def sum(*args) -> float:
    res = 0
    for num in args:
        res += num
    return res

class AdvancedCalc:
    def average(self,*args) -> float:
        sum, nums = 0, len(args)
        for num in args:
            sum += num
        return sum/nums
```

```python
#functions module present in greet subpackage
#-----------------------------------------------

def sayHello()-> str:
    """returns a greeting string """
    return "Hello user, hope you are doing amazing."
```

importing the functions submodule present in calc subpackage. It must be referenced with its full name.

```python
##myCode.py 
#-----------------------------------------------

import calc.functions
print(calc.functions.sum(1,2,3))

>6
```

Importing the submodule without referencing the package prefix.
```python 
##myCode.py  (alternate import)
#-----------------------------------------------

from calc import functions
print(functions.sum(1,2,3))

>6
```

Try to avoid above kind of import as it may lead to namespace conflicts, as shown below

```python
#myCode.py 
#-----------------------------------------------
from calc import functions
from greet import functions

print(functions.sayHello())
print(functions.sum(1,2))

>AttributeError: module 'greet.functions' has no attribute 'sum'
```


Importing the desired function or variable directly:
```python 
##myCode.py  (alternate import)
#-----------------------------------------------

from calc.functions import sum
print(sum(1,2,3))

>6
```

> * Note that when using ```from package import item```, the item can be either a submodule (or subpackage) of the package, or some other name defined in the package, like a function, class or variable. 
> * The import statement first tests whether the item is defined in the package; if not, it assumes it is a module and attempts to load it. If it fails to find it, an ImportError exception is raised.


### Relative Imports
---
Just don't use it, refer [stack overflow- how to do relative imports in python](https://stackoverflow.com/questions/72852/how-to-do-relative-imports-in-python)


### Import module from different directory using the sys module
---

Consider that we want to import something from module.py in main.py from the illustration below:

```
anotherPackage
   │   __init__.py
   │
   ├───subPackage1
   │   │   module.py
   │   │   __init__.py
   │   
   │
   └───subPackage2
       | main.py
       | __init__.py

```

```python
#module.py
#-----------------------------------------------

def doSomething():
    print("Doing something..")
```

```python
#main.py
#-----------------------------------------------

import sys
#print(sys.path)
#print('\n\n')


sys.path.append('D:\\Code\\Python\\PythonLearning\\Modules\\anotherPackage\\subPackage1')
#print(sys.path)

import module

module.doSomething()
```

> Refer [geeksforgeeks](https://www.geeksforgeeks.org/python-import-module-from-different-directory/) to find another method.