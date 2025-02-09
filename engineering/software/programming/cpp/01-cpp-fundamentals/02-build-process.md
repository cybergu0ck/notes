# Build Process

[Header files](./cpp-specific-features/cpp-headers.md) typically contain declarations, including function prototypes, class definitions, constants, and type definitions.

Source files contain the actual implementations of the functions and classes declared in header files.

<br>

![build](../_assets/build-process.png)

<br>
<br>

## Preprocessing

**_Preprocessing is the process of handling preprocessor directives and generating an expanded version of the source code._**

- Preprocessing is carried out by a preprocessor and it's tasks are:

  1. It strips all the comments from the source file and replaces each comment with a single space.

  2. Then it looks for preprocessor directives and performs plain text substitution.

<br>

#### Preprocessor Directive

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

## Compilation

**_Compilation is the process of converting the source code (cpp files) to the machine code (obj files)._**

- Technically the source code is converted to assembly instructions using an **assembler**, which is then translated to object code.

- A single source file (including the h files that it includes) is called a **translation unit**.
- Compiler checks for C++ syntax and translates the source code to object code.

- Each source file is compiled individually into an object file. Hence, a single object file may not contain all the necessary code, meaning the object file can contain code without implementation for it (beacause of declarations) and the implementation will be present in some other object file.

<br>
<br>

## Linking

**_Linking is the process of combining object files and libraries to produce a single executable file or a shared library._**

- **Symbol Resolution :** If a symbol is referenced in one object file but defined in another object file or a library, the linker connects the references to their corresponding definitions.

The executable file is OS specific even though it is binary code. This is because of the header info present in the binary which contains OS related data like build platform, system architecture, CPU etc.

<br>

### Library Linking

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
