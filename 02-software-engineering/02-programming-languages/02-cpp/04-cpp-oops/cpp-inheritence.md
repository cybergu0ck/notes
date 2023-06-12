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

* However,the derived class constructors, destructors and overloaded assignment operators can invoke the base-class versions.

<br>
<br>

# Passing arguments to base class constructors

- `Derived() :Base{}, doubled_value{ 0 } ` in the below code executes the no args constructor of Base class (this sets the `value` attribute of Base class, which is now a attribute of Derived class aswell to 0) and then it'll initialise the `doubled_value` attribute to 0.

  ```cpp
  #include <iostream>
  using namespace std;

  class Base
  {
      int value;
  public:
      Base() :value{ 0 } {
          cout << "constructor of base class with no args" << endl;
      }

      Base(int x) : value{ x } {
          cout << "constructor of base class with an int arg" << endl;
      }
  };


  class Derived : public Base
  {
      int doubled_value;

  public:
      Derived() :Base{}, doubled_value{ 0 } {
          cout << "constructor of derived class with no args" << endl;
      }

      Derived(int x) : Base{ x }, doubled_value{ x * 2 } {
          cout << "constructor of derived class with one arg" << endl;
      }
  };


  int main()
  {
          Base base_obj1;
          Base base_obj2{ 100 };

          Derived derived_obj1;
          Derived derived_obj2{ 200 };

  }


  /*
  constructor of base class with no args
  constructor of base class with an int arg
  constructor of base class with no args
  constructor of derived class with no args
  constructor of base class with an int arg
  constructor of derived class with one arg
  */
  ```
