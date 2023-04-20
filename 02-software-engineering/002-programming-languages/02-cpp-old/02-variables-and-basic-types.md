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
	extern int i; // declares but does not define i.
	int j;	// declares and defines j.
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

An identifier is **a sequence of characters used to denote one of the following:** **Object or variable name**.

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

![image](./_assets/2.png)

![image](./_assets/3.png)

<br/>

### Conventions for Variable Names

- An identifier should give some indication of its meaning. 
- Variable names normally are lowercase—`index`,not `Index` or `INDEX`. 
- Like `Sales_item`, classes we define usually begin with an uppercase letter.
- Identifiers with multiple words should visually distinguish each word, for example, `student_loan` or `studentLoan`,not `studentloan`.


<br/>
<br/>

## 2.2.4 Scope of a Name

- A scope is a part of the program in which a name has a particular meaning.
- Most scopes in C++ are delimited by curly braces.
- The same name can refer to different entities in different scopes. 
- Names are visible from the point where they are declared until the end of the scope in which the declaration appears.

`
 > ADVICE:DEFINE VARIABLES WHERE YOU FIRST USE THEM

It is usually a good idea to define an object near the point at which the object is first used. Doing so improves readability by making it easy to find the definition of the variable. More importantly, it is often easier to give the variable a useful initial value when the variable is defined close to where it is first used.


<br/>

### Nested Scopes

Scopes can contain other scopes. The contained (or nested) scope is referred to as an __inner scope__, the containing scope is the __outer scope__.

- Once a name has been declared in a scope, that name can be used by scopes nested inside that scope. 
- Names declared in the outer scope can also be redefined in an inner scope

> It is almost always a bad idea to define a local variable with the same name as a global variable that the function uses or might use.


<br/>
<br/>
<br/>

# 2.3 Compound Types

A compound type is a type that is defined in terms of another type. Pointers and References are famous compound types.

<br/>

## 2.3.1 References

A reference defines an alternative name for an object. A reference type “refers to” another type.

```cpp
int ival = 1024; 
int &refVal = ival; // refValrefers to (is another name for) ival int &refVal2;
int &refVal2;       // error: a reference must be initialized
```

- Ordinarily, when we initialize a variable, the value of the initializer is copied into the object we are creating. When we define a reference, instead of copying the initializer’s value, ___we bind the reference to its initializer.___
- Once initialized, a reference remains bound to its initial object. There is no way to rebind a reference to refer to a different object. Because there is no way to rebind a reference, references must be initialized.

> A reference is not an object. Instead, a reference is just another name for an already existing object. (Reference is an Alias)


- After a reference has been defined, all operations on that reference are actually operations on the object to which the reference is bound:
	- When we assign to a reference, we are assigning to the object to which the reference is bound. 
	- When we fetch the value of a reference, we are really fetching the value of the object to which the reference is bound. 
	- Similarly, when we use a reference as an initializer, we are really using the object to which the reference is bound.
- Because references are not objects, we may not define a reference to a reference.

Each identifier that is a reference must be preceded by the & symbol:

```cpp
int i = 1024, i2 = 2048; // iand i2are both ints 
int &r = i, r2 = i2;     // r is a reference bound to i; r2 is an int
int i3 = 1024, &ri = i3; // i3is an int; riis a reference bound to i3 
int &r3 = i3, &r4 = i2;  // both r3and r4are references
```

- With two exceptions that we’ll cover in § 2.4.1 (p. 61) and § 15.2.3 (p. 601), ___the type of a reference and the object to which the reference refers must match exactly.___

- Moreover, for reasons we’ll explore in § 2.4.1, a reference may be bound only to an object, not to a literal or to the result of a more general expression:
```cpp
double pi = 3.14;
int &math_pi = pi;  //Error a reference of type "int &" (not const-qualified) cannot be initialized with a value of type "double"
int &discount = 10; // initial value of reference to non-const must be an lvalue
```

<br/>
<br/>

## 2.3.2 Pointers

A pointer is a compound type that “points to” another type by holding the address of that object.
- Like references, pointers are used for indirect access to other objects. 
- Unlike a reference, a pointer is an object in its own right. 
- Pointers can be assigned and copied; a single pointer can point to several different objects over its lifetime. 
- Unlike a reference, a pointer need not be initialized at the time it is defined. 
- Like other built-in types, pointers defined at block scope have undefined value if they are not initialized.

<br/>

- We define a pointer type by writing a declarator of the form \*d,where d is the name being defined. 

	```cpp
	int ival = 42; 
	int *p = &ival; // pholds the address ofival; p is a pointer to ival
	```

- Because references are not objects, they don’t have addresses. Hence, we may not define a pointer to a reference.



- We can define multiple pointers in a single line but the \* must be repeated for each pointer variable:

	```cpp
	int *ip1, *ip2;  // both ip1and ip2are pointers to int 
	double dp, *dp2; // dp2is a pointer to double; dp is a double
	```

- With two exceptions, which we cover in § 2.4.2 (p. 62) and § 15.2.3 (p. 601), the types of the pointer and the object to which it points must match:
	```cpp
	double dval; 
	double *pd = &dval; // ok: initializer is the address ofa double 
	double *pd2 = pd;   // ok: initializer is a pointer to double 
	int *pi = pd;       // error: types ofpiand pddiffer 
	pi = &dval;         // error: assigning the address ofa double toapointer to int
	```

<br/>

### Pointer Value 

The value (i.e., the address) stored in a pointer can be in one of four states: 
1. It can point to an object. 
2. It can point to the location just immediately past the end of an object. 
3. It can be a null pointer, indicating that it is not bound to any object. 
4. It can be invalid; values other than the preceding three are invalid.

- It is an error to copy or otherwise try to access the value of an invalid pointer. As when we use an uninitialized variable, this error is one that the compiler is unlikely to detect. The result of accessing an invalid pointer is undefined. Therefore, we must always know whether a given pointer is valid. 
- Although pointers in cases 2 and 3 are valid, there are limits on what we can do with such pointers. Because these pointers do not point to any object, we may not use them to access the (supposed) object to which the pointer points. If we do attempt to access an object through such pointers, the behavior is undefined.

### Using a Pointer to Access an Object

- When a pointer points to an object, we can use the __dereference operator__ (the * operator) to access that object:
	```cpp
	int ival = 42;
	int *p = &ival; // pholds the address ofival; p is a pointer to ival 
	cout << *p;     // *yields the object to which ppoints; prints 42
	```
- Dereferencing a pointer yields the object to which the pointer points. We can assign to that object by assigning to the result of the dereference: 
	```cpp
	*p = 0; // *yields the object; we assign a new value to ivalthrough p 
	cout << *p; // prints 0
	```

- We may dereference only a valid pointer that points to an object.


<br/>
<br/>

### Null Pointers

- A null pointer does not point to any object.

- There are several ways to obtain a null pointer:
	```cpp
	int *p1 = nullptr; // equivalent to int*p1=0; 
	int *p2 = 0;// directly initializes p2from the literal constant 0
	int *p3 = NULL; // equivalent to int*p3=0; must #includecstdlib 
	```

- It is illegal to assign an int variable to a pointer, even if the variable’s value happens to be 0.
	```cpp
	int zero = 0; 
	pi = zero; // error: cannot assign an inttoapointer
	```

<br/>

### Assignment and Pointers

Unlike references which cannot be reassigned (as they are not objects), We can re-assign pointers to point to new objects. Assignment makes the pointer point to a different object :
```cpp
int i = 42;
int *ip = 0; //ip is a nullptr
ip = &i; //ip is now an int pointer pointing i
```

It can be hard to keep straight whether an assignment changes the pointer or the object to which the pointer points. The important thing to keep in mind is that ___assignment changes its left-hand operand.___

<br/>

### void* Pointers

The type void* is a special pointer type that can hold the address of any object.

There are only a limited number of things we can do with a void* pointer: We can compare it to another pointer, we can pass it to or return it from a function, and we can assign it to another void* pointer. We cannot use a void* to operate on the object it addresses—we don’t know that object’s type, and the type determines what operations we can perform on the object.

<br/>
<br/>

## 2.3.3 Understanding Compound Type Declarations

- As we’ve seen, a variable definition consists of a base type and a list of declarators. Each declarator can relate its variable to the base type differently from the other declarators in the same definition. 
- Thus, a single definition might define variables of different types:
	```cpp
	int i = 1024, *p = &i, &r = i; // iis an int; pis a pointer to int; r is a reference to int
	```

<br/>

### Defining Multiple Variables

It is a common misconception to think that the type modifier (* or &) applies to all the variables defined in a single statement.
```cpp
int* p1, p2; // p1 is a pointer to int; p2 is an int
```

<br/>

### Pointers to Pointers

We indicate each pointer level by its own *. That is, we write \** for a pointer to a pointer, \*** for a pointer to a pointer to a pointer, and so on:
```cpp
int my_variable = 100;
int *my_pointer = &my_variable;
int **my_pointer_to_pointer = &my_pointer;
*my_pointer_to_pointer = 1;  //An error,as it refers to my_pointer and we can't assign an int to a pointer.
**my_pointer_to_pointer =1; //legal as it refers to my_variable
```

<br/>

### References to Pointers

- A reference is not an object. Hence, we may not have a pointer to a reference. 
- However, because a pointer is an object, we can define a reference to a pointer:
```cpp
int my_variable = 100;
int *my_pointer = &my_variable;
int *&yo_pointer = my_pointer;  //yo_pointer is a reference to a pointer.
*yo_pointer = 200;  //We are actually dereferencing my_pointer,my_variable is now 200
```


<br/>
<br/>
<br/>

# 2.4 Const Qualifier

> Qualifiers give some property to the identifier, IT IS NOT A TYPE. 

We can make a variable unchangeable by defining the variable’s type as `const`.
Because we can’t change the value of a const object after we create it, ___it must be initialized.___

~~~c
const int bufSize = 512;

bufSize = 480; // error: attempt to write to const object
~~~

<br/>

### Initialization and const
---

~~~c
int num = 42;
const int constNum = num;
int num = constNum;
~~~

- The const(ness) of `constNum` matters only for operation that might change `constNum`. Hence a non-const variable can be copied to a const one.
- Similarly a const variable can be copied to a non-const variable.

<br/>

### By Default, const Objects Are Local to a File

Reason: 

	- compiler will usually replace uses of the variable with its corresponding value during compilation. 
	- To substitute the value for the variable, the compiler has to see the variable’s initializer.
	- When we split a program into multiple files, every file that uses the const must have access to its initializer.
	- In order to see the initializer, the variable must be defined in every file that wants to use the variable’s value.
	- To support this usage, yet avoid multiple definitions of the same variable, const variables are defined as local to the file.

>Therefore, When we define a const with the same name in multiple files, it is as if we had written definitions for separate variables in each file.

* Sometimes we have a const variable that we want to share across multiple files but whose initializer is not a constant expression, In such case, we don’t want
the compiler to generate a separate variable in each file but We want to define the const in one file, and declare it in the other files that use that object.

- ___To share a const object among multiple files, you must define the variable as `extern`.___

~~~c
// file_1.cc defines and initializes a const that is accessible to other files
extern const int bufSize = fcn();

// file_1.h
extern const int bufSize; // same bufSize as defined in file_1.cc

~~~

 #### Concept Clarity

~~~cpp
const int buf; //error : const must be initialised.
int cnt = 0; //legal
const int sz = cnt; //legal
++cnt; //legal
++sz; // error : const canot be modified
~~~

<br/>

### References to const

We can create a reference to const variable but that reference can't modify the const variable. 
~~~c
const int constNum = 10;
const int &constRef = constNum; //the reference must be of const int type.

constRef = 1; //error
~~~

<br/>

### Initialization and References to const

~~~c
double dval = 3.14;
int &ri = dval; //Illegal as dval is of double type
~~~

The first exception for "the type of reference should match the type of the object that is being bound is" :
~~~c
double dval = 3.14;
const int &ri = dval; //legal

/*
compiler transforms the code to something like:

const int temp = deval;
const int &ri = temp;

*/
~~~

<br/>

### A Reference to const May Refer to an Object That Is Not const

- Binding a reference to const to an object says nothing about whether the underlying object itself is const. 
- Because the underlying object might be non const, it might be changed by other means:

~~~c
int num = 10;
int &numRef1 = num;
const int &numRef2 = num;

std::cout << numRef2; //yields 10

numRef1 = 0;

std::cout << numRef2; //yields 0
~~~

>Binding numRef2 to the (nonconst) int num is legal. However, we cannot use numRef2 to changenum. Even so, the value in num still might change. We can change num by assigning to it directly, or by assigning to another reference bound to num, such as numRef1.

<br/>

### Pointers and const

- Like a ___reference to const___, a ___pointer to const___ may not be used to change the object to which the pointer points. 
- We may store the address of a const object only in a pointer to const

~~~c
const int num2 = 20;
int *num2Pointer = &num2; //Ilegal as num2 is a const qualifier.

const int num3 = 30;
const int *num3Pointer = &num3;
*num3Pointer =40; //Ileagal, const can not be modified. 
~~~

we noted that there are two exceptions to the rule that the types of a pointer and the object to which it points must match. 

The first exception is that we can use a pointer to const to point to a nonconst object

~~~c
int num1 = 10;
const int *num1Pointer = &num1;
~~~

>Like a reference to const, a pointer to const says nothing about whether the object to which the pointer points is const. Defining a pointer as a pointer to
const affects only what we can do with the pointer. It is important to remember that there is no guarantee that an object pointed to by a pointer to const won’t change.


>It may be helpful to think of pointers and references to const as pointers or references ”that think they point or refer to const.”

<br/>

### const Pointers

- Unlike references, pointers are objects. Hence, as with any other object type, we can have a pointer that is itself const.
- Like any other const object, a const pointer must be initialized, and once initialized, its value (i.e., the address that it holds) may not be changed.
- We indicate that the pointer is const by putting the const after the *. This placement indicates that it is the pointer, not the pointed-to type, that is const

~~~cpp
int num = 10;
int *const numPointer = &num ; //numPointer will always point to num

const double pi = 3.14159;
const double *const pip = &pi; // pip is a const pointer to a const object. see explanation below

/*
since pi is a const double we have to make pip(const pointer) as a const double too!
*/
~~~

<br/>

### Top-Level const

As pointers are objects, we can talk independently about whether a pointer is const and whether the objects to which it can point are const. 

- We use the term ___top-level___ const to indicate that the pointer itself is a const. 
- When a pointer can point to a const object, we refer to that const as a ___low-level const___.

~~~c++
int num1 = 10;
int *const numPointer1 = &num1; //can't change the value of numPointer1, hence const is top level.

const int num2 = 10; //can't change num, hence const is top level. 
const int *numPointer2 = &num2; //can change numPointer2, hence const is low level.

const int *const numPointer3 = numPointer2; //Left most const is low level, right most is not.

const int &num2Ref =num2; //const in reference is always low level!
~~~

> Top level and low level matter's when copying objects. 
> 1. top level const are ignored, an object can be copied from or copied into a const. 
> 2. low level const's are never ignored. When we copy an object,
both objects must have the same low-level const qualification or there must be a conversion between the types of the two objects. In general, we can convert a nonconst to const but not the other way round.


~~~cpp
int num1 = 10;
int *const num1Pointer = &num1; //top level const pointer.
int *randomPointer = num1Pointer; //top level const can be copied.

const int num2 = 10;
const int *num2Pointer = &num2;
int *anotherRandomPointer = num2Pointer; //ERROR: can't ignore low level const.

//since the object being copied is const qualified type, the type of identifier (anotherRandomPointer) also must be const qualified. 
~~~

<br/>

### `constexpr` and Constant Expressions

- A constant expression is an expression whose value cannot change and that can be evaluated at compile time.
	- A literal is a constant expression. 
	- A const object that is initialized from a co`nstant expression is also a constant expression.

