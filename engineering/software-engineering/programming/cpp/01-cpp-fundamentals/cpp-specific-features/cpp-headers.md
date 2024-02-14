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

- without include guards, the compiler will see the declaration everytime the header file is included in source files. (this is an error)

  ```h
  #ifndef _ANY_MACRO_H_  //this can be any unique name
  #define _ANY_MACRO_H_

  //Declarations

  #endif
  ```

  - `#ifndef` are include guards.
  - Include guards check wether the macro (_ANY_MACRO_H_ in this the above code)is defined. If it's not defined, it defines ir and includes the content of the header file. If it's already defined (due to previous inclusion), the content is skipped.
  - The [pragma directive preprocessor](#pragma-directive-preprocessor) can also be used.

<br>
<br>

## Pragma Directive Preprocessor

`pragma` is a compiler-specific directive that tells the preprocessor to include the file only once.

```h
#pragma once

//Declaration
```

- While widely supported, it might not be supported by all compilers.
