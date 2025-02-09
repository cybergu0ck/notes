# STL Set

```cpp
#include <unordered_set>  //Library for unordered_set and unordered_multiset
#include <set>  //Library for unordered_set and multiset
```

<br>
<br>



### Implementation

| Property       | ordered variants   | unordered variants |
| -------------- | ------------------ | ------------------ |
| Implementation | Self Balancing BST | Hash Table         |

<br>
<br>

### Implementation

| Property                         | ordered variants          | unordered variants |
| -------------------------------- | ------------------------- | ------------------ |
| Search Time (avg /worst case)    | $O(log(n))$ / $O(log(n))$ | $O(1)$ / $O(n)$    |
| Insertion Time (avg /worst case) | $O(log(n))$ / $O(log(n))$ | $O(1)$ / $O(n)$    |
| Deletion Time (avg /worst case)  | $O(log(n))$ / $O(log(n))$ | $O(1)$ / $O(n)$    |

- The worst case for unordered variants is $O(n)$, when the hash function is poor and causes collisions but this is a rare case.

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

- Using user defined classes in sets (Need to know about operator overloading!). Notice how Person with name edision is not in the set as age is considered here and duplication is not allowed.

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
