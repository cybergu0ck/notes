# STL Set

A std::set is a STL container that stores unique elements in a specific order.

- Defined in the `<set>` header.

<br>
<br>

## Initialisation

```cpp
#include<iostream>
#include<set> //Library to be included

int main()
{
	std::set<int> set1;                     //Default Constructor
	std::set<int> set2 = {1,2,3};           //Initialiser List
	std::set<int> set3{2,3,4};              //Initialiser List
	std::set<int> set4{set3};               //Copy constructor will be called
	std::set<int> set5{ std::move(set4) };  //Move constructor will be called
}
```

<br>
<br>

## Methods

<br>

### Adding Elements

- Inserting elements.

  ```cpp
  #include <iostream>
  #include <set>

  int main()
  {
      std::set<int> my_set = { 1,2,3 };
      my_set.insert(4);
      my_set.insert({ 5,6,7 });
      std::pair<std::set<int>::iterator, bool> res = my_set.insert(1);  //Returns a pair, first is iterator to element and second is true if inserted, false if already exists.
  }
  //1       2       3       4       5       6       7
  ```

- Emplacing elements.

<br>

### Accessing Elements

```cpp
#include <iostream>
#include <set>

int main()
{
	std::set<int> my_set = { 1,2,3 };
	std::cout << *my_set.begin() << "\n";		//Accessing the first element; using iterator
	std::cout << *my_set.rbegin() << "\n";		//Accessing the last element; using reverse iterator

	std::set<int>::iterator it = my_set.find(2);
	if (it != my_set.end())
	{
		std::cout << "Found the element with value " << *it;
	}
}
```

<br>

### Finding Elements

```cpp
#include <iostream>
#include <set>

int main()
{
	std::set<int> my_set = { 1,2,3 };

	std::set<int>::iterator it = my_set.find(2);
	if (it != my_set.end()){
		std::cout << "Found the element with value " << *it;
	}
	else{
		std::cout << "Element not found";
	}
}
```

<br>

### Removing Elements

<br>

### Number of Elements

<br>

### Emptyness

<br>
<br>

## Types of STL Sets

1. **Set** : _A set is an associative container that stores unique elements in sorted order._
2. **Multi Set** : _A multiset is an associative container that stores elements (allows duplicates) in sorted order._
3. **Unordered Set** : _An unordered is an associative container that stores unique elements in un-sorted order._
4. **Unordered Multiset** : _An unordered_multiset is an associative container that stores elements (allows duplicates) in un-sorted order._

<br>

### Illustration

|                 | std::set | std::muliset | std::unordered_set | std::unordered_multset |
| --------------- | -------- | ------------ | ------------------ | ---------------------- |
| Unique elements | true     | false        | true               | false                  |
| Order           | true     | true         | false              | false                  |
| Header file     | `<set>`  | `<set>`      | `<unordered_set>`  | `<unordered_set>`      |

<br>

### Implementation

|                | std::set       | std::mulitset  | std::unordered_set | std::unordered_multiset |
| -------------- | -------------- | -------------- | ------------------ | ----------------------- |
| Implementation | Red Black Tree | Red Black Tree | Hash Table         | Hash Table              |

<br>

### Time Complexities

|           | std::set   | std::mulitset | std::unordered_set  | std::unordered_multiset |
| --------- | ---------- | ------------- | ------------------- | ----------------------- |
| Insertion | $O(log n)$ | $O(log n)$    | $\theta(1)$, $O(n)$ | $\theta(1)$, $O(n)$     |
| Deletion  | $O(log n)$ | $O(log n)$    | $\theta(1)$, $O(n)$ | $\theta(1)$, $O(n)$     |
| Search    | $O(log n)$ | $O(log n)$    | $\theta(1)$, $O(n)$ | $\theta(1)$, $O(n)$     |

- For the unordered variants the time complexity is $\theta(1)$ i.e. average case and $O(n)$ i.e. worst case, when the hash function is poor causing collisions (rare).

<br>

### Space Complexities

|     | std::map | std::mulitmap | std::unordered_map | std::unordered_multimap |
| --- | -------- | ------------- | ------------------ | ----------------------- |
|     | $O(n)$   | $O(n)$        | $O(n)$             | $O(n)$                  |
