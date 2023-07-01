# Websites ranking programming langauages

- [TIOBE index](https://www.tiobe.com/tiobe-index/)
- [PYPL ranking](https://pypl.github.io/PYPL.html)
- [IEEE spectrum ranking](https://spectrum.ieee.org/top-programming-languages-2022)
- [Redmonk ranking](https://redmonk.com/sogrady/2022/10/20/language-rankings-6-22/)

<br>
<br>

# Evolution of Cpp

- C++ before C++11 standard is called _Classical C++_ and post C++11 standard is called _Modern C++._

  | Year | Standard                                 |
  | ---- | ---------------------------------------- |
  | 1979 | Bjarne Stroustrup created C with classes |
  | 1989 | Commercial release of C++                |
  | 1998 | C++98 standard                           |
  | 2003 | C++03 standard                           |
  | 2011 | C++11 standard                           |
  | 2014 | C++14 standard                           |
  | 2017 | C++17 standard                           |

<br>
<br>

# C++ is a strongly typed language

A strongly typed language is a programming language in which variables have specific types, and the type of a variable is enforced at compile-time. In a strongly typed language, the type of a variable must be explicitly declared or inferred, and the language's type system ensures that operations and assignments are performed only between compatible types.

<br>
<br>

# C ++ is a structured programming language

Structured programming refers to a programming paradigm that emphasizes the use of structured control flow constructs and modular code organization. An important thing here when we call a function the control will branch to that function and after finishing it, the control automatically comes back to the initial point.

<br>
<br>

# Build Process

## Preprocessor

- A preprocessor is a program that processes the source code before the compiler sees it.
- It strips all the comments from the source file and replaces each comment with a single space.
- Then it looks for preprocessor directives and performs plain text substitution.
- The preprocessor doesn't understand C++ (that is the job of the compiler), It simply get's the source code ready for compilation.

- Preprocessor directive are lines in the source code that begin with a #. Here are some:

  ```cpp
  #include
  #ifdef
  #ifndef
  #define
  #if
  #elif
  #else
  #endif
  #line
  #error
  #pragma
  ```

* For example the #include preprocessor directive replaces that line with the code that is present in the file (referred by the #include preprocessor directive)
* It supports conditional compilation, preprocessor directives can be used to execute OS or platform specific code.

<br>
<br>

## Compiler

- The C++ compiler checks for the syntax and translates the source code to object code (obj file, binary code) and this process is called compilation.
- In the case of a multi-file program, each file is compiled individually into object file.

* The object file contains the compiled code and some metadata but lacks information about other symbols (functions, variables) defined in other source files.
  <br>
  <br>

## Linker

- After compilation, the linker links together all the object files and any library files (.lib, compiled binary code). It combines the object files, libraries, and necessary runtime components to create a stand-alone executable (.exe, binary code)
- When using external libraries, the declaration for the code is present in the header files (h file, text files) and the definitions are compiled library files (lib file, binary code)

* Essentially the linker performs **symbol resolution** (The linker resolves references to symbols (functions, variables) across different object files. If a symbol is referenced in one source file but defined in another, the linker connects the references to their corresponding definitions.) and **library linking** (Libraries are precompiled collections of object files that provide additional functionality. The linker can include necessary libraries to resolve dependencies. Libraries can be either static (linked directly into the executable) or dynamic/shared (loaded at runtime).)

<br>
<br>

> Why is the exe not OS agnostic even though it is binary code? <br> <br> Every executable file has _header info_, which holds certain details with regard to the platform on which the exe was built. ex:
>
> - Was built on 16-bit=, 32-bit etc.. ADDRESSING SYSTEM ?
> - Was built on Intel family CPU or some other ?
> - When the EXE is being launched, which function must be first invoked, what is its address ? <br>

<br>

> <br>
> Hence the exe comprises of the header info, the compiled object code along with the compiled library code. <br>
> <br>

<br>
<br>

# Comments

- In C++, the preprocessor strips out the comments hence the compiler never sees them.

* Single line comments using //
* Multi line comments using /\* \*/

<br>
<br>

# main funciton

- Every C++ program must have only 1 main function, which is the starting point of the program execution.
- A C++ program can have many files and the main fucntion must be present in one of the file.

* There are two versions of the main

  - The below main doesn't expect any OS inforation (ex: program.exe)

    ```cpp
    int main(){
        //code
        return 0;
    }
    ```

  - The below version expects OS info in the form of arguments (ex: program.exe argument1 argument2)

    ```cpp
    int main(int argc, char *argv[]){
        //code
        return 0;
    }
    ```

<br>
<br>

# About Memory

When the exe occupies the process memory (RAM), it organises itself into 4 categories:

<br>

## 1. Code Segment

- It is the area of process memory that holds all code instructions.
- The data on the code segment has the lifetime of the exe.

* The code segment occupies fixed memory size and is not flexible.

<br>

## 2. Data Segment

- It is the area of process memory where all **global** variables, **static** variables and **physical** consts (Literals) reside.
- The data on the data segment has the lifetime of the exe.

* The data segment occupies fixed memory size and is not flexible.

<br>

## 3. Stack

- It is the area of process memory where all function's **local** variables and activation records [function stack-frame] reside.
- The data on the stack has the lifetime of the function.
- The memory occupied by the stack is varible in size and is flexible.

<br>

## 4. Heap

- It is the area of process memory that is used for dynamic memory allocation.
- The lifetime of the data on the heap is controlled by the programmer.
- The memory occupied by the heap is varible in size and is flexible.

<br>
<br>

# Activation Records (function stack frame)

In C++, whenever a function is called and it is handled in a 3 step process: prolog, business-logic and epilog.

<br>

## Prolog

- Upon a function execution, A stack-frame will be created on the stack area of the process. This stack-frame is likely to hold all the formal parameters of the said function if any.

  ```
            |     |  <--stackpointer
  0xHH..   |-----|  <--basepointer     [main function stack ]
  ```

- In the exe (binary), the prolog instructions are generated by the compiler itself.

<br>

## Business Logic

- It is the logic or code present inside the function, written by the programmer

  ```
          |  para2 |  <--stackpointer
          |  para1 |
          |--------|  <--basepointer  [called function stack ]
          | 0xHH.. |
  0xHH..  |--------|                  [main function stack ]
  ```

<br>

## Epilog

- Unwinding of the stack, opposite of prolog

  ```
          |  para2 |
          |  para1 |
          |--------|                     [called function stack ]
          | 0xHH.. |  <--stackpointer
  0xHH..  |--------|  <--basepointer     [main function stack ]
  ```

<br>
<br>

# Calling Convention

- A set of rules that govern the state of activation record or function stack-frame.
- Any language that supports the concept of functions or procedures will have its own set of rules engaging this aspect.

<br>

## Pascal Calling Convention (`__pascal` calling convention)

- The pushing of the arguments onto the activation record is done from LEFT-TO-RIGHT order.
- The de-allocation of the **called** function activation record is the responsibility of the **called** himself.
- Supports fixed-parameter design only.

<br>

## C Calling Convention (`__cdecl` calling convention)

- The pushing of the arguments onto the activation record is done from RIGHT-TO-LEFT order.
- The de-allocation of the **called** function's activation record is the responsibility of the **callee** and not the **called**.
- Supports both fixed-parameter design as well as variable parameter design.

<br>

## Standard Call Calling Convention ( `__stdcall` calling convention)

- The pushing of the arguments onto the activation record is done from RIGHT-TO-LEFT order. [ borrowed from __cdecl ]
- The de-allocation of the CALLED function activation record is the responsibility of the CALLED himself. [ borrowed from __pascal ]
- Supports fixed-parameter design only. [ borrowed from __pascal ]

<br>
<br>

> <br> If we want to support C users as a C++ developpers, we must use C calling convention! <br> <br>

<br>
<br>

# Initialisation vs Assignment in C++

- Initialisation is when the value is bound to the varibale when it is created.
- Assignment is overriding the value (garbage or any existing value) of a varibale by a new value.

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

# Namespaces

- Namespaces in C++ are a way of organizing code into logical groups. They are used to avoid name collisions, which can occur when two different libraries or modules define the same identifier.
- :: is the Scope Resolution Operator and is used to resolve the name we want to use.

```cpp
using namespace std; //Use the entire std namespace
using std::cout; //This is a qualified using namespace where we use only select names
```

<br>
<br>

# Basic input Output

- C++ has cout, cin, cerr and clog representing streams. (must have #include <iostream>)
- cout is the standard output stream that defaults to the console and uses the insertion operator (<<)
- cin is the standard input stream that takes keyboard input and uses the exertion operator (>>)

<br>
<br>

# Running C++ on command line

- Make sure to be in the directort containing the cpp file.
- The following command will result in the executable with default name as a.exe

  ```
  g++ -Wall -std=c++14 main.cpp
  ```

  - here -W is for warnings and -Wall means show all warnings.
  - here -std refers to the standard of C++.
  - main.cpp is the source file.

- The following command can be used to name the executable, main.exe in this case.

  ```
  g++ -Wall -std=c++14 main.cpp -o main.exe
  ```

  - here main.exe is the name of the executable created for main.cpp

* Run the executable by typing just the name of the executable without .exe

<br>
<br>
