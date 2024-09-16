# Constructors

**_Constructor is a special member function of a class that is invoked automatically whenever an object is created._**

- It must have the same name as the class.
- It does not have any return type associated.

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

  - The data members of the above class are not initialised here, we should always initialise the data members.

<br>

Some important points about constructors:

- Constructors donot create objects for that class nor initialises class members, the programmer has to initialise them.
- However they are mostly used for initialisating data members but can perform anything the programmer desires.
- Constructors can be overloaded.

<br>
<br>

## Overloaded Constructors

```cpp
#include <iostream>

class MyClass
{
private:
    int num;
    int *num_ptr;

public:
    MyClass();	            //default constructor, also known as the no-arg constructor
    MyClass(int);	        //overloaded one-arg constructor
    MyClass(int, int);      //overloaded two-arg constructor
};

MyClass::MyClass()
{
    std::cout << "default constructor is called" << std::endl;
}

MyClass::MyClass(int x)
{
    std::cout << "overloaded one arg constructor is called" << std::endl;
}

MyClass::MyClass(int x, int y)
{
    std::cout << "overloaded two arg constructor is called" << std::endl;
}

int main()
{
    MyClass obj1;				//  obj1.MyClass::MyClass(&obj1);
    MyClass obj2{ 100 };		//  obj1.MyClass::MyClass(&obj1, 100);
    MyClass obj3{ 100,1 };	    //  obj1.MyClass::MyClass(&obj1, 100, 1);

}

//default constructor is called
//overloaded one arg constructor is called
//overloaded two arg constructor is called
```

<br>
<br>

## Compiler Synthesised Constructors

The compiler generates a default constructor by itself only if a class declares no constructors.

```cpp
#include <iostream>

class MyClass {
public:
    int member;

    //no constructors are declared. Hence the compiler will synthesize a default constructor.
};

int main() {
    MyClass object;
    std::cout << object.member; //will have garbage value
}

//4200987
```

```cpp
#include <iostream>

class MyClass {
public:
    int member;
    MyClass(int num):member{num}{};

    //default constructor is not declared but one-arg constructor declared.
};

int main() {
    MyClass object;
    std::cout << object.member;
}

//Compiler Error: no default constructor exists for class "MyClass"
```

<br>
<br>

### Initialisation of Class Data Members

```cpp
#include <iostream>

class MyClass
{
public:
    int num;
    int *num_ptr;

public:
    MyClass();	            //default constructor, also known as the no-arg constructor
};

MyClass::MyClass()
{
    std::cout << "default constructor is called" << std::endl;

    num = 0;                //This is not initialisation but assignment
    num_ptr = new int(0);   //This is not initialisation but assignment
}

int main()
{
    MyClass obj1;

    std::cout << obj1.num << '\n';
}

//default constructor is called
//0
```

- In the above code, we are actually _assigning the values to the data members inside the constructor and not technically initialising._ When a MyClass object is created, it invokes the constructor. In the prolog phase of the constructor, the data members (whose size in known as type is known to the compiler) initialises them with garbage values. Then in the business logic of the constructor, they are assigned the given values.

<br>

#### In-class Initialisation

```cpp
class MyClass {
public:
	int num{10};
};
```

<br>

#### Constructor Initialiser List

//TODO - Link the initialisation notes and prolog notes here

- We can initialise the data members using constructor initialiser list, this will initialise the data members in the prolog phase itself. (check out the meaning of initialise in 01-introduction.md).
- The order in which the parameters are initilaised is the order in which they are written in the class and not the paramter initialisation list in the constructor definition.

  ```cpp
  #include <iostream>

  class MyClass
  {
  public:
      int num;
      int *num_ptr;

  public:
      MyClass();	            //default constructor, also known as the no-arg constructor
  };

  MyClass::MyClass():num{0}, num_ptr{new int(0)}
  {
      std::cout << "default constructor is called" << std::endl;
  }

  int main()
  {
      MyClass obj1;
      std::cout << obj1.num << '\n';
  }

  //default constructor is called
  //0
  ```

<br>
<br>

# Delegated Constructors

