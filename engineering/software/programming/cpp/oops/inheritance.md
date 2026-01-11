# Inheritance

Inheritance is the mechanism by which a class can acquire properties and behaviors from another class.

- **Base Class** is the class from which other classes inherit properties and behaviors. They are also known as Super Class or Parent Class.
- **Derived Class** is the class that inherits properties and behaviors from a base class and can also extend or modify them. They are also called as Sub Class or Child Class.
- Inheritance facilitates [Is A realtion](#is-a-relationship).

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

- The construction of an derived class object will always be the sum of the sizes of all non-static data members of the base class and the sum size of all non-static data members of the derived class. It does not matter which access specifier we are using at the time of inheritance, _the access specifier deals with only access to those data_.

<br>
<br>
<br>

## Virtual methods

Find it in [runtime polymorphism](./polymorphism/run-time-polymorphism.md#virtual-methods)

<br>
<br>
<br>

## Is a relationship

The derived object contains all the data corresponsing to it's base class, Hence we can use a derived object as if it were a base object i.e. _Derived is a Base_.

<br>
<br>

### Derived to base conversion

Derived-to-base conversion is the implicit conversion which allows the binding a base class referance or pointer to the base class part of a derived object. Derived "IS-A" Base.

```cpp
#include <iostream>
class Vehicle {
public:
    virtual ~Vehicle() {} //Virtual destructor for safe deletion
};

class Car : public Vehicle {
};

int main() {
    Car* myCar = new Car();
    Vehicle* myFavVehicle = myCar; // Base pointer points directly to the derived object
    Vehicle& myFav = *myCar; // Base reference binds to the dereferenced pointer (the object)

    delete myFavVehicle; // Works correctly because of the virtual destructor
    return 0;
}
```

- `myFavVehicle` is a pointer type (`Vehicle*`) in stack. It points to a `Car` object created in the heap.
- The automatic derived-to-base conversion applies only for conversions to a _reference or pointer type_. There is no such conversion from a derived-class type to the base-class type.
- Checkout [accessibility of derived to base conversion](#accesssibility-of-derived-to-base-conversion) in the context of different types of inheritance based on access specifier.

<br>
<br>

### Base to derived conversion

There is no implicit conversion from base to derived.

```cpp
Base base_obj;
Derived derived_obj;

Base *base_ptr = &derived_obj;
Derived *derived_ptr = base_ptr; //Still an error even if the base_ptr is bound to a derived object!
```

- Checkout [down casting](../data-types/casting.md#down-casting).

<br>
<br>
<br>

## Object Slicing

Object slicing occurs when a base class object is initialised or assigned with a derived class object, resulting in the loss of the derived class-specific attributes and methods.

- In the following code, the `display` method of `Base` class is called.

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

- When pointers are used, we invoke polymorphism i.e. [derived to base conversion](#derived-to-base-conversion).

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

      Base* baseObj2 = &derivedObj;
      baseObj2->display();          //Base value: 1, Derived value: 2
      return 0;
  }
  ```

<br>
<br>
<br>

## Preventing inheritance

`final` keyword is to be used to prevent a class from being used as a base class.

```cpp
class Base final {

};

class Derived: public Base {

};

//'Derived': cannot inherit from 'Base' as it has been declared as 'final'
```

- `final` specifier when used with virtual functions will not let any derived class function to override it.

  ```cpp
  class Base {
  public:
      virtual void say_hello() final
      {
      }

  };

  class Derived: public Base {
  public:
      virtual void say_hello()  //Error: virtual function 'virtual void Derived::say_hello()' overriding final function
      {
      }

  };
  ```

<br>
<br>
<br>

## Access Control in Inheritance

### Protected Members

- Like public, protected members are accessible to members and friends of classes derived from this class.
- Like private, protected members are inaccessible to users of the class.
- _A derived class member or friend may access the protected members of the base class only through a derived object. The derived class has no special access to the protected members of base-class objects_

  ```cpp
  class Base
  {
  protected:
      int protected_member;
  };

  class Derived: public Base
  {
  public:
      friend void access_protected_member(Derived &obj)
      {
          obj.protected_member = 10;  //No Error because access_protected_member can access protected member in Derived class.
      }
      friend void access_protected_member(Base &obj)
      {
          obj.protected_member = 10; //Error because access_protected_member cannot access protected member of Base class.
      }
  };
  ```

<br>

### Public Inheritance

1. All public and protected members of the base class, if any, are accessible in the derived class as 'public' and 'protected' respectively.
2. Private members of the base class remain inaccessible in the derived class, for all types of inheritance.

<br>
<br>

### Protected Inheritance

1. The public and protected members of the base class, if any, are accessible in the derived class as 'protected' members.
   - The derived class and its derived classes can access these members.
2. Private members of the base class remain inaccessible in the derived class, for all types of inheritance.

<br>
<br>

### Private Inheritance

1. The public and protected members of the base class, if any, are accessible in the derived class as 'private' members.
   - Only the derived class can access these members; any class deriving from it won't have access.
2. Private members of the base class remain inaccessible in the derived class, for all types of inheritance.

<br>

### Accesssibility of Derived to Base Conversion

_For any given point in the code, if a public member of the base class would be accessible, then the derived-to-base conversion is also accessible, and not otherwise._

//TODO - Learn this

<br>

### Friendship and Inheritance

//STUB - Learn these when needed. Knowledge available in textbook.

<br>
<br>

## Constructors in Inheritance

//TODO - Learn this; Inherited constructors

<br>
<br>

## Destructors in Inheritance

//TODO - Learn this; Virtual Destructors; Derived Class destructor; Calls to Virtuals in Constructors and Destructors

<br>
<br>

## Copy Control in Inheritance

//STUB - Learn these when needed. Knowledge available in textbook.

<br>
<br>

## Multiple Inheritance

//STUB - Learn these when needed. Knowledge available in textbook.

<br>
<br>

## Virtual Inheritance

//STUB - Learn these when needed. Knowledge available in textbook.

<br>
<br>
<br>

## Abstract Base Class

**An abstract class in C++ is a class that cannot be instantiated directly and is designed to be a base class for other classes.**

- An abstract class contains _at least one pure virtual function_.
- Abstract base classes are typically used to define a common interface for derived classes.
- We cannot (directly) create objects of a type that is an abstract base class.

  ```cpp
  class Base
  {
  public:
      virtual void hello() = 0; //pure virtual function and thus Base is an abstract class
  };

  int main()
  {
      Base obj;
  }

  //compilation error: cannot declare variable 'obj' to be of abstract type 'Base'
  ```

  ```cpp
  void foo(Base obj)
  {
      //cannot use Base object as parameter as it is an abstract class
  }
  //compilation error
  ```

<br>

### Concrete Class

- In C++, a concrete class is a class that can be instantiated directly, unlike an abstract class. It provides complete implementations for all of its member functions, including any virtual functions inherited from base classes.

<br>

### Interface in C++

- Unlike languages like Java or C#, interfaces in C++ are achieved using Abstract classes.
- It is convention to use precede the name of the abstract class using 'I\_' if we intend to use it as an interface. example: I_Shape

<br>
<br>
<br>

# Miscallaneous

//TODO - Clean the rest of the notes

### Override specifier

- C++ 11 presented the `override` keyword to explicitely define the overriding behaviour.

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
