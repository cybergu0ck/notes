//NOTE - Review this notes after having reviewd oops

# Storage Class Specifiers

<br>

## `extern` specifier

_`extern` specifier facilitates the accessibility of global non-static variables across translational units._

- Each translation unit operates within its own scope, global variables declared in one translational unit are not accessible to other units.

  ```cpp
  //file1.cpp
  int a{10};
  ```

  ```cpp
  //file2.cpp
  #include <iostream>
  extern int a;

  int main(){
      std::cout << a << std::endl;  //10
  }
  ```

- Global non-static functions are directly accessible in other translation units without the need for the `extern` keyword, as long as their prototypes are provided.This is because functions in C++ have external linkage by default, which means they can be referenced across translation units without any additional keywords.

  ```cpp
  //file1.cpp
  #include <iostream>
  void foo(){
    std::cout << "fooyo";
  }
  ```

  ```cpp
  //file2.cpp
  void foo();

  int main(){
      foo();  //fooyo
  }
  ```

<br>
<br>

## `static` specifier

The `static` specifier's application is based on the context of where it is used.

<br>

### Local Static Variable

_local static variable preserves it's value across multiple function calls._

- Local static variables are one's that have function scope.
- The local static variable is initialized only once and retains its value between function invocations.
- Static variables reside in the [data segment](../01-cpp-fundamentals/01-introduction.md#c-memory) of the process memory. As such, they are already present on the data segment even before the function is called.
- For integral type varibles like int, the default value that is used for initialisaton on the data segment is zero.

  ```cpp
  #include <iostream>

  void add_plot()
  {
      static int num_plots; //Initialised to zero as it is an int
      num_plots++;
      //add plot logic
      std::cout << "total number of plots = " << num_plots << std::endl;
  }

  int main()
  {
      add_plot();
      add_plot();
      add_plot();
  }

  //total number of plots = 1
  //total number of plots = 2
  //total number of plots = 3
  ```

<br>

### Global Static Variable

_Global static variable preserves it's accessibility and limits it's scope to the translation unit where it is declared._

- The global static variable is not accessible from other translation units as it has internal linkage.

  ```cpp
  //file1.cpp
  static int a{10}; //Scope is limited to only this translation unit
  ```

  ```cpp
  //file2.cpp
  #include<iostream>
  extern int a;

  int main(){
    std::cout << a; //linker error
  }
  ```

<br>

### Global Static Function

_Global static function preserves it's accessibility and limits it's scope to the translation unit where it is declared._

- We can declare the function and use the definition from another translation unit.

  ```cpp
  //file1.cpp
  #include <iostream>

  static void fun(){
    std::cout << "fun called";
  }
  ```

  ```cpp
  //file2.cpp
  extern void fun(); //same result with or without "extern"

  int main(){
    fun();  //linker error
  }
  ```

<br>

### Static Member Variable

_static member variable is a member variable of a class that is shared among all instances of that class._

- It is important to remember that objects will only take responsibility of allocating memory for the non-static data members of the class because objects are created on the stack or heap while static members reside in the data segment.

- Static member variables need to be defined separately outside of the class declaration. This is because they are shared across all instances of the class and need to be allocated memory.

  ```cpp
  #include <iostream>

  class Entity {
  public:
    static int x;
    void printIt() {
      std::cout << x << "\n";
    }
  };

  int Entity::x;	//static data members of a class needs to be declared globally

  int main() {
    Entity e1 = Entity();
    e1.x =5;
    e1.printIt();	//5

    Entity e2 = Entity();
    e2.x =1;
    e2.printIt();	//1
    e1.printIt();	//1
  }
  ```

- It is a convention of refer to a static member variable using the class name and scope resolution operator intead of using objects.

  ```cpp
  int main() {
    Entity::x = 100;  //No need to instantiate an object!

    Entity e = Entity();
    e.printIt();  //100
  }
  ```

<br>

### Static Member Function

_Static member function is a member function of a class that belongs to the class itself rather than to instances of the class._

- Static member functions can be invoked without objects.
- Non-static member functions implicitly receive a pointer to the object they are invoked on as their first parameter, called the "implicit `this` pointer". However it is not the case for static member functions, hence they donot have access to the object's member variables and member functions!

- Static member functions has access only to static member variables.

  ```cpp
  #include <iostream>

  class Entity {
  public:
    int x;
    static void printIt() {
      std::cout << x << "\n"; //Compiler Error Here as printIt doesnt have implicit `this` pointer and thus cannot access `x`
    }
  };

  int main() {
    Entity e = Entity();
    e.x = 100;
    e.printIt();
  }
  ```

  ```cpp
  #include <iostream>

  class Entity {
  public:
    static int x;
    static void printIt() {
      std::cout << x << "\n";
    }
  };

  int Entity::x;	//static int variables are initialised to zero

  int main() {
    Entity::printIt();	//0
  }
  ```
