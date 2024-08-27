# Pair

__A std::pair is a container defined in the `<utility>` header that holds two heterogeneous objects as a single unit.__


<br>
<br>

## Initialisation

```cpp
#include<iostream>
#include<vector>
#include<utility>  //library to include

int main()
{
	std::pair<int, std::string> pair1; //Default initialization
	std::pair<int, std::string> pair2{42, "Hello"}; //Direct initialization
	std::pair<int, std::string> pair3 = std::make_pair(43, "Bye");
	std::pair<int, std::string> pair4(pair3); // Copy initialization
	std::pair<int, std::string> pair5(std::move(pair4)); // Move initialization

	std::cout << pair1.first << " and " << pair1.second << std::endl;    //Accessing the elements of the pair
}
```

<br>
<br>
