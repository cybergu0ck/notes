
### var and val
---
The most basic decision for a data identifier is whether it can change its contents during program execution, or if it can only be assigned once. This is controlled by two keywords: 

1. var, short for variable, which means you can reassign its contents. 
2. val, short for value, which means you can only initialize it; you cannot reassign it.

> `var identifier = initialization`

> `val identifier = initialization`


### Data Types
---
A ___type___ (also called data type) tells Kotlin how you intend to use that data.
- type provides the set of values that the expression can take.
- type also defines the operations that can be performed on the data.

Int, Double, String are some data types

___Type inference___ refers to the ability of the compiler to deduce the type of a value based on the context in which it is used. We can be more verbose and specify the type:

> `val identifier : Type = initialization`

```kotlin
val n = 1 // Type Inference
val n: Int = 1 //Type is defined Explicitely  
```

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

### Function
---
A function is like a small program that has its own name, and can be executed (invoked) by calling that name from another function.

The basic form of a function is :
```kotlin
fun functionName(parameter1: Type1, parameter2: Type2,....):ReturnType{
	lines of code
	return result //Must be of the type that was defined above
}
```

If the function doesn’t provide a meaningful result, its return type is ___Unit___. You can specify Unit explicitly if you want, but Kotlin lets you omit it:

```kotlin
fun sayHello(){
	println("Hello!")
}

//The above function returns a Kotlin Unit
```

If a function is only a single expression, you can use the abbreviated syntax of an equals sign followed by the expression:

```kotlin
fun functionName(parameter: Type....):ReturnType = expression
```

- A function body surrounded by curly braces is called a ___block body___. 
- A function body using the equals syntax is called an ___expression body___. Kotlin can infer the return type of a function with expression body.


### if Expressions
---
The expression inside the parentheses after the ___if___ must evaluate to true or false. If true, the following expression is executed.
```kotlin
fun main() { 
if (1 > 0) 
	println("It's true!")
if (10 < 11) { 
	println("10 < 11") 
	println("ten is less than eleven")
	} 
}
/* Output: 
It's true! 
10 < 11 
ten is less than eleven 
*/
```

The ___else___ keyword allows you to handle both true and false paths:
```kotlin
fun main(){
	val number: Int = -11
	if (number > 0)
		println("Positive Number")
	else
		println("Negative Number or zero")
}

/* Output:
Negative Number or zero
*/
```

The else keyword is only used in conjunction with if. You are not limited to a single check—you can test multiple combinations by combining ___else___ and ___if___:
```kotlin
fun main(){
	val number: Int = 0
	if (number > 0)
		println("Positive Number")
	else if (number == 0)
		println("Number is zero")
	else
		println("Negative Number")
}
/* Output:
Number is zero
*/
```

When an ___if___ expression reaches a certain size and complexity you’ll probably use a ___when___ expression instead

Some ___if___ expression code are written below :

```kotlin
fun main() { 
	val num = 10 
	val result = if (num > 100) 4 else 42 
	println(result)
}
/* Output: 
42 
*/
```

```kotlin
fun trueOrFalse(exp: Boolean): String { 
	if (exp) 
		return "It's true!"
	return "It's false" 
	}
	
fun main() { 
	val b = 1
	println(trueOrFalse(b < 3)) 
	println(trueOrFalse(b >= 3))
}
/* Output: 
It's true! 
It's false 
*/
```

```kotlin
fun oneOrTheOther(exp: Boolean): String = 
	if (exp) 
		"True!" // No 'return' necessary as '=' is used in function definition
	else 
		"False"
		
fun main() { 
	val x = 1
	println(oneOrTheOther(x == 1)) 
	println(oneOrTheOther(x == 2))
}
/* Output: 
True! 
False 
*/
```


### String Templates
---
A ___String template___ is a programmatic way to generate a String.
If you put a $ before an identifier name, the String template will insert that identifier’s contents into the String:

```kotlin
fun main(){
	val answer = 99
	println("Found $answer !")
	println("printing a $1") // If what follows the $ isn’t recognizable as a program identifier, nothing special happens.
}
/* Output:
Found 99 !
printing a $1
*/
```

Strings can be concatenated using + :
```kotlin
fun main(){
	val myString = "This" + "is" + "my" + "String" +'!'
    println(myString)
}
/*Output:
ThisismyString!
*/
```

Placing an expression inside ${} evaluates it. The return value is converted to a String and inserted into the resulting String:

```kotlin
fun main(){
	val condition = true
    println(" ${ if (condition) 'a' else 'b'}")
    
    val num = 11
    println(" $num + 4 = ${11 + 4}")
}
/*Output:
a
11 + 4 = 15
*/
```

When a String must include a special character, such as a quote, you can either escape that character with a \ (backslash), or use a String literal in triple quotes:
```kotlin
fun main(){
	val mood = "Incredible"
    println("vibe right now is \"$mood\".")   //using backslash
    println("""vibe right now is "$mood".""") //using """
}
/*Output:
vibe right now is "Incredible". 
vibe right now is "Incredible".
*/
```

