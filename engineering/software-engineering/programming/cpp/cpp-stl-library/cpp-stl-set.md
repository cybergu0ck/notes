# STL Set

- Set is an associative container in C++ that stores a collection of unique, sorted elements.

* Must include the follwing preprocessor directive to use stl deque.

  ```cpp
  #include <set>
  ```

* Illustration of set initialisation

  ```cpp
  #include <iostream>
  #include <set>
  #include <algorithm>

  void display(std::set <int> l) {
    for (auto item : l) {
      std::cout << item << " ";
    }
  }

  int main() {
    std::set <int> s1{ 3,2,2,1};	//It is not an error to initialise with duplicate entries
    display(s1);	//1 2 3
  }
  ```

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
    bool operator<(const Person& rhs)const {
      return this->age < rhs.age;
    }
    bool operator==(const Person& rhs)const {
      return (this->name == rhs.name && this->age == rhs.age);
    }

  };
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

# Useful Functions

## insert()

- Elements can be inserted into a set using the insert() method.

  ```cpp
  #include <iostream>
  #include <set>
  #include <algorithm>

  void display(std::set <int> l) {
      for (auto item : l) {
          std::cout << item << " ";
      }
      std::cout << std::endl;
  }

  int main() {
      std::set <int> s1{ 3,2,2,1 };	//It is not an error to initialise with duplicate entries
      display(s1);	//1 2 3
      s1.insert(0);
      display(s1);	//0 1 2 3
      s1.insert(10);
      display(s1);	//0 1 2 3 10
  }
  ```

- The insert() method returns a std pair with an iterator as first item and a boolean as second, This second
  value is indicative of wether the insertion was successfull or not (indertion is unsuccessful when duplicate entries are inserted.)

  ```cpp
  int main() {
      std::set <int> s1{ 1,2,3};
      auto result = s1.insert(4);
      std::cout << *result.first << std::endl;	//4 represents the value of the iterator
      std::cout << result.second << std::endl;	//1 represents True
  }
  ```

<br>
<br>

## find()

- The value to be found is returned as an iterator.

  ```cpp
  int main() {
      std::set <int> s1{ 1,2,3};
      auto iter = s1.find(2);
      std::cout << *iter << std::endl;	//2
  }
  ```

  <br>
  <br>

## erase()

- Used to remove an element

  ```cpp
  #include <iostream>
  #include <set>
  #include <algorithm>

  void display(std::set <int> l) {
      for (auto item : l) {
          std::cout << item << " ";
      }
  }

  int main() {
      std::set <int> s1{ 1,2,3};
      auto iter = s1.find(2);
      s1.erase(iter);
      display(s1);	//1,3
  }
  ```

<br>
<br>

## count()

- Returns the count of the number of times an element is present in the set, Although this doesn't make sense for a set. It is used to determine
  if an element is present in the set or not.

      ```cpp
      int main() {
          std::set <int> s1{ 1,2,3};
          std::cout << s1.count(40) << std::endl;	//0, indicating that the element is not present
      }
      ```

<br>
<br>

## empty()

- To check if a set is empty or not.

<br>
<br>

## clear()

- Used to remove all the elements from the set.

<br>
<br>

# Types of sets

## multi_set

It is type of set ordered by key but allows duplicate elements.

<br>
<br>

## unordered_set

It is a type of set which is unordered and doesn't allow duplicate elements

<br>
<br>

## unordered_multiset

It is type of set that is unordered and allows duplicate elements.
