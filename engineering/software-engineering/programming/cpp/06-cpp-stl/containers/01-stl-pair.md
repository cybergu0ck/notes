# STL Pair

A std::pair is a STL container that holds two heterogeneous objects as a single unit.

- It is defined in the `<utility>` header.

<br>
<br>

## Initialisation

```cpp
#include<iostream>
#include<vector>
#include<utility>  //library to include

int main()
{
	std::pair<int, std::string> pair1;                              //Default initialization
	std::pair<int, std::string> pair2{42, "Hello"};                 //Direct initialization
	std::pair<int, std::string> pair3 = std::make_pair(43, "Bye");  // Using std::make_pair()
	std::pair<int, std::string> pair4(pair3);                       // Copy initialization
	std::pair<int, std::string> pair5(std::move(pair4));            // Move initialization
}
```

<br>
<br>

## Methods

- Reading and Writing the elements of the pair.

  ```cpp
  #include <iostream>
  #include <utility>

  int main()
  {
      std::pair<int, int> coordinates;
      coordinates.first = 101;
      std::cout << coordinates.first << " " << coordinates.second << "\n";
  }

  //101  0
  ```
