# Variables

_**Variables** are abstractions for memory locations in C++._

- variables have **type** and **value**.
- variables must be declared before it is used in C++.

<br>
<br>

## Variable Declaration

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
<br>

## Variable Initialization

<!-- TODO
Need to revamp this part

initiaisation can be categorised as
    scalars (single values)
    aggregates (like arrays)
    classes, add in class notes and add a link here
 -->

_**Initialisation** is when the value is bound to the variable when it is declared._

- Unitialised variables have random garbage values.
- Different types of variable initialisation.

  ```cpp
  int age; //uninitialised
  int age = 10; //C-like initialization
  int age (21); // Constructor initialization
  int age {21} ; // C++11 list initialization
  ```

<br>

### Default Initialization

When a variable is defined without an initializer, it is default initialised.

- For built-in types,
  - If the variable is defined outside any function, it is initialised to zero.
  - If the variable is defined inside the function, it is uninitialised with undefined value.
- For user-defined types,
  - Most classes lets objects to be defined without explicit initializers.
  - Some classes require that every object be explicitly initialized.

<br>
<br>

## Variable Assignment

_**Assignment** is overriding the value (garbage or any existing value) of a varibale by a new value._

```cpp
int main()
{
	int a{ 0 };		//initialisation: 0 is stored in a as soon as a is created

	int b;			//b has some garbage value
	b = 10;			//assignment: b now stores 10 instead of the garbage value
}
```

<br>
<br>

## Global Variables

- Uninitialised global variables have value 0.
- global variables are accessible throught the program

<br>
<br>
<br>
