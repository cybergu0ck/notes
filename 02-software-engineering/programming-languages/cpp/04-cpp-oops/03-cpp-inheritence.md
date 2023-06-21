# Inheritence

Inheritance is a powerful feature of object-oriented programming that allows us to create new classes from existing classes. The new class, called the derived class, inherits the properties and behaviors of the existing class, called the base class. This allows us to reuse code and reduce the amount of code we need to write.

- It is **Single Inheritence** if a new class is created from another 'single' class.
- It is **Multiple Inheritence** if a new class is created from two or more other classes.

There are three types of inheritance in C++:

1. Public inheritance: The derived class inherits all the public members of the base class. (Establishes a "is a" relationship)
1. Protected inheritance: The derived class inherits all the public and protected members of the base class. (Establishes "has a" relationship)
1. Private inheritance: The derived class inherits all the private members of the base class. (Establishes "has a" relationship)

<br>

## Base Class / Parent Class / Super Class

- The class being extended or inherited from.

<br>

## Derived Class / Child Class / Sub Class

- The class being created by inheriting attributes and methods from the base class.

<br>
<br>

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

> Haven't studied this, from what I have heard it's better to avoid this XD <br>
> <br>
