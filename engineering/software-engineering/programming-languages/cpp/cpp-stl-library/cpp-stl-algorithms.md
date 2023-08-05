# stl algorithms

## copy_if() and back_inserter()

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

void display(std::vector<int> vec) {
	std::for_each(vec.begin(), vec.end(), [](int value) {std::cout << value << " "; });		//for_each is a stl algorithm
	std::cout << std::endl;
}

int main() {
	std::vector<int> vec1{ 1,2,3,4,5,6,7,8,9,10 };
	std::vector<int> vec2{ 2,4 };
	std::copy_if(vec1.begin() + 5, vec1.end(), std::back_inserter(vec2), [](int x) {return x % 2 == 0; });
	display(vec1);
	display(vec2);
}


//1 2 3 4 5 6 7 8 9 10
//2 4 6 8 10
```

<br>
<br>
<br>

## transform()

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

void display(std::vector<int> vec) {
	std::for_each(vec.begin(), vec.end(), [](int value) {std::cout << value << " "; });		//for_each is a stl algorithm
	std::cout << std::endl;
}

int main() {
	std::vector<int> vec1{ 1,2,3 };
	std::vector<int> vec2{ 2,2,2,2,2 };
	std::vector<int> vec3;
	std::transform(vec1.begin(), vec1.end(), vec2.begin(), std::back_inserter(vec3), [](int x, int y) {return x * y; });
	display(vec1);
	display(vec2);
	display(vec3);
}


//1 2 3
//2 2 2 2 2
//2 4 6
```
