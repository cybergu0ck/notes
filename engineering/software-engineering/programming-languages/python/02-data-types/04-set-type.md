# Python set

1. Sets are one among the 4 built in datatypes to store collection of data. (other 3 are tuple, list, dict)
1. Sets are mutable.
1. Sets are unordered (No index).
1. Sets contain unique items, hence no duplicates.
1. Sets can have items of different datatypes, but those datatypes must be hashable.

# Creating sets

- Using curly braces

  ```python
  a = 10
  mySet = {100,'abc',a}
  print(mySet)

  #>{10, 100, 'abc'}
  ```

- Using set() function
  ```python
  mySet2 = set({1, 'abs'})
  print(mySet2)

      #>{1, 'abs'}
      ```

  <br/>

# Meaning of Hashable

An object is hashable if it has a hash value which never changes during its lifetime (it needs a hash() method), and can be compared to other objects (it needs an eq() or cmp() method). Hashable objects which compare equal must have the same hash value.

Hashability makes an object usable as a dictionary key and a set member, because these data structures use the hash value internally.

All of Python’s immutable built-in objects are hashable, while no mutable containers (such as lists, dictionaries, sets) are. Objects which are instances of user-defined classes are hashable by default; they all compare unequal, and their hash value is their id().

```python
not_a_set = {1,2,('a',1), ['a',1]}  #the tuple is hashable, while a list is not
print(not_a_set)

#> TypeError: unhashable type: 'list'
```

<br/>

# Accesing items from a set

Cannot be accesed using index as they are unordered.

```python
# Type casting

mySet = {100,'abc',None}
print(list(mySet)[0])

#>100
```

```python
# can directly check is item in present in set or not.
mySet = {100,'abc',None}
print(100 in mySet)

#>True
```
