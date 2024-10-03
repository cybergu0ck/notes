# Operator Overloading

- Operator overloading is a feature in C++ that allows programmers to redefine the meaning of operators for user-defined data types. This can make code more concise and readable, and can also improve the flexibility and expressiveness of a program.
- The following operators cannot be overloaded

  | Operator             | Symbol |
  | -------------------- | ------ |
  | Scope Resolution     | ::     |
  | Conditional Operator | ?:     |
  | pointer to a member  | .\*    |
  | dot operator         | .      |
  | Size Of              | sizeof |

* Basic rules while overloading operators

  - precedence and associativity of operators cannot be changed.
  - 'arity' cannot be changed (ex: unary operators cannot be made binary)
  - cannot overload operators for primitive type (ex: int, double, etc)
  - cannot create new operators
  - [], (), ->, and the assignment operator must be declared as member methods while other operators can be declared as member or global methods.

<br>
<br>

# Assignment Operator Overloading

- Note that copy elision doesn't apply for assignments and is pertinant to constructions. As such, it is typically not possible to implicitely eliminate copy or move assignments and hence can be critical for performance.

//TODO - Link to copy elision notes

<br>

## Copy Assignment Operator

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

## Move Assignment Operator

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

# Stream Operator Overloading

- cin s a global object of istream class and >> opertaor is a member function of istream class. (similarly cout and ostream). As such we cannot try to overload them in their class (becuase it is a standard library). We cannot overload them within our class because by doing so, the cin and cout objects (belonging to their respective classes) cannot call the member functions of our class. Hence we do it globally and use `friend`.

  ```cpp
  #include <iostream>

  class MyClass
  {
      int a;
      friend std::istream& operator>>(std::istream& input, MyClass& obj); //if this is not done, then this function won't have access to 'a'.
      friend std::ostream& operator<<(std::ostream& output, MyClass& obj);
  };


  std::istream& operator>>(std::istream & input, MyClass & obj)
  {
      std::cout << "Enter a number for data attribute a" << std::endl;
      input >> obj.a;
      return input;
  }

  std::ostream& operator<<(std::ostream& output, MyClass& obj)
  {
      output << obj.a;
      return output;
  }


  int main()
  {
      MyClass obj1;
      std::cin >> obj1;
      std::cout << "The value of obj1.a is " << obj1;

  }

  //Enter a number for data attribute a
  //12
  //The value of obj1.a is 12
  ```

<br>
<br>

# Unary Operator Overloading //REVIEW - Needs Review

- Unary operator can have prefix notation and postfix notation, we can faciliate both in unary operator overloading.

  ```cpp
  #include <iostream>

  class MyClass
  {
  private:
      int a;

  public:
      MyClass(int x = 2) : a{ x } {}
      MyClass& operator++();		//prefix implementation
      MyClass operator++(int);    //postfix implementation
      int get_a()
      {
          return a;
      }
  };

  MyClass& MyClass::operator++()  //return by reference
  {
      ++a;
      return *this;
  }



  MyClass MyClass::operator++(int)   //return by value as the object being returned is local object
  {
      MyClass temp{ *this };
      this->a++;
      return temp;
  }

  int main()
  {
      MyClass obj1;
      MyClass res1;
      res1 = ++obj1;
      std::cout << "-----prefix example-----" << std::endl;
      std::cout << "The value of obj1 after prefix increment is " << obj1.get_a() << std::endl;
      std::cout << "The value of res1 after prefix increment is " << res1.get_a() << std::endl;
      std::cout << "\n";
      std::cout << "-----postfix example-----" << std::endl;
      MyClass obj2;
      MyClass res2;
      res2 = obj2++;
      std::cout << "The value of obj2 after prefix increment is " << obj2.get_a() << std::endl;
      std::cout << "The value of res2 after prefix increment is " << res2.get_a() << std::endl;

  }

  //---- - prefix example---- -
  //The value of obj1 after prefix increment is 3
  //The value of res1 after prefix increment is 3
  //
  //---- - postfix example---- -
  //The value of obj2 after prefix increment is 3
  //The value of res2 after prefix increment is 2
  ```

<br>
<br>

# Arrow Assignment Overloading //REVIEW - Needs Review

- Find a good case for using this (I don't think the following code is a good use case), However checkout arrow operator overloading in PIMPL model.

  ```cpp
  #include <iostream>

  class MyClass
  {
  private:
      int a;

  public:
      MyClass(int x = 2) : a{ x } {}
      MyClass* operator->();		//overloaded arrow operator declaration

      void print_a()
      {
          std::cout << "data attribute a = " << a << std::endl;
      }
  };

  MyClass* MyClass::operator->()
  {
      return this;
  }


  int main()
  {
      //allocate an array of MyClass objects on the heap
      MyClass* arr = new MyClass[5];

      arr[0].print_a();   //arr[0] is a MyClass object hence we need not use ->

      //If we wanted to use ->, for code readability we must provide an overloaded operator
      arr[1]->print_a();  //Here arr[1] is a MyClass object
  }

  //data attribute a = 2
  //data attribute a = 2
  ```

<br>
<br>
<br>
