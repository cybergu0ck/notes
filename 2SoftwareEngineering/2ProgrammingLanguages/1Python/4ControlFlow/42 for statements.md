
Python’s `for` statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence.

```python
# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, end = '\t')

#> cat  window  defenestrate
```

iterating using more than 1 variable
```python
results = [('ramesh',100), ('tate',69), ('bil',0)]

for name, marks in results:
    print(f'{name} has scored {marks} in the exam.')

#>ramesh has scored 100 in the exam. 
#>tate has scored 69 in the exam. 
#>bil has scored 0 in the exam.
```


### Iterating over collections while modifying it
---
Code that modifies a collection while iterating over that same collection can be tricky to get right. Instead, it is usually more straight-forward to loop over a ___copy of the collection___ or to ___create a new collection___:

Suppose we want to delete inactive users from this dictionary.
```python
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

for user, status in users.items():
    if status == 'inactive':
        del users[user]
        
#>RuntimeError: dictionary changed size during iteration
```

Instead, we can iterate over a copy of the dictionary as follows:
```python
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

print(users)

#>{'Hans': 'active', '景太郎': 'active'}
```

We can also create a new dictionary:
```python
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

active_users = {}

for user, status in users.items():
    if status == 'active':
        active_users[user] = status
active_users

#>{'Hans': 'active', '景太郎': 'active'}
```


### Using __`range()`__ and __`len()`__ functions in loops
---
```syntax
range(start, end, step)

start: The value of the start parameter (or `0` if the parameter was not supplied)
stop: The value of the stop parameter
step: The value of the step parameter (or `1` if the parameter was not supplied)

```

> The arguments to the range constructor must be integers (either built-in [`int`](https://docs.python.org/3/library/functions.html#int "int") or any object that implements the [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__") special method).

```python
nums = [1,2,3,4,5]

for index in range(len(nums)):
    print(nums[index], end='\t')

#> 1   2   3   4   5
```

```python
nums = [0,1,2,3,4,5]

for index in range(2,4):             #It is exclusive of 'stop' parameter in range
    print(nums[index], end='\t')

#> 2   3
```

```python
nums = [0,1,2,3,4,5]

for index in range(len(nums)-1, -1, -1):   #Reverse order
    print(nums[index], end='\t')

#>5  4  3  2  1  0
```


### using __`enumerate()`__ in loops
---

```syntax
enumerate(iterable, start=0)


equvivalent to:

def enumerate(iterable, start=0):
    n = start
    for elem in iterable:
        yield n, elem
        n += 1
```

```python
seasons = ['Spring', 'Summer', 'Fall', 'Winter']

print(list(enumerate(seasons)))             #If list() is not used then it returns enumerate object.
print(list(enumerate(seasons, start=1)))

#>[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
#>[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

```

```python
myList = ['a','b','c']

for index,value in enumerate(myList):
    print(index, value)
    
#>0 a
#>1 b
#>2 c
```

```python
myDict = {'apple':1, 'ball':2, 'cat':3000}

for index, value in enumerate(myDict):
    print(index, value)

#>0 apple
#>1 ball
#>2 cat
```

