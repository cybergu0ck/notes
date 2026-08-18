# String

## Difference between string and character array

| String                                                               | Character Array                           |
| -------------------------------------------------------------------- | ----------------------------------------- |
| string is a C++ class and string variables are objects of this class | character array is an array of characters |
| Slow access speed                                                    | Fast access speed                         |
| Memory is allocated dynamically                                      | Memory is allocated statically            |
| Array decay is impossible                                            | Array decay might occur                   |

<br>
<br>

## Methods

<br>

### Element Access

```cpp
#include <iostream>
#include <string>

int main() {
    std::string word = "abcdefg";
    std::cout << word.front() << std::endl;  //Returns the first character; a
    std::cout << word.back() << std::endl;  //Returns the last character; g
    std::cout << word.at(1) << std::endl;   //Returns the character at first index; b
    std::cout << word[2] << std::endl;   //Returns the character at second index; c
    return 0;
}
```
