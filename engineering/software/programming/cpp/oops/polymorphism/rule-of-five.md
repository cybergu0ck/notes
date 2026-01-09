# Rule of five

<br>
<br>
<br>

## Destructor

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

## Copy constructors

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

### Shallow Copy Constructor

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

### Deep Copy Constructor

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

## Copy assignment

```cpp
#include <iostream>

class MyClass {
public:
    int num;
    int* num_ptr;
public:
    MyClass();		                        //default constructor
    MyClass(int, int);		                //two-arg constructor
    MyClass(const MyClass& source);         //copy constructor
    MyClass& operator=(const MyClass& rhs); //copy assignment or assignment operator overloading for copy
    MyClass(MyClass&& source) noexcept;     //move constructor
    ~MyClass();                             //destructor
};

MyClass::MyClass() : num{ 0 }, num_ptr{ new int(0) }{
    std::cout << "The default constructor is called" << std::endl;
}

MyClass::MyClass(int x, int y) : num{ x }, num_ptr{ new int(y) }{
    std::cout << "The two-arg constructor is called" << std::endl;
}

MyClass::MyClass(const MyClass& source) : num{ source.num } {
    std::cout << "The copy constructor is called" << std::endl;

    num_ptr = new int(*source.num_ptr);  //Deep Copy
}

MyClass& MyClass::operator=(const MyClass& rhs)
{
    std::cout << "copy assignment operator is called." << "\n";

    if (this != &rhs)
    {
        delete num_ptr;                   //Delete the existing data

        num_ptr = new int(*rhs.num_ptr);  //Perform the deep copy
        num = rhs.num;
    }
    return *this;                       //This is for chaining of copy assignments (ig)
}


MyClass::MyClass(MyClass&& source) noexcept : num{ source.num }, num_ptr{ source.num_ptr }{
    std::cout << "The move constructor is called" << std::endl;
    source.num = 0;             //Leave the original object in a default kind of a state.
    source.num_ptr = nullptr;   //Null out the source's pointer to avoid double deletion.
}

MyClass::~MyClass() {
    std::cout << "The destructor is called" << std::endl;
    delete num_ptr;  //Clean Up
}
```

```cpp
int main()
{
    MyClass obj1{1,10};
    MyClass obj2{2,20};
    obj1 = obj1;        //self assignment
    obj2 = obj1;        //obj2.operator=(obj1);

    std::cout << obj1.num << " " << *obj1.num_ptr << "\n";
    std::cout << obj2.num << " " << *obj2.num_ptr << "\n";
}

//The two - arg constructor is called
//The two - arg constructor is called
//copy assignment operator is called.
//copy assignment operator is called.
//1 10
//1 10
//The destructor is called
//The destructor is called
```

- An assignment occurs when an object is already initialised and we want to assign another object to it. See below:

  ```cpp
  MyClass obj1{1,1};
  MyClass obj2 = obj1;  //NOT ASSIGNMENT; equivalent to MyClass obj2{obj1};
  ```

  ```cpp
  MyClass obj1, obj2;
  obj2 = obj1;	//ASSIGNMENT; as obj2 has already been initialised and obj1 is an l value!
  ```

- Chainging of assignments will work only if the return type of the copy assignment is by referance. Otherwise, the subsequent assignments in the chaining would perform copy assignment on temporaries.

  ```cpp
  int main()
  {
      MyClass obj1{1,10};
      MyClass obj2{2,20};
      MyClass obj3{3,30};

      obj3 = obj2 = obj1;  //obj3.operator=(obj2.operator=(obj1))

      std::cout << obj1.num << " " << *obj1.num_ptr << "\n";
      std::cout << obj2.num << " " << *obj2.num_ptr << "\n";
      std::cout << obj3.num << " " << *obj3.num_ptr << "\n";
  }

  //The two - arg constructor is called
  //The two - arg constructor is called
  //The two - arg constructor is called
  //copy assignment operator is called.
  //copy assignment operator is called.
  //1 10
  //1 10
  //1 10
  //The destructor is called
  //The destructor is called
  //The destructor is called
  ```

<br>
<br>

### Strong Exception Guarantee

- This is the basic implmentation of the copy assignment operator. This doesn't provide strong exception guarantee: Suppose the `new` operation fails, in this case the `*this` object is already modified (`num_ptr` is deleted).

  ```cpp
  MyClass& MyClass::operator=(const MyClass& rhs)
  {
      std::cout << "copy assignment operator is called." << "\n";

      if (this != &rhs)
      {
          delete num_ptr;                   //Delete the existing data

          num_ptr = new int(*rhs.num_ptr);  //Perform the deep copy
          num = rhs.num;
      }
      return *this;                       //This is for chaining of copy assignments (ig)
  }
  ```

