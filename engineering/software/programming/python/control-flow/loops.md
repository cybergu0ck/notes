# Loops

<br>
<br>
<br>

## For Loops

<br>
<br>

### looping over a collection

Python’s `for` statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence.

```python
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, end = '\t')

#> cat  window  defenestrate
```

- For loop with unpacking.

  ```python
  results = [('ramesh',100), ('tate',69), ('bil',0)]

  for name, marks in results:
      print(f'{name} has scored {marks} in the exam.')

  #>ramesh has scored 100 in the exam.
  #>tate has scored 69 in the exam.
  #>bil has scored 0 in the exam.
  ```

<br>

#### Looping over a collection with modification

- Code that modifies a collection while iterating over that same collection can be tricky to get right. Instead, it is usually more straight-forward to loop over a **_copy of the collection_** or to **_create a new collection_**.

- Suppose we want to delete inactive users from this dictionary.

  ```python
  users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

  for user, status in users.items():
      if status == 'inactive':
          del users[user]
         
  #>RuntimeError: dictionary changed size during iteration
  ```

- Instead, we can iterate over a copy of the dictionary as follows:

  ```python
  users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

  for user, status in users.copy().items():
      if status == 'inactive':
          del users[user]

  print(users)

  #>{'Hans': 'active', '景太郎': 'active'}
  ```

<br>
<br>

### For loop using range and len function

- The syntax of `range()`

  ```
  range(start, end, step)
  ```

  - start: The value of the start parameter (or `0` if the parameter was not supplied)
  - stop: The value of the stop parameter
  - step: The value of the step parameter (or `1` if the parameter was not supplied)

- Examples :

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

<br>
<br>

### Enumerated for loops

- ```python
  seasons = ['Spring', 'Summer', 'Fall', 'Winter']

  print(list(enumerate(seasons)))             #If list() is not used then it returns enumerate object.
  print(list(enumerate(seasons, start=1)))

  #>[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
  #>[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

  ```

- ```python
  myList = ['a','b','c']

  for index,value in enumerate(myList):
      print(index, value)

  #>0 a
  #>1 b
  #>2 c
  ```

- ```python
  myDict = {'apple':1, 'ball':2, 'cat':3000}

  for index, value in enumerate(myDict):
      print(index, value)

  #>0 apple
  #>1 ball
  #>2 cat
  ```

<br>
<br>
<br>

## While loops

<br>
<br>

## Break statement

`break` is used to terminate an ongoing loop.

```python
users = {'Éléonore': 'inactive','Hans': 'active', '景太郎': 'active'}

inactive_count = 0

for user, status in users.items():
    if status == 'active':
        print("active users found, do not perform maintainence")
        break                           #breaks entirely out of the for loop
    else:
        inactive_count += 1

if inactive_count == len(users):
    print("All users are inasctive, perform maintenance.")

#>active users found, do not perform maintainence
```

<br>
<br>
<br>

## Continue statement

`continue` is used to skip an interation in an ongoing loop.

```python
odd_nums = []

for num in range(10):
    if num%2 ==0:
        continue          #skips this iteration and starts the next iteration.
    odd_nums.append(num)

print(odd_nums)

#> [1, 3, 5, 7, 9]
```

<br>
<br>
<br>

## Else after loops

- The `else` block just after for/while is executed only when the loop is NOT terminated by a `break` statement.

- Making everyone inactive in the above illustration.

  ```python
  users = {'Éléonore': 'inactive','Hans': 'inactive', '景太郎': 'inactive'}

  for user, status in users.items():
      if status == 'active':
          print("active users found, do not perform maintainence")
          break                           #breaks entirely out of the for loop
  else:
      print("All users are inactive, perform maintenance.")

  #>All users are inasctive, perform maintenance.
  ```

- Same code present above but using while loop (just shows how choosing the right loop makes the job so easy)

  ```python
  users = {'Éléonore': 'inactive','Hans': 'inactive', '景太郎': 'inactive'}

  enumerated = list(enumerate(users))  #[(0, 'Éléonore'), (1, 'Hans'), (2, '景太郎')]
  index = 0

  while index in (0,len(users)-1):
      if users[enumerated[index][1]] == 'active':
          print("active users found, do not perform maintainence")
          index += 1
          break
      else:
          index+=1
  else:
      print("All users are inactive, perform maintenance.")

  #>All users are inasctive, perform maintenance.
  ```
