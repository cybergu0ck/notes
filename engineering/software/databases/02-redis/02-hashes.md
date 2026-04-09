# Contents

- [Hashs](#hashs)
- [Create Fields](#create-fields)
    - [`hset` [ O(1) ]](#hset-o1)
- [Read Field Values](#read-field-values)
    - [`hget` [ O(1) ]](#hget-o1)
    - [`hgetall` [ O(n) ]](#hgetall-on)
- [Update Fields](#update-fields)
- [Delete fields](#delete-fields)
    - [`hdel` [ O(1) ]](#hdel-o1)

<br>
<br>
<br>




# Hashs

- hashes are collections of filed-value pairs.
- similar to JSON objects, java hashmap or a python dictionary.
- they are mutable
- they store field values as strings (hence are flat, no nesting)

<br>
<br>
<br>

# Create Fields

### `hset` [ O(1) ]

```
hset key field value [field value ...]
```

```cmd
hset player:1 name Thor race Asguardian level 9 hp 70 gold 70
```

<br>
<br>
<br>

# Read Field Values

### `hget` [ O(1) ]

```
hget key field
```

```cmd
hget player:1 race
```

<br>

### `hgetall` [ O(n) ]

```
hgetall key
```

```cmd
hgetall player:1
```

<br>
<br>
<br>

# Update Fields

Use hset command to update fields or add new fields!

<br>
<br>
<br>

# Delete fields

### `hdel` [ O(1) ]

```
hdel key field [field ...]
```

```cmd
hdel player:1 gold
```
