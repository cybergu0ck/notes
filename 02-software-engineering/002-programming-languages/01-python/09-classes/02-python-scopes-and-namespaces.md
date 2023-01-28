
# Python Namespaces


***A namespace is a mapping from names to objects.***

* Most namespaces are currently implemented as Python dictionaries, but that’s normally not noticeable in any way (except for performance), and it may change in the future.
* Examples of namespaces are: 
    * the set of built-in names (containing functions such as abs(), and built-in exception names); 
    * the global names in a module;
    * In a sense the set of attributes of an object also form a namespace. 
* The global namespace for a module is created when the module definition is read in; normally, module namespaces also last until the interpreter quits.

>The important thing to know about namespaces is that there is absolutely no relation between names in different namespaces; for instance, two different modules may both define a function maximize without confusion — users of the modules must prefix it with the module name.

The statements executed by the top-level invocation of the interpreter, either read from a script file or interactively, are considered part of a module called __main__, so they have their own global namespace. (The built-in names actually also live in a module; this is called builtins.)

<br/>
<br/>
<br/>

# Python Scope

***A scope is a textual region of a Python program where a namespace is directly accessible.***

At any time during execution, there are 3 or 4 nested scopes whose namespaces are directly accessible:

* The innermost scope, which is searched first, contains the local names

* The scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contain non-local, but also non-global names

* The next-to-last scope contains the current module’s global names

* The outermost scope (searched last) is the namespace containing built-in names

```python
# global scope

def outer_func():

    # enclosing scope

    def inner_func():

        # local scope

        return None

    inner_func()
    return None

print('something')
```

A special quirk of Python is that – if no global or nonlocal statement is in effect – assignments to names always go into the innermost scope.

> ***Assignments do not copy data — they just bind names to objects.*** 

The same is true for deletions: the statement `del` x removes the binding of x from the namespace referenced by the local scope.

The `global` statement can be used to indicate that particular variables live in the global scope and should be rebound there; 

The `nonlocal` statement indicates that particular variables live in an enclosing scope and should be rebound there.


Look at this code to understand scope.
```python
x = "Jungle"

def outer_func():
    """This is the enclosing function."""
    x = "Logic"

    def inner_func():
        """This is the local function."""
        x = "Justin Timberlake"

        print(f'the vale of x: {x} and has {id(x)}')

    inner_func()
    print(f'the vale of x: {x} and has {id(x)}')

outer_func()
print(f'the vale of x: {x} and has {id(x)}')
```
```
the vale of x: Justin Timberlake and has 2339254066176
the vale of x: Logic and has 2339248242416
the vale of x: Jungle and has 2339253146032
```


```python
x = "Jungle"

def func():
    x = "Logic" # Here, it changed the x (present in global scope) to "Logic"
    
func()
print(x)
```
```
Jungle
```
  

Using `global` keyword:

```python
x = "Jungle"

def func():
    global x    # It means that we are refering to the 'x' in global space.
    x = "Logic" # Here, it changed the x (present in global scope) to "Logic"
    
func()
print(x)
```
```
Logic
```
Using `nonlocal` kwyword:

```python
x = "Jungle"

def outer_func():
    """This is the enclosing fucntion."""
    x = "Logic"

    def inner_func():
        """This is the local function."""
        nonlocal x # This means we are refering to the x of the enclosing scope.
        x = "Justin Timberlake"
    
    inner_func()  #No use as "Justin Timberlake" is limited to the local scope of inner_func
    print(x)

outer_func()
```
```
Justin Timberlake
```

If you can tell the output of the following code without looking at it then gg.

```python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```
```
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
```

`Builtins` is the last scope that is searched last. One thing to note here is that if we use the names that are bounded to builtin namespace in our global or enclosing or local scopes then it might lead to errors (when we call builtin functions)

The properties and methods present in buitlin module are 
```python
import buitlins
print(dir(builtins))
```

Noob error would be 
```python
collection = [1,2,3,4]

# we are using the name min in our global scope, which is actually present in the builtins namespace. 
def min():
    pass  

least = min(collection)
least
```
```
TypeError: min() takes 0 positional arguments but 1 was given
```

```python
collection = [1,2,3,4] 

min = min(collection)  #DINOT name variables with the name present in builtin namespace.
print(min)
```
```
TypeError: min() takes 0 positional arguments but 1 was given
```