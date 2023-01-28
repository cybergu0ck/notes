
Objects have individuality, and multiple names (in multiple scopes) can be bound to the same object. ***This is known as aliasing in other languages.***

- This can be safely ignored when dealing with immutable basic types (numbers, strings, tuples). 
- The problem comes from a misunderstanding of what variables are in Python. If you're used to most traditional languages, you have a mental model of what happens in the following sequence:

```python
a = 1
a = 2
```

- You believe that `a` is a memory location that stores the value 1, then is updated to store the value 2. That's not how things work in Python. 

> ***A Python variable is a symbolic name that is a reference or pointer to an object.*** 

- Hence, `a` starts as a reference to an object with the value 1, then gets reassigned as a reference to an object with the value 2. Those two objects may continue to coexist even though `a` doesn't refer to the first one anymore; in fact they may be shared by any number of other references within the program.


Two different objects can have the same name!
```python
#use built in function id() which gives the identity of the object.

a = 1
print(id(a))

a = 2
print(id(a))

#>1429903638768
#>1429903638800
```
```
1429903638768  
1429903638800
```



Conversly, same object can have multiple names!
```python
a = 1
print(id(a))

b = 1
print(id(b))

#>1429903638768
#>1429903638768
```
<br/>

However, aliasing has a possibly surprising effect on the semantics of Python code involving mutable objects such as lists, dictionaries, and most other types. This is usually used to the benefit of the program, since aliases behave like pointers in some respects. For example, passing an object is cheap since only a pointer is passed by the implementation; and if a function modifies an object passed as an argument, the caller will see the change — this eliminates the need for two different argument passing mechanisms as in Pascal.