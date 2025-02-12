# Enumeration

_**Enumeration** is a user defined type that consists of a set of named integral constants._

- Using enumerations increases readability and decreases logical errors.

<br>
<br>

## Enumeration Syntax

```
enum name : type {};
```

- "enum" is a keyword.
- "name" is the optional name of the enumeraion.
- "type" can be ommitted as the compiler is capable of deducing it.
- the enumerators are listed inside { }.

<br>
<br>

## Initialisation of enumerators

Enumerations can be implicitely or explicitely initialised as shown here.

```cpp
#include<iostream>

enum {Red, Green, Blue};  // Implicit Initialisation => Red=0, Green=1, Blue=2
enum {Normal=400, Critical=653};  //Explicit Initialisation => Normal=400, Critical=653
enum {Slow=10, Decent, Fast};  //Implicit-Explicit Initalisation => Slow=10, Decent=11, Fast=12

int main(){
    std::cout << Green << "\n";     //1
    std::cout << Critical << "\n";  //653
    std::cout << Decent << "\n";    //11
}
```

<br>
<br>

## Type Safety of Enumerations

### Un-Named Enumeration

Un-named enumerations are anonymous. They are not type-safe.

```cpp
#include<iostream>

enum {Red, Green, Blue};

int main(){
    int my_color = Red;
    std::cout << my_color << "\n";  //0
    my_color = 100;                 //This is allowed by the compiler as the type of my_color is "int"
    std::cout << my_color << "\n";  //100

}
```

<br>

### Named Enumeration

Named enumerations are type safe.

```cpp
#include<iostream>

enum Color{Red, Green, Blue};

int main(){
    Color my_color = Red;
    std::cout << my_color << "\n";  //0
    my_color = 2;  //a value of type "int" cannot be assigned to an entity of type "Color"
}
```

<br>
<br>

## Scoping of Enumerations

### Unscoped Enumeration

If enumerations are unscoped, any other variable or enum in that scope (global) cannot have the same name as any of the enumerators.

```cpp
#include<iostream>

enum Color{Red, Green, Blue};

float Green{56.6};  //error: 'float Green" redeclared...

int main(){
    std::cout << Green << "\n";
}
```

- It also facilitates buggy code with logical errors.

  ```cpp
  #include <iostream>

  enum Whale{Blue, Beluga, Gray};
  enum Shark{Greatwhite, Hammerhead, Bull};


  int main() {
    if (Beluga == Hammerhead) {
      std::cout << "A beluga whale is equvivalent to a hammerhead shark.";
    }
  }

  //A beluga whale is equvivalent to a hammerhead shark.
  ```

<br>

### Scoped Enumeration

Enumerations with the class/struct keyword are scoped enumerations.

```cpp
#include<iostream>

enum class Color{Red, Green, Blue};

int main(){
    Color my_color= Color::Green;
}
```

- Scoped enumerations faciliate the usage of same names for different variables.

  ```cpp
  #include<iostream>

  enum class Color{Red, Green, Blue};

  float Green{56.6};

  int main(){
      std::cout << Green << "\n"; //56.6
  }
  ```

- Scoped enumerations lack implicit conversions!

  ```cpp
  enum class Whale{Blue, Beluga, Gray};

  int main() {
    int my_whale{ Whale::Beluga };		//error; implicit converison is not possible
    Whale my_whale{ Whale::Beluga };	//valid
  }
  ```

- It prevents logical errors.

  ```cpp
  #include <iostream>

  enum class Whale{Blue, Beluga, Gray};
  enum class Shark{Greatwhite, Hammerhead, Bull, Blue};

  int main() {
    if (Whale::Blue == Shark::Blue) //Compiler error; Cannot compare two different operand types
    {
      //code
    }
  }
  ```