- Delegated constructors in C++ are a feature introduced in C++11 that allow a constructor to call another constructor of the same class.
- Instead of initialising the data attributes in every constructor, we can use the constructor that has most args as delegated constructor.
- This can be useful for reducing code duplication and improving readability but at the cost of performance.
- _Delegated constructors should not be preffered as it introduces additional function calls_, hence affecting performace.

  ```cpp
  #include <iostream>

  class MyClass {
  private:
      int num;
      int* num_ptr;
  public:
      MyClass();				//default constructor
      MyClass(int);			//1 arg constructor
      MyClass(int, int);	    //2 arg constructor
  };

  MyClass::MyClass(int x, int y) : num{ x }, num_ptr{ new int(y)}{
      //This overloaded 2 arg constructor will be used for delegated constructors
      std::cout << "The overloaded 2 arg constructor called and the value of num = " << num << std::endl;
  }

  MyClass::MyClass(int x) : MyClass(x, 0) {
      //Initialising num with x and num_ptr to point to an int with value 0 in the prolog phase of this function.
      std::cout << "The overloaded 1 arg constructor is called and the value of num = " << num << std::endl;
  }

  MyClass::MyClass() : MyClass(0, 0) {
      //Initialising num with 0 and num_ptr to point to an int with value 0 in the prolog phase of this function.
      std::cout << "default constructor called." << std::endl;
  }

  int main() {
      MyClass obj1{};
      MyClass obj2{ 1 };
      MyClass obj3{ 10,10 };
  }

  //The overloaded 2 arg constructor called and the value of num = 0
  //default constructor called.
  //The overloaded 2 arg constructor called and the value of num = 1
  //The overloaded 1 arg constructor is called and the value of num = 1
  //The overloaded 2 arg constructor called and the value of num = 10
  ```

  - In the above code, note that the delagted constructor is called first (in prolog phase itself) before the actual constructor is called.

<br>
<br>
<br>

# Destructor

**_Destructor is a special kind of member function that is invoked automatically when the object is destroyed._**

- Destructors are generally used to perform cleanup operations but can perform anything the programmer desires.
- Destructors have the same name as the class preceded by a tilde symbol (~)
- Destructors have no return type and no parameters.
- There can be only 1 destructor for a class hence it cannot be overloaded unlike constructors.

- Illustration of destructors, they are called when the object dies i.e. when the scope of the object ends.

  ```cpp
  #include <iostream>

  class MyClass {
  private:
      int num;
      int* num_ptr;
  public:
      MyClass();		//default constructor
      ~MyClass();     //destructor
  };

  MyClass::MyClass() : num{ 0 }, num_ptr{ new int(0)}{
      std::cout << "The default constructor is called" << std::endl;
  }

  MyClass::~MyClass(){
      std::cout << "The destructor is called" << std::endl;

      delete num_ptr;  //Clean Up
  }

  int main() {
      MyClass obj1{};
      {
          MyClass obj1{};  //Note that variables can have same name in different scopes!
      }
      MyClass* obj2 = new MyClass();  //The destructor for this object is never called!
  }

  //The default constructor is called
  //The default constructor is called
  //The destructor is called
  //The default constructor is called
  //The destructor is called
  ```

<br>
<br>
<br>

# Copy Constructors

**_A copy constructor is a constructor which can be called with an argument of the same class type and copies the content of the argument without mutating the argument._**

- It takes a _single object of its own kind as parameter by reference._
- If there is no copy constructor defined in the class and the class objects happens to copy construct objects, then the compiler would assume a copy constructor which will perform member-to-member copy (bitwise copy) and will also be inlined.
- It is good practice to provide the copy constructor with a const reference parameter.
- Copy constructors are called when:

  - An existing object is used to initialise a new object.
  - An object is passed to a function by value.
  - An object created locally in a function is returned by value. (However, modern compilers might perform Return Value Optimisation and [Copy Elision](../01-cpp-fundamentals/cpp-specific-features/cpp-copy-elision.md) and thus eliminate this copy process.)

- Passing the object by reference in the copy constructor is essential to avoid infinite recursion. If the object is taken by value in the copy constructor then while the copy constructor would be called, it would keep calling itself as the objects are passed by value!

