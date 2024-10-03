# STL List

- list is a doubly-linked list container in C++. It is a linear data structure that allows efficient insertion and deletion of elements at both ends (front and back) as well as in the middle.
- These donot provide direct access to the elements using the at() or [ ] and hence are used in scenarios where random access is not necessary.
- Must include the follwing preprocessor directive to use stl deque.

  ```cpp
  #include <list>
  ```

<br>
<br>

# Useful Functions

## size() and max_size()

<br>
<br>

## front() and back()

<br>
<br>

## push_back() and push_front()

<br>
<br>

## pop_back() and pop_front()

<br>
<br>

## emplace_back() and emplace_front()

<br>
<br>

## insert()

- Used to insert an element before an element (iterator to be provided)

  ```cpp
  #include <iostream>
  #include <list>
  #include <algorithm>

  void display(std::list<int> l) {
      for (auto item : l) {
          std::cout << item << " ";
      }
  }

  int main() {
      std::list<int> l1{ 1,2,3 };
      auto iter = std::find(l1.begin(), l1.end(), 2);
      l1.insert(iter, 100);
      display(l1);		//1 100 2 3
  }
  ```

<br>
<br>

## erase()

```cpp
#include <iostream>
#include <list>
#include <algorithm>

int main() {
	std::list<int> l1{ 1,2,3 };
	auto iter = std::find(l1.begin(), l1.end(), 2);
	l1.insert(iter, 100);
	l1.erase(iter);  //erases the value that the iterator is pointing to i.e. 2
	display(l1);		//1 100 3
}
```

<br>
<br>

## resize()

```cpp
#include <iostream>
#include <list>
#include <algorithm>

void display(std::list<int> l) {
	for (auto item : l) {
		std::cout << item << " ";
	}
}

int main() {
	std::list<int> l1{ 1,2,3 };
	l1.resize(10);
	display(l1);		//1 2 3 0 0 0 0 0 0 0
}
```

<br>
<br>
<br>

# STL Forward list

- forward_list is a singly-linked list container in C++. It is a linear data structure that allows efficient insertion and deletion of elements at the front and in the middle, but not at the back.
- These donot provide direct access to the elements using the at() or [ ] and hence are used in scenarios where random access is not necessary.
- Must include the follwing preprocessor directive to use stl deque.

  ```cpp
  #include <forward_list>
  ```

<br>
<br>

# Useful Functions

## max_size()

- forward_list doesn't have size() method and only has max_size() method.

## front()

<br>
<br>

## insert_after()

```cpp
#include <iostream>
#include <forward_list>
#include <algorithm>

void display(std::forward_list<int> l) {
	for (auto item : l) {
		std::cout << item << " ";
	}
}

int main() {
	std::forward_list<int> l1{ 1,2,3,4,5 };
	auto iter = std::find(l1.begin(), l1.end(), 3);
	l1.insert_after(iter, 500);
	display(l1);	//1 2 3 500 4 5
}
```

<br>
<br>

## emplace_after()

<br>
<br>

## erase_after()

<br>
<br>

## resize()

<br>
<br>
