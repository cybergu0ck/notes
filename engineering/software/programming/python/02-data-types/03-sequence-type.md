# 1. Python lists

- lists are mutable.
- lists items can be of different data types.

<br/>
<br/>

## Creating lists

```python
myList = [1, 'all', {'a':1}, ('a','b',1)]
print(myList)

#>[1, 'all', {'a': 1}, ('a', 'b', 1)]
```

<br/>
<br/>

## Inserting Items

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

<br/>
<br/>

## Accessing Items

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

  ```python
  myList = [1, 'all', {'a':1}, ('a','b',1)]
  lastItem = myList.pop()
  print(lastItem)

  #>('a', 'b', 1)
  ```

<br/>
<br/>

## Deleting list Items

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
<br/>

## Sorting lists

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
<br/>

## Unpacking list

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
<br/>

## list Comphrehension

- The template for list comprehension is:

  ```
  new_list = [new_item for item in list]    #no conditions
  new_list = [new_item for item in list if condition]   #if condition only
  new_list = [new_item if condition else another_item for item in list ]   #if else condition
  ```

* An example of a simple list comprehension. (no condition)

  ```python
  var = [x for x in range(10)]
  print(var)

  #>[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  ```

- An example of a list comprehension with if condition. _The if statement should follow the for statement._

  ```python
  evenNums = [x for x in range(5) if x%2 ==0]
  print(evenNums)

  #>[0, 2, 4]
  ```

- An example of a list comprehension with if-else condition. _The if-else statement should lead the for statement._

  ```python
  evenNums = [x if x%2 ==0 else 'Odd' for x in range(5)]
  print(evenNums)

  #>[0, 'Odd', 2, 'Odd', 4]
  ```

* An example of a complex nested list comprehension.

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
<br/>

## list Methods

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

<br>
<br>
<br>
<br>

# 2. Python tuples

One among the 4 built in data types to store collection of data. (Other 3 are set, list and dict)

1. tuples are unmutable.
1. tuples are indexed. i.e. items in tuples are ordered.
1. tuples can contain duplicate Items.
1. tuple items can of be different datatypes.

<br>
<br>

## Creating tuples

- tuples are created using paranthesis.
  ```py
  myTup = (1, 'daf', True, 1)
  ```

<br>
<br>

## Inserting items into a tuple

As tuple is unmutable, we do not have append() or insert() methods. We create a new tuple when we modify it.

<br>

1. tuple concatenation using `+` operator

   ```py
   myTup = (1,2)
   myTup = myTup + ('z',)  # , is a must in this case else python will consider ('z') as str!
   print(myTup)

   #> (1, 2, 'z')
   ```

<br>

2. Unpacking inside a tuple

   ```py
   a = (1,2)
   b = 'z'
   new = (*a, b)   #THIS IS INTERSTING
   new

   #> (1, 2, 'z')
   ```

3. By Type Casting

   ```py
   a = (1,2)

   a = list(a)   #type casting into a list
   a.append('z')

   a = tuple(a)  # type casting back to a tuple
   print(a)

   #>(1, 2, 'z')
   ```

- Essentially by inserting items we are not modifying the tuple but rather a new tuple object is created every time we do some modification, hence we say tuples are immutable.

  ```py
  # id()  is an integer which is guaranteed to be unique and constant for this object during its lifetime.

  myTup = (1,2)
  print(id(myTup))

  myTup = myTup + ('z',)
  print(id(myTup))

  print('We can see that the id\'s are different')

  #>2146782040960
  #>2146803711872
  #>We can see that the id's are different
  ```

<br>
<br>

## Accesing items in tuple

- Accesing single item

  ```py
  myTup = (1,2,3,1,2)
  print(myTup[1])

  #>2
  ```

- Accesing multiple items

  ```py
  myTup = (1,2,3,4,1,2,3)
  print(myTup[0:2])

  #>(1, 2)
  ```

- Illustration for concept clarity

  ```py
  # for concept clarity [startIndex(included) : endIndex(exclusive) : step(default = 1)]

  thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
  print(thistuple[:-1])
  print(thistuple[-4:-1])
  print(thistuple[-2:])
  print(thistuple[::-1]) #Reverses the entire thing

  #>('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon')
  #>('orange', 'kiwi', 'melon')
  #>('melon', 'mango')
  #>('mango', 'melon', 'kiwi', 'orange', 'cherry', 'banana', 'apple')
  ```

<br>
<br>

## Deleting Items from a tuple

- Removing last item using manipulation

  ```py
  tup = (1,2,3,4,5)
  tup = tup[:-1]
  print(tup)

  #>(1, 2, 3, 4)
  ```

- Type casting

  ```py
  tup = (1,2,3,4,5)

  tup = list(tup)
  tup.pop(1)

  tup = tuple(tup)
  print(tup)

  #>(1, 3, 4, 5)
  ```

<br>
<br>

## Unpacking tuples

- It is done as shown here

  ```py
  fruits = ("apple", "banana", "cherry")

  red, yellow, purple = fruits
  print(red)

  #>'apple'
  ```

<br>
<br>

## \* Operator

- If the number of variables is less than the number of values, you can add an \* to the variable name and the values will be assigned to the variable as a list:

  ```py
  fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

  green, yellow, *red = fruits

  print(green)
  print(yellow)
  print(red)

  #>apple
  #>banana
  #>['cherry', 'strawberry', 'raspberry']
  ```

  ```py
  # if * is used on varible other than the last one, it'll do this
  (green, *tropic, red) = fruits

  print(green)
  print(tropic)
  print(red)

  #apple
  #['banana', 'cherry', 'strawberry']
  #raspberry
  ```

<br>
<br>
<br>
<br>

# 3. range
