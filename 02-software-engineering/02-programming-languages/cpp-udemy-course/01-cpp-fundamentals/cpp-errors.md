# Syntax Errors

- Error with the syntax of the langauge.

* Example : Missing semi colon

  ```cpp
  #include <iostream>
  int main()
  {
      int favNumber = 10
      return 0;
  }
  ```

<br>
<br>

# Semantic Errors

- Error with the meaning of the code
- Example: We are trying to add varibales of different types

  ```cpp
  #include <iostream>
  int main()
  {
      int favNumber = 10;
      std::string favString = "abcd";
      std::cout << favNumber + favString;
      return 0;
  }
  ```

<br>
<br>

# Linker Errors

- The error generated when all the parts that make up a program cannot be put together because one or more are missing.

* Example: (classic linker error) Here we are saying the compiler to find the deifinition of x elsewhere, the compilation is successfull without any errors however since the linker can not find the definition of x anywhere, it throws an unresolved error.

  ```cpp
  #include <iostream>

  extern int x;

  int main()
  {
      std::cout << x;
      return 0;
  }
  ```

<br>
<br>

# Logic Errors

- Mistakes by the programmer that cause a program to produce incorrect results
