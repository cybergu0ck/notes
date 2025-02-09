# Character

**_A character is a built-in type used to represent a single character._**

- A character typically occupies 1 byte (8 bits) of memory.

<br>
<br>

## Useful Functions Related to Characters

- Include the `cctype` library (i.e `#include<cctype>`) to use the following functions.

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

# C Style String

_**C style string is an arrays with variables of type char.**_

- “Hello, world!” in C++ has type `const char[14]`.
- They are essentially terminated by a null character (`\0`). Hence referred to as zero or null terminated strings and this is the reason for the extra 1 space.

<br>
<br>

## Initialising a C Style String

```cpp
char str1[6]{"hello"};             // an array of 6 char, indices 0 through 5; The last character would be null character.
const char str2[]{ "string" };     // The compiler will allocate the space based on the initialiser
constexpr char str3[] { "hello" }; // an array of 6 const char, indices 0 through 5
```

<br>
<br>

## Basic Functions

```cpp
#include <iostream>

int main() {
    char word[6];

    std::cin >> word;               //cin by itself wont check for the size limit of word and will overflow
    std::cin.get(word,6);           //Limit input to 5 characters + null terminator
    std::cout << word << std::endl; //Output; The << of cout class is overloaded to print all the characters until null character
    word[0] = 'a';                  //Modifying the character using indexing
    std::cout << sizeof(word) << "\n"; //This will print the size of the array which is 1 unit more than size of the actual string
}
```

<br>
<br>

## Useful Functions Related to C Style String

- Include `<cstring>` library to use the following functions.

  ```cpp
  #include <iostream>
  #include <cstring>

  int main() {
      char word[6] = "hello";
      std::cout << std::strlen(word) << "\n"; //Length of the string
      char another_word[6];
      std::strcpy(another_word, word);  //(destination, source) is the signature!
      std::cout << another_word << "\n";

      std::cout << std::strcmp(word, another_word) << "\n"; //Compare strings; Gives 0 if equal

      std::strcat(word, " hey");  //Append
      std::cout << word << "\n";
  }
  ```

<br>
<br>

## Array Decay

- The concept of [Array Decay](../cpp-arrays-and-vectors.md#array-decay) is applicable here too as C style strings are basically arrays.

  ```cpp
  #include <iostream>
  using namespace std;

  int main()
  {
    char word[] = "hello";
    cout << *word << endl; //h
  }
  ```

<br>
<br>

## Pointer to String Literal

As C style strings are essentially an array of characters ending with a null terminator, a pointer to a char (char\*) points to the first character of the array.

```cpp
const char* word = "hey"; //here "hey" is a C Style string i.e. an array of characters.
```

- `const` is must since C++03.

<br>
<br>
<br>

# C++ string

std::string is a class in the Standard Template Library (STL) used to represent strings.

- Like C-style strings, std::string are stored contiguous in memory.
- Unlike C-style strings, they are dynamic in size.
- Must use the preprocessor directive `#include<string>` and must use the `std` namespace.

<br>
<br>

## Useful Functions Related to std::string

```cpp
#include <iostream>
#include <string>
int main() {
    std::string s1{ "abcd" };
    std::cout << s1.substr(3,2) << std::endl;	//de  //Substring

    std::cout << s1[10] << "\n";  //No bounce checking
    std::cout << s1.at(10) << "\n";  //bounce checking; throws an error
}
```

## Concatenation

```cpp
#include <iostream>
#include <string>

int main() {
    std::string word1{"hello"};
    std::cout << word1 + " bye" << "\n";

    std::string illegal = "hello" + " bye";  //Error as both "hello" and " bye" are C style string and they don't support concatenation
    return 0;
}
```

<br>
<br>
<br>
