# STL Set

```cpp
#include <set>
```

<br>
<br>

## Types of sets

<br>

### set

_A set is an associative container that stores unique elements in sorted order._

<br>

### unordered_set

_An unordered is an associative container that stores unique elements in un-sorted order._

<br>

### multi_set

_A multiset is an associative container that stores elements (allows duplicates) in sorted order._

<br>

### unordered_multiset

_An unordered_multiset is an associative container that stores elements (allows duplicates) in un-sorted order._

<br>
<br>

### Time Complexity

| Property                    | ordered variants   | unordered variants |
| --------------------------- | ------------------ | ------------------ |
| Ordering                    | increasing order   | no ordering        |
| Implementation              | Self Balancing BST | Hash Table         |
| Search Time (worst case)    | $O(log(n))$        | $O(n)$             |
| Insertion Time (worst case) | $O(log(n))$        | $O(n)$             |
| Deletion Time (worst case)  | $O(log(n))$        | $O(n)$             |

<br>
<br>

## Initialisation

```cpp
#include<iostream>
#include<set> //Library to be included

int main()
{
	std::set<int> set1;           //Empty Set
	std::set<int> set2 = {1,2,3}; //Normal Initialisation
	std::set<int> set3{2,3,4};    //Initialiser List
	std::set<int> set4{set3};     //Copy constructor will be called
	std::set<int> set5{ std::move(set4) }; //Move constructor will be called
}
```

<br>
<br>

## Set APIs

```cpp
#include<iostream>
#include<set> //Library to be included

int main()
{
	std::set<int> set2 = {1,2,3}; //Normal Initialisation
	std::pair<std::set<int>::iterator,bool> res = set2.insert(4); //Returns a pair, first is iterator to element and second is true if inserted, false if already exists.
	set2.erase(0);  //Removal of an existing element from the set. no errors if the element is not present in the set.
	set2.clear();   //Empty the set.
	std::set<int>::iterator it = set2.find(1);	//Returns the iterator to the element with the specified value, end() if not found.
	int freq = set2.count(1);	//Returns the number of occurances of the given value (0 or 1 for sets)
	bool is_empty = set2.empty();	//Returns True if set is empty else False
	set2.size();    //Returns the size of the set
}
```

<br>
<br>

## User Defined classes with Sets


* Using user defined classes in sets (Need to know about operator overloading!). Notice how Person with name edision is not in the set as age is considered here and duplication is not allowed.

  ```cpp
  #include <iostream>
  #include <set>
  #include <algorithm>
  #include <string>

  class Person {

    std::string name;
    int age;
    friend std::ostream& operator<<(std::ostream& output, Person& obj);
  public:
    Person(std::string p1, int p2) :name{p1}, age{p2} {};

    //Overloading < operator
    bool operator<(const Person& rhs)const {
      return this->age < rhs.age;
    }

    //Overloading == operator
    bool operator==(const Person& rhs)const {
      return (this->name == rhs.name && this->age == rhs.age);
    }

  };

  //Overloading << operator
  std::ostream& operator<<(std::ostream& output, Person& obj)
  {
    output << obj.name;
    return output;
  }

  void display(std::set <Person> l) {
    for (auto item : l) {
      std::cout << item << " ";
    }
    std::cout << std::endl;
  }

  int main() {
    Person p1{ "oppie",24 };
    Person p2{ "tesla",19 };
    Person p3{ "edison",19 };
    std::set <Person> s1{ p1, p2, p3};	//Will be ordered based on age!
    display(s1);	//tesla oppie
  }
  ```

<br>
<br>
<br>

