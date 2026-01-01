_**Function** are reusable logically self-contained code that facilitates modularization of program._

- Code execution begins from `main` function in kotlin.

* Illustration of a Kotlin function

  ```kt
  fun main()
  {
      myFunction("Hey", "Fluffy")
  }

  fun myFunction(greeting : String, name : String)
  {
      println("$greeting, $name!")
  }
  ```

<br>
<br>
<br>
<br>

# Return value

- By default kotlin returns `Uint`, it is equivalent to `void` keyword in C++/Java.

  ```kt
  fun myFunction(greeting : String, name : String) //myFunction returns Uint type
  {
      println("$greeting, $name!")
  }
  ```

- Return type must be specified as follows

  ```kt
  fun myFunction(greeting : String, name : String) : String
  {
      return "$greeting, $name!"
  }
  ```

<br>
<br>
<br>

## Single expression function

Assignment opeartor `=` can be used instead of curly braces and explicit return keyword.

```kt
fun main()
{
    val text : String = myFunction("Hey", "Fluffy")
    println(text)  //Hey Fluffy!
}

fun myFunction(greeting : String, name : String) = "$greeting $name!"
```

<br>
<br>
<br>
<br>

# Function Parameters

_**Parameters** refer to the data that is passed into a funciton when it is called._

- parameters and arguments must match in _number, order and type_.

<br>
<br>
<br>

## Variable arguments

`vararg` keyword is used to pass variable number of arguments of same type.

```kt
fun main()
{
    val maxNumber : Int = getMax(1,2,55,6)
    println(maxNumber) //55
}

fun getMax(vararg numbers: Int) : Int {
    var max = numbers[0]
    for (number in numbers) {
        if (number > max) {
            max = number
        }
    }
    return max
}
```

<br>
<br>
<br>

## Default Argument Values

_**Default arguments** are values that are assigned to function parameters if no arguments are passed to the function when it is called._

```kt
fun main()
{
    searchFor("coding tutorials")
}
fun searchFor(search : String, searchEngine : String = "Google"){
    println("Searching for $search on $searchEngine")
}
```

<br>
<br>
<br>
<br>

# Extension function

They are functions that add new functionality to existing classes without modifying their source code or using inheritance.

- 'this' keyword refers to the receiver object.

```
fun ClassName.functionName(parameters): ReturnType {
    // function body
    // 'this' refers to the receiver object
}
```

```kt
fun main() {
    println("Enter a number :")
    val number: Int = readLine()!!.toInt()
    if(number.isEven()){
        println("The number is even")
    }else{
        println("The number is odd")
    }
}

fun Int.isEven() : Boolean {
    if(this % 2 == 0){  //Here this refers to the integer which calls isEven
        return true
    }else{
        return false
    }
}
```
