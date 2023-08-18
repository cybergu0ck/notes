# Enumerations

- A enumeration is a user defined type that models a set of constant integral values.
- Using enumerations increases readability and decreases logical errors.
- The structure of an enumeration is as follows:

  ```
  enum-key enum-name : enumerator-type {};
  ```

  - enum-key defines the scope of the enumeration.
  - enum-name is the optional name of the enumeraion.
  - enumerator-type can be ommitted as the compiler is capable of deducing it.
  - the enumerators are listed inside { }.

<br>
<br>
<br>

# Initialisation of enumerators

## Implicit Initalization

- The compiler will initialise the enumerators

  ```cpp
  #include <iostream>

  enum {Red, Green, Blue};

  int main() {
      int my_color;
      my_color = Green;
      std::cout << my_color << std::endl; //1
  }

  //Red is initialised to 0 and Blue is initialised to 2
  ```

<br>
<br>

## Explicit Initialisation

- We intialise the enumerators explicitely

  ```cpp
  #include <iostream>

  enum {Red=1, Green=3, Blue=5};

  int main() {
      int my_color;
      my_color = Green;
      std::cout << my_color << std::endl; //3
  }
  ```

<br>
<br>

## Implicit/Exlicit Initialisation

- The compiler will increment the explicitely intialised integral value by 1 for subsequent enumerators.

  ```cpp
  #include <iostream>

  enum {Red=10, Green, Blue};

  int main() {
      int my_color;
      my_color = Green;
      std::cout << my_color << std::endl; //11
  }
  ```

<br>
<br>
<br>
 
# Enumeration names

- Enumeration names provide type safety. On the contrary, enumeration defined without names are anonymous and provide no type safety.

* Anonymously defined enumeration with no type safety.

  ```cpp
  #include <iostream>

  enum {Red, Green, Blue};

  int main() {
      int my_color;
      my_color = Green; //valid
      my_color = 100; //also valid
  }
  ```

* enumerations with type safety

  ```cpp
  #include <iostream>

  enum Color {Red, Green, Blue};

  int main() {
      Color my_color;
      my_color = Green; //valid
      my_color = 100; //error (type safety)
  }
  ```
