# Run time polymorphism

Run-time polymorphism is the ability of a program to use a single name (interface) to represent multiple behaviors, where the exact (implementation) is resolved at run time.

* It is also known as dynamic binding or late binding in C++.

<br>
<br>
<br>



## Virtual methods

A virtual method is a member function declared within a base class using the `virtual` keyword, intended to be overridden by derived classes.

* Virtual method is also known as polymorphic method.
- Understand [inheritance](../inheritance.md) to understand this topic.

<br>

- Virtual methods enable dynamic binding when called through a pointer or reference.
- Any nonstatic member function, other than a constructor, can be a virtual method.
- The `virtual` keyword is used only in the class declaration, not in the function definition outside the class body.
- A method that is declared as virtual in the base class is implicitly virtual in the derived classes as well.
- Derived classes need not always override the virtual methods that they inherit, in such cases it inherits the version defined in the base class.

* The function signatures of the virtual methods must be same in both base class and derived class for the derived class to override the base. If signatures are different, then it is considered as a redefiniton in the derived class i.e. considered as a fresh new method.

  ```cpp
  #include <iostream>
  using namespace std;

  class Base {
  public:
      virtual void say_hello() const
      {
          cout << "Hello, I am a Base class object " << endl;
      }
  };

  class Derived : public Base {
  public:
      virtual void say_hello()        //won't be overriden as
      {
          cout << "Hello, I am a Derived class object " << endl;
      }
  };


  int main()
  {
      Base* b_ptr = new Base();
      b_ptr->say_hello();

      Base* d_ptr = new Derived();  //we can do this becuase Derived obj is a Base obj too (inheritance)
      d_ptr->say_hello();

      delete b_ptr;
      delete d_ptr;
  }

  //Hello, I am a Base class object
  //Hello, I am a Base class object

  //Check this [stack overflow](https://stackoverflow.com/questions/9488168/virtual-function-const-vs-virtual-function-non-const)
  ```

- Virtual methods that have default arguments should use the same argument values in the base and derived classes.
  - When a call is made through a reference or pointer to base, the default argument(s) will be those defined in the base class. The base-class arguments will be used even when the derived version of the function is run.

- Non-virtual methods can be declared and left undefined. This doesn't lead to compilation error until they are not called. Note that this is never a good practice.

    ```cpp
    class MyClass
    {
    public:
        void hello();
    };

    int main()
    {
        MyClass obj;
    }
    ```

- Virtual functions must always be defined because the version of the function that will be called may not be known until run time.

  ```cpp
  class MyClass
  {
  public:
      virtual void declared_but_not_defined();
  };

  int main()
  {
      MyClass obj;
  }

  //liner error: undefined reference to `vtable for MyClass'
  ```


<br>
<br>
<br>

## Polymorphic class



<br>
<br>
<br>


## Virtual method table

The virtual method table is a static lookup table created by the compiler for every class that contains at least one [virtual function](../oops/05-cpp-inheritence.md#virtual-functions).

- Virtual method table is also known as "vtable".
- A vtable is typically implemented as a static array of function pointers.
- There is only one vtable per class, regardless of how many objects of that class you create.
- If a class has no virtual functions, the compiler doesn't create a vtable.
- Note that vtable is fully constructed at compile time. The compiler stores the vtable in the read only data segment of the executable.

<br>
<br>

### Illustration for vtable

```cpp
#include <iostream>
class Vehicle {
public:
    virtual void startEngine() {
        std::cout << "Vehicle engine started." << std::endl;
    }
    
