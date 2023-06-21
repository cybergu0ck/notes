# Assigment Operator (=)

- An `lvalue` (locator value) represents an object that occupies some identifiable location in memory (i.e. has an address).
- `rvalues` are defined by exclusion. Every expression is either an lvalue or an rvalue, so, an rvalue is an expression that does not represent an object occupying some identifiable location in memory.
  - R-value: r-value” refers to data value that is stored at some address in memory. A r-value is an expression, that can’t have a value assigned to it, which means r-value can appear on right but not on left hand side of an assignment operator(=).

<br>
<br>

# Arithmetic Operators

| Operator | Operation          |
| -------- | ------------------ |
| +        | Addition           |
| -        | Subtraction        |
| \        | Divison            |
| \*       | Multiplication     |
| %        | Modulo (remainder) |

<br>
<br>

# Increment (++) and Decrement (--) Operators

- Increases or decreases the value by 1.
- Can be used with integers, floats and pointers.

## prefix

- does the increment/decrement first and then the assignment

  ```cpp
  int main()
  {
      int num = 1;
      int new_num = ++num; // num = num + 1 and then new_num = num
      cout << new_num;
      return 0;
  }
  //2
  ```

<br>

## postfix

- Does the assignment first and then the increment/decrement.

  ```cpp
  int main()
  {
      int num = 1;
      int new_num = num++; //new_num = num and then num = num + 1
      cout << new_num;
      return 0;
  }

  //1
  ```

* Check this out

  ```cpp
  int main()
  {
      int num = 1;
      int another = ++num + 10; // num = num + 1 and then another = num + 10; Hence another is 12
      int new_num = num++ + 10; // new_num = num + 10 and then num = num + 1; Hence new_num is 11
      return 0;
  }
  ```

<br>
<br>

# Type conversions (Coersions)

- Higher types are the types that can hold larger values.
- Lower types are the types with less size.
- _Lower types can be converted to higher types as lowertype can fit in the size of higher type._
- example : short and char types are always converted to ints

* Promotion : Conversion to a higher type, generally occurs in math expressions.

  ```cpp
  int main()
  {
      int num1 = 1;
      double num2 = 2.5;
      cout << num1 + num2; //3.5
      return 0;
  }
  ```

* Demotion : Converion to a lower type, generally occurs in assignments.

  ```cpp
  int main()
  {
      int num {0};
      num = 100.2
      cout << num;    //100
      return 0;
  }
  ```

<br>

## Explicit type casting

- `static_cast <type>` is used to cast something to `type`.

<br>
<br>

# Equality Operators

| Operator | Operation    |
| -------- | ------------ |
| ==       | Equal to     |
| !=       | Not equal to |

- 10 == 10.0 will result in true.
- 10 == 9.999999999 will also result in true.

<br>
<br>

# Relational Operators

- relational operators result to bool types.

  | Operator | Operation                    |
  | -------- | ---------------------------- |
  | >        | Greater than                 |
  | >=       | Greater than or equal to     |
  | <        | Less than                    |
  | <=       | Less than or equal to        |
  | <=>      | three way comaprison (C++20) |

<br>
<br>

# Logical Operators

- logical operators result to bool types.

  | Operator    | Operation   |
  | ----------- | ----------- |
  | not (!)     | negation    |
  | and (&&)    | logical and |
  | or ( \|\| ) | logical or  |

<br>
<br>

# Bitwise Operators

> Complete this

<br>
<br>

# Compound Assignment Operators

| Operator | Example     | Meaning          |
| -------- | ----------- | ---------------- |
| +=       | lhs += rhs  | lhs = lhs + rhs  |
| -=       | lhs -= rhs  | lhs = lhs - rhs  |
| \*=      | lhs \*= rhs | lhs = lhs \* rhs |
| /=       | lhs /= rhs  | lhs = lhs / rhs  |
| %=       | lhs %= rhs  | lhs = lhs % rhs  |
| >>=      | lhs >>= rhs | lhs = lhs >> rhs |
| <<=      | lhs <<= rhs | lhs = lhs << rhs |
| &=       | lhs &= rhs  | lhs = lhs & rhs  |
| ^=       | lhs ^= rhs  | lhs = lhs ^ rhs  |
| \|=      | lhs \|= rhs | lhs = lhs \| rhs |

<br>
<br>

# Operator Precedence

- The precendence is tabulated from higher (top ones) to lower (bottom ones)

| Operator                               | Associativity |
| -------------------------------------- | ------------- |
| [] -> . ()                             | left to right |
| ++ -- not -(unary) \*(de-ref) & sizeof | right to left |
| \* / %                                 | left to right |
| + -                                    | left to right |
| << >>                                  | left to right |
| < <= > >=                              | left to right |
| == !=                                  | left to right |
| &                                      | left to right |
| ^                                      | left to right |
| \|                                     | left to right |
| &&                                     | left to right |
| \|\|                                   | left to right |
| = op= ?:                               | right to left |
