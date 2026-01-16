# Sets

A set is an unordered collection of unique elements in Python.

- Sets do not allow duplicate values.
- Sets are unordered as they do not contain indexing.
- Sets are mutable.
- Sets can have items of different datatypes, but those datatypes must be hashable.

<br>
<br>
<br>

## Set creation

- Using curly braces.

  ```python
  a = 10
  mySet = {100,'abc',a}
  print(mySet)

  #>{10, 100, 'abc'}
  ```

- Using `set` function.

  ```python
  mySet2 = set({1, 'abs'})
  print(mySet2)

  #>{1, 'abs'}
  ```

<br>
<br>
<br>

## Criteria for set item

An item can be a member of a set if it is [hashable](#hashability).

- Common hashable types that can be items of a set:
  - Numbers: int, float, complex
  - Strings: str
  - Tuples (if they contain only hashable elements)
  - Frozen sets: frozenset
  - Booleans: bool
  - Instances of user defined classes.
  - None

* Few non-hashable types that can't be items of a set:

  - Lists: list
  - Dictionaries: dict
  - Sets: set
  - Other mutable objects

* Note that a tuple is hashable while a list is not.

  ```python
  not_a_set = {1,2,('a',1), ['a',1]}  #the tuple is hashable, while a list is not
  print(not_a_set)

  #> TypeError: unhashable type: 'list'
  ```

<br>
<br>

### Hashability

An object is "hashable" if it has a hash value which never changes during its lifetime (has `hash` method) and can be compared to other objects (has `eq` or `cmp` method).

- Hashable objects which compare equal must have the same hash value.
- Hashability makes an object usable as a dictionary key and a set member, because these data structures use the hash value internally.
- All of Python’s immutable built-in objects are hashable.
- None of mutable containers (such as lists, dictionaries, sets) are hashable.
- Objects which are instances of user-defined classes are hashable by default; they all compare unequal, and their hash value can be checked using `id` method.

<br>
<br>
<br>

## Set comprehension

Set comprehension is a concise way to create sets in Python using a single line of code with a loop and optional conditions.

- Set comprehensions with basic loop

  ```py
  squares = {x**2 for x in range(5)} # Square numbers from 0 to 4
  # Result: {0, 1, 4, 9, 16}


  ```

- Set comprehensions with conditional filtering.

  ```py
  numbers = [1, 2, 3, 4, 5, 6]
  evens = {x for x in numbers if x % 2 == 0} # Even numbers from a list
  # Result: {2, 4, 6}

  numbers = {x for x in range(20) if x % 2 == 0 or x % 3 == 0} # Numbers divisible by 2 or 3
  # Result: {0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18}
  ```

- Set comprehensions with conditional expression (contains if-else).

  ```py
  numbers = {x if x % 2 == 0 else x * 10 for x in range(6)} # Even numbers stay the same, odd numbers multiply by 10
  # Result: {0, 2, 4, 10, 30, 50}
  ```

- Set comprehensions with both conditonal expression and conditional filtering.

  ```py
  # Transform with if-else, then filter with if
  result = {x if x % 2 == 0 else x * 10 for x in range(10) if x > 3} # Only keeps x > 3, then applies the if-else transformation
  # Result: {4, 6, 8, 50, 70, 90}
  ```

- Set comprehensions with nested loops.

  ```py
  # Pairs from two lists
  pairs = {(x, y) for x in [1, 2] for y in ['a', 'b']}
  # Result: {(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')}
  ```

<br>
<br>
<br>

## Set operators

Sets support mathematical set operations using both operators and methods.

<br>
<br>

### Union

`|` or `union()` combines all the elments from both sets without duplicates.

```py
set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1 | set2
# Result: {1, 2, 3, 4, 5}

result = set1.union(set2)
# Result: {1, 2, 3, 4, 5}

# Multiple sets
result = set1 | set2 | {6, 7}
# Result: {1, 2, 3, 4, 5, 6, 7}
```

<br>
<br>

### Intersection

`&` or `intersecton()` returns only elements common to both sets.

```py
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1 & set2
# Result: {3, 4}

result = set1.intersection(set2)
# Result: {3, 4}
```

<br>
<br>

### Difference

`-` or `difference()` returns elements in the first set but not in the second.

```py
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1 - set2
# Result: {1, 2}

result = set2 - set1
# Result: {5, 6}

result = set1.difference(set2)
# Result: {1, 2}
```

<br>
<br>

### Symmetric difference

`^` or `symmetric_difference()`returns elements in either set, but not in both.

```py
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1 ^ set2
# Result: {1, 2, 5, 6}

result = set1.symmetric_difference(set2)
# Result: {1, 2, 5, 6}
```

<br>
<br>

### Subset

`<=` or `issubset()` checks if all elements of one set are in another.

```py
set1 = {1, 2}
set2 = {1, 2, 3, 4}

result = set1 <= set2  # True (set1 is subset of set2)
result = set1.issubset(set2)  # True

# Proper subset (strict subset)
result = set1 < set2  # True (subset but not equal)
```

<br>
<br>

### Superset

`>=` or `issuperset()` checks if one set contains all elements of another.

```py
set1 = {1, 2, 3, 4}
set2 = {1, 2}

result = set1 >= set2  # True (set1 is superset of set2)
result = set1.issuperset(set2)  # True

# Proper superset (strict superset)
result = set1 > set2  # True (superset but not equal)
```

<br>
<br>

### Disjoint

`isdisjoint()` checks if two sets have no common elements.

```py
set1 = {1, 2, 3}
set2 = {4, 5, 6}

result = set1.isdisjoint(set2)  # True (no common elements)

set3 = {3, 4, 5}
result = set1.isdisjoint(set3)  # False (3 is common)
```

<br>
<br>

### Inplace operators

Modifies the original set.

```py
set1 = {1, 2, 3}

set1 |= {4, 5}  # Union update
# set1 is now {1, 2, 3, 4, 5}

set1 &= {2, 3, 4}  # Intersection update
# set1 is now {2, 3, 4}

set1 -= {3}  # Difference update
# set1 is now {2, 4}

set1 ^= {4, 5}  # Symmetric difference update
# set1 is now {2, 5}
```

<br>
<br>
<br>

## Set methods

<br>
<br>

### Insertion

1. `add(element)` to add a single element to the set.

   ```py
   my_set = {1, 2, 3}
   my_set.add(4)
   # Result: {1, 2, 3, 4}

   my_set.add(2)  # No effect - already exists
   # Result: {1, 2, 3, 4}
   ```

   - Time complexity : $O(1)$.

1. `update(iterable)` to add multiple elements from an iterable(list, tuple, set, string).

   ```py
   my_set = {1, 2, 3}
   my_set.update([4, 5, 6])
   # Result: {1, 2, 3, 4, 5, 6}

   my_set.update([7, 8], {9, 10})
   # Result: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

   # With strings (adds each character)
   my_set = {'a', 'b'}
   my_set.update("cd")
   # Result: {'a', 'b', 'c', 'd'}
   ```

   - Time complexity : $O(k)$, where $k$ is the number of elements in the iterable.

<br>
<br>

### Search

1. `in` operator checks if an element exists in the set.

   ```py
   my_set = {1, 2, 3, 4, 5}

   result = 3 in my_set  # True
   result = 10 in my_set  # False
   ```

   - Time complexity : $O(1)$.

1. `not in` operator checks if an element does not exist in the set.

<br>
<br>

### Access

There's no special method to access a particular element in a set especially because indexing don't work.

- Most likely, search and deletion are difficient in the case of sets.

<br>
<br>

### Deletion

- `remove(element)` deletes a specified element if present otherwise raises `KeyError`.

  ```py
  s = {1, 2, 3}
  s.remove(2)
  # s = {1, 3}

  mySet = {1,2,"hello"}
  mySet.remove("you")
  #KeyError: 'you'
  ```

  - Time complexity : $O(1)$.

- `discard(element)` deletes a specified element if present and does nothing if it doesn't exist.

  ```py
  s = {1, 2, 3}
  s.discard(2)
  # s = {1, 3}

  mySet = {1,2,"hello"}
  mySet.discard("you")
  #mySet = {1,2,"hello"}
  ```

  - Time complexity : $O(1)$.

- `pop()` removes and returns an arbitrary element and raises `KeyError` if set is empty.

  - Time complexity : $O(1)$.

* `clear()` empties the entire set.

  - Time complexity : $O(n)$.

<br>
<br>