    virtual ~Vehicle() {}
};
class Car : public Vehicle {
public:
    void startEngine() override {
        std::cout << "Car engine roars to life!" << std::endl;
    }
};
```
* Illustartion of `Vehicle`'s vtable.

    | Index | Function pointer |
    |---|---|
    | 0 | &Vehicle::~Vehicle() |
    | 1 | &Vehicle::startEngine()|

<br>

* Illustartion of `Car`'s vtable.

    | Index | Function pointer |
    |---|---|
    | 0 | &Car::~Car() |
    | 1 | &Car::startEngine()|

<br>

* For any class hierarchy, the compiler ensures that a specific virtual function always sits at the exact same index in every related vtable.
    * If the compiler decides zeroth index for destructor and first index for `startEngine` in `Vehicle`'s vtable.
    * When `Car` inherits from `Vehicle`, it must respect those same space assignemnts. that is zeroth index for destructor and first index for `startEngine` in `Car`'s vtable.


<br>
<br>
<br>

## Virtual pointer

The "virtual pointer is a hidden pointer added to every instance of a class that has a [vtable](#virtual-method-table).

- It is known as "vptr".
- It points to the [vtable](#virtual-method-table) of the class that created the object.
- Every polymorphic class has it's own "vptr".

<br>
<br>

### Illustration for vptr

```cpp
#include <iostream>
class Vehicle {
public:
    virtual void startEngine() {
        std::cout << "Vehicle engine started." << std::endl;
    }
    
