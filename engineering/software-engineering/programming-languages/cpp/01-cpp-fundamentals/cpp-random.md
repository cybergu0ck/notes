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
