# PImpl

_"Pointer to implementation" or "pImpl" is a C++ programming technique that removes implementation details of a class from its object representation by placing them in a separate class, accessed through an opaque pointer._

- pImpl removes this compilation dependency; changes to the implementation do not cause recompilation.
- pImpl is also known as the "Compiler Firewall" or "Opaque Pointer" idiom.

<br>
<br>

## Illustration

- Consider the following class and a main file.

  ```cpp
  //myclass.h
  #pragma once

  class MyClass {
  public:
      MyClass(int number);
      int getNumber();
      void setNumber(int number);
  private:
      int m_data;
  };
  ```

  ```cpp
  //myclass.cpp
  #include "myclass.h"

  MyClass::MyClass(int number):m_data{number}{}

  int MyClass::getNumber()
  {
      return m_data;
  }

  void MyClass::setNumber(int number)
  {
      m_data = number;
  }
  ```

  ```cpp
  //main.cpp
  #include "myclass.h"
  #include <iostream>

  int main()
  {
      MyClass obj{ 10 };
      std::cout << obj.getNumber() << "\n";
      obj.setNumber(20);
      std::cout << obj.getNumber() << "\n";
  }
  ```

- There are 2 drawbacks:
  1. The private data of the class is not abstracted as it is present in the header file.
  2. Any change in the header file will lead to recompilation of all the files that use the header file.

<br>

### Using PImpl

The above mentioned drawbacks can be taken care using PImpl implementation.

```cpp
//myclass.h
#pragma once
#include <memory>

class MyClass {
public:
	MyClass(int number);
	~MyClass(); //Required as we are using unique_ptr
	int getNumber();
	void setNumber(int number);
private:
	struct Impl;
	std::unique_ptr<Impl> pimpl;
};
```

```cpp
//myclass.cpp
#include "myclass.h"

struct MyClass::Impl {
	Impl(int number):m_data{number}{}

	int m_data;
};

MyClass::MyClass(int number) :pimpl{new Impl(number)} {}

MyClass::~MyClass(){}

int MyClass::getNumber()
{
	return pimpl->m_data;
}

void MyClass::setNumber(int number)
{
	pimpl->m_data = number;
}
```

```cpp
//main.cpp
#include "myclass.h"
#include <iostream>

int main()
{
	MyClass obj{ 10 };
	std::cout << obj.getNumber() << "\n";
	obj.setNumber(20);
	std::cout << obj.getNumber() << "\n";
}
```

<br>

## Copy Constructor for PImpl

```cpp
MyClass::MyClass(const MyClass& other):pimpl{new Impl(*other.pimpl)}{}
```

<br>

## Overloaded Assignment Operator for PImpl

One version is to take the parameter by value and use the memory library's swap function.

```cpp
MyClass& MyClass::operator=(MyClass rhs)
{
	swap(pimpl, rhs.pimpl);
	return *this;
}
```
