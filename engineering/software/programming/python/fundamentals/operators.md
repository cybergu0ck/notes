# Operators

<br>
<br>
<br>

## Arithmetic operators

| Operator | Operation                        | Example       |
| -------- | -------------------------------- | ------------- |
| +        | Addition                         | 1 + 2 = 3     |
| -        | Subtraction                      | 1 + 2 = 3     |
| \*       | Multiplication                   | 2 \* 2 = 4    |
| \        | Divison                          | 15 / 4 = 3.75 |
| %        | Modulo (remainder)               | 15 % 4 = 3    |
| //       | Floor division (floor(quotient)) | 15 // 4 = 3   |

<br>
<br>
<br>

## Assignment operators

| Operator | Operation                               | Example                                       |
| -------- | --------------------------------------- | --------------------------------------------- |
| =        | Basic assignment                        | x = 10                                        |
| :=       | Assignment expression (Walrus operator) | if (n := len(my_list)) > 10 #check and assign |

<br/>
<br/>

### Compound assignment operators

| Operator | Operation                 | Example (if `x = 10`) | Equivalent To | Result |
| :------- | :------------------------ | :-------------------- | :------------ | :----- |
| `+=`     | Addition Assignment       | `x += 5`              | `x = x + 5`   | `15`   |
| `-=`     | Subtraction Assignment    | `x -= 2`              | `x = x - 2`   | `8`    |
| `*=`     | Multiplication Assignment | `x *= 3`              | `x = x * 3`   | `30`   |
| `/=`     | Division Assignment       | `x /= 4`              | `x = x / 4`   | `2.5`  |
| `//=`    | Floor Division Assignment | `x //= 4`             | `x = x // 4`  | `2`    |
| `%=`     | Modulo Assignment         | `x %= 3`              | `x = x % 3`   | `1`    |
| `**=`    | Exponentiation Assignment | `x **= 2`             | `x = x ** 2`  | `100`  |
| `&=`     | Bitwise AND Assignment    | `x &= 3`              | `x = x & 3`   | `2`    |
| `\| =`   | Bitwise OR Assignment     | `x \| = 3`            | `x = x \| 3`  | `11`   |
| `^=`     | Bitwise XOR Assignment    | `x ^= 3`              | `x = x ^ 3`   | `9`    |
| `>>=`    | Right Shift Assignment    | `x >>= 1`             | `x = x >> 1`  | `5`    |
| `<<=`    | Left Shift Assignment     | `x <<= 1`             | `x = x << 1`  | `20`   |

- Unlike other languages, Python doesn't have increment (`++`) and decrement (`--`) operators.

<br/>
<br/>
<br/>

## Relational Operators

Relational operators result to bool types.

| Operator | Operation                | Example   |
| :------- | :----------------------- | :-------- |
| `==`     | Equal to                 | `x == y`  |
| `!=`     | Not equal to             | `x != y`  |
| `>`      | Greater than             | `x > y`   |
| `<`      | Less than                | `x < y`   |
| `>=`     | Greater than or equal to | `x >= 10` |
| `<=`     | Less than or equal to    | `y <= 20` |

<br/>
<br/>
<br/>

## Logical Operators

Logical operators result to bool types.

| Operator | Description                                                 | Example (if `x = 5`) | Result  |
| :------- | :---------------------------------------------------------- | :------------------- | :------ |
| `and`    | Returns `True` if **both** statements are true              | `x < 10 and x > 3`   | `True`  |
| `or`     | Returns `True` if **at least one** statement is true        | `x < 5 or x == 5`    | `True`  |
| `not`    | Reverses the result (Returns `False` if the result is true) | `not(x < 10)`        | `False` |

<br/>
<br/>
<br/>

## Bitwise Operators

| Symbol | Operator            |
| ------ | ------------------- |
| &      | bitwise AND         |
| \|     | bitwise OR          |
| ~      | bitwise NOT         |
| ^      | bitwise XOR         |
| <<     | bitwise Left Shift  |
| >>     | bitwise Right Shift |

<br/>
<br/>

### Bitwise and

- Decimal 5 is Binary 0101. (5 is `0b0101`)
- Decimal 6 is Binary 0110. (6 is `0b0110`)
- 5 & 6 should give `0b0100` which is 4 (Perform AND bit by bit)

```python
print(5 & 6)

#4
```

<br/>
<br/>

### Bitwise or

Exactly same like AND but instead performs OR.

<br/>
<br/>

### Bitwise not

Invert all the 1's to 0's and 0's to 1's.

<br/>
<br/>

### Bitwise xor

Performs XOR operation bitwise. XOR operation follows : `A ^ B = A * B' + A' * B` and its truth table is shown below

| A   | B   | A^ B |
| --- | --- | ---- |
| 0   | 0   | 0    |
| 0   | 1   | 1    |
| 1   | 0   | 1    |
| 1   | 1   | 0    |

Illustration:
5 is `0b0101` and 1 is `0b0001`, Performing Bitwise XOR results in `0b0100` which is 4.

```python
print(5^1)

#4
```

<br/>
<br/>

### Bitwise left shift

Shift the bits in the Left Side (In binary) of the operator by the number (in decimal) present in Right Side of the operator

5 is 0b0101, Hence for `5 << 3` we must shift the bits in binary of 5 by 3 places, gives us `0b_0010_1000` (In Python, underscores are used to group digits without messing with the magnitude of the number). `0b_0010_1000` is 40

```python
print(5 << 3)

#40
```

<br/>
<br/>

### Bitwise right shift

Same concept as Left Shift but Shift Right Instead.

## Operator precedence

| Precedence  | Operator                                                 | Description                                      |
| :---------- | :------------------------------------------------------- | :----------------------------------------------- |
| 1 (Highest) | `()`                                                     | Parentheses (Grouping)                           |
| 2           | `**`                                                     | Exponentiation (Power)                           |
| 3           | `+x`, `-x`, `~x`                                         | Unary plus, Unary minus, Bitwise NOT             |
| 4           | `*`, `/`, `//`, `%`                                      | Multiplication, Division, Floor division, Modulo |
| 5           | `+`, `-`                                                 | Addition, Subtraction                            |
| 6           | `<<`, `>>`                                               | Bitwise left and right shifts                    |
| 7           | `&`                                                      | Bitwise AND                                      |
| 8           | `^`                                                      | Bitwise XOR                                      |
| 9           | `\|`                                                     | Bitwise OR                                       |
| 10          | `==`,`!=`, `>`,`>=`,`<`,`<=`,`is`,`is not`,`in`,`not in` | Comparisons, Identity, and Membership            |
| 11          | `not`                                                    | Logical NOT                                      |
| 12          | `and`                                                    | Logical AND                                      |
| 13          | `or`                                                     | Logical OR                                       |
| 14 (Lowest) | `=`, `+=`, `-=`, `*=`, etc.                              | Assignment operators                             |

<br>
<br>

### Associativity

When two operators have the same precedence level, Python uses associativity to determine the order.

- Left-to-Right: Most operators are evaluated from left to right.
- Right-to-Left: The exponentiation operator (\*\*) is a notable exception.
