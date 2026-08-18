# padding

- In C++, padding refers to the practice of adding extra bytes to a structure or class in order to align its members on specific memory boundaries.
- The purpose of padding is to optimize memory access and improve performance by ensuring that the structure's members are accessed efficiently.

* By default the compiler will consider the largest data attribute of a class for calculating padding. In the following example even though the total size of the data attributes of MyClass is 13 bytes, the output is hinting that the size is 16 bytes. This is because the compiler considers `double d`'s 8 byte (largest data attribute) and tries to fill other data attributes within 8 bytes. If the data can't be fit, it'll padd the remaining bytes and fills the data in the next 8 bytes. (See image)

  ```cpp
  #include <iostream>

  class MyClass
  {
      char c;			//1 byte
      int i;			//4 bytes
      double d;		//8 bytes
  };

  int main()
  {
      MyClass obj;
      std::cout << "The size of the MyClass object is " << sizeof(obj) << " bytes." << std::endl;
  }

  //The size of the MyClass object is 16 bytes.
  ```

> Add Image

- We can set the size considered by the compiler for calculating padding by using `#pragma pack()` in 1,2,4,8... bytes.
- `#pragma pack(1)` essentially means no padding. We are gaining storage size at the expense of accessing speed.

  ```cpp
  #include <iostream>
  #pragma pack(1)

  class MyClass
  {
      char c;			//1 byte
      int i;			//4 bytes
      double d;		//8 bytes
  };

  int main()
  {
      MyClass obj;
      std::cout << "The size of the MyClass object is " << sizeof(obj) << " bytes." << std::endl;
  }

  //The size of the MyClass object is 13 bytes.
  ```

> Add Image

- `#pragma pack(4)` for illustration

  ```cpp
  #include <iostream>
  #pragma pack(4)

  class MyClass
  {
      char c;			//1 byte
      int i;			//4 bytes
      double d;		//8 bytes
  };

  int main()
  {
      MyClass obj;
      std::cout << "The size of the MyClass object is " << sizeof(obj) << " bytes." << std::endl;
  }

  //The size of the MyClass object is 16 bytes.
  ```

> Add Image

<br>
<br>

> <br> It is good practice to order the data attributes in increasing order of their size! This will strike the balance between storage size and accessing speed <br> <br>

<br>
<br>

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

<br>
<br>