<br>
<br>

## Shallow Copy Constructor

- Shallow copy is member to member copy, meaning all the data attributes of the object is just copied to new one.
- Shallow copy works fine without pointers but when pointers are involved it leads to dangling pointers.

  ```cpp
  #include <iostream>

  class MyClass {
  private:
      int num;
      int* num_ptr;
  public:
      MyClass();		                //default constructor
      MyClass(const MyClass& source); //copy constructor
      ~MyClass();                     //destructor
  };

  MyClass::MyClass() : num{ 0 }, num_ptr{ new int(0)}{
      std::cout << "The default constructor is called" << std::endl;
  }

  MyClass::MyClass(const MyClass& source) : num{ source.num }, num_ptr{source.num_ptr}{
      //this->num_ptr simply points to the same location pointed by source.num_ptr, will create dangling pointers!
      std::cout << "The copy constructor is called" << std::endl;
  }

  MyClass::~MyClass(){
      std::cout << "The destructor is called" << std::endl;
      delete num_ptr;  //Clean Up
  }

  int main() {
      MyClass* obj1 = new MyClass();
      MyClass obj2{ *obj1 };
      delete obj1;                //This will delete num_ptr of obj1, obj2's num_ptr now points to invalid memory!
  }

  //Run Time Error
  ```

<br>
<br>

## Deep Copy Constructor

```cpp
#include <iostream>

class MyClass {
private:
    int num;
    int* num_ptr;

public:
    MyClass();		                //default constructor
    MyClass(const MyClass& source); //copy constructor
    ~MyClass();                     //destructor
};

MyClass::MyClass() : num{ 0 }, num_ptr{ new int(0)}{
    std::cout << "The default constructor is called" << std::endl;
}

MyClass::MyClass(const MyClass& source) : num{ source.num }{
    std::cout << "The copy constructor is called" << std::endl;

    num_ptr = new int(*source.num_ptr);  //Deep Copy
}

MyClass::~MyClass(){
    std::cout << "The destructor is called" << std::endl;
    delete num_ptr;  //Clean Up
}
```

- Initialising an object using an existing object.

  ```cpp
  int main() {
      MyClass* obj1 = new MyClass();
      MyClass obj2{ *obj1 };  //same as MyClass obj2 = *obj1;
      delete obj1;
  }

  //The default constructor is called //(by obj1)
  //The copy constructor is called    //(by obj2)
  //The destructor is called          //(by obj1)
  //The destructor is called          //(by obj2)
  ```

- Passing an object by value.

  ```cpp
  void Foo(MyClass obj_foo){
      //Just to illustrate copy constructor being called.
      //The copy constructor is called because the function accepts MyClass by value.
      //The copy contructor will not be called if the function were to accept MyClass by refernce.
  }

  int main() {
      MyClass obj;
      Foo(obj);
  }

  //The default constructor is called //(by obj)
  //The copy constructor is called    //(by obj_foo in Foo)
  //The destructor is called          //(by obj_foo in Foo)
  //The destructor is called          //(by obj)
  ```

- Copy constructor will not be called when passing an object by reference.

  ```cpp
  void Foo(MyClass& obj_foo){
      //The copy contructor will not be called if the function were to accept MyClass by refernce.
  }

  int main() {
      MyClass obj;
      Foo(obj);
  }

  //The default constructor is called (by obj)
  //The destructor is called          (by obj)
  ```

- Returning an object from a function by value (Without Return Value Optimisation)

  ```cpp
  MyClass Goo(){
      MyClass obj_goo;
      return obj_goo;
  }

  int main() {
      MyClass obj = Goo();
  }

  //The default constructor is called //(by obj_goo)
  //The copy constructor is called    //(by obj)
  //The destructor is called          //(by obj_goo)
  //The destructor is called          //(by obj)
  ```

- If the compiler performs Return Value Optimisation then the copy constructor will not be called.

  ```cpp
  MyClass Goo(){
      MyClass obj_goo;
      return obj_goo;
  }

  int main() {
      MyClass obj = Goo();  //obj_goo is essentially constructed here itself!
  }

  // The default constructor is called
  // The destructor is called
  ```

