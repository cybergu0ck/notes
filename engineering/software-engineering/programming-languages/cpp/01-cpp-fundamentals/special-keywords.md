# extern keyword

- When used in the context of global variables, `extern` is used to declare a variable that is defined in another source file or translation unit. It extends the visibility and linkage of the variable to multiple files, allowing them to access and share the same global variable.

  ```cpp
  //file1.cpp
  int a{10};
  ```

  ```cpp
  //file2.cpp
  #include <iostream>

  extern int a;

  int main()
  {
      std::cout << a << std::endl;  //10
  }
  ```

<br>
<br>
<br>

# `const` correctness

<br>

## const correctness with references

- a reference to a const datatype must also be const

  ```cpp
  int main()
  {
    const int a{ 10 };
    int& ref1 = a;        //error
    const int& ref2 = a;  //ok
  }
  ```
