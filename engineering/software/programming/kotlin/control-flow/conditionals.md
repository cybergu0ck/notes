# If

```kt
if(age <= 18){
    println("Minor")
}
```

- If can be used as an expression as follows

  ```kt
  val status = if (age >= 18) "Adult" else "Minor"
  ```

<br>
<br>
<br>
<br>

# Else if

```kt
if(age <= 18){
    println("Minor")
} else if(age > 18 && age <= 60){
    println("Adult")
}
```

<br>
<br>
<br>
<br>

# Else

```kt
if(age <= 18){
    println("Minor")
} else if(age > 18 && age <= 60){
    println("Adult")
} else {
    println("Senior")
}
```

<br>
<br>
<br>
<br>

# When

```kt
when (dayNumber) {
    1 -> println("Monday")
    2 -> println("Tuesday")
    else -> println("Invalid day") // 'else' is like 'default'
}
```

- `when` can be used with multiple consitions and ranges.

  ```kt
  when (score) {
      90, 100 -> println("Perfect!")
      in 70..89 -> println("Great job")
      !in 0..100 -> println("Invalid score")
      else -> println("Keep trying")
  }
  ```

- `is` keyword can be used in `when` blocks to check types.

  ```kt
  when (x) {
      is String -> println(x.length) // x is automatically treated as a String here
      is Int -> println(x + 1)
  }
  ```
