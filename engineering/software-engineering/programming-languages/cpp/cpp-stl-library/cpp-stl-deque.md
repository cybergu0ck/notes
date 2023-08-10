# STL deque

- deque stands for "double-ended queue." It is a sequence container that allows efficient insertion and deletion of elements at both ends (front and back) with constant time complexity.

* Must include the follwing preprocessor directive to use stl deque.

  ```cpp
  #include <deque>
  ```

* The elements in a stl deque are not stored in contigious memory, there are stored in blocks (within which memory is contigious) and different blocks may be present in varoious part of the memory.

- Compared to vector, deque offers faster insertion and deletion at both ends, but slower random access and possibly slightly higher memory overhead.

<br>
<br>
<br>

# Useful Functions

## size() and max_size()

<br>
<br>

## using [ ] to get the value at the index

<br>
<br>

## at() to get the value at the index

<br>
<br>

## front() and back()

```cpp
#include <iostream>
#include <deque>

int main() {
	std::deque<int>deck1{ 1,2,3,4,5 };
	std::deque<int>deck2{ 10,100 }; //ten items with value 100
	std::cout << deck1.front() << std::endl;	//1
	std::cout << deck2.back() << std::endl;		//100
}
```

<br>
<br>

## push_back() and push_front()

```cpp
#include <iostream>
#include <deque>

int main() {
	std::deque<int>deck1{ 1,2,3,4,5 };
	std::deque<int>deck2{ 10,100 }; //ten items with value 100
	deck1.push_front(600);
	std::cout << deck1.front() << std::endl;	//600
	deck2.push_back(0);
	std::cout << deck2.back() << std::endl;		//0
}
```

<br>
<br>

## pop_back() and pop_front()

<br>
<br>

## emplace_back() and emplace_front()

<br>
<br>
