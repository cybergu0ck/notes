# Encapsulation

_**Encapsulation** is a method of wrapping up the data and code acting on the data into a single unit._

<br>
<br>

## C Structs

_A **struct** in C is a user-defined data type that facilitates grouping of related vairables of different types as a single entity._

```cpp
struct Person {
    char name[50];
    int age;
    float height;
};

int main() {
    struct Person person1;      //struct keyword must be used here

    strcpy(person1.name, "John Doe");
    person1.age = 25;
    person1.height = 1.75;

    printf("Name: %s\n", person1.name);
    printf("Age: %d\n", person1.age);
    printf("Height: %.2f\n", person1.height);

    return 0;
}
```

<br>

- C follows **function centric approach** and lays more emphasis on functions and cares less for the data.
- Disadvantage of C structs is that all the data is public and hence can be missused.

  ```c
  struct Employee
  {
      float salary;
  };

  struct Student
  {
      float marks;
  };

  int main()
  {
      struct Employee e1;
      struct Student s1;
      s1.marks = e1.salary;  //there is no way to not allow this in C!
  }
  ```

<br>
<br>

## C++ Structs

_A **struct** in C++ is a user-defined data type that facilitates grouping of related functions along with the related vairables of different types as a single entity._

- C++ structs are called as extended structs.
- C++ provides Encapsulation through extended structs.
- C++ follows a **data centric approach** and lays more emphasis on data and cares less for functions.

```cpp
#include <iostream>

struct Employee
{
private:  //supports access specifier, it is "public" by default
    float salary;

    void get_bonus()
    {
        std::cout << "gets a bonus" << std::endl;
    }
};
```

<br>
<br>

### Acess Modifiers

- C++ provides three kinds of access modifiers:

    <ol type="1">
        <li>public : accessible anywhere</li>
        <li>private : accessible only by members or friends of the class.</li>
        <li>protected : accessible by members of the class and members of derived class and friends of the class.(not accesible by objects of base and derived classes!)</li>
    </ol>

- The member methods in the class declaration always has access to to the member attributes!

<br>

### Differences between C structs and C++ structs

| C struct                                                                                                           | C++ struct                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| Can only have variables as its member                                                                              | Can have both variables as well as functions as its member                                                                   |
| No variable of the struct plan can be qualified with an extended qualifier like 'const', 'static', 'volatile' etc. | Any member can be qualified with the extended qualifiers, like 'const', 'static' & 'volatile' if need be.                    |
| Does not provide support for access-specifiers, by default all members are 'public'.                               | Provides support for 3 different access-specifiers, like private, public and protected. By default, all members are 'public' |

<br>
<br>

## Class

_A **Class** in C++ is a user-defined data type that facilitates grouping of related functions along with the related vairables of different types as a single entity._

```cpp
#include <iostream>

class Employee
{
    //private by default
    float salary;

    void get_bonus()
    {
        std::cout << "gets a bonus" << std::endl;
    }
};
```

- Class is exactly similar to C++ structs except that the default access specifier is private. If the access speicifer is explicitely mentioned in all classes then the C++ code will work if we replace "class" by "struct".

<br>
<br>

## C++ Object Model

According to the C++ Object Model (Bjarne model), when an object is created,

- The object only represents the data members physically.
- The member functions are a single-copy on the code-segment (part of process memory) and is logically connected to all instances of the extended struct or class plan.

<br>

- Hence, The size of an object is influenced only by the number of **non-static** data members of the struct/class plan, Functions are common to all the objects of the struct/class kind.

  ```cpp
  #include <iostream>
  #pragma pack(1)	//disabling padding

  class Employee
  {
      //private by default
      char department;	//char occupies 1 byte
      float salary;		//float occupies 4 bytes

      void get_bonus()
      {
          std::cout << "gets a bonus" << std::endl;
      }
  };

  int main()
  {
      Employee the_guy;
      std::cout << "Employee object occupies " <<  sizeof(the_guy) << " bytes" << std::endl;
  }

  //Employee object occupies 5 bytes
  ```

