# Variables

Variables are named containers to store data values.

<br>
<br>
<br>

## Creation of variables

- Python is dynamically types i.e. no need to declare the data type when it is created and the variable can be used to hold another type.

* Unlike other languages, Python doesn't have a command to declare a variable, a variable is created the moment it is assigned a value.

  ```py
  x = 5          # x is an integer
  x = "X"        # x is now a string
  name = "Alice" # name is a string
  pi = 3.14      # pi is a float
  ```

<br>
<br>
<br>

## Naming rules

Identifiers must follow the naming conventions :

- Must start with a letter or an underscore.
- Cannot start with a number.
- Can only contain alpha-numeric characters and underscores
- Identifiers are case-sensitive.
- Identifiers can't be reserved keywords.

<br>
<br>
<br>

## Multiple assignment

Python facilitates multiple assignment in a single line.

- Many values to multiple variables.
  ```py
  x, y, z = "Orange", "Banana", "Cherry"
  ```
- One value to multiple variables.
  ```py
  x = y = z = "Orange"
  ```

* Example showing multiple assignment.

  ```python
  listed = [1,2,3]

  def swap(i,j):
      listed[i] = listed[j]
      listed[j] = listed[i]
  swap(1,2)

  print(listed)

  #>[1, 3, 3]
  ```

  ```python
  listed = [1,2,3]

  def swap(i,j):
      listed[i],listed[j] = listed[j],listed[i]

  swap(1,2)

  print(listed)

  #>[1, 3, 2]
  ```

<br>
<br>
<br>

## Scope of variables

<!-- //TODO - Fill this later -->
