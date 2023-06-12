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

# C++ Build Process

- Program : It's like a recipe! full of instructions.
- Programming Language : Source code, High level (understable to humans)
- Binary : Object code, Low Level (understandable to computers)
- Compiler : Translates High level source code to Low level Object code.
- Linker : Links our object code with other object code (of libraries) and creates an executable program.
- Syntax : The rules that must be followed when writing programs in specific programming languages

<br>
<br>

# Preprocessor

- A preprocessor is a program that processes the source code before the compiler sees it.
- It strips all the comments from the source file and replaces each comment with a single space. Then it looks for preprocessor directives and executes them.
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
