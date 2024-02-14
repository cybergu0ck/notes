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

- overloaded assignment operator is called whenever an object is assigned to another object, If an overloaded assignment operator is not defined, then the compiler will generate one and perform member wise copy.

  ```cpp
  #include <iostream>

  class MyClass
  {
  private:
      int a;

  public:
      MyClass(int x = 2): a{x}{}
      MyClass& operator=(MyClass& x);		//overloaded assignment operator declaration

      void modify()
      {
          a = 10;
      }

      void print_a()
      {
          std::cout << "data attribute a = " << a << std::endl;
      }
  };

  MyClass& MyClass::operator=(MyClass& x)
  {
      std::cout << "overloaded assignment operator called" << std::endl;
      this->a = x.a;
      return *this;
  }

  int main()
  {

      MyClass obj1;
      //MyClass obj2 = obj1;  //This is not assignment, It is equivalent to MyClass obj2{obj1}
      MyClass obj2;
      obj1.modify();
      obj2 = obj1;		// obj2.operator=(obj1)
      obj2.print_a();
  }

  //overloaded assignment operator called
  //data attribute a = 10
  ```

<br>

### Concept Clarity

- An assignment occurs when an object is already initialised and we want to assign another object to it. See below:

  ```cpp
  MyClass obj1{21};
  MyClass obj2 = obj1;  //NOT assignment; equivalent to MyClass obj2{obj1};
  ```

  ```cpp
  MyClass obj1, obj2;
  obj2 = obj1;	//this IS assignment as obj2 has already been initialised and obj1 is an l value!
  ```

<br>

## Chaining of Assignment Operator

- For the overloaded assignment operator to facilitate chaining (multiple assignments in one line), the overloaded assignment operator must return a lvalue (the return type must be lvalue reference).

  ```cpp
  #include <iostream>

  class MyClass
  {
  private:
      int a;

  public:
      MyClass(int x = 2) : a{ x } {}
      MyClass& operator=(MyClass& x);		//The return type must be MyClass& for chaining!

      void modify()
      {
          a = 10;
      }

      void print_a()
      {
          std::cout << "data attribute a = " << a << std::endl;
      }
  };

  MyClass& MyClass::operator=(MyClass& x)
  {
      std::cout << "overloaded assignment operator called" << std::endl;
      this->a = x.a;
      return *this;
  }

  int main()
  {

      MyClass obj1, obj2, obj3;
      MyClass result;
      obj1.modify();
      obj2.modify();
      obj3.modify();
      result = obj1 = obj2 = obj3;        //chaining; result.operator=(obj1.operator=(obj2.operator=(obj3)))
      result.print_a();
  }

  //overloaded assignment operator called
  //overloaded assignment operator called
  //overloaded assignment operator called
  //data attribute a = 10
  ```

<br>

> If the return type of the overloaded assignment operator is not a reference, it returns a rvalue, copy of the assigned object rather than a reference to it. In this case, chaining multiple assignments together wouldn't work because the subsequent assignment operators would be operating on temporary objects instead of the original objects.

<br>
<br>

# Unary Operator Overloading

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

# Arrow Assignment Overloading

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
<br>

# From old notes

- The following class will be used for illustration

  ```cpp
  #include <iostream>
  #include <cstring>
  using namespace std;

  class Mystring {
  private:
    char* str;
  public:
    Mystring();
    Mystring(const char* s);
    Mystring(const Mystring& source);
    ~Mystring();
    void display() const;
    int get_length() const;
    const char* get_str() const;
  };

  Mystring::Mystring(): str{nullptr}
  {
    str = new char[1];	//allocate 1 character of space on the heap
    *str = '\0';

  }

  Mystring::Mystring(const char* s)
  {
    if (s == nullptr) {
      str = new char[1];
      *str = '\0';
    }
    else {
      str = new char[std::strlen(s) + 1];
      std::strcpy(str, s);
    }
  }

  Mystring::Mystring(const Mystring& source):Mystring(source.str)
  {
    cout << "copy constuctor called" << endl;
  }


  Mystring::~Mystring()
  {
    delete[] str;
  }


  void Mystring::display() const
  {
    cout << str << endl;
  }

  int Mystring::get_length() const
  {
    return std::strlen(str);
  }


  const char* Mystring::get_str() const
  {
    return str;
  }
  ```

<br>
<br>

<br>
<br>

# Overloading the assignment operator (move)

- If r value is being assigned (rhs) then we must define an overloaded move assignment operator.
- In the below code, The Mystring object is created as a temporary (r value) and being assigned to s1.

  ```cpp
  Mystring s1;
  s1 = Mystring{"Frank"}; // overloaded move assignment operator is ideal
  ```

* Checkout the implementation for overloading move assignment operator.

  ```cpp
  //Mystring& operator=(Mystring&& rhs) noexcept; <add this in class declaration>

  Mystring& Mystring::operator=(Mystring&& rhs)noexcept
  {
    if (this == &rhs) {
      return *this;
    }
    delete[] str;
    str = rhs.str;
    rhs.str = nullptr;  //We must not forget to null this out!
    return *this;
  }

  int main()
  {
    Mystring s1;
    s1 = Mystring{ "Temp" };
    cout << s1.get_str() << endl;  //Temp
  }
  ```

<br>

# Overloading operators as member methods

> Fill Notes / check this out when needed <br> > <br>
