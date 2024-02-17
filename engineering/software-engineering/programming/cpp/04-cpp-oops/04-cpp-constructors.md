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
    int a;
    double b;

public:
    MyClass();	//default constructor; also known as the no-argument constructor
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

## Compiler Synthesised Constructors

- The compiler generates a default constructor automatically only if a class declares no constructors.

  ```cpp
  #include <iostream>

  class MyClass {
  public:
      int member;
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
  };

  int main() {
      MyClass object;
      std::cout << object.member;
  }

  //Compiler Error: no default constructor exists for class "MyClass"
  ```

- If a class has a member that has a class type, and that class doesn't have a default constructor then the compiler is unable to synthesize one. (I'm guessing this is compiler specific)

<br>
<br>

## Initialisation of members

```cpp
#include <iostream>

class MyClass{
private:
    int a;
    double b;

public:
    MyClass(int, double);	//2 arg constructor
};

MyClass::MyClass(int x, double y){
    a = x;	//This is Assignment and not Initialisation!
    b = y;	//This is Assignment and not Initialisation!
    std::cout << "data attribute a = " << a << " and b = " << b << std::endl;
}

int main(){
    MyClass obj{ 1, 2.2 };
}

//data attribute a = 1 and b = 2.2
```

In the above code, we are actually _assigning the values to the data attributes inside the constructor and not technically initialising._ When a MyClass object is created, it invokes the constructor. In the prolog phase of the constructor, the data attributes (whose size in known as type is known to the compiler) initialises them with garbage values. Then in the business logic of the constructor, they are assigned the given values.

<br>

### In-class Initialisation

```cpp
class MyClass {
public:
	int member{10};
};
```

<br>

### Constructor initialiser list

- We can initialise the data members using constructor initialiser list, this will initialise the data members in the prolog phase itself. (check out the meaning of initialise in 01-introduction.md).
- The order in which the parameters are initilaised is the order in which they are written in the class and not the paramter initialisation list in the constructor definition.

  ```cpp
  #include <iostream>

  class MyClass{
  private:
      int a;
      double b;

  public:
      MyClass(int, double);	//2 arg constructor
  };

  MyClass::MyClass(int x, double y): a{x}, b{y}{
      //using constructor initialisation list
  }

  int main(){
      MyClass obj{ 1, 2.2 };
  }
  ```

<br>
<br>

# Delegated constructors

- Delegated constructors in C++ are a feature introduced in C++11 that allow a constructor to call another constructor of the same class. This can be useful for reducing code duplication and improving readability.

- Instead of initialising the data attributes in every constructor, we can use the constructor that has most args as delegated constructor.

- In the following code, note that the delagted constructor is called first (in prolog phase itself) before the actual constructor is called.

  ```cpp
  #include <iostream>

  class MyClass{
  private:
      int a;
      double b;
  public:
      MyClass();				//default constructor
      MyClass(int);			//1 arg constructor
      MyClass(int, double);	//2 arg constructor
  };

  MyClass::MyClass(int x, double y) : a{ x }, b{ y }{
      //This overloaded 2 arg constructor will be used for delegated constructors
      std::cout << "The overloaded 2 arg constructor called; data attribute a = " << a << " and b = " << b << std::endl;
  }

  MyClass::MyClass(int x) : MyClass(x, 0){
      //initialising b  to 0 using delegated constructor, which is already called in prolog phase of this constructor
      std::cout << "The overloaded 1 arg constructor is called. " << std::endl;
  }

  MyClass::MyClass() : MyClass(0, 0){
      //initialising both data attributes to 0 using delegated constructor, which is already called in prolog phase of this constructor
      std::cout << "default constructor called." << std::endl;
  }

  int main(){
      MyClass obj1{};
      MyClass obj2{ 1 };
      MyClass obj3{ 1,1.2 };
  }

  //The overloaded 2 arg constructor called; data attribute a = 0 and b = 0
  //default constructor called.
  //The overloaded 2 arg constructor called; data attribute a = 1 and b = 0
  //The overloaded 1 arg constructor is called.
  //The overloaded 2 arg constructor called; data attribute a = 1 and b = 1.2
  ```

- _Delegated constructors should not be preffered as it introduces additional function calls_, hence affecting performace.

<br>
<br>
<br>

# Destructors

