# STL

- A library of powerful, reusable, adaptable, generic classes and functions.
- It is implemented using C++ templates.
- It implements common data structures and algorithms.
- STL has 3 main components:

  1. **Containers** : Collection of objects or primitive types (array, vector, deque, stack, set, map etc).

     - Types of containers provided by STL are:
       1. Sequence containers : array, vector, list, forward_list, deque
       1. Associative containers : set, multi set, map, multi map
       1. Container adapters : stack, queue, priority queue

  1. **Algorithms** : Functions for processing sequences of elements from containers. (find, max, count, accumulate, sort etc)

  1. **Iterators** : Generate sequences of elements from containers. (forward, reverse, by value, by reference, constant etc)

     - Types of iterators provided by STL

       1. Input iterators : from the container to the program.
       1. Output iterators : from the program to the container.
       1. Forward iterators : Navigate one item at a time in one direction.
       1. Bi-directional iterators : Navigate one item at a time both directions.
       1. Random access iterators : Directly access a container item.

<br>
<br>
<br>

# Generic Programming with macros

- This is not a good practice but must be known to deal with legacy C++ code (a lot of it is out there)

* macros begin with a # sign and all directives that begin with # are preprocessor directives.
* Preprocessor directives doesn't know C++, it just replaces the stuff wherever it is used! (i.e. simple substitution)

* There is no type assocaiated with macros, the preprocessor is doing simple substituition

  ```cpp
  #include <iostream>

  #define PI 3.16

  int main()
  {
      double radius{ 1 };
      double area = PI * radius * radius; //the preprocessor just replaces the PI with 3.16 here
      std::cout << area << std::endl;
  }
  ```

* An illustrative example of why it is bad practice to use this

  ```cpp
  #include <iostream>

  #define SQUARED 5*5

  int main()
  {
      double wrong_ans = 100 / SQUARED;  //we expect 4 but preprocessor just replaces it and we get 100 / 5* 5
      std::cout << wrong_ans << std::endl;  //but we get 100;
  }
  ```

* macros with arguments are even more prone to bugs

  ```cpp
  #include <iostream>

  #define SQUARE(a) a*a

  //#define SQUARE(a) (a*a) is better!

  int main()
  {
      int two_squared = SQUARE(2);
      std::cout << two_squared << std::endl;  //4
  }
  ```

<br>
<br>
<br>

# Generic Programming with Function Templates

- C++ templates are like blueprints and the compiler generates the appropriate functions/class from the templates.

- This illustration shows the use of templates, we can create a single function using template instead of creating the same function to support different types. In this example, since < is used within the function, all types that support < can be used as Template type T.

  ```cpp
  #include <iostream>

  template <typename T>

  T min(T a, T b)
  {
      return (a < b) ? a : b;  //return a if a < b else return b
  }

  int main()
  {
      std::cout << min<int>(10, 2) << std::endl;  //we can explicitely mention the type
      std::cout << min(2.5, 5.5) << std::endl;    //the compiler is also smart enough to figure it out
  }
  ```

* If we want to use user defined classes with template funcitons, we must make sure that it supports the opeations and methods

  ```cpp
  #include <iostream>
  #include <string>

  template <typename T>

  T min(T a, T b)
  {
      return (a < b) ? a : b;  //return a if a < b else return b
  }


  struct Person
  {
      std::string name;
      int age;

      //overloaded assignment operator
      bool operator<(const Person& rhs)const
      {
          return this->age < rhs.age; //this takes care of the (a<b) in the template function!
      }
  };


  int main()
  {
      Person p1{ "Curly", 19};
      Person p2{ "Moey", 25 };
      Person p3 = min(p1, p2);
      std::cout << p3.name << std::endl;  //Curly
  }
  ```

* Another example with overloading << operators

  ```cpp
  #include <iostream>
  #include <string>

  template <typename T1, typename T2>

  void display(T1 a, T2 b)
  {
      std::cout << a << " " << b << std::endl;
  }

  struct Person
  {
      std::string name;
      int age;
  };

  //overloadin the << operator (hence it is kept outside the Person class)
  std::ostream& operator<<(std::ostream& os, const Person& p)
  {
      os << p.name;
      return os;
  }

  int main()
  {
      Person p1{ "Curly", 19};
      Person p2{ "Moey", 25 };
      display(p1, p2);        //Curly Moey
  }
  ```

<br>
<br>
<br>

# Generic programming with class templates

- It is similar to template functions

  ```cpp
  #include <iostream>
  #include <string>

  template <typename T>

  class Item
  {
  private:
    std::string name;
    T value;  //this can be of any type as long as it supports the methods and operations
  public:
    Item(std::string name_value, T value_value) : name{ name_value }, value{ value_value } {};
    std::string get_name() { return name; }
    T get_value() { return value; }
  };

  int main()
  {
    Item<int> first{ "first", 10 };		//we must specify the template type, here it is the second argument 10, an int
    std::cout << first.get_value() << std::endl;		//10

    Item <Item<std::string>> item_in_item{"item_name", { "inner_item_name", "inner_item_value" }};
    std::cout << item_in_item.get_name() << std::endl;		//inner_name
    std::cout << item_in_item.get_value().get_name() << std::endl;	//inner_item_name
    std::cout << item_in_item.get_value().get_value() << std::endl;	//inner_item_value
  }
  ```
