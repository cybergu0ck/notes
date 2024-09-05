# Inheritance

## Dynamic Binding

Dynamic binding in the context of inheritance is the process where the method to be invoked is determined at runtime based on the type of the object, typically using virtual functions.

- A base class uses virtual functions to allow derived classes to override them, enabling dynamic binding when called through a pointer or reference.

- Any nonstatic member function, other than a constructor, may be virtual.
- The `virtual` keyword is used only in the class declaration, not in the function definition outside the class body. i.e.
- A function that is declared as virtual in the base class is implicitly virtual in the derived classes as well.
- A derived-class function that overrides an inherited virtual function must have the same parameter type(s) as the base-class function that it overrides.
- The return type of a virtual in the derived class also must match the return type of the function from the base class.
  - There is one exception to this, If D is derived from B, then a base class virtual can return a B*
    and the version in the derived can return a D*.
- Derived classes need not always override the virtual functions that they inherit, in that case it inherits the version defined in the base class.

### Override specifier

- C++ 11 presented the `override` keyword to explicitely define the overriding behaviour.

- A function can be declared and not defined as long as it is never used.

  ```cpp
  class RandomClass{
      void declared_but_not_defined();
  };

  int main()
  {}

  //no compilation errro
  ```

- Virtual function needs to be defined irrespective of it's usage becuase the compiler has no way to determine wether a virtual function is used. At run time, the approriate function (base or derived) is called due to dynamic binding.

  ```cpp
  class RandomClass{
      virtual void declared_but_not_defined();
  };

  int main()
  {}

  //compilation error
  ```

## Is A Relationship

- The base and the derived parts of an object are not guaranteed to be stored contiguously. The standard doesn't specify how the derived objects are laid out in memory.
- The derived object contains all the data corresponsing to it's base class, Hence we can use a derived object as if it were a base object.

- Derived-to-base conversion is the implicit conversion which allows the binding a base class referance or pointer to the base class part of a derived object. Derived IS-A Base.

  ```cpp
  Derived derived_obj;

  Base *ptr = &derived_obj;
  Base &ref = derived_obj;
  ```

- The automatic derived-to-base conversion applies only for conversions to a _reference or pointer type_. There is no such conversion from a derived-class type to the base-class type.

- There is no implicit conversion from base to derived.

  ```cpp
  Base base_obj;
  Derived derived_obj;

  Derived *ptr = &base_obj;
  Derived &ref = base_obj;

  Base *base_ptr = &derived_obj;
  Derived *derived_ptr = base_ptr; //Still an error even if the base_ptr is bound to a derived object!
  ```

- //REVIEW - Add about dynamic_cast and static_cast of Base to derived.

- Object slicing occurs when a base class object is initialised or assigned with a derived class object, resulting in the loss of the derived class-specific attributes and methods.

  - It is not a good practice and hence pointers or references to the base class objects must be preferred.

    ```cpp
    #include <iostream>

    class Base {
    public:
        int baseValue;
        virtual void display() const {
            std::cout << "Base value: " << baseValue << std::endl;
        }
    };

    class Derived : public Base {
    public:
        int derivedValue;
        void display() const override {
            std::cout << "Base value: " << baseValue << ", Derived value: " << derivedValue << std::endl;
        }
    };

    int main() {
        Derived derivedObj;
        derivedObj.baseValue = 1;
        derivedObj.derivedValue = 2;

        // Object slicing occurs here
        Base baseObj1{derivedObj};  //calls the compiler synthesised copy constructor
        Base baseObj2 = derivedObj; //calls the compiler synthesised copy assignment
        baseObj.display();          // Base value: 1

        return 0;
    }
    ```

## Constructors in the context of Inheritance

- Although, the base class constructor is called before the derived class constructor is called. The derived class cannot intialise the class members of the base class without explicitley using a base class constructor.
- The base class is initialised first and then the derived class, in the order in which they are declared in the class.
- The constructor body of a derived constructor can assign values to its public or protected base-class members. Although it can assign to those members, it generally should not do so. Like any other user of the base class, a derived class should respect the interface of its base class by using a constructor to initialize its inherited members.

