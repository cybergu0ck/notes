# Constants

_**Constants** are variables that connot change their value._

<br>
<br>

## Const Qualifier

_`const` qualifier facilitates constants in C++._

- Attempt to modify a const qualified variable is an error.

- The constness matters only for operations that might change the const qualified variable.

  ```cpp
  #include <iostream>

  int main()
  {
    int non_const_number{ 100 };
    const int const_number = non_const_number;	//ok; value of non_const_number is copied to the value of const_number
    int ano = const_number;		//ok; value of const_number is copied to the value of ano
  }
  ```

- const qualified variables must be initialised as they cannot change their values later.

  ```cpp
  const int i = get_size(); // ok: initialized at run time
  const int j = 42; // ok: initialized at compile time
  const int k; // error: k is uninitialized const
  ```

- const variables are local to a file.

<br>

### Const and References

Checkout [const qualifier with references](./05-references.md#const-correctness-with-lvalue-references)

<br>

### Const and Pointers

Checkout [const qualifier with pointers](./04-pointers.md#const-correctness-with-pointers)

<br>
<br>

## Top Level Const

<br>
<br>

## Constant Expression

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

<br>
<br>
