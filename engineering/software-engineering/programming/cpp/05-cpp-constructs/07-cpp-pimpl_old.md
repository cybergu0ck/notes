# PIMPL (Pointer to IMPLementation)

- PIMPL is a design pattern in C++ that aims to reduce coupling and improve encapsulation by hiding implementation details of a class from its clients.
- The PIMPL model is also known as the "Compiler Firewall" or "Opaque Pointer" idiom.
- In the PIMPL model, the public interface of a class consists of a thin wrapper that holds a pointer to an opaque type representing the private implementation. The actual implementation details are encapsulated within a separate private class, often referred to as the "implementation class."

* Without the PIMPL (i.e. the class Manager in this example), for any object created on the heap we need to take care of deallocation. PIMPL encapsulates this.

  ```cpp
  #include <iostream>
  using namespace std;

  class MyClass
  {
      int a;
  public:
      MyClass(int x = 0) : a(x)
      {
          cout << "1 arg constructor called for MyClass object" << endl;
      }
      ~MyClass()
      {
          cout << "destructor called for MyClass object" << endl;
      }
      void print_a()
      {
          cout << "The data attribute a = " << a << endl;
      }
  };


  class Manager
  {
      //This is a wrapper class for MyClass, This is a PIMPL model and a RAII
      MyClass* ptr;

  public:
      Manager(int x)
      {
          ptr = new MyClass(x);	//creates a MyClass object on the heap, calls the constructor
      }

      ~Manager()
      {
          delete ptr;			//calls the destructor
      }

      void print_a()
      {
          ptr->print_a();
      }
  };

  int main()
  {
      Manager obj{ 21 };
      obj.print_a();

  }

  //1 arg constructor called for MyClass object
  //The data attribute a = 21
  //destructor called for MyClass object
  ```

<br>
<br>

# Using Overloaded Arrow Operator for PIMPL design

- Notice that member functions of the MyClass is not accesible by the Manager objects, In the above code we have a function with the same name print_a in the Manager which calls the print_a of MyClass.
- We can use the overloaded arrow operator to make this code better

  ```cpp
  #include <iostream>
  using namespace std;

  class MyClass
  {
      int a;
  public:
      MyClass(int x = 0) : a(x)
      {
          cout << "1 arg constructor called for MyClass object" << endl;
      }
      ~MyClass()
      {
          cout << "destructor called for MyClass object" << endl;
      }
      void print_a()
      {
          cout << "The data attribute a = " << a << endl;
      }
  };


  class Manager
  {
      //This is a wrapper class for MyClass, This is a PIMPL model and a RAII
      MyClass* ptr;

  public:
      Manager(int x)
      {
          ptr = new MyClass(x);	//creates a MyClass object on the heap, calls the constructor
      }

      ~Manager()
      {
          delete ptr;
      }

      MyClass* operator->() //Overloaded Arrow Operator
      {
          return ptr;
  }
  };

  int main()
  {
      Manager obj{ 21 };
      obj->print_a();     //obj is not a pointer! under the hood: obj.operator=()
  }

  //1 arg constructor called for MyClass object
  //The data attribute a = 21
  //destructor called for MyClass object
  ```

<br>
<br>

# PIMPL relying on compiler generated copy constructor

- The compiler generated copy constructor leads to dangling poiters in PIMPL design.

* The following code is the same code (as above), However when we copy construct objects it compiles well but throws linker error.

  ```cpp
  #include <iostream>
  using namespace std;

  class MyClass
  {
      int a;
  public:
      MyClass(int x = 0) : a(x)
      {
          cout << "1 arg constructor called for MyClass object" << endl;
      }
      ~MyClass()
      {
          cout << "destructor called for MyClass object" << endl;
      }
      void print_a()
      {
          cout << "The data attribute a = " << a << endl;
      }
  };


  class Manager
  {
      //This is a wrapper class for MyClass, This is a PIMPL model and a RAII
      MyClass* ptr;

  public:
      Manager(int x)
      {
          ptr = new MyClass(x);	//creates a MyClass object on the heap, calls the constructor
      }

      ~Manager()
      {
          delete ptr;			//calls the destructor
      }

      MyClass* operator->()
      {
          return ptr;
      }
  };

  int main()
  {
      Manager obj1{ 21 };
      obj1->print_a();
      Manager obj2{ obj1 };	//compiles but doesnt link (linker error/ run time error)
  }
  ```

<br>

> Add Image from one note

<br>
<br>