<br>
<br>

## Base Class

- **_Base classes should define a virtual destructor._** Virtual destructors are needed even if they do no work.

- A class must be defined, not just declared, before we can use it as a base class. Because the derived class must have the information of the members of the base class.

  ```cpp
  class Base;  //Forward declaration

  class Derived:public Base{  //Error
  };

  class Base{ //Class Definiton
  };
  ```

## Final specifier

- C++ 11 pressented the `final` keyword to prevent a class from being used as a base class.

## Virtual Inheritance

solves diamond inheritance problem

<br>
<br>
<br>

# Inheritance (Old Notes)

**_Inheritance is the mechanism by which a class can acquire properties and behaviors from another class._**

- **Base Class** is the class from which other classes inherit properties and behaviors. They are also known as Super Class or Parent Class.
- **Derived Class** is the class that inherits properties and behaviors from a base class and can also extend or modify them. They are also called as Sub Class or Child Class.
- Inheritance facilitates **_IS-A relationship_**, A Derived class IS A Base class.

- The syntax for inheritance is as shown, The access specifiers can be public, private and protected. _If no access specifier is defined then by default private is considered._

  ```cpp
  #include <iostream>

  class Base {
      // Base class members
  };

  class Derived : access_specifier Base {   //private by default
      // Derived class members
  };
  ```

<br>

Some Important points about Inheritance:

- Inheritance can be Single or Multiple based on the number of classes it inherits from.
- Inheritance can be public, protected and private based on the access specifier.
- The construction of an derived class object will always be the sum of the sizes of all non-static data members of the base class and the sum size of all non-static data members of the derived class. It does not matter which access specifier we are using at the time of inheritance, _the access specifier deals with only access to those data_.

<br>
<br>

## Public Inheritance

1. All public and protected members of the base class, if any are accessible in the derived class as 'public' and 'protected' respectively.
1. Private members of the base class remain inaccessible in the derived class, for all types of inheritance.

<br>
<br>

## Protected Inheritance

1. The public and protected members of the base class, if any are accessible in the derived class as 'protected' members.
   - The Derived class and it's derived classes can access these members.
2. Private members of the base class remain inaccessible in the derived class, for all types of inheritance.

<br>
<br>

## Private Inheritance

1. The public and protected members of the base class, if any are accessible in the derived class as 'private' members.
   - Only the Derived class can access these members, any class deriving from it won't have access.
2. Private members of the base class remain inaccessible in the derived class, for all types of inheritance.

<br>
<br>
<br>

# Constructors and Destructors in the context of Inheritence

- When a derived object is created the base class constructor executes first and then the derived class constructor executes.
- When a derived object is destroyed, the derived class destructor executes then the base class destructor executes, each destructor should free resources allocated in it's own constructors.

  ```cpp
  #include <iostream>
  using namespace std;
  class Base
  {
  public:
      Base() {
          cout << "constructor of base class is executing..." << endl;
  }
      ~Base() {
          cout << "destructor of base class is executing..." << endl;
      }
  };
  class Derived : public Base
  {
  public:
      Derived() {
          cout << "constructor of derived class is executing..." << endl;
      }
      ~Derived() {
          cout << "destructor of derived class is executing..." << endl;
      }
  };
  int main()
  {
      {
          Base base_obj;
      }
      {
          Derived derived_obj;
      }
  }
  /*
  constructor of base class is executing...
  destructor of base class is executing...
  constructor of base class is executing...
  constructor of derived class is executing...
  destructor of derived class is executing...
  destructor of base class is executing...
  */
  ```

- A derived class doesn't inherit

  - Base class constructor
  - Base class destructor
  - Base class overloaded assignment operators
  - Base class friend functions

- If

<br>
<br>

# Illustration for concept clarity

