# For loop

```kt
//Inclusive
for (i in 1..5) {
    println(i)      // 1, 2, 3, 4, 5
}

//Non-inclusive
for (i in 1 until 5) {
    println(i)      // 1, 2, 3, 4 (Excludes 5)
}

//Stepping and Downwards
for (i in 10 downTo 0 step 2) {
    println(i)      // 10, 8, 6, 4, 2, 0
}
```

<br>
<br>
<br>
<br>

# Functional looping

For collections, `forEach` is preferred.

```kt
val items = listOf("A", "B", "C")
items.forEach { item ->
    println(item)
}
```

<br>
<br>
<br>
<br>

# While loop

```kt
var x = 5
while (x > 0) {
    x--
}
```

<br>
<br>
<br>
<br>

# Do while

```kt
do {
    val y = retrieveData()
} while (y != null)
```

<br>
<br>
<br>
<br>

# Break and continue

- break: Terminates the nearest enclosing loop.
- continue: Skips the current iteration and proceeds to the next one.

<br>
<br>
<br>

## Labels

breaking to a specific nested loop using labels.

```kt
outer@ for (i in 1..3) {
    for (j in 1..3) {
        if (i == 2) {
            break@outer // Jumps out of the entire outer loop
        }
        println("$i,$j")
    }
}
```
