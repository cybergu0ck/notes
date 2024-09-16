# Polymorphism

Polymorphism is the ability to use the same code to operate on different types of objects. This makes the code more flexible.

<br>
<br>

# Types of Polymorphism in C++

- C++ supports two types of polymorphism.
  1. Compile Type / Early Binding / Static Binding
  2. Run Time / Late Binding / Dynamic Binding

<br>
<br>

# Compile Time Polymorphism

- Compile time polymorphism occurs before the program is run i.e. during the compilation.
- This is the default case in C++.
- Function overloading and operator overloading are examples.
- Compile time polymorphism is also called as early binding or static binding.

<br>
<br>

# Naming Convention

## C++ Naming Convention

- This is the default naming convention in C++. Here the function names are subjected to name mangling (and are decorated) done by the compiler.

* We can see this either:

  - By generating the assembly files (.asm) [This is for Visual Studio Environment and not for G++ compiler based environments!]

    - Project Properties > Configuration Properties > C/C++ > Output Files > Set Assembler Output : (/FA)
    - After compiling, open the asm file that is generated in the VS project folder (x64 > Debug > filename.asm)
    - use Search (Ctrl + F) and search as follows `Line <line number where function is called>`

    ```asm
    ; Line 21
      call	?fun@@YAXXZ				; fun
    ```

  - using `__FUNCDNAME__` and printing it to the console.
    ```cpp
    void fun()    //under the hood: extern "C++" void __cdecl fun()
    {
      cout << __FUNCDNAME__ << endl;    //?fun@@YAXXZ is printed when fun is called.
    }
    ```

<br>

- This is how, C++ supports polymorphic functions! Even though in our text files (.h and .cpp) we see overloaded functions having the same name, This is not true under the hood. C++ compiler will mangle the names and each overloaded function will have unique name.

* Here we see overloaded functions (has same name but different parameters)

  ```cpp
  #include <iostream>

  void fun()
  {
    std::cout << "first fun" << std::endl;
  }

  void fun(char c)
  {
    std::cout << "overloaded fun" << std::endl;
  }

  int main()
  {
    fun();		//this is line 16
    fun('x');	//this is line 17
  }
  ```

* Compiling and search the line numbers in the asm files we ca see the the unique decorated names.

  ```asm
  ; Line 15
    call	?fun@@YAXXZ				; fun
  ; Line 16
    mov	cl, 120					; 00000078H
    call	?fun@@YAXD@Z				; fun
  ```

<br>
<br>

## Raw names and understanding decorated names

<br>

- In order to decorate the compiler uses 'raw-names'.

* `typeid(char).raw_name()` is the syntax to cout raw name of char data type.

* The raw names for the primitive data types are as follows:

  | primitive name         | raw name |
  | ---------------------- | -------- |
  | raw name for char is   | .D       |
  | raw name for int is    | .H       |
  | raw name for float is  | .M       |
  | raw name for double is | .N       |
  | raw name for bool is   | .\_N     |
  | raw name for void is   | .X       |

- Undersanding the decorated global functions (like: ?fun@@YAXXZ)

  | syntax | meaning                                                                                           |
  | ------ | ------------------------------------------------------------------------------------------------- |
  | ?fun   | starts with a standard '?' followed by the original function name                                 |
  | @@     | stringizing operator, that clubs 2 strings [ the original name and the compiler generated string] |
  | Y      | starts with 'Y' for all global functions                                                          |
  | A      | calling convention indicator, 'A' indicates it is using the default calling convention            |
  | X      | return-type indicator, returns 'void'                                                             |
  | X      | input(s) indicator, input is 'void'                                                               |
  | Z      | ends with 'Z' for all functions                                                                   |

<br>

- All member functions of a class follow **only** _C++ naming convention_. We use naming conventions (extern "C") to provide backward compatibility foe C users. classes (specifically member functions of the classes) makes no sense for C users and hence the reason.

* Undersanding the decorated member functions (like: ?input@CA)

  | syntax    | meaning                                                                                         |
  | --------- | ----------------------------------------------------------------------------------------------- |
  | ?input@CA | 'input' is a member function of class CA                                                        |
  | Q         | Indicates the access-specifier [Q means public], whether 'public' (or) 'private' (or) protected |
  | A         | Indicates whether the method is a const method or non-const method ['A' means non-const method] |
  | E         | Indicates the calling convention employed [E means it is using the def. calling convention]     |
  | X         | return type is void                                                                             |
  | X         | input to the function is also void                                                              |
  | Z         | Z is the de-limiting character.                                                                 |

<br>
<br>

## C Naming Convention

- There is no such name mangling in C (hence no support for polymorphic functions)
- Hence if C++ developper need to support C users, they have to mitigate the name mangling done by the compiler (else the names would look right in text files h and cpp but under the hood they are decorated and when the C user calls the functions, it is not found in the binary!)
- This is done by using C naming convention

* Here, we can see that the function names are not decorated

  ```cpp
  #include <iostream>

  extern "C" void fun()
  {
    std::cout << __FUNCDNAME__ << std::endl; //fun
  }


  int main()
  {
    fun();
  }
  ```

<br>

> <br> C++ naming convention facilitates decoration, thereby supports function overloading (and polymorphism).
> C naming convention does not facilitate decoration, thereby does not support function overloading (and polymorphism) <br> <br>

<br>

- Some nuances are listed here

  ```cpp
  //OK, can overload
  void fun();            // ===> extern "C++" void fun();      ===>  _Z3funv (g++),  ?fun@@YAXXZ
  void fun(int x);       // ===> extern "C++" void fun(int x); ===>  _Z3funi,  ?fun@@YAXH@Z

  //CANNOT OVERLOAD, AMBIGUITY ERROR
  extern "C" void fun();      // ===>  fun
  extern "C" void fun(int x); // ===>  fun

  //OK, CAN BE OVERLOADED
  extern "C" void fun();        // ===>  fun
  extern "C++" void fun(int x); // ===>  _Z3funi,  ?fun@@YAXH@Z

  extern "C" void fun();    //  ===>  fun
  extern "C++" void fun();  // ===>  _Z3funV, ?fun@@YAXXZ

  //CALL STATEMENT, leads to ambiguity error
  fun();  //will lead to ambiguity error, compiler has too many options, does not know which function to bind to.
  ```

* As a library developper we can group all the functions in both h and cpp files and make them extern "C" (check syntax online if needed)

<br>
<br>