- Consider the following class declaration to understand constructors in the context of inheritance.

  ```cpp
  #include <iostream>
  using namespace std;

  class Base
  {
  public:
      int value;
      int doubled_value;
      Base() :value{ 0 } , doubled_value{0}{
          //default constructor
          cout << "default constructor of base class with no args" << endl;
      }

      Base(int val) : value{ val }, doubled_value{ val*2 }  {
          //overloaded constructor
          cout << "overloaded constructor of base class with an int arg" << endl;
      }
  };


  class Derived : public Base
  {
  public:
      int trippled_value;
      Derived() :trippled_value{ 0 } {
          //default constructor
          cout << "default constructor of derived class with no args" << endl;
      }

      Derived(int val) : trippled_value{ val * 3 } {
          //overloaded constructor
          cout << "overloaded constructor of derived class with one arg" << endl;
      }
  };
  ```

* Now if we create a Derived Object with no arguments, then the compiler will first call the default constructor (no args) of the Base class and then the default constructor (no args) of the Derived class as shown here

  ```cpp
  int main()
  {
      Derived dobj;
      cout << dobj.trippled_value << endl;
      cout << dobj.doubled_value << endl;
      cout << dobj.value << endl;
  }
  //default constructor of base class with no args
  //default constructor of derived class with no args
  //0
  //0
  //0
  ```

* When we create a Derived object with an argument, the defualt constructor (no args) of Base class is called first (NOT the overloaded constructor of Base class) and then the overloaded class constructor of Derived Class is executed as shown here:

  ```cpp
  int main()
  {
      Derived dobj(30);
      cout << dobj.trippled_value << endl;
      cout << dobj.doubled_value << endl;
      cout << dobj.value << endl;

  }

  //default constructor of base class with no args
  //overloaded constructor of derived class with one arg
  //90
  //0
  //0
  ```

<br>

## Invoking Overloaded Base Class Constructors

- However,the derived class constructors, destructors and overloaded assignment operators can invoke the base-class versions and arguments can also be passed.

- Here we are invoking the overloaded constructor of Base class in the overloaded constructor of Derived class, As always the Base part is executed before the Derived Part.

  ```cpp
  /*
  modified (invoking Base class from derived calss) class definiton

  Derived(int val) : Base{val}, trippled_value{ val * 3 } {
      //overloaded constructor
      cout << "overloaded constructor of derived class with one arg" << endl;
  }
  */


  int main()
  {
      Derived dobj(30);
      cout << dobj.trippled_value << endl;
      cout << dobj.doubled_value << endl;
      cout << dobj.value << endl;

  }

  //overloaded constructor of base class with an int arg
  //overloaded constructor of derived class with one arg
  //90
  //60
  //30
  ```

<br>
<br>

# Compiler generating constructors

## In the context of Inheritance

- If the derived class doesnt have any constructor and the base class has one, then the compiler will generate one for the derived class.

  ```cpp
  #include <iostream>
  using namespace std;

  class Base {
      int i;
  public:
      Base() :i{ 0 } {
          cout << "Base class default constructor called" << endl;
      }
  };

  class Derived : public Base {
  public:
      //no constructors for derived class, yet the compiler will generate one as base has one
  };

  int main()
  {
      Derived obj;
  }

  //Base class default constructor called
  ```

<br>

## In the context of containment

- If the derived class has a Base class object as a data attribute, The compiler will generate a constructor if we have not defined one.

  ```cpp
  #include <iostream>
  using namespace std;

  class Base {
      int i;
  public:
      Base() :i{ 0 } {
          cout << "Base class default constructor called" << endl;
      }
  };

  class Derived : public Base {
      Base b;	//Derived HAS-A Base (containment)
  public:
      //no constructors for derived class, yet the compiler will generate one
  };

  int main()
  {
      Derived obj;
  }

  //Base class default constructor called
  //Base class default constructor called
  ```

<br>

## In the context of Hybrid Inheritance

<br>
<br>

# Copy/Move constructors and overloaded assignment operator in context of inheritance

