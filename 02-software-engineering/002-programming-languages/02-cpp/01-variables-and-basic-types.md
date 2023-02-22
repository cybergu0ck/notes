Types determines the meaning of the data and operations in our programs.


# 2.1 Primitive Built-in types
C++ defines a set of primitive types that include the __arithmetic types__ and a special type named __void__.

## 2.1.1 Arithmetic Types

![image](./_assets/1.png)

<br/>

#### Signed and Unsigned types

> Make notes

<br/>

## 2.1.2 Type conversions

Among the operations that many types support is the ability to convert objects of the given type to other, related types.
- Type conversions happen automatically when we use an object of one type where an object of another type is expected

```cpp
bool b = 42;   // bis true
int i = b;     // ihas value 1
i = 3.14;      // ihas value 3
double pi = i; // pihas value 3.0
unsigned char c = -1; // assuming 8-bit chars, chas value 255 signed char c2 = 256; 
signed char c2 = 256; // assuming 8-bit chars, the value ofc2is undefined
```

<br/>
<br/>

## 2.1.3 Literals

- when a value is self evident it is a literal.
- Every literal has a type. The form and value of a literal determine its type.

<br/>

### Integer and Floating-Point Literals

- We can write an integer literal using decimal, octal, or hexadecimal notation.
- Normal integers are decimal
	```
	20
	```
- Integer literals that begin with 0 (zero) are interpreted as octal.
	```
	024
	```
- Those that begin with either 0x or 0X are interpreted as hexadecimal. 
	```
	0x14
	```


- Although integer literals may be stored in signed types, technically speaking, the value of a decimal literal is never a negative number. If we write what appears to be a negative decimal literal, for example, -42, the minus sign is not part of the literal. The minus sign is an operator that negates the value of its (literal) operand.

- Floating-point literals include either a decimal point or an exponent specified using scientific notation. Using scientific notation, the exponent is indicated by either E or e:
	```
	3.14159 3.14159E0 0. 0e0 .001
	```

<br/>

### Character and Character String Literals

- A character enclosed within single quotes is a literal of type char.
	```
	’a’ // character literal
	```
- Zero or more characters enclosed in double quotation marks is a string literal:
	```
	"Hello World!" // string literal
	```

<br/>

### Escape Sequences

Our programs cannot use any of these characters directly. Instead, we use an escape sequence to represent such characters. An escape sequence begins with a backslash.


| Escape Sequence     | symbol |
| ----------- | ----------- |
| Newline   | \n       |
| Horizontal tab   | \t        |
| Vertical Tab | \v |
| alert (bell) | \a |
| Backspace | \b |
|Double quote | \\" |
| Single Quote | \\' |
| Backslash | \\\ |
| Carriage Return | \r |


<br/>

### Boolean and Pointer Literals

- The words true and false are literals of type bool
- The word nullptr is a pointer literal

<br/>
<br/>
<br/>

# 2.2 Variables

___A variable provides us with named storage that our programs can manipulate.___
- Each variable in C++ has a type. The type determines the size and layout of the variable’s memory, the range of values that can be stored within that memory, and the set of operations that can be applied to the variable. 
- C++ programmers tend to refer to variables as “variables” or “objects” interchangeably.

<br/>

## 2.2.1 Variable Definitions

- A simple variable definition consists of a __type specifier__, followed by a list of one or more variable names separated by commas, and ends with a semicolon.
- A definition may (optionally) provide an initial value for one or more of the names it defines

```cpp
int sum=0, value, units_sold =0 ;
```

<br/>

###  Initializers

- An object that is initialized gets the specified value at the moment it is created.
- When a definition defines two or more variables, the name of each object becomes visible immediately. Thus, it is possible to initialize a variable to the value of one defined earlier in the same definition.

> Initialization in C++ is a surprisingly complicated topic. Many programmers are confused by the use of the = symbol to initialize a variable. _It is tempting to think of initialization as a form of assignment, but initialization and assignment are different operations in C++_.

> Initialization is not assignment. Initialization happens when a variable is given a value when it is created. Assignment obliterates an object’s current value and replaces that value with a new one.

<br/>

### List Initialization

we can use any of the following four different ways to define an` int` variable named `units_sold` and initialize it to 0:
```cpp
int units_sold = 0; 
int units_sold = {0}; 
int units_sold{0};  // This is list initialzation
int units_sold(0);
```

<br/>

### Default Initialization

When we define a variable without an initializer, the variable is default initialized. Such variables are given the “default” value. What that default value is depends on the type of the variable and may also depend on where the variable is defined.


> Make Notes


<br/>
<br/>

## 2.2.2 Variable Declarations and Definitions

- ___Separate compilation___ lets us split our programs into several files, each of which can be compiled independently.
	- When we separate a program into multiple files, we need a way to share code across those files. 
	- To support separate compilation, C++ distinguishes between declarations and definitions.  
   
- A declaration makes a name known to the program. A file that wants to use a name defined elsewhere includes a declaration for that name. 

- A definition creates the associated entity.

<br/>

- A variable declaration specifies the type and name of a variable. A variable definition is a declaration. In addition to specifying the name and type, a definition also allocates storage and may provide the variable with an initial value.

- To obtain a declaration that is not also a definition, we add the extern keyword and may not provide an explicit initializer:
	```cpp
	extern int i; // declares but does not define i int j;
	int j;	// declares and defines j
	```
 - We can provide an initializer on a variable defined as extern, but doing so overrides the extern.An extern that has an initializer is a definition:
	```cpp
	extern double pi = 3.1416; // definition
	```
- It is an error to provide an initializer on an extern inside a function.

> Variables must be defined exactly once but can be declared many times.

- To use the same variable in multiple files, we must define that variable in one—and only one—file. Other files that use that variable must declare—but not define—that variable.


<br/>
<br/>

## 2.2.3 Identifiers

- Identifiers in C++ can be composed of letters, digits, and the underscore character. 
- The language imposes no limit on name length. 
- Identifiers must begin with either a letter or an underscore. 
- Identifiers are case-sensitive; upper- and lowercase letters are distinct.
	```cpp
	// defines four different intvariables 
	int somename, someName, SomeName, SOMENAME;
	```
- The language reserves a set of names, listed in Tables 2.3 and Table 2.4, for its own use. These names may not be used as identifiers
- The identifiers we define in our own programs may not contain two consecutive underscores
- Nor can an identifier begin with an underscore followed immediately by an uppercase letter. 
- In addition, identifiers defined outside a function may not begin with an underscore.