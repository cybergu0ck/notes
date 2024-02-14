# Constants

_**Constants** are variables that connot change their value._

<br>
<br>

## Types of constants in C++

### Literal Constants

- They are values that are represented directly in the code. They can be used to represent numbers, characters, strings, and Boolean values.
- examples:
  - integer literal constants like 12, 12u (unsigned integer), 12l (long integer), 12ll (long long integer)
  - floating point literal constatants like 12.1 (Double), 12.1F (Float), 12.1 (Long Double)
  - character literal constants like \n, \t etc

<br>

### Declared constants

- constants declared using the `const` keyword.

  ```cpp
  const int year = 2000;
  ```

<br>

### Defined constants

- constants declared using #define preprocessor directive
- Donot use this is modern C++.

  ```cpp
  #define pi 3.141
  ```
