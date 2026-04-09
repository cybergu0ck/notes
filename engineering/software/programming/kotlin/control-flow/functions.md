# Contents

- [Function](#function)
  - [Return value](#return-value)
    - [Single expression function](#single-expression-function)
  - [Function Parameters](#function-parameters)
    - [Variable arguments](#variable-arguments)
    - [Default Argument Values](#default-argument-values)
  - [Storing functions in variables](#storing-functions-in-variables)
  - [Lambda expression](#lambda-expression)
  - [Function as data type](#function-as-data-type)
    - [Shorthand syntax](#shorthand-syntax)
    - [Trailing lambda syntax](#trailing-lambda-syntax)
  - [Nullable function types](#nullable-function-types)
  - [Extension function](#extension-function)

<br>
<br>
<br>




# Function

Function are reusable logically self-contained code that facilitates modularization of program.

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

## Return value

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

### Single expression function

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

## Function Parameters

Parameters refer to the data that is passed into a funciton when it is called.

- parameters and arguments must match in _number, order and type_.

<br>
<br>

### Variable arguments

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

### Default Argument Values

Default arguments are values that are assigned to function parameters if no arguments are passed to the function when it is called.

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

## Storing functions in variables

To refer to a function as a value, the function reference operator (`::`) must be used.

```kt
fun main() {
    val trickFunction = ::trick
    trickFunction()
}

fun trick() {
    println("No treats!")
}

//No treats!
```

- The following code when executed will give an error.

  ```kt
  fun main() {
      val trickFunction = trick
  }

  fun trick() {
      println("No treats!")
  }

  //Function invocation 'trick()' expected
  ```

<br>
<br>
<br>

## Lambda expression

Lambda expressions provide a concise syntax to define a function without the `fun` keyword.

- Lambda expressions can be directly stored in a variable without the function reference operator.

- The syntax of a lambda expression

  ```
  val variableName = {
      //function body
  }
  ```

- The `trick` function from the above example can be converted to a lambda expression as follows

  ```kt
  fun main() {
      val trickFunction = trick
      trick()
      trickFunction()
  }

  val trick = {
      println("No treats!")
  }

  //No treats!
  //No treats!
  ```

- Lambda expression with parameters

  ```kt
  val greetLambda = { name:String, greet:String ->
      println("$greet, $name")
  }

  fun main() {
  greetLambda("Bill", "Hi")
  }

  //Hi, Bill
  ```

<br>
<br>
<br>

## Function as data type

Kotlin supports explicit type inference, The syntax to express this for function types

```
(parameters(optional)) -> return_type
```

- The following is an illustration for data type of standard kotlin function with no parameters and no return type.

  ```kt
  fun conventionalTrick(){
      println("No treats!")
  }

  fun main() {
      val standardtrickFunction: () -> Unit = ::conventionalTrick
  }
  ```

- The following is an illustration for data type of lambda expression with no parameters and no return type.

  ```kt
  val trick = {
      println("No treats!")
  }

  fun main() {
      val lambdaTrickFunction: () -> Unit = trick
  }
  ```

* The following is an illustration for data type of lambda expression with parameters and return type.

  ```kt
  val greet = {name: String, greet: String ->
      "$greet, $name"
  }

  fun main() {
      val greetFunction: (String, String) -> String = greet
  }
  ```

<br>
<br>

### Shorthand syntax

When a function has a single parameter, Kotlin implicitly assigns it the it name, so the parameter name and `->` symbol can be omitted, which makes your lambda expressions more concise.

- The following is a conventioanl lambda expression which accepts a single parameter.

  ```kt
  val printString : (String)->Unit = { input ->
      println(input)
  }

  fun main() {
  printString("This is a very long string")
  }

  //This is a very long string
  ```

- The following is the shorthand syntax for the above lambda expression.

  ```kt
  val printString : (String)->Unit = {
      println(it)
  }

  fun main() {
  printString("This is a very long string")
  }
  ```

<br>
<br>

### Trailing lambda syntax

The lamda expression can be placed aftet the closing parenthesis to call the function when the function type is the last parameter of that function.

```
functionName(parameter, lambdaExpression)
functionName(parameter) lambdaExpression
```

- Illustration of conventional lamda syntax

  ```kt
  val printString : (String)->Unit = {
      println(it)
  }

  fun printSomething(isDefault:Boolean, func:(String)->Unit){
      if(isDefault) {
          println("This is default print")
      } else {
          func("This is special print")
      }
  }

  fun main() {
  printSomething(false, printString)
  }
  //This is special print
  ```

- Using the trailing lambda syntax

  ```kt
  fun printSomething(isDefault:Boolean, func:(String)->Unit){
      if(isDefault) {
          println("This is default print")
      } else {
          func("This is special print")
      }
  }

  fun main() {
  printSomething(false) {println(it)}
  }
  //This is special print
  ```

- The composable functions in Jetpack Compose are typically called using trailing lambda syntax. Example :

  ```kt
  Column(modifier = Modifier.fillMaxSize()){
            Text(
                text = "Start billing",
                modifier = modifier,
                style = TextStyle(
                    fontSize = 24.sp
                )
            )
            Spacer(modifier = Modifier.height(24.dp))
            Button(onClick = { /* Your action here */ }) {
                Text(text = "Start")
            }
        }
  ```

<br>
<br>
<br>

## Nullable function types

Like other data types, function types can be declared as nullable. In these cases, a variable could contain a function or it could be null.

```
((parameters(opetional))->returnType?)
```

- Illustration

  ```kt
  fun callFunc(func : (()->Unit)?) {
      if(func != null){
          func()
      }
  }

  fun main() {
      val myLambda = { println("ho") }
      callFunc(null)
  }
  ```

<br>
<br>
<br>

## Extension function

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
