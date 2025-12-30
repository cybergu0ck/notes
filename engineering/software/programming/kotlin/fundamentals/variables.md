# Initialization

```
keyword identifier = value
```

<br>
<br>
<br>
<br>

# Immutable variables

Immutable variables (Read only) are intialised using `val` keyword.

```kt
val myVariable = 10
```

<br>
<br>
<br>
<br>

# Mutable variables

Mutable variables are intialised using `var` keyword.

```kt
var myVariable = 10
myVariable = 100
```

<br>
<br>
<br>
<br>

# Null safety

Kotlin’s "killer feature" is its built-in protection against the dreaded "NullPointerException".

- By default variables are Non-nullable i.e. cannot hold a null value.

  ```kt
  var message: String = "Hello"
  // message = null  <-- This would cause a compile error
  ```

- Variables can be made nullable by intialising them as follows :

  ```kt
  var greeting: String? = "Hi"
  greeting = null    // This is allowed
  ```

<br>
<br>
<br>
<br>

# Few rules

- camelCase is used in Kotlin
- No Implicit Conversions: Unlike some languages, Kotlin doesn't automatically turn an Int into a Long. You must use helper functions like .toLong() or .toDouble().
