# Constructors

- Constructor is a special member function that is invoked (automatically) whenever an object is created.
- Constructors are mostly used for initialisating data members but can perform anything the programmer desires.
- Constructors must have the same name as the class.
- Constructors do not have any return type associated.
- Constructors can be overloaded.

<br>

> It is crucial to know that
>
> - constructors donot create objects
> - constructors donot initialise objects (programmer has to do that)
> - compiler will not generate a constructor if we donot specify one. (other than the 4 exceptions stated below)
> - There are around 4 specific scenarios in C++98/2003 standards, where the compiler would assume a default constructor for a class which has not been provided with any constructor by the programmer.
>   - In the context of inheritance
>   - In the context of containment
>   - In the context of hybrid inheritance
>   - in the context of polymorphic classes.

<br>

- constructor will be automatically invoked whenever an object of the class is created, be it on stack or on the heap.

  ```cpp
  #include <iostream>


  class MyClass
  {
  private:
      int a;

  public:
      MyClass();	//constructor declaration
  };

  MyClass::MyClass()
  {
      std::cout << "constructor is called" << std::endl;
  }

  int main()
  {
      MyClass obj;	//object created on stack
      MyClass* obj_ptr = new MyClass; //object created on heap
  }

  //constructor is called
  //constructor is called
  ```

<br>
<br>

# Overloaded constructors

- As mentioned before constructors can be overlaoded.

  ```cpp
  #include <iostream>

  class MyClass
  {
  private:
      int a;
      double b;

  public:
      MyClass();	//default constructor declaration
      MyClass(int);	//overloaded one arg constructor
      MyClass(int, double); //overloaded two arg constructor
  };

  MyClass::MyClass()
  {
      std::cout << "default constructor is called" << std::endl;
  }

  MyClass::MyClass(int x)
  {
      std::cout << "overloaded one arg constructor is called" << std::endl;
  }

  MyClass::MyClass(int x, double y)
  {
      std::cout << "overloaded two arg constructor is called" << std::endl;
  }

  int main()
  {
      MyClass obj1;				//  obj1.MyClass::MyClass(&obj1);
      MyClass obj2{ 100 };		//  obj1.MyClass::MyClass(&obj1, 100);
      MyClass obj3{ 100,1.2 };	//  obj1.MyClass::MyClass(&obj1, 100, 1.2);

  }

  //default constructor is called
  //overloaded one arg constructor is called
  //overloaded two arg constructor is called
  ```

<br>
<br>

# Initialising the data attributes

- The business logic of constructor is always assignment and not initialisation. (check out the difference between them in 01-introduction.md)

* In the following code, we are actually _assigning the values to the data attributes inside the constructor and not technically initialising._

  ```cpp
  #include <iostream>

  class MyClass
  {
  private:
      int a;
      double b;

  public:
      MyClass(int, double);	//2 arg constructor
  };

  MyClass::MyClass(int x, double y)
  {
      a = x;	//This is Assignment and not Initialisation!
      b = y;	//This is Assignment and not Initialisation!
      std::cout << "data attribute a = " << a << " and b = " << b << std::endl;
  }


  int main()
  {
      MyClass obj{ 1, 2.2 };
  }

  //data attribute a = 1 and b = 2.2
  ```

<br>

## Explanation :

- When a MyClass object is created, it invokes the constructor. In the prolog phase of the constructor, the data attributes (whose size in known as type is known to the compiler) initialises them with garbage values. Then in the business logic of the constructor, they are assigned the given values.

  ```cpp
  //proof
  class MyClass
  {
      const int a;

  public:
      MyClass(int);
  };

  MyClass::MyClass(int x)
  {
      a = x;		//error because it is trying to assign to a const object (initialised with garbage)
  }
  ```

<br>

## Constructor initialiser list

- We can initialise the data members using constructor initialiser list, this will initialise the data members in the prolog phase itself. (check out the meaning of initialise in 01-introduction.md).
- The order in which the parameters are initilaised is the order in which they are written in the class and not the paramter initialisation list in the constructor definition.

  ```cpp
  #include <iostream>

  class MyClass
  {
  private:
      int a;
      double b;

  public:
      MyClass(int, double);	//2 arg constructor
  };

  MyClass::MyClass(int x, double y): a{x}, b{y}
  {
      //using constructor initialisation list
  }

  int main()
  {
      MyClass obj{ 1, 2.2 };
  }
  ```

<br>
<br>

# Delegated constructors

- Delegated constructors in C++ are a feature introduced in C++11 that allow a constructor to call another constructor of the same class. This can be useful for reducing code duplication and improving readability.

- Instead of initialising the data attributes in every constructor, we can use the constructor that has most args as delegated constructor.

  ```cpp
  #include <iostream>

  class MyClass
  {
  private:
      int a;
      double b;

  public:
      MyClass();				//default constructor
      MyClass(int);			//1 arg constructor
      MyClass(int, double);	//2 arg constructor
  };


  MyClass::MyClass(int x, double y) : a{ x }, b{ y }
  {
      //This overloaded 2 arg constructor will be used for delegated constructors
      std::cout << "The data attribute a = " << a << " and b = " << b << std::endl;
  }

  MyClass::MyClass(int x) : MyClass(x,0)
  {
      //initialising b  to 0 using delegated constructor
      std::cout << "overloaded one arg constructor called which in turn will call the delegated constructor" << std::endl;
  }

  MyClass::MyClass(): MyClass(0, 0)
  {
      //initialising both data attributes to 0 using delegated constructor
      std::cout << "default constructor called which in turn will call the delegated constructor" << std::endl;
  }

  int main()
  {
      MyClass obj1{};
      MyClass obj2{ 1 };
      MyClass obj3{ 1,1.2 };
  }

  //The data attribute a = 0 and b = 0
  //default constructor called which in turn will call the delegated constructor
  //The data attribute a = 1 and b = 0
  //overloaded one arg constructor called which in turn will call the delegated constructor
  //The data attribute a = 1 and b = 1.2
  ```

