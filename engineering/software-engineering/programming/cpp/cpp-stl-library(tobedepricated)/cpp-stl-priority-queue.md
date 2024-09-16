# STL Priority Queue

- It is data structure that allows insertion and removal of elements in order from the front of the container.
- Elements are stored internally as a vector by default.
- Elements are inserted in priority order (largest value will always be at the front)
- No iterators are supported.
- No STL algorithms are supported.

<br>
<br>
<br>

# Initialisation

```cpp
#include <queue>

int main() {
	std::priority_queue <int> q1;
}
```

<br>
<br>
<br>

# Useful Functions

## push()

- Insert an element into sorted order

<br>
<br>

## pop()

- Removes the top element (greatest)

  ```cpp
  #include <iostream>
  #include <queue>

  int main() {
      std::priority_queue <int> pq;
      pq.push(1);
      pq.push(100);
      pq.push(56);
      std::cout << pq.top() << std::endl;	//100
      pq.pop(); //removes 100
      std::cout << pq.top() << std::endl;	//56
  }
  ```

<br>
<br>

## top()

- Access the top element (greatest)

  ```cpp
  #include <iostream>
  #include <queue>

  int main() {
      std::priority_queue <int> pq;
      pq.push(59);
      std::cout << pq.top() << std::endl;	//59
  }
  ```

<br>
<br>

## empty()

- Returns true if the priority queue is empty.

<br>
<br>

## size()

- Returns the number of elements in the priority queue.