<br>
<br>
<br>

# Move Constructors

**_A move constructor is a constructor which can be called with an argument of the same class type and copies the content of the argument, possibly mutating the argument._**

<br>

- It takes a _single object of its own kind as parameter by r-value reference._
- If there is no move constructor defined in the class and then the compiler will use the copy constructors, which can be less efficient when dealing with large objects.
- Unlike copy constructor, The parameter in the move constructor is not `const` as we need to mutate that object.
- The `noexcept` keyword has to be used in both the declaration.
- The move constructor transfers ownership of resources from the source object to the newly constructed object, effectively "stealing" the data. The source object is left in a valid but unspecified state
- Move constructors are called when:
  - std::move is used.

```cpp
#include <iostream>
#include <vector>

class MyClass {
public:
    int num;
    int* num_ptr;
public:
    MyClass();		                    //default constructor
    MyClass(int, int);		            //two-arg constructor
    MyClass(const MyClass& source);     //copy constructor
    MyClass(MyClass&& source) noexcept; // move constructor
    ~MyClass();                         //destructor
};

MyClass::MyClass() : num{ 0 }, num_ptr{ new int(0)}{
    std::cout << "The default constructor is called" << std::endl;
}

MyClass::MyClass(int x, int y) : num{ x }, num_ptr{ new int(y)}{
    std::cout << "The two-arg constructor is called" << std::endl;
}

MyClass::MyClass(const MyClass& source) : num{ source.num }{
    std::cout << "The copy constructor is called" << std::endl;

    num_ptr = new int(*source.num_ptr);  //Deep Copy
}

MyClass::MyClass(MyClass&& source) noexcept : num{ source.num }, num_ptr{ source.num_ptr }{
    std::cout << "The move constructor is called" << std::endl;
    source.num = 0;             //Leave the original object in a default kind of a state.
    source.num_ptr = nullptr;   //Null out the source's pointer to avoid double deletion.
}

MyClass::~MyClass(){
    std::cout << "The destructor is called" << std::endl;
    delete num_ptr;  //Clean Up
}
```

- Classic illustration of move constructor.

  ```cpp
  int main() {
      MyClass obj1{ 10,100 };
      MyClass obj2 = std::move(obj1);

      std::cout << obj1.num << "\n";
      std::cout << obj2.num << "\n";
  }

  //The two - arg constructor is called
  //The move constructor is called
  //0
  //10
  //The destructor is called
  //The destructor is called
  ```

- When an object is instantiated with an r-value, Copy Elision occurs and the move constructor will not be called.

  ```cpp
  int main() {
      MyClass obj1{ MyClass()};
  }

  //The default constructor is called
  //The destructor is called
  ```

- Pushing an r-value to a container.

  ```cpp
  int main() {
      std::vector<MyClass> my_vector;
      my_vector.push_back(MyClass(1, 1));
  }

  //The two-arg constructor is called
  //The move constructor is called
  //The destructor is called
  //The destructor is called
  ```

- I want to understand the output here, this is a behaviour of container I feel. //REVIEW - Needs to be understood.

  ```cpp
  int main() {
      std::vector<MyClass> my_vector;
      my_vector.push_back(MyClass(1, 1));
      my_vector.push_back(MyClass(10, 1));
  }

  //The two - arg constructor is called
  //The move constructor is called
  //The destructor is called
  //The two - arg constructor is called
  //The move constructor is called
  //The move constructor is called
  //The destructor is called
  //The destructor is called
  //The destructor is called
  //The destructor is called
  ```

<br>
<br>

# `explicit` Constructor

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

<!--
This is from Mr Ganesh's (trainer) notes, Looks contradictory from the standard textbook

- compiler will not generate a constructor if we donot specify one. (other than the 4 exceptions stated below)
- There are around 4 specific scenarios in C++98/2003 standards, where the compiler would assume a default constructor for a class which has not been provided with any constructor by the programmer.
  - In the context of inheritance
  - In the context of containment
  - In the context of hybrid inheritance
  - in the context of polymorphic classes.

  - -->
