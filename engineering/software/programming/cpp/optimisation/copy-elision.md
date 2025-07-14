# Copy Elision

The elision (ommision) of the copy or move constructors is called copy elision.

- Copy Elision can be applied even if the copy or move constructors have side effects! Meaning that if some code is written when an object is copied or moved and the compiler happens to perform copy elision then that code won't be run at all.
- Until C++ 17, The compiler can perform either copy elision or use copy or move constructor but since C++ 17 the compiler mandatorily performs copy elision.
- It is permitted in the following circumstances.

  1. Named Return Value Optimisation.
  2. Return Value Optimisation.
  3. Object Instantiation from a Temporary.
  4. Exception thrown and caught by Value.

<br>

- Consider the following class.

  ```cpp
  #include <iostream>

  class MyClass {
  public:
      int num;
  public:
      MyClass();		                    //default constructor
      MyClass(const MyClass& source);     //copy constructor
      MyClass(MyClass&& source) noexcept; // move constructor
      ~MyClass();                         //destructor
  };

  MyClass::MyClass() :num{ 0 }
  {
      std::cout << "default constructor called" << "\n";
  }

  MyClass::MyClass(const MyClass& source):num{source.num}
  {
      std::cout << "copy constructor is called " << "\n";
  }

  MyClass::MyClass(MyClass&& source) noexcept:num{source.num}
  {
      std::cout << "move constructor is called " << "\n";
      source.num = 0;
  }

  MyClass::~MyClass()
  {
      std::cout << "destructor called " << "\n";
  }
  ```

1. Named Return Value Optimisation

   ```cpp
   MyClass Foo()
   {
       MyClass named;
       return named;       //Returning a named object by value
   }

   int main()
   {
       MyClass obj = Foo();
   }

   //default constructor called
   //destructor called
   ```

2. Return Value Optimisation

   ```cpp
   MyClass Foo()
   {
       return MyClass();   //Returning a temporary object by value
   }

   int main()
   {
       MyClass obj = Foo();
   }

   //default constructor called
   //destructor called
   ```

3. Object Instantiation from a Temporary.

   ```cpp
   int main()
   {
       MyClass obj{ MyClass() };
   }

   //default constructor called
   //destructor called
   ```

4. Exception thrown and caught by Value. (I have not understand this)

   ```cpp
   MyClass Foo()
   {
       MyClass obj;
       throw obj;
   }

   int main()
   {
       try {
           Foo();
       }
       catch (MyClass obj)
       {
       }
   }

   //default constructor called
   //move constructor is called
   //destructor called
   //copy constructor is called
   //destructor called
   //destructor called
   ```

<br>
<br>
