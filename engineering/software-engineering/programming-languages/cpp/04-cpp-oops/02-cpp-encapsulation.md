# Encapsulation

- Encapsulation is a method of wrapping up the data and code acting on the data into a single unit.

## C structs

- C follows **function centric approach** and lays more emphasis on functions and cares less for the data.
- In the C programming language, a struct is a user-defined data type that allows you to group related variables of different types into a single entity.

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

- Disadvantage of this approach is that the compiler wont be able to check for missuse of data. See the following illustration.

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

      //code to set the salary and marks for both struct

      s1.marks = e1.salary;  //this may be gross miss-use of data that the compiler will allow!
  }
  ```

<br>
<br>

# C++ structs (extended structs) / Encapsulation

- C++ follows a **data centric approach** and lays more emphasis on data and cares less for functions.
- C++ structs allows the functions (that acts on the struct data) along with the data as it's members. (This is **Encapsulation**)

  ```cpp
  #include <iostream>

  struct Employee
  {
  private:
      float salary;

      void get_bonus()
      {
          std::cout << "gets a bonus" << std::endl;
      }
  };
  ```

<br>
<br>

# Acess Modifiers

- C++ provides three kinds of access modifiers:

  1. public : accessible anywhere
  2. private : accessible only by members or friends of the class.
  3. protected : accessible by members of the class and members of derived class.(not accesible by objects of base and derived classes!)

* The member methods in the class declaration always has access to to the member attributes!

<br>

## Differences between C structs and C++ structs

| C struct                                                                                                           | C++ struct                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| Can only have variables as its member                                                                              | Can have both variables as well as functions as its member                                                                    |
| No variable of the struct plan can be qualified with an extended qualifier like 'const', 'static', 'volatile' etc. | Any member can be qualified with the extended qualifiers, like 'const', 'static' & 'volatile' if need be.                     |
| Does not provide support for access-specifiers, by default all members are 'public'.                               | Provides support for 3 different access-specifiers, like private, public and protected. By default, all members are 'private' |

<br>
<br>

# C++ Object Model / Bjarne Model

The BJARNE model states, when an object gets created,

- The object only represents the data members physically.
- The member functions are a single-copy on the code-segment (part of process memory) and is logically connected to all instances of the extended struct or class plan.

<br>

- Hence, The size of an object is influenced only by the number of **non-static** data members of the struct/class plan, Functions are common to all the objects of the struct/class kind.
- static data members occupy data segment part of the process memory.
- illustration of calculating the size of a class object, see notes on #pragma pack().

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

<br>
<br>

# Class

- By default C++ structs (extended structs) have public access specifier. To distinguish between a C struct and C++ struct, `class` keyword was introduced. In a class, if no access specifier is stated, the compiler would assume `private` as default.

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

<br>

> <br> If the access specifiers are explicitely mentioned for all the data members (attributes and member functions), then C++ code will work if we replace all `class` keyword with `struct` keyword. <br> <br>

<br>
<br>

# `this` pointer

- It is a pointer to the object and hence contains the address of the object.
- `this` is a reserved keyword.
- It can be only used in the scope of the class (local scope) and hence resides in the stack.

```cpp
void Account::set_balance(double bal)
{
    balance = bal; //   this->balance = bal; behind the scenes!
}
```

<br>

- The invoked member functions donot know which object is invoking it. `this` is actually a hidden formal paramter in member functions. `this` acts as a link field between the objects and the member functions of the class.
- It is a const pointer of the class type.

  ```cpp
  class MyClass
  {
      int a;

  public:
      void foo();		//under the hood: foo(MyClass* const this)
  };

  void MyClass::foo()
  {
      //does nothing
  }
  ```

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

# `mutable` keyword

- In C++, the `mutable` keyword is used to modify the behavior of a non-static data member of a class. When a data member is declared as mutable, it indicates that the member can be modified even within a const-qualified member function.

* Consider this illustration where we can create resizable gui screens and also fixed terminal by making the Screen object as const. However even in the terminal obj we need the cursor to move but the below code doesnt facilitate this. _const object can call const qualified member function only_ (keep this in mind, review const correctness)

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

* The above problem can be solved by making the x,y attributes as `mutable` like `mutable int x,y;` in the class declaration
