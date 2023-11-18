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

#TODO - Complete this revamp

## Initialisation of enumerators

Enumerations can be implicitely or explicitely initialised as shown here.

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

<br>
<br>
<br>

# Unscoped enumeration

- Run the following code and try to understand the usefullness. (Input a number such as 0, 1,..)

  ```cpp
  #include <iostream>

  enum State {engine_failure, inclement_weather, nominal, unknown};
  enum Sequence {Abort, Hold, Launch};


  //overloading the stream extraction operator to allow user to enter a state of State enumeration
  std::istream& operator>>(std::istream &is, State& state)
  {
    std::underlying_type_t<State> user_input;	//user_input will be a number so we can write this as "int user_input;"
    is >> user_input;

    switch (user_input) {
    case engine_failure:
    case inclement_weather:
    case nominal:
    case unknown:
      state = State(user_input);
      break;
    default:
      std::cout << "Invalid Launch State" << std::endl;
      state = unknown;
    }
    return is;
  }

  //overloading the stream insertion operator to insert the string representation of the sequence
  std::ostream& operator<< (std::ostream& os, const Sequence& sequence) {
    switch (sequence) {
    case Abort:
      os << "Abort";
      break;
    case Hold:
      os << "Hold";
      break;
    case Launch:
      os << "Launch";
      break;
    }
    return os;
  }

  void initiate(Sequence sequence) {
    std::cout << "Initiate " << sequence << " sequence!" << std::endl;  //uses overloaded << operator
  }

  int main() {
    State state;
    std::cout << "Enter Launch state: ";
    std::cin >> state;

    switch (state) {
    case engine_failure:
    case unknown:
      initiate(Abort);
      break;
    case inclement_weather:
      initiate(Hold);
      break;
    case nominal:
      initiate(Launch);
      break;
    }
  }
  ```

<br>
<br>
<br>

# Scoped enumeration

## Need

- The following is permitted by the compiler as both "Beluga" and "Hammerhead" have integral value of 1 but it is a potential logical error.

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

* Without scoped enumerations we cannot have same names in different enumerations.

  ```cpp
  #include <iostream>

  enum Whale{Blue, Beluga, Gray};
  enum Shark{Greatwhite, Hammerhead, Bull, Blue};

  int main() {
  }

  //Error; Redefinition
  ```

<br>
<br>

## Scoping enumerations using class or struct keyword

- Scoping is done as follows,

  ```cpp
  enum class Whale{Blue, Beluga, Gray};
  enum class Shark{Greatwhite, Hammerhead, Bull, Blue};

  int main() {
    int my_whale{ Whale::Beluga };		//error; implicit converison is not possible
    Whale my_whale{ Whale::Beluga };	//valid
  }
  ```

* Scoped enumerations work similar to unscoped enumerations, except for the obvious scope resolution that must be used scoped enumerations lack implicit conversions!

* It prevents logical errors

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