    virtual ~Vehicle() {}
};
class Car : public Vehicle {
public:
    void startEngine() override {
        std::cout << "Car engine roars to life!" << std::endl;
    }
};
int main() {
    
    Vehicle* myVehicle = new Vehicle(); 
    Car* myCar = new Car();
    Vehicle* myFavVehicle = new Car(); //Base class pointer points to a derived object
    delete myVehicle;
    delete myCar;
    delete myFavVehicle;
    return 0;
}
```

* `myVehicle` is a pointer type (`Vehicle*`) in stack. It points to a `Vehicle` object created in the heap. That heap object has a "vptr" that points to "vtable" of the `Vehicle` class.
* `myCar` is a pointer type (`Car*`) in stack. It points to a `Car` object created in the heap. That heap object has a "vptr" that points to "vtable" of the `Car` class.
* `myFavVehicle` is a pointer type (`Vehicle*`) in stack. It points to a `Car` object created in the heap. That heap object has a "vptr" that points to "vtable" of the `Car` class.


<br>
<br>
<br>

## Criteria for run time polymorphism

1. Inheritance : A hierarchical relationship must exist between a base class and a derived class.
1. Virtual method : Base class should declare virtual method and the derived class must override it.
1. Pointer or Reference : The function must be invoked through a pointer or reference to the base class that points to an object of a derived class.

    - A call to a virtual function is bound at compile time when it is made on an expression with a simple type, such as nonreference or nonpointer.

        ```cpp
        #include <iostream>

        class Base
        {
        public:
            virtual void hello()
            {
                std::cout << "Hello, World! from Base" << std::endl;
            }
        };

        class Derived: public Base
        {
        public:
            void hello()
            {
                std::cout << "Hello, World! from Derived" << std::endl;
            }
        };

        int main()
        {
            Base obj = Base();
            obj.hello();       //Static binding

            Base* b = new Derived();
            b->hello();       //Dynamic binding
            delete b;
        }

        //Hello, World! from Base
        //Hello, World! from Derived
        ```

<br>
<br>
<br>

## Run time polymorphism mechanism


* Specifically run time polymorphism is the ability of a program to invoke different implementations of the same interface through a base-class reference or pointer, where the actual function executed is determined at run time based on the dynamic type of the object.

* When a virtual function is called through a base class pointer, the program follows the [vptr](#virtual-pointer) of the actual object to its [V-Table](#virtual-method-table) and executes the function located at the designated offset.

* Understand using the following example. 

    ```cpp
    #include <iostream>

    class Vehicle {
    public:
        virtual void startEngine() {
            std::cout << "Vehicle engine started." << std::endl;
        }
        
        virtual ~Vehicle() {}
    };

    class Car : public Vehicle {
    public:
        void startEngine() override {
            std::cout << "Car engine roars to life!" << std::endl;
        }
    };

    int main() {
        
        Vehicle* myVehicle = new Car(); // Base class pointer points to a derived class object
        myVehicle->startEngine();  // Late binding occurs here
        delete myVehicle;
        return 0;
    }

    //Car engine roars to life!
    ```

* `myVehicle` is a `Vehicle*` type. `myVehicle` is a pointer stored on the stack that points to an object in heap. In the heap, a `Car` object is allocated. This object contains all the data from both `Vehicle` and `Car` classses and a "vptr" pointing to the "vtable" for the `Car` class.

    ```cpp
    Vehicle* myVehicle = new Car();
    ```

* When the program encounters `myVehicle->startEngine()` during compile time, The compiler notes that `startEngine` method is marked `virtual`. Instead of compiling the function implementation, it generates the code that says "Go to the object pointed to by `myVehicle`, follow it's vptr to the vtable and call the function at the specified index reserved for `startEngine`". At run time, the program just executes these instructions.


<br>
<br>
<br>

## Circumventing run time polymorphism

Scope operator can be used to prevent dynamic binding of virtual method and call a specific version.

- If a derived virtual method that intended to call its base-class version omits the scope operator, the call will be resolved at run time as a call to the derived version itself, resulting in an infinite recursion.


    ```cpp
    #include<iostream>

    class Base {
    public:
        virtual void display() {
            std::cout << "Base display" << std::endl;
        }
    };

    class Derived : public Base {
    public:
        void display() override {
            display();  //Intended to call Base::display(), but omitted 'Base::'
            
            std::cout << "Derived display" << std::endl;
        }
    };

    int main()
    {
        Derived* obj = new Derived();
        obj->display();
    }

    //Infinite loop or Seg fault
    ```


- This is required for when a derived class virtual method needs to call the base class one.

  ```cpp
  #include <iostream>

  class Base
  {
  public:
      virtual void hello()
      {
          std::cout << "Hello, World! from Base" << std::endl;
      }
  };

  class Derived: public Base
  {
  public:
      void hello()
      {
          this->Base::hello();      //Use of scope operator
      }
  };

  int main()
  {
      Base* b = new Derived();
      b->hello();
      delete b;
  }

  //Hello, World! from Base
  ```

<br>
<br>

## Pure Virtual Function

A pure virtual function is a virtual function that has no implementation in the base class and must be overridden by any derived class.

- A pure virtual function is declared using following syntax.

  ```cpp
  class Base
  {
  public:
      virtual void hello() = 0; //pure virtual function and thus Base is an abstract class
  };
  ```

- Unlike virtual functions which must be defined, pure virtual functions can be left undefined or can be defined.

<br>
<br>
<br>


## RTTI

RTTI is a language mechanism that provides information about an object's data type at runtime.

- This is necessary because, in a [polymorphic class]() hierarchy, a pointer of type `Base*` might point to an object of type `Derived1`, `Derived2`, or even a further subclass. Without RTTI, the program would only see the "interface" (the Base) and not the "identity" (the Derived).
- RTTI stands for Run-Time Type Information.
- In most compilers, a pointer to a Type Information Object (`std::type_info`) is stored inside the vtable (usually at the very beginning).

<br>
<br>

### Criteria for RTTI

RTTI is not available for all data types. The criteria for RTTI :

1. Polymorphic classes only: The class must contain at least one virtual function. This forces the compiler to generate a [vtable](#virtual-method-table), which acts as the storage header for RTTI data.
1. Compiler support : Compiler must support it. Optionally it also can be turned off using `-fno-rtti` flag to save memory and performance.

<br>
<br>

### Core operators for RTTI

RTTI is accessed through two primary C++ operators:

1. `dynamic_cast<T>` : Check the working of [dynamic cast](../data-types/casting.md#dynamic-casting).
1. `typeid` : Used to retrieve the actual type of an object. It returns a reference to a constant `std::type_info object`.


<br>
<br>
<br>