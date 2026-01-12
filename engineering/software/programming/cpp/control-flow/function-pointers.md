# Function Pointers

- Function pointers are variables that can store the address of a function in a programming language. In other words, they are pointers that point to executable code, specifically functions.
- Essentially function pointers point to the CODE-SEGMENT area of the process memory.
- function pointers facilitate funciton callbacks by passing function pointers as arguments to a function.

* Checkout the syntax for initialising, assigning and calling funciton pointers

  ```cpp
  #include <iostream>
  #include <vector>

  double compute(float x, std::vector<double> y)
  {
      std::cout << "The result of computation is 2.2 " << std::endl;
      return 2.2;
  }

  void just_call(double (*para)(float, std::vector<double>), float x, std::vector<double> y)
  {
      (*para)(x,y);
  }

  int main()
  {
      double (*fptr_to_compute)(float, std::vector<double>) { &compute };

      //fptr_to_compute = &<some other function>; //Syntax for Assignment

      (*fptr_to_compute)(1.2, { 1.2,2.2 });	//Syntax for function call
      just_call(fptr_to_compute, 1.2, { 1.2,2.2 });	//passing function pointers as arguments
  }

  //The result of computation is 2.2
  //The result of computation is 2.2
  ```

* `typedef` is used to make the code readable

  ```cpp
  #include <iostream>
  #include <vector>

  double compute(float x, std::vector<double> y)
  {
      std::cout << "The result of computation is 2.2 " << std::endl;
      return 2.2;
  }

  typedef double (*FPTR)(float, std::vector<double>);

  void just_call(FPTR para, float x, std::vector<double> y)
  {
      (*para)(x, y);
  }


  int main()
  {
      FPTR fptr_to_compute{ &compute };  //Syntax for using typedef function pointers

      //fptr_to_compute = &<some other function>; //Syntax for Assignment

      (*fptr_to_compute)(1.2, { 1.2,2.2 });	//Syntax for function call
      just_call(fptr_to_compute, 1.2, { 1.2,2.2 });         //passing function pointers as arguments
  }


  //The result of computation is 2.2
  //The result of computation is 2.2
  ```

<br>
<br>

# Function pointers with class member functions

- The syntax is different for static and non-static member functions.

  ```cpp
  #include <iostream>
  using namespace std;

  class MyClass
  {
  public:
      //non-static member functions
      void fun1(int x) { cout << "fun1 called" << endl; }

      //static member funciton
      static void fun2(int x) { cout << "fun2 called" << endl; }
  };

  int main()
  {
      //non static member functions
      void (MyClass:: * fp)(int) = &MyClass::fun1;   //the syntax uses ::*

      MyClass obj1;       //created on the stack
      (obj1.*fp)(21);     //the syntax uses .* operator

      MyClass* obj2_ptr = new MyClass;    //created on the heap
      (obj2_ptr->*fp)(21);    //the syntax uses ->* operator
      delete obj2_ptr;


      //static member functions
      void (*f)(int) = &MyClass::fun2;  //As the member function is static, we initialise the function pointer as if it were global!

      (*f)(21);   //invoking is done without any object
  }

  //fun1 called
  //fun1 called
  //fun2 called
  ```

* Callbacks in member functions of a class

  ```cpp
  #include <iostream>
  using namespace std;

  class MyClass
  {
  public:
      void fun1(int x) { cout << "fun1 called" << endl; }
      void just_call(void(MyClass:: *para)(int), int x)
      {
          (this->*para)(x);   //syntax
      }

  };

  int main()
  {
      void (MyClass::*fptr)(int) = &MyClass::fun1;
      MyClass obj;
      obj.just_call(fptr, 21);            //approach 1
      obj.just_call(&MyClass::fun1, 21);  //approach 2
  }

  //fun1 called
  //fun1 called
  ```

* The above code using typedef

  ```cpp
  #include <iostream>
  using namespace std;

  class MyClass;  //forward declaration
  typedef void (MyClass::* FPTR)(int);

  class MyClass
  {
  public:
      void fun1(int x) { cout << "fun1 called" << endl; }
      void just_call(FPTR para, int x)
      {
          (this->*para)(x);   //syntax
      }

  };

  int main()
  {
      FPTR fptr = &MyClass::fun1;
      MyClass obj;
      obj.just_call(fptr, 21);            //approach 1
      obj.just_call(&MyClass::fun1, 21);  //approach 2
  }

  //fun1 called
  //fun1 called
  ```

<br>
<br>

# Function Objects (functor)

A functor is a function object that can be invoked as if it were a function.

- It is an instance of a class or a struct that overloads the function call operator operator().

* The functor (MyClass object here) acts like a wrapper for the function (fun here)
* we can essentially add logic in the biz logic of the overloaded function operator function and this will wrap the original function.

  ```cpp
  #include <iostream>
  using namespace std;

  //global function
  void fun()
  {
      std::cout << "fun called" << std::endl;
  }

  typedef void (*FP)();

  class MyClass
  {
  private:
      FP p;
  public:
      MyClass(FP x): p{x}
      {}
      void fun1(int x)
      { cout << "fun1 called" << endl; }

      void invoke()
      {
          (*p)();
      }

      void operator()()
      {
          (*p)();
      }
  };

  int main()
  {
      FP fp{ &fun };
      MyClass obj{ fp };
      obj.invoke();   //user defined member function
      obj();          //overloaded function operator (functor); obj.operator()();
  }

  //fun called
  //fun called
  ```

<br>
<br>
