# Casting 

## Type conversions (Coersions)

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
<br>


## Explicit casting


### reinterpret_cast

- This casting operator is the most powerful, but also the most dangerous, as it performs low-level reinterpretation of the bits of an object from one type to another.
- It allows you to convert between unrelated types, such as between pointers and integers, but it should be used sparingly and with a deep understanding of the implications.
- It is also called as C style cast or forced cast.

<br>
<br>

### static_cast

- This casting operator is used for performing conversions that are known at compile-time and can be checked for safety.
- It is primarily used for implicit conversions between compatible types, such as converting from one arithmetic type to another or from a pointer to a base class to a pointer to a derived class.
- It supports both upcasting and down casting.
- It is also called safe cast or compile time cast.

<br>
<br>

### dynamic_cast

- It supports only down casting.
- Also called as safe cast or run time cast.

<br>
<br>

### const_cast

-
