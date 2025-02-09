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