**_Destructors is a special kind of member function that is invoked automatically when the object is destroyed._**

- Destructors are generally used to perform cleanup operations but can perform anything the programmer desires.
- Destructors have the same name as the class preceded by a tilde symbol (~)
- Destructors have no return type and no parameters.
- There can be only 1 destructor for a class hence it cannot be overloaded unlike constructors.

- Illustration of destructors, they are called when the object dies i.e. when the scope of the object ends.

  ```cpp
  #include <iostream>
  class MyClass
  {
  private:
      std::string name;
  public:
      MyClass(std::string name);
      ~MyClass();  //destrcutor declaration
  };

  MyClass::MyClass(std::string name) : name{ name }{}

  MyClass::~MyClass(){
      std::cout << "destructor called by " << name << std::endl;
  }

  int main(){
      {
          MyClass obj1{ "first_obj" };
      }		//obj1 calls the destructor here as it's scope ends here

      MyClass obj2{ "second_obj" }; //calls it's destructor when main ends
  }

  //destructor called by first_obj
  //destructor called by second_obj
  ```

<br>
<br>
<br>

# Copy Constructors

**_Copy constructor is a special type of constructor that initializes a new object as a copy of an existing object of the same class._**

- It takes a single object of its own kind as parameter by reference.
- Copy constructors are called when objects are passed into functions as parameters, because by default objects are passed by value.
- If there is no copy constructor defined in the class and the class objects happens to copy construct objects, then the compiler would assume a copy constructor which will perform member-to-member copy (bitwise copy) and will also be inlined.
- It is good practice to provide the copy constructor with a const reference parameter.

<br>
<br>

## Shallow Copy Constructor

- Shallow copy is member to member copy, meaning all the data attributes of the object is just copied into the new one.

  ```cpp
  #include <iostream>

  class MyClass{
  private:
      int a;
      double b;
      std::string name;
  public:
      MyClass(int = 10, double = 2.5, std::string = "anonymous");
      MyClass(const MyClass& source); //copy constructor declaration
  };

  MyClass::MyClass(int x, double y, std::string name_val) : a{ x }, b{ y }, name{ name_val }{
      //notice that we have used default values for parameters
      std::cout << "three arg overloaded constructor called by " << name << std::endl;
  }

  MyClass::MyClass(const MyClass& source) : a{ source.a }, b{ source.b }, name{ source.name }{
      std::cout << "copy constructor called by " << name << std::endl;
  }

  //global function
  void tester(MyClass x){
      //just to show that copy constructor is called when objects are passed into functions!
  }

  int main(){
      MyClass obj1{};		//calls the three arg constructor
      MyClass obj2{ obj1 };  //obj2 calls the copy constructor
      tester(obj1);			////calls the copy constructor
  }

  //three arg overloaded constructor called by anonymous
  //copy constructor called by anonymous
  //copy constructor called by anonymous
  ```

- We can write the copy constructor using delegated constructor, but should not be preffered as it introduces an additional function call.

  ```cpp
  MyClass::MyClass(const MyClass& source) : MyClass{source.a, source.b}{
      std::cout << "copy constructor called" << std::endl;
  }
  ```

- If the class has variables created on the heap then the shallow copy constructor generally lead to dangling pointers!

  ```cpp
  #include <iostream>

  class MyClass {
      int* ptr;
  public:
      MyClass(int value = 0) {
          ptr = new int;
          *ptr = value;
      }

      MyClass(const MyClass& source) : ptr{ source.ptr } {
          //this is performing shallow copy as it is mearly copying the data attributes.
      }

      ~MyClass(){
          delete ptr;
      }
  };

  int main(){
      MyClass obj1;
      MyClass obj2{ obj1 };
  }

  //run time error
  ```

  > Add Image

<br>
<br>

## Deep Copy Constructor

```cpp
#include <iostream>

class MyClass {
    int* ptr;
public:
    MyClass(int value=0){
        ptr = new int;
        *ptr = value;
    }

    MyClass(const MyClass& source){
       ptr = new int;   //this is performing deep copy as it is creating a new heap instance
       *ptr = *source.ptr
    }

    ~MyClass(){
        delete ptr;
    }
};

int main(){
    MyClass obj1;
    MyClass obj2{ obj1 };
}

//no errors
```

