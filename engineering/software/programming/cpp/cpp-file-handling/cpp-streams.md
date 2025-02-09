# Streams

<br>
<br>

# string streams

- Allows us to read and write from strings in memory much as we would read and write to files.
- The following header file must be included to use string streams `#include <sstream>`.
- stringstream class allows us to read and write from string streams, the istringstream class allows to read from string streams and the ostringstream class allows to write to string streams.

* To use a string stream
  1. include the sstream header file.
  1. Declare a string stream object.
  1. Connect it to a std::string.
  1. Read/Write data from/to the string stream using formatted I/O.

<br>
<br>

## Reading from string streams

```cpp
#include <sstream>
#include <string>
#include <iostream>

int main() {
	int num{};
	double total{};
	std::string name{};
	std::string	info{ "Moe 100 1234.5" };

	std::istringstream iss{ info }; //we connect the stringstream object to a std::string
	iss >> name >> num >> total;
	std::cout << name << " " << num << " " << total << std::endl;
}

//Moe 100 1234.5
```

<br>
<br>

## Writing to string streams

```cpp
#include <sstream>
#include <string>
#include <iostream>

int main() {
	int num{100};
	double total{99.9};
	std::string name{"frank"};
	std::ostringstream oss{};
	oss << name << " " << num << " " << total;
	std::cout << oss.str() << std::endl;	//calling this method displays the internal buffer of stringstream.
}

//frank 100 99.9
```
