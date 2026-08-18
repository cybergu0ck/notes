# Stream

**Stream is an abstraction that represents flow of data.**

- Streams provide a way to perform input and output operations in a consistent manner, regardless of the underlying device (e.g., console, file, string).

<br>
<br>

## Input Streams

Input streams are streams used for reading data.

- This is facilitated by `std::istream` class.
- The class is declared in `<istream>` header file but mostly used indirectly through `<iostream>` header.

- The following are some examples of input streams:

  - Standard Input Stream (`std::cin`), is an instance of `std::istream`.
  - String Input Stream (`std::istringstream`) is a derived class of `std::istream`.
  - File Input Stream (`sd::ifstream`) is a derived class of `std::istream`.

<br>

### Standard Input Stream

Standard input stream is used to read data from the standard input, generally a keyboard.

- `std::cin` is an instance of `std::istream` and not a class byitself. Hence use the `#include<iostream>` statement.
- It reads strings until it encounters the first whitespace character.

  ```cpp
  #include <iostream>
  #include <string>

  int main() {
      std::string buffer;
      std::cin >> buffer;   //User input : "abc   def"
      std::cout << buffer;  //abc
      return 0;
  }
  ```

- Reading multiple values.

  ```cpp
  #include <iostream>
  #include <string>

  int main() {
      std::string buffer1, buffer2, buffer3;
      std::cin >> buffer1 >> buffer2 >> buffer3;  //User input : hello hu hi
      std::cout << buffer1 << " " << buffer2 << " " << buffer3; //Output : hello hu hi
      return 0;
  }
  ```

- Checkout [std::getline](#getline-function) to read full line of text.

<br>

### String Input Stream

String input stream are strings used as streams.

- This is facilitated by `std::istringstream` class, which is derived from `std::istream` class.
- The class is declared in `<sstream>` header file.

- Initialisation and extraction. Note that istringstream objects can't be directly output to the console, they need to be extracted first.

  ```cpp
  #include <iostream>
  #include <sstream>
  #include <string>

  int main() {
      std::string data{"hello"};
      std::istringstream is{data};  //Initialisation

      std::string output_buffer;
      is >> output_buffer; //Extraction
      std::cout << output_buffer; //hello

      return 0;
  }
  ```

- Checkout usage of string input stream along with [std::getline](#getline-function).

<br>

### File Input Stream

//STUB - Learn when needed

- This is facilitated by `std::ifstream` class, which is derived from `std::istream` class.
- The class is declared in `<ftream>` header file.

<br>

### Getline Function

- The syntax of getline function is as follows:

  ```cpp
  std::getline(std::istream& is, std::string& str);
  std::getline(std::istream& is, std::string& str, char delim);
  ```

  - `is` is the input stream from which to read (examples: std::cin, std::istringstream, std::ifstream)
  - `str` is the string where the read line will be stored.
  - `delim` is a optional parameter which indicates the end of line, by default it is newline character (`\n`).

- Example usage of getline function in a while loop

  ```cpp
  #include <iostream>
  #include <sstream>
  #include <string>

  int main() {
      std::string strs{"hello-hi-bye-kai"};
      std::string buffer;

      std::istringstream is{strs};
      while (std::getline(is, buffer, '-')) {
          std::cout << buffer << "\t\t";
      }

      return 0;
  }
  ```

<br>
<br>

## Output Streams

Output streams are streams used for writing data.

- This is facilitated by `std::ostream` class.
- The class is declared in `<ostream>` header file but mostly used indirectly through `<iostream>` header.

- The following are some examples of output streams:

  - Standard Output Stream (`std::cout`), is an instance of `std::ostream`.
  - String Output Stream (`std::ostringstream`) is a derived class of `std::ostream`.
  - File Output Stream (`sd::ofstream`) is a derived class of `std::ostream`.

//STUB - Can fill elaborated notes, similar to the above section

<br>

## Bidirectional Streams

Bidirectional streams ares streams used for both reading and writing data.

- The following are some examples of bidirectional streams:

  - String Stream (`std::stringstream`)
  - File Stream (`sd::fstream`)

<br>
<br>
