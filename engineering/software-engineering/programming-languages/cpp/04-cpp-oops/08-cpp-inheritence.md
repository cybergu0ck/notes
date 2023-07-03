# Inheritance

- Creating new classes by using the code present in already defined classes, extending the data.
- Inheritance facilitates **_IS-A relationship_**, A Derived object IS A Base object.

* The construction of an derived class object will always be the sum of the sizes of all non-static data members of the base class and the sum size of all non-static data members of the derived class. It does not matter which access specifier we are using at the time of inheritance.
* The Derived Class has all the data members of the Base class and Access Specifiers deals with only access to those data.

<br>
<br>

# Base Class and Derived Class

## Base Class

- The class being extended or inherited from.
- Base Classes are also known as Parent Class or Super Class.

<br>

## Derived Class

- The class being created by inheriting attributes and methods from the base class.
- Derived Classes are also known as Child Class or Sub Class.

<br>
<br>

# Types of Inheritance

## Based on the Base Class

- It is **Single Inheritence** if a new class is created from another 'single' class.
- It is **Multiple Inheritence** if a new class is created from two or more other classes.

<br>
<br>

## Based on the access specifiers

Different behaviour of inheritance is facilitated using the access specifiers in C++.

### Private Inheritance

- syntax: `class Derived : private Base`
- The base class private members are not accessible in the derived class.
- The protected and public members of the base, if any are accessible in the derived class as 'private' members.

<br>

### Protected Inheritance

- syntax: `class Derived : protected Base`
- The base class private members are not accessible in the derived class.
- The protected and public members of the base, if any are accessible in the derived class as 'protected' members.

<br>

### Public Inheritance

- syntax: `class Derived : public Base`
- The base class private members are not accessible in the derived class.
- The protected members of the base, if any are accessible in the derived class as 'protected' members.
- The public members of the base, if any are accessible in the derived class as 'public' members.

<br>
<br>

# Implementation

- The syntax for inheritance is as shown below

* access specifiers can be public, private and protected. If no access specifier is defined then by default private is considered.

  ```cpp
  #include <iostream>

  class Base {
      // Base class members
  };

  class Derived : access_specifier Base {
      // Derived class members
  };
  ```

* Illustration on which members are accessible

  ```cpp
  #include <iostream>
  using namespace std;

  class Base
  {
  public:
      int public_var{ 101 };
      void public_func() {
          cout << "this is a public function" << endl;
      }
  protected:
      int protected_var{ 102 };
      void protected_func() {
          cout << "this is a protected function" << endl;
      }
  private:
      int private_var{ 103 };
      void private_func() {
          cout << "this is a private function" << endl;
      }
  };


  class Derived : public Base
  {
  public:
      void accessing_parent_protected() {
          protected_func();
          cout << protected_var << endl;
      }

      //has error
      void accessing_parent_private() {
          private_func();					//error
          cout << private_var << endl;	//error
      }
  };


  int main()
  {
      Base base_obj;
      cout << base_obj.public_var << endl;  //ok,101
      base_obj.public_func();	//ok,this is a public function

      cout << base_obj.protected_var << endl; //error
      base_obj.protected_func();	//error

      cout << base_obj.private_var << endl; //error
      base_obj.private_func();	//error


      Derived derived_obj;

      cout << derived_obj.public_var << endl;
      derived_obj.accessing_parent_protected();  //ok
  }
  ```

<br>
<br>

# Constructors and Destructors with Inheritence

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

* A derived class doesn't inherit

  - Base class constructor
  - Base class destructor
  - Base class overloaded assignment operators
  - Base class friend functions

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
