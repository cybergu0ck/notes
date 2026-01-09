# Polymorphism

Polymorphism is the ability to use the same code to operate on different types of objects. This makes the code more flexible.

<br>
<br>
<br>

## Types of Polymorphism in C++

- C++ supports two types of polymorphism.
  1. Compile Type / Early Binding / Static Binding
  2. Run Time / Late Binding / Dynamic Binding



<br>
<br>
<br>

## Compile Time Polymorphism


Compile-time polymorphism is the ability of a program to use a single name (interface) to represent multiple behaviors, where the exact (implementation) is resolved by the compiler at compile time.

- Compile time polymorphism occurs before the program is run i.e. during the compilation.
- Compile time polymorphism is also called as early binding or static binding.
- Few forms of compile time polymorphism are 

    1. Function overloading
    1. Operator overlaoding
    1. Templates (parametric polymorphism)


### Function overloading

<br>
<br>

### Overloaded constructors

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
<br>


## Polymorphic internals

<br>

### Virtual method table

The "vtable" is a static lookup table created by the compiler for every class that contains at least one [virtual function](../oops/05-cpp-inheritence.md#virtual-functions).

* It contains the memory addresses of the virtual functions for that specific class.
* There is only one vtable per class, regardless of how many objects of that class you create.
* If a class has no virtual functions, the compiler doesn't create a vtable.

<br>
<br>

### Virtual pointer

The "vptr" is a hidden pointer added to every instance of a class that has a [vtable](#virtual-method-table).

* It points to the [vtable](#virtual-method-table) of the class that created the object.
* Every polymorphic class has it's own "vptr".


<br>
<br>

### RTTI

RTTI is a language mechanism that provides information about an object's data type at runtime.

* This is necessary because, in a [polymorphic class]() hierarchy, a pointer of type `Base*` might point to an object of type `Derived1`, `Derived2`, or even a further subclass. Without RTTI, the program would only see the "interface" (the Base) and not the "identity" (the Derived).
* RTTI stands for Run-Time Type Information.
* In most compilers, a pointer to a Type Information Object (`std::type_info`) is stored inside the vtable (usually at the very beginning).

<br>

#### Criteria for RTTI

RTTI is not available for all data types. The criteria for RTTI :

1. Polymorphic classes only: The class must contain at least one virtual function. This forces the compiler to generate a [vtable](#virtual-method-table), which acts as the storage header for RTTI data.
1. Compiler support : Compiler must support it. Optionally it also can be turned off using `-fno-rtti` flag to save memory and performance.

<br>

#### Core operators for RTTI

RTTI is accessed through two primary C++ operators:

1. `dynamic_cast<T>` : Check the working of [dynamic cast](../data-types/casting.md#dynamic-casting).
1. `typeid` : Used to retrieve the actual type of an object. It returns a reference to a constant `std::type_info object`.