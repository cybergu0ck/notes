# Variables

- varibales are abstractions for memory locations in C++.

* variables have **type** and **value**.
* variables must be declared before it is used in C++.

<br>

## Declaring variables

```
variableType variableName;
```

<br>

- Variable names can contain letters, numbers and underscores.
- Variable names must begin with a letter or an underscore.
- Variable names are case sensitive.
- Variable names cannot be reserved keywords.
- Variable names cannot be redeclared.
- Use either camelCase or snake_case and be consistent with it.

<br>

## Initialising variables

- unitialised variables have random values.
- Different types of variable initialisation.

  ```cpp
  int age; //uninitialised
  int age = 10; //C-like initialization
  int age (21); // Constructor initialization
  int age {21} ; // C++11 list initialization
  ```

<br>
<br>

# Global varibales

- uninitialised global variables have value 0.
- global variables are accessible throught the program


<br>
<br>
<br>

# Constants

- constants are variables that connot change their value.

<br>

## Types of constants in C++

### 1. Literal Constants

- They are values that are represented directly in the code. They can be used to represent numbers, characters, strings, and Boolean values.
- examples:
  - integer literal constants like 12, 12u (unsigned integer), 12l (long integer), 12ll (long long integer)
  - floating point literal constatants like 12.1 (Double), 12.1F (Float), 12.1 (Long Double)
  - character literal constants like \n, \t etc

<br>

### 2. Declared constants

- constants declared using the `const` keyword.

  ```cpp
  const int year = 2000;
  ```

<br>

### 3. Defined constants

- constants declared using #define preprocessor directive
- Donot use this is modern C++.

  ```cpp
  #define pi 3.141
  ```
