# Contents

- [Type inference](#type-inference)
- [Explicit typing](#explicit-typing)
- [Data types](#data-types)
  - [Nullability](#nullability)
    - [Nullable types](#nullable-types)
    - [Non-nullable types](#non-nullable-types)
  - [Handling nullable variables](#handling-nullable-variables)
    - [Safe call operator](#safe-call-operator)
    - [Not null assertion operator](#not-null-assertion-operator)
    - [Elvis operator](#elvis-operator)

<br>
<br>
<br>




A **_type_** (also called data type) tells Kotlin how you intend to use that data.

- type provides the set of values that the expression can take.
- type also defines the operations that can be performed on the data.
- Int, Double, String, Boolean are some data types

<br>
<br>
<br>
<br>

# Type inference

**_Type inference_** refers to the ability of the compiler to deduce the type of a value based on the context in which it is used.

```kotlin
val myNumber = 1 // Type Inference
```

<br>
<br>
<br>
<br>

# Explicit typing

Kotlin figures out data type automatically based on the value, However explicit typing can also be done.

```
keyword identifier : datatype = value
```

```kt
var myNumber : Int = 100
```

<br>
<br>
<br>
<br>

# Data types

```kotlin
//Some Basic Data Types
fun main(){
	val whole: Int = 11
	val fractional: Double = 1.4
	val isTrue: Boolean = true //Its true and not True!
	val words: String = " SOmebizzareword"
	val character: Char = 'z'
	val lines:String = """ dafgdag
	dagdagd a
	dagdag
	"""
}
```

//TODO - Finish up this section later on

<br>
<br>
<br>

## Nullability

A variable can be assigned with `null` value to represent no value at all.

<br>
<br>

### Nullable types

Nullable types are variables that can hold `null`.

```kt
fun main() {
    var myVariable: String = "Hey"
    myVariable = null
}

//Null cannot be a value of a non-null type 'String'.
```

<br>
<br>

### Non-nullable types

Non-null types are variables that can't hold `null`.

- To declare nullable variables in Kotlin, you need to add a `?` operator to the end of the type.

```kt
fun main() {
    var myVariable: String? = "Hey"  //nyVariable is a nullable string
    myVariable = null
}
```

<br>
<br>
<br>

## Handling nullable variables

Kotlin intentionally applies syntactic rules so that it can achieve null safety, which refers to a guarantee that no accidental calls are made on potentially null variables. This doesn't mean that variables can't be null. It means that if a member of a variable is accessed, the variable can't be null.

```kt
fun main() {
    var favoriteActor: String? = "Sandra Oh"
    println(favoriteActor.length)
}

//Compiler error
//Only safe (?.) or non-null asserted (!!.) calls are allowed on a nullable receiver of type 'String?'.
```

<br>
<br>

### Safe call operator

Safe call operator `?.` is to be used to access methods or properties of nullable variables.

The safe call operator allows safer access to nullable variables because the Kotlin compiler stops any attempt of member access to null references and returns null for the member accessed.

```kt

fun main() {
    var favoriteActor: String? = null
    println(favoriteActor?.length) //prints null

    var favFood: String? = "Burger"
    println(favFood?.length) //prints 6
}
```

<br>
<br>

### Not null assertion operator

not-null assertion operator `!!` is used to access methods or properties of nullable variables. It asserts that the value of the variable is not `null`,regardless of whether it is or isn't.

- Unlike `?.` safe-call operators, the use of a `!!` not-null assertion operator may result in a `NullPointerException` error being thrown if the nullable variable is indeed `null`.

```kt
fun main() {
    var favoriteActor: String? = "Sandra Oh"
    println(favoriteActor!!.length)
}

//9
```

```kt
fun main() {
    var favoriteActor: String? = null
    println(favoriteActor!!.length)
}

//Exception in thread "main" java.lang.NullPointerException
// at FileKt.main (File.kt:3)
// at FileKt.main (File.kt:-1)
// at jdk.internal.reflect.NativeMethodAccessorImpl.invoke0 (:-2)
```

<br>
<br>

### Elvis operator

- Syntax for using the elvis operator.

  ```
  result = nullableValue  ?: fallbackValue
  ```

* Example :

  ```kt
  val name: String? = null
  val displayName = name ?: "Guest"

  println(displayName) // Output: Guest
  ```

* The elvis operator can be used along with the safe call operator.

  ```kt
  fun main() {
      var favoriteActor: String? = "Sandra Oh"

      val lengthOfName = favoriteActor?.length ?: 0

      println("The number of characters in your favorite actor's name is $lengthOfName.")
  }
  ```
