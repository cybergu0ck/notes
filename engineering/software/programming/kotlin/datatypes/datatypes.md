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