- We can write the above copy constructor using the delegated constuctor as follows:

  ```cpp
    MyClass(const MyClass& source) :MyClass{*(source.ptr)} {
    }
  ```

<br>
<br>
<br>

# Move constructors (Update this section of notes)

> checkout the notes for l values, r values, l value references and r value references. <br>

<br>

- If we donot define a move constructor, the compiler will use the copy constructor instead! this results in lot of memory when dealing with large amounts if data.
- Move constructors moves an object instead of copying it. It copies the address of the resource from source to the current object and nulls out the pointer in the source pointer.
- This can be a significant performance improvement.
- Move constructors are called when an object is created from a temporary object (**r values**).

* The definition for move constructor is similar to that of copy construtor. `const` is removed becuase we have to null the source pointer and r value references are used in parameters instead of l value references.

  ```cpp
  type(const type &source);   //copy constructor definition
  type(type &&source);        //move constructor definiton
  ```

* The following code doesn't have a move constructor defined, hence the compiler will use the copy constructor instead when class objects are created to pass into functions. This is not memory efficient.

  ```cpp
  #include <iostream>
  #include <vector>
  using namespace std;

  class Player {

  public:
      std::string name;   //string
      int* xp;            //raw pointer
      Player(string name_value = "None", int xp_val =0); //constructor prototype (notice we have used default values)
      Player(const Player& source);           // copy constructor prototype

  };

  //constructor definition
  Player::Player(string name_value, int xp_val) : name{ name_value }
  {
      xp = new int;
      *xp = xp_val;
      //initialises the name  and xp attribute
  }

  //copy constructor definition (must perform deep copy as raw pointer is present in class)
  Player::Player(const Player& source) : Player{ source.name, *source.xp }
  {
      cout << "copy constructor is called for : " << source.name << endl;
  }


  int main()
  {
      vector <Player> vec;
      vec.push_back(Player{ "hero" });  //These Player objects are temporary objects i.e. r values
      vec.push_back(Player{ "bad_guy" });
  }

  /*
  copy constructor is called for : hero
  copy constructor is called for : bad_guy
  copy constructor is called for : hero

  here the hero copy constructor is called more than once because of vector behaviour
  */

  ```

<br>

- Since the objects being passed into functions are r value (temporary), we can make it efficient by defining a move constructor which will override the copy constructor.
- We must use `noexcept` in function prototype and definiton in visual studio, for unkown reason.

  ```cpp
  #include <iostream>
  #include <vector>
  using namespace std;

  class Player {

  public:
      std::string name;   //string
      int* xp;            //raw pointer
      Player(string name_value = "None", int xp_val =0); //constructor prototype (notice we have used default values)
      Player(const Player& source);           // copy constructor prototype
      Player(Player&& source)noexcept;                // move constructor prototype

  };

  //constructor definition
  Player::Player(string name_value, int xp_val) : name{ name_value }
  {
      xp = new int;
      *xp = xp_val;
      //initialises the name  and xp attribute
  }

  //copy constructor definition (must perform deep copy as raw pointer is present in class)
  Player::Player(const Player& source) : Player{ source.name, *source.xp }
  {
      cout << "copy constructor is called for : " << source.name << endl;
  }


  //move constructor definition (must null the source raw pointer as raw pointers is present in the class)
  Player::Player(Player&& source)noexcept : Player{ source.name, *source.xp }
  {
      source.xp = nullptr;
      cout << "move constructor is called for : " << source.name << endl;
  }


  int main()
  {
      vector <Player> vec;
      vec.push_back(Player{ "hero" });  //These Player objects are temporary objects i.e. r values
      vec.push_back(Player{ "bad_guy" });
  }

  /*
  move constructor is called for : hero
  move constructor is called for : bad_guy
  move constructor is called for : hero
  */
  ```

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

<!--
This is from Mr Ganesh's (trainer) notes, Looks contradictory from the standard textbook

- compiler will not generate a constructor if we donot specify one. (other than the 4 exceptions stated below)
- There are around 4 specific scenarios in C++98/2003 standards, where the compiler would assume a default constructor for a class which has not been provided with any constructor by the programmer.
  - In the context of inheritance
  - In the context of containment
  - In the context of hybrid inheritance
  - in the context of polymorphic classes.

  - -->
