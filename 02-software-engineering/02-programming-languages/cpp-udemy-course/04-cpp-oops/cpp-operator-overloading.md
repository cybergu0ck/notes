# Operator Overloading

- Operator overloading is a feature in C++ that allows programmers to redefine the meaning of operators for user-defined data types. This can make code more concise and readable, and can also improve the flexibility and expressiveness of a program.
- The following operators cannot be overloaded

  | Operator             | Symbol |
  | -------------------- | ------ |
  | Scope Resolution     | ::     |
  | Conditional Operator | :?     |
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

# Overloading the assignment operator (copy)

- concept clarity for assignment and definiton, An assignment occurs when an object is already initialised and we want to assign another object to it. See below:

  ```cpp
  Mystring s1{ "frank" };
  Mystring s2 = s1;  //NOT assignment; equivalent to Mystring s2{s1};

  s2 = s1;	//this IS assignment as s2 has already been initialised and s1 is an l value!
  ```

* If we donot provide an overloaded assignment operator, the compiler will generate a default one, which will perform member wise copy (which is shallow copy), this is sufficient if the class does not have raw pointer attributes.
* We can define an overloaded assignment opearator,
* If l value is being assigned (rhs) then we must define an overloaded copy assignment operator.
* If raw pointers are present in class, we will overload the copy assignment operator to perform deep copy on l value references! syntax is as follows (using debugger we can see that the control jumps to the copy overloaded function when assignment occurs)

  ```
  type& type::operator=(const type &rhs)
  ```

  ```cpp
  //Mystring& operator=(const Mystring& rhs); <add this in class declaration>

  Mystring& Mystring::operator=(const Mystring& rhs)
  {

    if (this == &rhs)   //checking self assignment (ex case: s2 = s2)
    {
      return *this;
    }

    delete[] str;	                                //deallocate storage since we are overwriting it
    str = new char[std::strlen(rhs.str) + 1];	    //allocate the required amount of storage
    std::strcpy(str, rhs.str);		                //perform copy which is now a deep copy
    return *this;
  }


  int main()
  {
    Mystring s1{ "frank" };
    cout << s1.get_str() << endl;		//frank

    Mystring s2;
    s2 = s1;	                      //under the hood: s2.operator=(s1); i.e. overloaded copy assignment operator is called

    cout << s2.get_str() << endl;		//frank
  }
  ```

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

> Fill Notes / check this out when needed <br>
> <br>
