# Header Files

**_Header files are files that typically contain declarations of functions, classes, variables, and other constructs, without providing the actual implementation._**

<br>
<br>

## Need for header files

- **Modularity** : Header files facilitates organizing of code.
- **Reusability** : They facilitate code reuse.
- **Encapsulation** : Allows the [seperation of declaration from the implementation](../../04-cpp-oops/02-cpp-encapsulation.md#seperation-of-declaration-and-implementation), It also enables the programmer to conceal the implementation.
- **Avoiding duplicate declarations** : If the source file (.cxx or .cpp) is directly included in another source file, then it'll lead to linking errors as the definitions will be duplicated (one from both translational unit). Same happens if header files without include guards are included. Header files with [include guards](#include-guards) solves this issue.

<br>
<br>

## Include Guards

- without include guards, the compiler will see the declaration everytime the header file is included in a file. (this is an error)
- there are two kinds:

  1. using `ifndef` directive preprocessor

     ```h
     #ifndef _ACCOUNT_H_  //this can be any unique name
     #define _ACCOUNT_H_

     //account class declaration

     #endif
     ```

  1. using `pragma` directive preprocessor

     ```h
     #pragma once

     //account class declaration
     ```

<br>
<br>