<br>

> <br> From the above output, it looks when obj1 is created it calls 2 args constructor instead of default constructor, one should not be carried away seeing the ouput. obj1 calls the default constructor only but the delegated constructor is called in it's prolog phase. Hence we see the cout statement of default constructor after the cout statement in two arg constructor. <br> <br>

<br>
<br>

# Destructors

- Destructors are also special kind of member function that is invoked automatically when the object is destroyed.
- Destructors are generally used to perform cleanup operations but can perform anything the programmer desires.
- Destructors have the same name as the class preceded by a tilde symbol (~)
- Destructors have no return type and no parameters.
- There can be only 1 destructor for a class hence it cannot be overloaded unlike constructors.

<br>

> <br> It is a misconception that a destructor destroys objects! <br> <br>

<br>

- Illustration of destructors, they are called when the object dies i.e. when the scope of the object ends.

  ```cpp
  #include <iostream>

  class MyClass
  {
  private:
      int a;
      double b;
      std::string name;

  public:
      MyClass(int = 10, double = 2.5, std::string = "anonymous");
      ~MyClass();  //destrcutor declaration

  };

  MyClass::MyClass(int x, double y, std::string name_val): a{x}, b{y}, name{name_val}
  {
  }

  MyClass::~MyClass()
  {
      std::cout << "destructor called by " << name << std::endl;
  }

  int main()
  {
      {
          MyClass obj1{ 100, 9.9, "first_obj" };
      }		//obj1 calls the destructor here as it's scope ends here

      MyClass obj2{ 100, 9.9, "second_obj" }; //calls it's destructor when main ends
  }

  //destructor called by first_obj
  //destructor called by second_obj
  ```

<br>
<br>

# Copy Constructors

- A constructor that takes a single object of its own kind as a parameter by reference is called a copy constructor.
- Copy constructors are needed when a new object under construction is being initialized with an object of its own kind.
- Copy constructors are also called when objects are passed into functions as parameters, because pass by value is the default case in C++.

- If there is no copy constructor defined in the class and the class objects happens to copy construct objects, then the compiler would assume a copy constructor which will perform member-to-member copy (bitwise copy) and will also be inlined.

* It is good practice to provide the copy constructor with a const reference parameter.

<br>

- Illustration of copy construction

  ```cpp
  #include <iostream>

  class MyClass
  {
  private:
      int a;
      double b;
      std::string name;

  public:
      MyClass(int = 10, double = 2.5, std::string = "anonymous");
      MyClass(const MyClass& source); //copy constructor declaration

  };

  MyClass::MyClass(int x, double y, std::string name_val): a{x}, b{y}, name{name_val}
  {
      //default constructor, notice that we have used default values for paramters
      std::cout << "two arg constructor called by " << name <<  std::endl;
  }

  MyClass::MyClass(const MyClass& source) : a{source.a}, b{source.b}, name{source.name}
  {
      std::cout << "copy constructor called by " << name << std::endl;
  }

  //global function
  void tester(MyClass x)
  {
      //just to show that copy constructor is called when objects are passed into functions!
  }

  int main()
  {
      MyClass obj1{};		//calls the two arg constructor
      MyClass obj2{ obj1 };  //obj2 calls the copy constructor (notice output is misleading)
      tester(obj1);			////calls the copy constructor
  }

  //two arg constructor called by anonymous
  //copy constructor called by anonymous
  //copy constructor called by anonymous
  ```

- We can write the copy constructor using delegated constructor like:

  ```cpp
  MyClass::MyClass(const MyClass& source) : MyClass{source.a, source.b}
  {
      std::cout << "copy constructor called" << std::endl;
  }
  ```

> Is this bad as it will increase the number of function calls? DOUBT

<br>
<br>

# `explicit` constructor

- A constructor that is tagged with `explicit` keyword is an explicit constructor, as such it is used to prevent implicit conversions during object construction.

* Illustration to understand implicit conversion. In the following code when x is assigned to obj, the one arg constructor of MyClass assists the compiler for implicitley conversion (we can see it being called in the debugger) and the data attribute is now set to the value of x i.e. 10.

  ```cpp
  #include <iostream>

  class MyClass
  {
  private:
      int a;

  public:
      MyClass(int = 1);
  };

  MyClass::MyClass(int x): a{x}
  {}

  int main()
  {
      int x{ 10 };
      MyClass obj;
      obj = x;        //compiler allows this as an implicit conversion is made
  }
  ```

> one arg constructors are generally called as conversion constructors as they facilitate implicit conversion. <br> <br>

- We can use `explicit` to avoid this

  ```cpp
  #include <iostream>

  class MyClass
  {
  private:
      int a;

  public:
      explicit MyClass(int = 1);
  };

  MyClass::MyClass(int x): a{x}
  {}

  int main()
  {
      int x{ 10 };
      MyClass obj;
      obj = x;        //compiler raises error
  }
  ```
