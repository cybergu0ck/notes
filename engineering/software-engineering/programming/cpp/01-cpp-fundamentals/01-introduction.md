# Evolution of C++

C++ before C++11 standard is called **Classical C++** and post C++11 standard is called **Modern C++**.

<br>

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
<br>

# Nature of C++

### C++ is a strongly typed language

A strongly typed language is a programming language in which variables have specific types, and the type of a variable is enforced at compile-time. In a strongly typed language, the type of a variable must be explicitly declared or inferred, and the language's type system ensures that operations and assignments are performed only between compatible types.

<br>

### C ++ is a structured programming language

Structured programming refers to a programming paradigm that emphasizes the use of structured control flow constructs and modular code organization. An important thing here when we call a function the control will branch to that function and after finishing it, the control automatically comes back to the initial point.

<br>
<br>

# Build Process

[Header files](./cpp-specific-features/cpp-headers.md) typically contain declarations, including function prototypes, class definitions, constants, and type definitions.

Source files contain the actual implementations of the functions and classes declared in header files.

<br>

![build](../_assets/build-process.png)

<br>
<br>

## 1. Preprocessing

**_Preprocessing is the process of handling preprocessor directives and generating an expanded version of the source code._**

- Preprocessing is carried out by a preprocessor and it's tasks are:

  1. It strips all the comments from the source file and replaces each comment with a single space.

  2. Then it looks for preprocessor directives and performs plain text substitution.

<br>

### Preprocessor Directive

**_A preprocessor directive is a command in the source code that instructs the preprocessor to perform specific actions before the compilation process._**

- Preprocessor directive begin with a #.

- The `#include` directive replaces that line with the code that is present in the file (referrred by the directive, generally a header file)
- The `#define` directive performs macro substituition.
- It supports conditional compilation, preprocessor directives can be used to execute OS or platform specific code (using `#ifdef`, `#ifndef`, `#endif`, etc.).

- Some of the preprocessor directives are:

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

<br>
<br>

## 2. Compilation

**_Compilation is the process of converting the source code (cpp files) to the machine code (obj files)._**

- Technically the source code is converted to assembly instructions using an **assembler**, which is then translated to object code.

- A single source file (including the h files that it includes) is called a **translation unit**.
- Compiler checks for C++ syntax and translates the source code to object code.

- Each source file is compiled individually into an object file. Hence, a single object file may not contain all the necessary code, meaning the object file can contain code without implementation for it (beacause of declarations) and the implementation will be present in some other object file.

<br>
<br>

## 3. Linking

**_Linking is the process of combining object files and libraries to produce a single executable file or a shared library._**

- **Symbol Resolution :** If a symbol is referenced in one object file but defined in another object file or a library, the linker connects the references to their corresponding definitions.

The executable file is OS specific even though it is binary code. This is because of the header info present in the binary which contains OS related data like build platform, system architecture, CPU etc.

<br>

## Library Linking

Libraries can be liked wither statically or dynamically.

#### Static Linking of libraries

**_Static linking is the process of linking a static library, where the symbols are resolved and linked at compile time, into the executable itself._**

- A static library is a precompiled object code (It contains the implementations of the library).
- They have .lib file extension in windows and .a (archive file) in linux.
- The executable derived after static linking contains all the necessary code.
- Other programs (executables) cannot share the static library because they need to be linked at compile time, to the executable itself.

<br>

#### Dynamic Linking of libraries

**_Dynamic linking is the process of linking a dynamic library, where the symbols are resolved and linked at run time, when the dynamic library is loaded to the memory._**

- A dynamic library is also a precompiled object code (It contains the implementations of the library).
- They have .dll (dynamic link library) file extension in windows and .so (shared object) in linux.
- The executable derived after dynamic linking doesnt contain the implementations for the code used from the library.
- This allows multiple programs (executables) to share a single copy of the dynamic library because they are linked at runtime, when they are loaded in memory.

<br>
<br>
<br>

# Comments

- In C++, the preprocessor strips out the comments hence the compiler never sees them.
- Single line comments using //
- Multi line comments using /\* \*/

<br>
<br>
<br>

# `main` function

- Every C++ program must have only 1 `main` function, which is the starting point of the program execution.
- A C++ program can have many files and the `main` fucntion must be present in one of the file.
- There are two versions of the main

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
<br>

# C++ Memory

When the exe occupies the process memory (RAM), it organises itself into 4 categories:

<br>

| Type         | Contains                                                       | Size     | Lifetime                 |
| ------------ | -------------------------------------------------------------- | -------- | ------------------------ |
| Code Segment | Code Instructions                                              | Fixed    | Lifetime of exe          |
| Data Segment | Global Variables, Static Variables, Physical consts (literals) | Fixed    | Lifetime of exe          |
| Stack        | Local Variables, Activation Records (function stack frame)     | Flexible | Lifetime of the function |
| Heap         | Used for Dynamic Memory Allocation                             | Flexible | Controlled by dev        |

<br>
<br>
<br>

# Calling Convention

A set of rules that govern the state of activation record or function stack-frame.Any language that supports the concept of functions or procedures will have its own set of rules engaging this aspect.

<br>

| Calling Convention | Syntax      | Pushing order | Responsibility of De-allocation of called function | Parameter Design   |
| ------------------ | ----------- | ------------- | -------------------------------------------------- | ------------------ |
| Pascal             | \_\_pascal  | Left to Right | Called function itself                             | Fixed              |
| C                  | \_\_cdecl   | Right to Left | Callee function                                    | Fixed and Variable |
| Standard           | \_\_stdcall | Right to Left | Called function itself                             | Fixed              |

> <br> If we want to support C users as a C++ developpers, we must use C calling convention! <br> <br>

<br>
<br>
<br>

# Namespaces

_**Namespace** is a declarative region that provides a way to organize code into logical groups and avoid naming conflicts._

```cpp
using namespace std; //Use the entire std namespace
using std::cout; //This is a qualified using namespace where we use only select names
```

- `::` is the Scope Resolution Operator and is used to resolve the name we want to use.

<br>
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

#TODO - Go through this concept and make sophesticated notes on this topic

<br>
<br>