- Whether a given object (or expression) is a constant expression depends on the types and the initializers.

~~~c
int staff_size = 27; //Not a const expr, even though it is initialised from a literal, the type is not const qualified.

const int max_files = 20; //Const expr

const int workload = get_work_load(); //Not a Const expr as the value of initialiser is not known at compile time.

const int additional_files = max_files +1; //const expr
~~~

> Under the new standard C++11, we can ask the compiler to verify that a variable is a constant expression by declaring the variable in a constexpr declaration. 

Variables declared as `constexpr` are implicitly const and must be initialized by constant expressions:

~~~c
constexpr int mf = 20; // 20 is a constant expression
constexpr int limit = mf + 1; // mf + 1 is a constant expression
constexpr int sz = size(); // ok only if size is a constexpr function
~~~

Although we cannot use an ordinary function as an initializer for a `constexpr` variable, The new standard lets us define certain functions as `constexpr`. Such functions must be simple enough that the compiler can evaluate them at compile time. We can use `constexpr` functions in the initializer of a `constexpr` variable.

<br/>

### Literal Types

The types we can use in a `constexpr` are known as “literal types” because they are simple enough to have literal values.

- Of the types we have used so far, the arithmetic, reference, and pointer types are literal types. 
- Our Sales_item class and the library IO and string types are not literal types. Hence, we cannot define variables of these types as `constexprs`.



