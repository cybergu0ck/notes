# std::string

_std::string_ is a class that represents a sequence of characters.

- defined in the _<string>_ header.
- manages memory automatically unlike c-style strings.

<br>
<br>

## initialisation

```cpp
// Default initialization
std::string empty_string; //empty string

// Initializer list initialization (C++11 and later)
std::string greeting = {"Hello, world!"}; // Note: This creates a std::string from a const char*

// Copy initialization
std::string name = "John Doe";

// Fill initialization
std::string stars(10, '*'); // 10 asterisks: "**********"

// Constructing from a C-style string
const char* c_str = "C-style string";
std::string from_c_str(c_str);

// Constructing from part of another string
std::string another_string = "This is a longer string";
std::string sub_string(another_string, 5, 6); // "is a " (from index 5, length 6)

// Moving from another string (C++11 and later)
std::string moved_string = std::move(another_string); // another_string is now in a valid but unspecified state.
```

<br>
<br>

## string literal vs std::string

c-style strings are null terminated character arrays, while std::string is a class in the standard library.

- "hello" is a c-style string of type _const char\*_.
- it is strongly advised to use std::string over c-style string despite the overhead.

<br>
<br>

## methods

<br>

### access

1. _char operator[](size_t pos)_

   - returns the character at pos _without bounds checking_.
   - has $O(1)$ time complexity.

<br>

1. _char at(size_t pos)_

   - returns the character at pos _with bounds checking_.
   - has $O(1)$ time complexity.

<br>

1. _char front()_

   - returns the first character.
   - has $O(1)$ time complexity.

<br>

1. _char back()_

   - returns the last character.
   - has $O(1)$ time complexity.

<br>

1. _std::string substr(size_t pos, size_t len)_

   - returns the substring of length len starting at pos.
   - has $O(n)$ time complexity.

<br>

### search

1. _size_t find(std::string str)_

   - returns the first index if str is a substring otherwise std::string::npos.
   - has $O(n*m)$ time complexity.

<br>

1. _size_t rfind(std::string str)_

   - returns the last index if str is a substring otherwise std::string::npos.
   - has $O(n*m)$ time complexity.

<br>

### insertion

1. _push_back(char character)_

   - append a single character to _\*this_.
   - has amortised $O(1)$ time complexity, average is $O(1)$ and is $O(n)$ in case of relocation.

<br>

1. _append(std::string str)_

   - append str to `*this`.
   - has amortised $O(1)$ time complexity, average is $O(1)$ and is $O(n)$ in case of relocation.

<br>

1. _operator += (std::string str)_

   - append str to `*this`.

<br>

1. _std::string insert(size_t pos, std::string str)_

   - insert str at pos.
   - has amortised $O(n)$ time complexity, average is $O(n)$ and is $O(n+m)$ in case of relocation.

<br>

### deletion

1. _std::string erase(size_t pos, size_t len)_

   - erase len number of characters starting at pos.
   - has $O(n)$ time complexity.

<br>

1. _void pop_back()_

   - remove the last character.
   - has $O(1)$ time complexity.

<br>

1. _void clear()_

   - remove all the characters.
   - has $O(1)$ time complexity.

<br>

### modification

1. _std::string replace(size_t pos, size_t len, const std::string& str)_

   - replace len number of charcaters starting at pos with the given str.
   - has $O(n)$ time complexity.
   - example:
     ```cpp
     #include <iostream>
     using namespace std;
     int main()
     {
     std::string word{"abcdefghijk"};
     std::string res = word.replace(1, 1, "xyz"); //character 'b' will be replaced with "xyz"
     std::cout << res;
     return 0;
     }
     //axyzcdefghijk
     ```

<br>

### miscallaneous

1.  _const char \* c_str()_

    - return the pointer to the underlying array, basically return the c-style string.
    - has $O(1)$ time complexity.

<br>

1.  _bool empty()_

    - returns true if the string is empty otherwise false.
    - has $O(1)$ time complexity.

<br>

1.  _size_t size()_

    - returns the number of characters.
    - _length_ also returns the same result.
    - has $O(1)$ time complexity.

<br>

1.  _int compare(std::string str)_

    - returns 0 if str and the `*this` is equal, <0 if `*this` is lexicographically less than str, >0 if `*this` is lexicographically greater than str.
    - has $O(n)$ time complexity.

<br>
<br>
