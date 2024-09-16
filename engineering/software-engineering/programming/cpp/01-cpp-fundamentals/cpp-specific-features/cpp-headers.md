# Header Files

**_Header files are files that typically contain declarations of including function prototypes, class definitions, constants, and type definitions; without providing the actual implementation._**

- They have .h file extension.
- They provide an interface to the functionality implemented in source files.

<br>
<br>

## Need for header files

- **Modularity** : Header files facilitates organizing of code.
- **Reusability** : They facilitate code reuse.
- **Encapsulation** : Allows the [seperation of declaration from the implementation](../../04-cpp-oops/02-cpp-encapsulation.md#seperation-of-declaration-and-implementation), It also enables the programmer to conceal the implementation.
- **Avoiding duplicate declarations** : If the source file (.cxx or .cpp) is directly included in another source file, then it'll lead to linking errors as the definitions will be duplicated (one from both translational unit). Same happens if header files without include guards are included. Header files with [include guards](#include-guards) solves this issue.

<br>
<br>

## Preventing Multiple Inclusion

- When a header is included more than once in the same transalation unit, It may lead to

  - Compilation error because of multiple definition.
  - Longer compilation time.
  - Polution of namespace.

- We can prevent multiple inclusion of the header file _in the same translation unit_ in several ways.
- Header files would most likely be included in more than one translation unit, this is not a problem unless the header file contains definitions. In which case the [defintion](../build-process.md#declaration-and-defintion) would appear in more than one translation unit, which is an error.

<br>

### Include Guards

```h
#ifndef ANY_MACRO_H  //this can be any unique name
#define ANY_MACRO_H
//Declarations
#endif //ANY_MACRO_H
```

- `#ifndef` are include guards.
- Include guards check wether the macro (ANY_MACRO_H in this the above code)is defined. If it's not defined, it defines ir and includes the content of the header file. If it's already defined (due to previous inclusion), the content is skipped.

<br>

### Pragma Directive Preprocessor

```h
#pragma once
//Declaration
```

- `pragma` is a compiler-specific directive that tells the preprocessor to include the file only once.

- While widely supported, it might not be supported by all compilers.

<br>

Note that the above mentioned ways donot prevent inclusion of header files in different transalation units.

<br>
<br>
 
## Dependency in header

It is ideal to keep dependencies very less in header files. Instead of including the dependency (`#include <other header>`) directly in the header file, it is ideal to do that in the relevant source file and use forward declarations in the header if needed.

- The illustration describes the reason for the above statement. If header with lot of dependencies is included in other headers, then for every change in any one of the parent header will trigger chain of compilation for all the headers, having dependecies in the source file would solve this problem as source files are not included by other files and any change in the parent dependencies would trigger compilation of the source file itself and would'nt propogate.

  ![image](../../_assets/chain-recomp.png)