- The following implementation facilitates strong exception guarantee, In this case even if the `new` operation fails, The `*this` object is not modified. We donot need to check for self assignment aswell, becase of the temporaries.

  ```cpp
  MyClass& MyClass::operator=(const MyClass& rhs)
  {
      std::cout << "copy assignment operator is called." << "\n";

      //Create temporaries
      int new_num = rhs.num;
      int* new_num_ptr = new int(*rhs.num_ptr);

      //Delete exisiting
      delete num_ptr;

      //Create copies
      num = new_num;
      num_ptr = new_num_ptr;

      return *this;
  }
  ```

<br>

### Copy and Swap Idiom

- Copy and swap Idiom decreases code duplication.

  ```cpp

  ```

//TODO - Learn this stuff; use this video link (https://www.youtube.com/watch?v=7Qgd9B1KuMQ); basically there is a point he mentions in this video saying std::swap uses move constructor and hence when iplementing swap function, we shouldn't use the std::swap or something.

<br>
<br>

## Move constructors

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
<br>

<!--
This is from Mr Ganesh's (trainer) notes, Looks contradictory from the standard textbook

- compiler will not generate a constructor if we donot specify one. (other than the 4 exceptions stated below)
- There are around 4 specific scenarios in C++98/2003 standards, where the compiler would assume a default constructor for a class which has not been provided with any constructor by the programmer.
  - In the context of inheritance
  - In the context of containment
  - In the context of hybrid inheritance
  - in the context of polymorphic classes.

  - -->

<br>
<br>
<br>

## Move assignment

```cpp
#include <iostream>

class MyClass {
public:
    int num;
    int* num_ptr;
public:
    MyClass();		                            //default constructor
    MyClass(int, int);		                    //two-arg constructor
    MyClass(const MyClass& source);             //copy constructor
    MyClass& operator=(const MyClass& rhs);     //copy assignment or assignment operator overloading for copy
    MyClass(MyClass&& source) noexcept;         //move constructor
    MyClass& operator=(MyClass&& rhs) noexcept; //move assignment or assignment operator overloading for move
    ~MyClass();                                 //destructor
};

MyClass::MyClass() : num{ 0 }, num_ptr{ new int(0) }{
    std::cout << "The default constructor is called" << std::endl;
}

MyClass::MyClass(int x, int y) : num{ x }, num_ptr{ new int(y) }{
    std::cout << "The two-arg constructor is called" << std::endl;
}

MyClass::MyClass(const MyClass& source) : num{ source.num } {
    std::cout << "The copy constructor is called" << std::endl;

    num_ptr = new int(*source.num_ptr);  //Deep Copy
}

MyClass& MyClass::operator=(const MyClass& rhs)
{
    std::cout << "copy assignment operator is called." << "\n";

    //Create temporaries
    int new_num = rhs.num;
    int* new_num_ptr = new int(*rhs.num_ptr);

    //Delete exisiting
    delete num_ptr;

    //Create copies
    num = new_num;
    num_ptr = new_num_ptr;

    return *this;
}

MyClass::MyClass(MyClass&& source) noexcept : num{ source.num }, num_ptr{ source.num_ptr }{
    std::cout << "The move constructor is called" << std::endl;
    source.num = 0;             //Leave the original object in a default kind of a state.
    source.num_ptr = nullptr;   //Null out the source's pointer to avoid double deletion.
}

MyClass& MyClass::operator=(MyClass&& rhs) noexcept
{
    std::cout << "The move assignment is called" << "\n";

    if (this != &rhs)
    {
        //Delete existing resources
        delete num_ptr;

        //Steal the resources
        num_ptr = rhs.num_ptr;  //do not allocate a new memory!
        num = rhs.num;

        //Leave the rhs in a default like state
        rhs.num_ptr = nullptr;
        rhs.num = 0;
    }
    return *this;
}

MyClass::~MyClass() {
    std::cout << "The destructor is called" << std::endl;
    delete num_ptr;  //Clean Up
}
```

- Assigning a temporary

  ```cpp
  int main()
  {
      MyClass obj1{1,10};
      obj1 = MyClass{ 3,30 };

      std::cout << obj1.num << " " << *obj1.num_ptr << "\n";
  }

  //The two - arg constructor is called
  //The two - arg constructor is called
  //The move assignment is called
  //The destructor is called
  //3 30
  //The destructor is called
  ```

- Using std move

  ```cpp
  int main()
  {
      MyClass obj1{1,10};
      MyClass obj2{3,30};

      obj1 = std::move(obj2);

      std::cout << obj1.num << " " << *obj1.num_ptr << "\n";
      //std::cout << obj2.num << " " << *obj2.num_ptr << "\n";   //obj2's num_ptr will be a null pointer
  }

  //The two - arg constructor is called
  //The two - arg constructor is called
  //The move assignment is called
  //3 30
  //The destructor is called
  //The destructor is called
  ```

<br>
<br>
<br>
