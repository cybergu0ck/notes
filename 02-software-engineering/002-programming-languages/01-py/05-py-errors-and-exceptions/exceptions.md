# Errors in Python

A python program terminates as soon as it encounters an unhandled error. These errors can be broadly classified into two classes:

1. Syntax errors
2. Logical errors (Exceptions)

## Syntax Errors
---

Error caused by not following the proper structure (syntax) of the language is called syntax error or parsing error.


## Logical errors (Exceptions)
---

Errors that occur at runtime (after passing the syntax test) are called exceptions or logical errors.

Examples are
- ZeroDivisionError
- FileNotFoundError
- KeyError


Check out this website to know about all the built in exceptions  
https://www.programiz.com/python-programming/exceptions


#### "*We can handle these built-in and user-defined exceptions in Python*"


### B. Built in Exceptions

* In Python, exceptions can be handled using a try statement.
* The critical operation which can raise an exception is placed inside the try clause. 
* The code that handles the exceptions is written in the except clause.
- Syntax is 
- 
```
try:
	block

except Exception:
    block
```


```python
try :
    num = 10/0
    print(num)

except Exception:   #here Exception is not defined, so the code catches all the errors in try block and handles them same.
    print("Can't divide by Zero.")

>Can't divide by Zero.
```

```python
try:
    num = var 

except ZeroDivisionError: # See how the code only catches ZeroDivisonError and other errors are not handled.
    print("Can not divide by zero.")

>NameError                                 Traceback (most recent call last)
Cell In [11], line 2
      1 try:
----> 2     num = var 
      4 except ZeroDivisionError:
      5     print("Can not divide by zero.")

NameError: name 'var' is not defined
```

* It is a good programming practice to specify which exceptions an except clause should catch. 
* A try clause can have any number of except clauses to handle different exceptions, however, only one will be executed in case an exception occurs

```python
import math 

try:
    num = math.sqrt(-1)

except ValueError:
    print(" ValueError has occured, check the values of the parameters being passed in your functions")
    pass

except ZeroDivisionError:
    print("ZeroDivisonError has occured, check if you are dividing by zero")
    pass

except:
    print("Error other than ValueError and ZeroDivisionError")
    pass
```

```
```Output
ValueError has occured, check the values of the parameters being passed in your functions
```



```
### Raising Exceptions in Python
---

We can raise exceptions ourself

```python
frens = ('Nes4Dinner', 'Verbie', 'Deshat', 'SaintAlucard')

try:
    newGuy = 'koustubh'
    if newGuy not in frens:
        raise Exception
except Exception:
    print('Not my fren, shoo off')

>Not my fren, shoo off
```


```python
try:
     a = -10
     if a <= 0:
         raise ValueError("That is not a positive number!")
except ValueError as ve:
     print(ve)

>That is not a positive number!

```



### The "Else" with Try Except
---

- The block of code in the else statement right after try except will be excuted only if no exceptions are raised in try block. If ther try block if clean and free of exceptions then the else block will execute.
- Exceptions, if present in else block will not be caught not handled.

```python
try:
    num = 3
    assert num % 2 == 0
except:
    print("Not an even number!")
else:  # Else block will not be executed in this code.
    reciprocal = 1/num
    print(reciprocal)

>Not an even number!

```

```python
try:
    num = 2
    assert num % 2 == 0
except:
    print("Not an even number!")
else:  # Else block will be executed in this code.
    reciprocal = 1/num
    print("The reciprocal of {} is {}.".format(num,reciprocal))

>The reciprocal of 2 is 0.5.
```

```python
try:
    num = 0
    assert num % 2 == 0

except Exception:
    print("Not an even number!")
    
else:  # Exceptions in else block are not caught nor handled
    reciprocal = 1/num
    print("The reciprocal of {} is {}.".format(num,reciprocal))
```
    
```Output
ZeroDivisionError                         Traceback (most recent call last)
Cell In [29], line 9
6     print("Not an even number!")
8 else:  # Exceptions in else block are not caught nor handled
----> 9     reciprocal = 1/num
10     print("The reciprocal of {} is {}.".format(num,reciprocal))

ZeroDivisionError: division by zero
```



### The "finally" block in try except
---
The finally block will be executed after the try except block and it doesn't depend on exceptions in try block.

```python
frens = ('Nes4Dinner', 'Verbie', 'Deshat', 'SaintAlucard')

try:
    newGuy = 'koustubh'
    if newGuy not in frens:
        raise Exception
except Exception:
    print('You have failed the fren test. Do I know you?')
else:
    print('You have passed the fren test. Whatup my man {}'.format(newGuy))
finally:
    print('...Thank you for participating')

>You have failed the fren test. Do I know you?
>...Thank you for participating

```

```python
frens = ('Nes4Dinner', 'Verbie', 'Deshat', 'SaintAlucard')

try:
    newGuy = 'Nes4Dinner'
    if newGuy not in frens:
        raise Exception
except Exception:
    print('You have failed the fren test. Do I know you?')
else:
    print('You have passed the fren test. Whatup my man {}?'.format(newGuy))
finally:
    print('...Thank you for participating')

>You have passed the fren test. Whatup my man Nes4Dinner?
>...Thank you for participating

```