# Lists

- Lists are ordered sequence of strings.
- similar to javascript array, python list.
- lists are useful to implement stacks and queues.

#

<br>
<br>
<br>

# Adding Elements to the list

### `rpush` and `lpush` [ O(1) ]

```
rpush key element [element ...]
```

<br>
<br>
<br>

# Removing Elements to the list

### `rpop` and `lpop` [ O(1) ]

```
lpop key
```

<br>
<br>
<br>

# Reading/ Traversing the list

### `lrange` [ O(s + n) ]

- Returns the elements for the given indexes.
- indexing starts from 0.
- start and end are both inclusive.

```
lrange key start end
```

- The code prints first 3 songs.
  ```
  lrange playlist 0 2
  ```

<br>
<br>
<br>

# Get the number of elements from the list

### `llen` [ O(1) ]

- Returns the number of elements in the list.

  ```
  llen key
  ```