- Code with copy constructors, when the Manager object is being copy constructed, it will call the Manager Class's copy constructor. In it's biz logic at ` ptr = new MyClass(*(source.ptr));`, the copy constructor of MyClass is called because a MyClass object is being used to initialise a new MyClass object on the heap. Use the code and debug it to see the control flow!

  ```cpp
  #include <iostream>
  using namespace std;

  class MyClass
  {
      int a;
  public:
      MyClass(int x = 0) : a(x)
      {
          cout << "MyClass's 1 arg constructor called" << endl;
      }

      ~MyClass()
      {
          cout << "MyClass's destructor called" << endl;
      }

      void print_a()
      {
        cout << "The data attribute a = " << a << endl;
      }

      MyClass(const MyClass& source): a{source.a}
      {
          cout << "MyClass's copy constructor called" << endl;
      }
  };


  class Manager
  {
      //This is a wrapper class for MyClass, This is a PIMPL model and a RAII
      MyClass* ptr;

  public:
      Manager(int x)
      {
          ptr = new MyClass(x);	//creates a MyClass object on the heap, calls the constructor
      }

      ~Manager()
      {
          delete ptr;			//calls the destructor
      }

      MyClass* operator->()
      {
          return ptr;
      }

      Manager(const Manager& source)
      {
          ptr = new MyClass(*(source.ptr));
          cout << "Manager's copy constructor called" << endl;
      }
  };

  int main()
  {
      Manager obj1{ 21 };
      obj1->print_a();
      Manager obj2{ obj1 };	//compiles but doesnt link (linker error/ run time error)
  }


  //MyClass's 1 arg constructor called
  //The data attribute a = 21
  //MyClass's copy constructor called
  //Manager's copy constructor called
  //MyClass's destructor called
  //MyClass's destructor called
  ```

<br>

> Add Image

<br>
<br>

# PIMPL relying on compiler generated overloaded assignment operator

- The compiler generated overloaded assignment operator leads to memory leak in PIMPL design.

* When an assignment is done in PIMPL design without overloaded assignment operator, the compiler generates an overloaded assignment operator that performs member wise copy, hence at `obj2 = obj1;`, the members of obj1 are copied to obj2 members, now obj2's ptr will point to what obj1's ptr was pointing hence leading to memory leak (see the images) and linker error.

* When we define an overloaded copy constructor, In the Biz logic we modify the heap object directly by `*(this->ptr) = *(x.ptr);`

  ```cpp
  #include <iostream>
  using namespace std;

  class MyClass
  {
      int a;
  public:
      MyClass(int x = 0) : a(x)
      {
          cout << "MyClass's 1 arg constructor called" << endl;
      }

      ~MyClass()
      {
          cout << "MyClass's destructor called" << endl;
      }

      void print_a()
      {
          cout << "The data attribute a = " << a << endl;
      }

      MyClass(const MyClass& source): a{source.a}
      {
          cout << "MyClass's copy constructor called" << endl;
      }

      MyClass& operator=(const MyClass& x)
      {
          this->a = x.a;
          return *this;
      }
  };

  class Manager
  {
      //This is a wrapper class for MyClass, This is a PIMPL model and a RAII
      MyClass* ptr;

  public:
      Manager(int x)
      {
          ptr = new MyClass(x);	//creates a MyClass object on the heap, calls the constructor
      }

      ~Manager()
      {
          delete ptr;			//calls the destructor
      }

      MyClass* operator->()
      {
          return ptr;
      }

      Manager(const Manager& source)
      {
          ptr = new MyClass(*(source.ptr));
          cout << "Manager's copy constructor called" << endl;
      }

      Manager& operator=(const Manager& x)
      {
          //modifying the heap object itself instead of member wise copy
          *(this->ptr) = *(x.ptr);		//calls MyClass's overloaded assignment operator
          return *this;
      }

  };

  int main()
  {
      Manager obj1{ 21 };
      obj1->print_a();
      //Manager obj2{ obj1 };	//compiles but doesnt link (linker error/ run time error)
      Manager obj2{ 22 };
      obj2 = obj1;
      obj2->print_a();
  }

  //MyClass's 1 arg constructor called
  //The data attribute a = 21
  //MyClass's 1 arg constructor called
  //The data attribute a = 21
  //MyClass's destructor called
  //MyClass's destructor called
  ```

<br>

> Add image

<br>
<br>

# Rule of 3

- The Rule of Three is a guideline in C++ that states if a class requires one or more of the following three functions to manage dynamically allocated resources, then it likely needs to implement all three of them:

  1. Destructor
  2. Copy Constructor
  3. Overloaded Assignment Operator
