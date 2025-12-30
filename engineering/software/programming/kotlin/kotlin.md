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

If the function doesn’t provide a meaningful result, its return type is **_Unit_**. You can specify Unit explicitly if you want, but Kotlin lets you omit it:

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

- A function body surrounded by curly braces is called a **_block body_**.
- A function body using the equals syntax is called an **_expression body_**. Kotlin can infer the return type of a function with expression body.

### if Expressions

---

The expression inside the parentheses after the **_if_** must evaluate to true or false. If true, the following expression is executed.

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

The **_else_** keyword allows you to handle both true and false paths:

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

The else keyword is only used in conjunction with if. You are not limited to a single check—you can test multiple combinations by combining **_else_** and **_if_**:

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

When an **_if_** expression reaches a certain size and complexity you’ll probably use a **_when_** expression instead

Some **_if_** expression code are written below :

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

A **_String template_** is a programmatic way to generate a String.
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

### Repetition with while

---

The syntax of while loop is

```kotlin
while(boolean expression){
	//code to be repeated
}
```

example code:

```kotlin
fun condition(i:Int)= i<100

fun main(){
	var i =10
	while(condition(i)){
		print("*")
		i += 10
	}
}

/* Output:
*********
*/
```

The syntax of do-while loop is

```kotlin
do{
//code to be repeated

}while(condition)
```

Example:

```kotlin
fun main(){
var i = 1000
do{
print("=")
i += 1
}while(i<5)
}

/* Output:
=
*/
```

The code in the do statement will run once (for sure) and will loop based on the condition in while.

### Looping & Ranges

---

> The in keyword indicates that you are stepping through values:

The syntax for a for loop is

```kotlin
for (v in values){
	// Do something with v
}
```

Example

```kotlin
fun main() {
    for (i in 1..3){
        println("Hey $i")
    }
}
/* Output:
Hey 1
Hey 2
Hey 3
*/
```

A range is an interval of values defined by a pair of endpoints.

There are two basic ways to define ranges: 1. Using **_.._** syntax includes both bounds in the resulting range. 2. **_until_** excludes the end. The output shows that 10 is not part of the range

```kotlin
fun main() {
    for (i in 1..5){   //using .. syntax
        print("$i ")
    }
}
/*Output:
1 2 3 4 5
*/
```

```kotlin
fun main() {
    for (i in 1 until 5){   //using .. syntax
        print("$i ")
    }
}
/*Output:
1 2 3 4
*/
```

Using **_downTo_**, **_step_**,**_until_** in ranges in for loop

- **_downTo_** produces a decreasing range.
- **_step_** changes the interval.
- **_until_** can also be used with step

```kotlin
fun showRange(r: IntProgression){
    for (i in r){
        print("$i ")
    }
    print(" // $r")
    println()
}

fun main(){
    showRange(1..5)
    showRange(1 until 5)
    showRange(5 downTo 1)
    showRange(0..9 step 3)
    showRange(0 until 9 step 3)
    showRange(5 downTo 1 step 2)
}

/* Output:
1 2 3 4 5 // 1..5
1 2 3 4 // 1..4
5 4 3 2 1 // 5 downTo 1 step 1
0 3 6 9 // 0..9 step 3
0 3 6 // 0..6 step 3
5 3 1 // 5 downTo 1 step 2
*/
```

You can iterate over a range of elements that are whole quantities, like integers and characters, but not floating-point values.

> If you simply want to repeat an action a fixed number of times, you may use repeat() instead of a for loop.

```kotlin
fun main() {
   repeat(3){
       println("Hell yeah it is")
   }
}
/* Output:
Hell yeah it is
Hell yeah it is
Hell yeah it is
*/
```

### The in Keyword

---

The in keyword tests whether a value is within a range.

```kotlin
fun main() {
  var myRange = 1..10
  print(5 in myRange)
}

/*
true
*/
```