- Consider the following class definition for the illustration

  ```cpp
  #include <iostream>
  using namespace std;

  class Base
  {
  public:
      int value;
      int doubled_value;
      Base() :value{ 0 } , doubled_value{0}{
          //default constructor
          cout << "default constructor of base class with no args" << endl;
      }

      Base(int val) : value{ val }, doubled_value{ val*2 }  {
          //overloaded constructor
          cout << "overloaded constructor of base class with an int arg" << endl;
      }

      Base(const Base& other) :value{ other.value }, doubled_value{ other.doubled_value }{
          //copy constructor
          cout << "copy constructor of base class" << endl;
      }

      Base& operator = (const Base& rhs) {
          cout << "overloaded copy assignment of base class" << endl;
          //overloaded copy assigment operator
          if (this == &rhs) {
              return *this;
          }
          value = rhs.value;
          doubled_value = rhs.doubled_value;
          return *this;
      }
  };


  class Derived : public Base
  {
  public:
      int trippled_value;
      Derived() :trippled_value{ 0 } {
          //default constructor
          cout << "default constructor of derived class with no args" << endl;
      }

      Derived(int val) : Base{val} , trippled_value { val * 3 } {
          //overloaded constructor
          cout << "overloaded constructor of derived class with one arg" << endl;
      }

      Derived(const Derived& other) : Derived{other.value} {
          //copy constructor
          cout << "copy constructor of derived class" << endl;
      }

      Derived& operator=(const Derived& rhs) {
          cout << "overloaded copy assignment of derived class" << endl;
          //overloaded copy assignment operator
          if (this == &rhs) {
              return *this;
          }
          trippled_value = rhs.trippled_value;
          return *this;
      }
  };
  ```

* Consider the case of copy constructor

  ```cpp
  int main()
  {
      Derived obj(30);
      cout << obj.value << endl;          //30
      cout << obj.doubled_value << endl;  //60
      cout << obj.trippled_value << endl; //90


      Derived obj2{ obj };        //copy constructor
      cout << obj2.value << endl;
      cout << obj2.doubled_value << endl;
      cout << obj2.trippled_value << endl;
  }

  //overloaded constructor of base class with an int arg
  //overloaded constructor of derived class with one arg
  //30
  //60
  //90

  //overloaded constructor of base class with an int arg
  //overloaded constructor of derived class with one arg
  //copy constructor of derived class
  //30
  //60
  //90
  ```

* Now consider the case of overloaded assignment operator

  ```cpp
  int main()
  {
      Derived obj(30);
      cout << obj.value << endl;          //30
      cout << obj.doubled_value << endl;  //60
      cout << obj.trippled_value << endl; //90


      Derived obj2{ obj };        //copy constructor
      cout << obj2.value << endl;
      cout << obj2.doubled_value << endl;
      cout << obj2.trippled_value << endl;


      obj = obj2;  //overloaded copy assignment
      cout << obj.value << endl;          //30
      cout << obj.doubled_value << endl;  //60
      cout << obj.trippled_value << endl; //90
  }

  //overloaded constructor of base class with an int arg
  //overloaded constructor of derived class with one arg
  //30
  //60
  //90

  //overloaded constructor of base class with an int arg
  //overloaded constructor of derived class with one arg
  //copy constructor of derived class
  //30
  //60
  //90

  //overloaded copy assignment of derived class
  //30
  //60
  //90
  ```

<br>
<br>

# Redefining Base Class Methods

- Derived classes can not only invoke Base class methods but also override or redefine base class methods.

  ```cpp
  #pragma once
  #include <iostream>
  using namespace std;

  class Account {

  public:
      double balance;
      Account() :balance{ 0 }
      {
      }
      void deposit(double amount)
      {
          balance += amount;
      }
  };

  class SavingsAccount : public Account {
  public:
      void deposit(double amount)
      {
          amount += (amount * 0.1);
          Account::deposit(amount);
      }
  };

  int main()
  {
      SavingsAccount mine;
      mine.deposit(100);
      cout << mine.balance << endl;		//110 because deposite of SavingsAccount class is executed
  }
  ```

<br>
<br>

# Multiple Inheritance

> Haven't studied this, from what I have heard it's better to avoid this XD <br> > <br>
