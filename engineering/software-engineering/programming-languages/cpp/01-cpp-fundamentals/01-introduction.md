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

![build](../_assets/build-process.png)

<br>
<br>

## Preprocessor

Some crucial tasks handled are:

- It strips all the comments from the source file and replaces each comment with a single space.
- Then it looks for preprocessor directives and performs plain text substitution.

<br>

### Preprocessor Directive

Preprocessor directive are lines in the source code that begin with a #.

- For example the #include preprocessor directive replaces that line with the code that is present in the file (referred by the #include preprocessor directive)
- It supports conditional compilation, preprocessor directives can be used to execute OS or platform specific code.
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

## Compiler

Compiler checks for C++ syntax and translates the source code to object code.

- In the case of a multi-file program, each file is compiled individually into object files.
- It is important to note that the object files donot necessarily contain all the required code, for instance an object file might call a declared function whose implementation might be present in some other object file. The compiler doesn't raise any error for this!

<br>

### Assembler

During the compilation process the program called assembler converts the source code to assembly instructions which are later translated to object files.

<br>
<br>

## Linker

Linker links together all the object files to create an executable.

Primary tasks are:

- Symbol Resolution : If a symbol is referenced in one source file but defined in another, the linker connects the references to their corresponding definitions.
- Library Linking : Libraries will most likely have the declarations in header .h files and implementations in library .lib files. Linker resolves library dependencies statically (linked directly into the exe) or dynamically (loaded at runtime).

The executable file is OS specific even though it is binary code. This is because of the header info present in the binary which contains OS related data like build platform, system architecture, CPU etc.

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

# Activation Records (function stack frame)

In C++, whenever a function is called and it is handled in a 3 step process: prolog, business-logic and epilog.

![acti](../_assets/activation-record.png)

- The prolog instructions are written by the compiler and will be present in the exe.

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

# Initialisation vs Assignment in C++

_**Initialisation** is when the value is bound to the varibale when it is created._

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
