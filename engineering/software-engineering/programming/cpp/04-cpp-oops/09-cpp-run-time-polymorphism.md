# Run Time Polymorphsim/ Late Binding / Dynamic Binding

- Run time polymorphsim occurs at run time.
- Created using virtual functions along with base class pointers or base class references.
- function overloading (that occurs during run time) is an example.

<br>

## Virtual Function

- _Overridden functions are bound dynamically_ and **virtual functions are overridden.**
- We must declare the function we want to override (in the derived classes) as virtual in the Base class.

  ```cpp
  #include <iostream>
  using namespace std;

  class Base {
  public:
      virtual void say_hello()
      {
          cout << "Hello, I am a Base class object " << endl;
      }

      ~Base()
      {
          cout << "Base class destructor" << endl;
      }
  };

  class Derived: public Base {
  public:
      void say_hello()
      {
          cout << "Hello, I am a Derived class object " << endl;
      }

      ~Derived()
      {
          cout << "Derived class destructor" << endl;
      }
  };


  int main()
  {
      Base* b_ptr = new Base();
      b_ptr->say_hello();

      Base* d_ptr = new Derived();  //we can do this becuase Derived obj is a Base obj too (inheritance)
      d_ptr->say_hello();

      delete b_ptr;
      delete d_ptr;
  }


  //Hello, I am a Base class object
  //Hello, I am a Derived class object
  //Base class destructor
  //Base class destructor
  ```

- NOTE! The function signatures (in the base and derived classes) must be exactly same for overriding else it'll be considered as redefinition in the derived class. check this [stack overflow](https://stackoverflow.com/questions/9488168/virtual-function-const-vs-virtual-function-non-const) and the following illustration

  ```cpp
  #include <iostream>
  using namespace std;

  class Base {
  public:
      virtual void say_hello() const
      {
          cout << "Hello, I am a Base class object " << endl;
      }
  };

  class Derived : public Base {
  public:
      virtual void say_hello()        //won't be overriden as
      {
          cout << "Hello, I am a Derived class object " << endl;
      }
  };


  int main()
  {
      Base* b_ptr = new Base();
      b_ptr->say_hello();

      Base* d_ptr = new Derived();  //we can do this becuase Derived obj is a Base obj too (inheritance)
      d_ptr->say_hello();

      delete b_ptr;
      delete d_ptr;
  }

  //Hello, I am a Base class object
  //Hello, I am a Base class object
  ```

<br>

## Virtual Destructors

- In the above illustration, we can see that the base class destructor is called even for the pointer (of Base type) storing Derived class objects. This can be addressed using virtual destructors.
- Make it a rule to **_provide public virtual destructors for every class that contains virtual functions._**
- If the base class destructor is virtual then all derived class destructors are also virtual.
- For the curious, virtual **constructors** make no sense and it is not allowed in C++.

* In the following illustration, we make the destructor functions virtual and the run the same code as above.

  ```cpp
  #include <iostream>
  using namespace std;

  class Base {
  public:
      virtual void say_hello()
      {
          cout << "Hello, I am a Base class object " << endl;
      }

      virtual ~Base()
      {
          cout << "Base class destructor" << endl;
      }
  };

  class Derived : public Base {
  public:
      void say_hello()
      {
          cout << "Hello, I am a Derived class object " << endl;
      }

      ~Derived()
      {
          cout << "Derived class destructor" << endl;
      }
  };


  int main()
  {
      Base* b_ptr = new Base();
      b_ptr->say_hello();

      Base* d_ptr = new Derived();  //we can do this becuase Derived obj is a Base obj too (inheritance)
      d_ptr->say_hello();

      delete b_ptr;
      delete d_ptr;
  }

  //Hello, I am a Base class object
  //Hello, I am a Derived class object
  //Base class destructor
  //Derived class destructor
  //Base class destructor
  ```

<br>

## `override` specifier

