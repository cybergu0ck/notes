# Python Tuples

One among the 4 built in data types to store collection of data. (Other 3 are set, list and dict)

1. Tuples are unmutable.
1. Tuples are indexed. i.e. items in tuples are ordered.
1. Tuples can contain duplicate Items.
1. Tuple items can of be different datatypes.

<br>
<br>

# Creating Tuples

- Tuples are created using paranthesis.
  ```py
  myTup = (1, 'daf', True, 1)
  ```

<br>
<br>

# Inserting items into a Tuple

As tuple is unmutable, we do not have append() or insert() methods. We create a new tuple when we modify it.

<br>

1. Tuple concatenation using `+` operator

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

# Accesing items in Tuple

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

# Deleting Items from a Tuple

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

# Unpacking tuples

- It is done as shown here

  ```py
  fruits = ("apple", "banana", "cherry")

  red, yellow, purple = fruits
  print(red)

  #>'apple'
  ```

<br>
<br>

# \* Operator

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