<br/>
<br/>
<br/>

# 2.6 Defining your own data types.

At the most basic level, a data structure is a way to group together related data elements and a strategy for using those data.

### 2.6.1 structs (Creating `Sales_data`)

~~~cpp
struct Sales_data {
    std::string bookISBN;
    unsigned units_sold = 0;
    double revenue = 0.0;
};
~~~

> The close curly that ends the class body must be followed by a semicolon.

The data members of a class define the contents of the objects of that class type.

Our class has three data members: 
1. a member of type string named `bookNo`. 
1. an unsigned member named `units_sold`.
1. a member of type double named `revenue`.


Each Sales_data object will have these three data members.

- we can supply an in-class initializer for a data member, which will be used to initialize the data members.
- Members without an initializer are default initialized.

<br/>

### 2.6.2 Using Sales_data

the data members in structs can be accessed using the dot operator.

~~~cpp
//given that Sales_data is defined as given in the above code.

int main(){
    Sales_data data1;
    std::cout << "enter isbn..." << std::endl;
    std::cin >> data1.bookISBN;    //accesing data member of the struct.
}
~~~

<br/>

### 2.6.3 Writing own header files

- When we define a class, there may be only one definition of that class in any given source file.
- In addition, if we use a class in several different files, the class’s definition must be the same in each file.
- For the above reason, they are generally defined in header files.

