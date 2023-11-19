# Variables

_**Varibales** are abstractions for memory locations in C++._

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
