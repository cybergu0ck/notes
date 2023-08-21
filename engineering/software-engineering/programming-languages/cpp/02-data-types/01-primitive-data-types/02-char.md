# Character Functions

- Character Functions typically refer to functions that operate on characters (individual characters) or strings (sequences of characters). These functions are part of the C++ Standard Library and are used for various text manipulation tasks.
- Must use the preprocessor directive `#include<cctype>`.

* Some of the useful character funcitons are

  | function   | Description                          |
  | ---------- | ------------------------------------ |
  | isalpha(c) | True if c is a letter                |
  | isalnum(c) | True if c is a letter or digit       |
  | isdigit(c) | True if c is a digit                 |
  | islower(c) | True if c is a lowercase letter      |
  | isprint(c) | True if c is a printable character   |
  | ispunct(c) | True if c is a punctuation character |
  | isupper(c) | True if c is a uppercase letter      |
  | isspace(c) | True if c is a whitespace            |
  | tolower(c) | Returns lowercase of c               |
  | toupper(c) | Returns uppercase of c               |

<br>
<br>
<br>

# C-style Strings

- They are sequence of characters stored contiguously in memory.
- They are implemented as an array of characters.
- Terminated by a null character.
- Referred to as zero or null terminated strings.
- Must use the preprocessor directive `#include<cstring>`.

- Initialising c-style strings

  ```cpp
  #include <iostream>
  #include <cctype>
  #include <cstring>

  int main() {
      char name[20]{ "Frank" }; //Uninitialised c-style strings contain garbage
      std::cout << name << std::endl;	//Frank
  }
  ```

* Finding the length of the string using `strlen`. (In Visual Studio strlen_s must be used.)

  ```cpp
  #include <iostream>
  #include <cctype>
  #include <cstring>

  int main() {
      char name[20]{ "Frank" };
      std::cout << strlen(name) << std::endl;	//5
  }
  ```

* Copying strings using `strcpy` (In Visual Studio strcpy_s must be used.)

  ```cpp
  #include <iostream>
  #include <cctype>
  #include <cstring>

  int main() {
      char name[20]{ "Frank" };
      char another_name[20]{};
      strcpy_s(another_name, name);
      std::cout << another_name << std::endl;	//Frank
  }
  ```

* Concatinating strings using `strcat` (In Visual Studio strcat_s must be used.)

  ```cpp
  #include <iostream>
  #include <cctype>
  #include <cstring>

  int main() {
      char name[20]{ "Frank" };
      strcat_s(name, "ie");
      std::cout << name << std::endl;	//Frankie
  }
  ```

<br>
<br>
<br>

# C++ Strings

- std::string is a class in the Standard Template Library.
- Like C-style strings, std::string are stored contiguous in memory.
- Unlike C-style strings, they are dynamic in size.
- Must use the preprocessor directive `#include<string>` and must use the `std` namespace.

- Different ways of initialising C++ strings

  ```cpp
  #include <iostream>
  #include <string>

  int main() {
      std::string s1{ "Abigale" };
      std::string s2{ s1 };
      std::string s3{ "Abigale" ,3};
      std::string s4{ s3,0,2 };
      std::string s5{ 3, 'X' };
      std::cout << s1 << std::endl; //Abigale
      std::cout << s2 << std::endl; //Abigale
      std::cout << s3 << std::endl; //Abi
      std::cout << s4 << std::endl; //Ab
      std::cout << s5 << std::endl; //♥X
  }
  ```

* Assignments in C++ strings

  ```cpp
  #include <iostream>
  #include <string>

  int main() {
      std::string s1;
      s1 = "C++ Rocks!";
      std::string s2{ "Hello" };
      s2 = s1;
      std::cout << s2 << std::endl; //C++ Rocks!
  }
  ```

* Concatinating C++ strings

  ```cpp
  #include <iostream>
  #include <string>

  int main() {
      std::string part1{ "C++" };
      std::string part2{ "is a powerful" };

      std::string sentence = part1 + " " + part2 + " language";  //C++ is a powerful language
      sentence = "C++" + " is powerful";  //Illegal as C style literals cannot be concatinated using +
  }
  ```

* Accessing C++ strings. Note that at() performs bounce checking.

  ```cpp
  #include <iostream>
  #include <string>

  int main() {
      std::string s1{ "abcd" };
      std::cout << s1[0] << std::endl;	//a
      std::cout << s1.at(1) << std::endl;	//b
  }
  ```

* C++ strings can be compared character by character lexically using comparision operators.

<br>

## Usefull C++ string methods

- Getting substrings

  ```cpp
  #include <iostream>
  #include <string>

  int main() {
      std::string s1{ "abcd" };
      std::cout << s1.substr(0,2) << std::endl;	//ab
      std::cout << s1.substr(3,2) << std::endl;	//de
  }
  ```
