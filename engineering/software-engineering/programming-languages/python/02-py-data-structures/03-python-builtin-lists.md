- Lists are mutable.
- Lists items can be of different data types.

<br/>

# Creating Lists

```python
myList = [1, 'all', {'a':1}, ('a','b',1)]
print(myList)

#>[1, 'all', {'a': 1}, ('a', 'b', 1)]
```

<br/>

# Inserting Items

- `insert()` : Inserts a given element at a given index in a list.

  ```python
  myList = [1,2,3,4,5,6]
  myList.insert(0, 'Zero')
  print(myList)

  #>['Zero', 1, 2, 3, 4, 5, 6]
  ```

- `append()` : Insertion to the end of the list.

  ```python
  myList = [1,2,3,4,5,6]
  myList.append(7)
  print(myList)

  #>[1, 2, 3, 4, 5, 6, 7]
  ```

# Accessing Items

- Accessing a single item using index

  ```python
  myList = [1, 'all', {'a':1}, ('a','b',1)]
  print(myList[1])

  #>'all'
  ```

- Accesing multiple items using range notation

  ```python
  myList = [1, 'all', {'a':1}, ('a','b',1)]
  print(myList[0:1])

  #>[1]
  ```

  - We can use out of index numbers with this notation,

    ```python
    arr = [1,2,3,4]
    print(arr[6:])
    print(arr[:10])

    #>[]
    #>[1,2,3,4]
    ```

- Accesing last item using `pop()`

  ````python
  myList = [1, 'all', {'a':1}, ('a','b',1)]
  lastItem = myList.pop()
  print(lastItem)

      #>('a', 'b', 1)
      ```

  <br/>
  ````

# Deleting List Items

- `remove()` : Used to remove a specific item from a list.

  ```python
  myList = [1,2,3,4,5,6]
  myList.remove(3)
  print(myList)

  #>[1, 2, 4, 5, 6]
  ```

- `pop()` : Used to remove the last item or a specific item at a specific index

  ```python
  myList = [1,2,3,4,5,6]
  myList.pop()
  myList.pop(0)
  print(myList)

  #>[2, 3, 4, 5]
  ```

- `del` keyword : Used to remove a specific item at a specific index.

  ```python
  myList = [1,2,3,4,5,6]
  del myList[1]
  print(myList)

  #[1, 3, 4, 5, 6]
  ```

- `clear()` : to clear the entire list.

      ```python
      myList = [1,2,3,4,5,6]
      myList.clear()
      print(myList)

      #>[]
      ```

  <br/>

# Sorting Lists

- Using `sort()` method.

  ```python
  myList = [6,4,5,1,2,3]
  myList.sort()   # sort() method is inplace
  print(myList)

  #>[1, 2, 3, 4, 5, 6]
  ```

- Using `sorted()` function

  ```python
  myList = [6,4,5,1,2,3]
  sortedList = sorted(myList)    #sorted() function is not in place
  print(sortedList)

  #>[1, 2, 3, 4, 5, 6]
  ```

<br/>

# Unpacking List

If all items of a list were tuples of same len.

```python
myList = [('A',1),('B',2),('C',3),('D',4)]

for item1, item2 in myList:
    print(item1, item2)

#>A 1
#>B 2
#>C 3
#>D 4
```

```python
myList = [[1,2,3],['a','b','c']]

for i,j,k in myList:
    print(i,j,k)

#>1 2 3
#>a b c
```

<br/>

# List Comphrehension

```
variable = [expression for condition]
```

```python
var = [x for x in range(10)]
print(var)

#>[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

- Using only if inside comphrension, single if statement should follow for statement

  ```python
  evenNums = [x for x in range(5) if x%2 ==0]
  print(evenNums)

  #>[0, 2, 4]
  ```

- Using if else inside comphrensions,**_if else should lead the for statement_**

  ```python
  evenNums = [x if x%2 ==0 else 'Odd' for x in range(5)]
  print(evenNums)

  #>[0, 'Odd', 2, 'Odd', 4]
  ```

## An example of a Complex list comprehension

```python
#The conventional way

keyPlayers = ['Raze', 'Viper']
teamCombinations = [['Omen','KillJoy','Neon'],['Raze', 'Breach'], ['Raze','Reyna']]

res = []

for team in teamCombinations:
    for player in team:
        if player in keyPlayers:
            res.append(player)

print(res)

#>['Raze', 'Raze']
```

```python
# The same thing using list comprehension

keyPlayers = ['Raze', 'Viper']
teamCombinations = [['Omen','KillJoy','Neon'],['Raze', 'Breach'], ['Raze','Reyna']]

res = [player for team in teamCombinations for player in team  if player in keyPlayers]
orint(res)

# See that the order of for statements is similar to the conventional way!

#>['Raze', 'Raze']
```

<br/>

# list Methods

- `index()` : Returns the lowest index where the element appears.

  ```python
  myList = [1,2,3,4,5,6]
  print(myList.index(2))

  #>1
  ```

- `reverse()` : To get the reverse of the list.

  ```python
  myList = [1,2,3,4,5,6]
  myList.reverse()
  print(myList)

  #>[6, 5, 4, 3, 2, 1]
  ```

- `max()` : get the item with maximum value

  ```python
  myList = [6,4,5,1,2,3]
  res = max(myList)
  print(res)

  #>6
  ```

- `extend()`: extend the list

  ```python
  list1 = [1,2,3]
  list2 = ['a','b','c']

  list1.extend(list2)

  print(list1)

  #>[1, 2, 3, 'a', 'b', 'c']
  ```