- Refer [process memory](../01-cpp-fundamentals/01-introduction.md#c-memory) and [padding](../01-cpp-fundamentals/cpp-random.md#padding), to understand about #pragma.

<br>
<br>

## This Pointer

_`this` is the implicit parameter used by member functions to access the object on which they were called._

```cpp
#include <iostream>

class MyClass
{
public:
    int getData()
    {
        return data;
    }

    //Under the hood
    // int getData(MyClass* const this)
    // {
    //     return this->data;
    // }

private:
	int data{100};
};

int main()
{
	MyClass obj = MyClass();
	int res = obj.getData();    //obj.getData(&obj)
	std::cout << res << "\n";
}
```

- When we call a member function, this is initialised with the address of the object on which the function was invoked.
- `this` is a const pointer as it it is intended to always refer to "this" object.
- It is illegal for us to define a parameter or a variable named `this`.

<br>

### Use cases

- `this` can be used in the case where the name of the member attribute and the parameter name are the same.

  ```cpp
  void Account::set_balance(double balance)
  {
      balance = balance; //ambiguous and may result in wrong output
  }
  ```

  ```cpp
  void Account::set_balance(double balance)
  {
      this->balance = balance; //non-ambiguous
  }
  ```

- `this` is used to determine if two objects are the same

  ```cpp
  bool Player::compare_objects(const Player& other)
  {
      bool res;
      if (this == &other)
      {
          res = true;
      }
      else
      {
          res = false;
      }
      return res;
  }
  ```

<br>
<br>

## Const Member Functions

Member functions that use `const` are called const member functions.

- `const` modifies the type of the implicit [this](#this-pointer) pointer. A `const` following the parameter list indicates that `this` is a pointer to const.s

  ```cpp
  #include <iostream>

  class MyClass
  {
  public:
      int getData() const
      {
          return data;
      }

      //Under the hood
      //int getData(const MyClass* const) const
      //{
      //   return this->data;
      //}

  private:
      int data{100};
  };

  int main()
  {
      const MyClass obj = MyClass();
      int res = obj.getData();   //obj.getData(const &obj)
      std::cout << res << "\n";
  }
  ```

* For const qualified member functions, since `this` is a constant pointer to a const, the code inside the member function can only perform Read operations and cannot perform Write operations as it would modify the this object.

- const objects, references and pointers to const objects may call only const member functions.
- non const objects, references and pointers to non const objects can call both const and non const member functions.
- Constructors and destructors cannot be const qualified.

<br>
<br>

## Member Functions Returning This Object

```cpp
#include <iostream>

class MyClass
{
public:
  int data{100};

public:
  MyClass& getClone()
  {
    return *this;
  }
};

int main()
{
  MyClass first_obj = MyClass();
  MyClass second_obj = first_obj.getClone();
  std::cout << first_obj.data << "\n";
  std::cout << second_obj.data << "\n";
}

//100
//100
```

<br>
<br>

## Mutable Keywords

_`mutable` keyword is used to modify the behavior of a non-static data member of a class. When a data member is declared as mutable, it indicates that the member can be modified even within a const-qualified member function._

<br>

- Consider this illustration where we can create resizable gui screens and also fixed terminal by making the Screen object as const. However even in the terminal obj we need the cursor to move but the below code doesnt facilitate this. _const object can call const qualified member function only_ (keep this in mind, review const correctness)

  ```cpp
  #include <iostream>

  class Screen
  {
      /* Simulates a GUI screen (can resize)  or a Terminal Screen (fixed size) */
  private:
      int width, height;  //size of the screen
      int x, y;   //the cursor cordinates
  public:
      Screen(int w = 1920, int h = 1080, int x_val = 1, int y_val = 1) : width{ w }, height{ h }, x{ x_val }, y{ y_val }
      {
          //initialises the screen to 1920*1080 with the cursor at 1,1
      }

      void resize()
      {
          //resizing is only for gui (non-const obj)
          width -= (width / 2);
      }

      void move_cursor()
      {
          //simulating cursor movement for gui (non const obj)
          x++; //
      }

      void move_cursor() const
      {
          //simulating cursor movement for terminal (const obj)
          x++;  //modify data attribute in a const qualified function
      }

  };

  int main()
  {
      Screen gui;
      gui.resize();
      gui.move_cursor();

      const Screen terminal;
      terminal.resize();      //flags error (this is desirable as we like fixed size terminal)
      terminal.move_cursor(); //flags error (this is not desirable as we like the cursor to move)
  }
  ```

- The above problem can be solved by making the x,y attributes as `mutable` like `mutable int x,y;` in the class declaration

<br>
<br>

## Seperation of Declaration and Implementation

- We can seperate the class specification (declaration) from the implementation using header files.
  - .h file for class declaration
  - .cpp file for the class implementation

<br>

- Consider the following header file that contains the declaration

  ```h
  //account.h

  #pragma once

  class Account {
  private:
      double balance;
  public:
      double get_balance();
      void set_balance(double);
  };
  ```

- the following source file contains the implementation

  ```cpp
  //account.cpp

  #include <iostream>
  #include "account.h"   //include the header!
  using namespace std;


  void Account::set_balance(double bal) {
      balance = bal;
  }

  double Account::get_balance() {
      return balance;
  }


  int main()
  {
      Account mine;
      mine.set_balance(100);
      cout << mine.get_balance() << endl;
  }
  ```

<br>
<br>
