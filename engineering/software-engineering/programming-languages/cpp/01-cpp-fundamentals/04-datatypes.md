# C++ Primitive datatypes

size and precision of a data type is dependent on the platform and the compiler.

## character datatype

| Type     | Size                                              |
| -------- | ------------------------------------------------- |
| char     | 1 byte (8 bits)                                   |
| char16_t | Atleast 16 bits                                   |
| char32_t | Atleast 32 bits                                   |
| wchar_t  | can represent the largest available character set |

<br>

## Integer datatype

#TODO - Finish this whole file

<br>
<br>
<br>

# Type conversions (Coersions)

- Higher types are the types that can hold larger values.
- Lower types are the types with less size.
- _Lower types can be converted to higher types as lowertype can fit in the size of higher type._
- example : short and char types are always converted to ints

* Promotion : Conversion to a higher type, generally occurs in math expressions.

  ```cpp
  int main()
  {
      int num1 = 1;
      double num2 = 2.5;
      cout << num1 + num2; //3.5
      return 0;
  }
  ```

* Demotion : Converion to a lower type, generally occurs in assignments.

  ```cpp
  int main()
  {
      int num {0};
      num = 100.2
      cout << num;    //100
      return 0;
  }
  ```

<br>

## Explicit type casting

- `static_cast <type>` is used to cast something to `type`.

<br>
<br>