- As mentioned above, the function signatures (in base and derived classes) must be exactly same for overriding, any change in the signature will be considered as redifinition (which is not overridable)
- The override specifier introduced in C++ 11 standard, when used in the derived class functions which we intend to override the base class function, it'll throw an error if there are changes in the signatures.
- Checkout the following illustration, We would want the say_hello function in the derived classes to override, however there is change in the function signature (which we may forget) since we used `override` in derived class's say_hello, the compiler throws an error, reminds us.

  ```cpp
  #include <iostream>
  using namespace std;

  class Base {
  public:
      virtual void say_hello() const
      {
          cout << "Hello, I am a Base class object " << endl;
      }

      virtual ~Base()
      {
          cout << "Base class destructor" << endl;
      }
  };

  class Derived: public Base {
  public:
      void say_hello() override
      {
          cout << "Hello, I am a Derived class object " << endl;
      }

       ~Derived()
      {
          cout << "Derived class destructor" << endl;
      }
  };


  int main()
  {
      Base* b_ptr = new Base();
      b_ptr->say_hello();

      Base* d_ptr = new Derived();  //we can do this becuase Derived obj is a Base obj too (inheritance)
      d_ptr->say_hello();

      delete b_ptr;
      delete d_ptr;
  }

  //ERROR: 'Derived::say_hello' method with override specifier 'override' did not override any base class methods.
  ```

<br>

## `final` specifier

- `final` specifier when used with a class will not let any other class to be derived from it.

  ```cpp
  class Base final {

  };

  class Derived: public Base {

  };

  //'Derived': cannot inherit from 'Base' as it has been declared as 'final'
  ```

* `final` specifier when used with virtual functions will not let any derived class function to override it.

  ```cpp
  #include <iostream>
  using namespace std;

  class Base {
  public:
      virtual void say_hello() final
      {
          cout << "Hello, I am a Base class object " << endl;
      }

      virtual ~Base()
      {
          cout << "Base class destructor" << endl;
      }
  };

  class Derived: public Base {
  public:
      virtual void say_hello()
      {
          cout << "Hello, I am a Derived class object " << endl;
      }

      virtual ~Derived()
      {
          cout << "Derived class destructor" << endl;
      }
  };


  int main()
  {
      Base* b_ptr = new Base();
      b_ptr->say_hello();

      Base* d_ptr = new Derived();  //we can do this becuase Derived obj is a Base obj too (inheritance)
      d_ptr->say_hello();

      delete b_ptr;
      delete d_ptr;
  }


  //ERROR: 'Base::say_hello':function declared as 'final' cannot be overridden by 'Derived::say_hello'
  ```

<br>
<br>

# Abstract class, Concrete class and Pure Virtual Functions

<br>

## Concrete class

- In C++, a concrete class is a class that can be instantiated directly, unlike an abstract class. It provides complete implementations for all of its member functions, including any virtual functions inherited from base classes.

<br>

## Abstract class using pure virtual functions

- In C++, an abstract class is a class that cannot be instantiated directly. It is designed to be used as a base class for other classes and serves as a blueprint for derived classes.
- An abstract class is created using a Pure Virtual Function. Any class that contains a pure virtual function is an Abstract class.

<br>

- A pure virtual function is a virtual function that is used to make a class abstract, is declared using the virtual keyword and '=0' in the end.

  ```cpp
  class IShape {
  public:
        virtual void draw() = 0; //pure virtual function (derived classes must and should override)
    };
  ```

* _The virtual functions in the derived classes must be overidden using the `override` keyword else those derived classes will also be abstract._

<br>

> An abstract class is typically used when we want to define a common interface or behavior that derived classes must implement. <br> <br> This concept is also used when it doesn't make sense to have implementation in base class but we need implementation in concrete class. for example we can have an abstract class called Shape with pure virtual function like draw, the implementation for draw in the abstract Shape class doesn't make sense but say concrete classes derived from abstract Shape like Circle, Square etc need implementation for draw function.

<br>

> "Program to Abstraction and not Implementation"

<br>

## Abstract class as an interface

- Unlike languages like Java or C#, interfaces in C++ are achieved using Abstract classes.
- It is convention to use precede the name of the abstract class using 'I\_' if we intend to use it as an interface. example: I_Shape

> COMPLETE NOTES
