# Operators

<br>
<br>

## Arithmetic Operators

| Operator | Operation          |
| -------- | ------------------ |
| +        | Addition           |
| -        | Subtraction        |
| \        | Divison            |
| \*       | Multiplication     |
| %        | Modulo (remainder) |

<br>
<br>

## Assigment Operators

- An `lvalue` (locator value) represents an object that occupies some identifiable location in memory (i.e. has an address).
- `rvalues` are defined by exclusion. Every expression is either an lvalue or an rvalue, so, an rvalue is an expression that does not represent an object occupying some identifiable location in memory.
  - R-value: r-value” refers to data value that is stored at some address in memory. A r-value is an expression, that can’t have a value assigned to it, which means r-value can appear on right but not on left hand side of an assignment operator(=).

<br>

### Compound Assignment Operators

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

## Relational Operators (Comparsion Operators)

Relational operators result to bool types.

| Operator | Operation                    |
| -------- | ---------------------------- |
| ==       | Equal to                     |
| !=       | Not equal to                 |
| >        | Greater than                 |
| >=       | Greater than or equal to     |
| <        | Less than                    |
| <=       | Less than or equal to        |
| <=>      | three way comaprison (C++20) |

<br>
<br>

## Increment and Decrement Operators

Increases or decreases the value by 1.

### prefix

- Does the increment/decrement first and then the assignment

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

### postfix

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
      int another = ++num + 10; // num = num + 1 and then another = num + 10;
      std::cout << another << std::endl; //12
      int new_num = num++ + 10; // new_num = num + 10 and then num = num + 1;
      std::cout << new_num << std::endl;  //12
      return 0;
  }
  ```

<br>
<br>

## Logical Operators

Logical operators result to bool types.

| Operator    | Operation   |
| ----------- | ----------- |
| not (!)     | negation    |
| and (&&)    | logical and |
| or ( \|\| ) | logical or  |

<br>
<br>

## Bitwise Operators

<!-- TODO : Complete this part -->

<br>
<br>

## Address of Operator (&)

- & is used as Address of Operator when
- When & is used as the "address-of" operator, as in &variable, it returns a pointer to the memory address of the variable. The resulting data type is a pointer type.

<br>
<br>

# Operator Precedence

The precendence is tabulated from higher (top ones) to lower (bottom ones)

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

<br>
<br>
