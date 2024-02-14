# STL Map

STL (Standard Template Library) maps are a part of the C++ Standard Library and provide an associative container that stores elements in key-value pairs.

- Must include the follwing preprocessor directive to use stl deque.

  ```cpp
  #include <list>
  ```

- Maps automatically sort their elements based on the keys.

* Under the hood, STL maps are typically implemented using balanced binary search trees, such as Red-Black Trees.
* STL maps are useful when you need a collection of key-value pairs with efficient search, insertion, and deletion based on the keys.
* STL offers 4 types of maps:
  1. std::map
  1. std::undordered_map
  1. std::multimap
  1. std::unordered_multiimap

<br>
<br>

# Initialising maps

```cpp
#include <iostream>
#include <map>
#include <string>

int main()
{
	std::map<std::string, int> m1{
		{"Larry", 10},
		{ "Moe", 20 }
	};
}
```

<br>
<br>
<br>

# Useful Functions

## size() and max_size()

```cpp
#include <iostream>
#include <map>
#include <string>

int main()
{
	std::map<std::string, int> m1{
		{"Larry", 10},
		{ "Moe", 20 }
	};
	std::cout << m1.size() << std::endl;	//2
	std::cout << m1.max_size() << std::endl; //230584300921369395
}
```

<br>
<br>

# insert() method and make_pair stl function

- There are different ways to isnert key value pairs

  ```cpp
  #include <iostream>
  #include <map>
  #include <string>

  int main()
  {
      std::map<std::string, int> m1{
          {"Larry", 10},
          { "Moe", 20 }
      };

      std::pair<std::string, int> p1{"Curly", 99};
      m1.insert(p1);
      m1["zoe"] = 10;
      m1.at("frank") = 100;
  }
  ```

<br>
<br>

## find() method and erase() method

```cpp
#include <iostream>
#include <map>
#include <string>

void display(std::map<std::string,int> map) {
	auto iter = map.begin();
	std::cout << "{ ";
	while (iter != map.end()) {
		std::cout  << iter->first << ":" << iter->second  << ", ";
		iter++;
	}
	std::cout << "}";
}

int main()
{
	std::map<std::string, int> m1{
		{"Larry", 10},
		{ "Moe", 20 }
	};
	display(m1);	//{ Larry:10, Moe:20, }
	auto iter = m1.find("Moe");
	m1.erase(iter);
	display(m1);	//{ Larry:10, }
}
```

<br>
<br>

## clear() method and empty() method

- clear() method removes all the elements from the map.
- empty() method returns true if the map is empty else returns false.
