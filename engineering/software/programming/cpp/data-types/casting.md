# Casting

Casting is the process of converting a value or a variable from one data type to another.

* To completely understand this concept, knowledge of [oops](../oops/) is necessary.

<br>
<br>
<br>

## Types of casting

<br>
<br>

### Based on explicitness

<br>

####  Implicit casting

Casting is performed automatically by thecompiler when it is safe to do so.


* Example: Converting an int to a double.


<br>

####  Explicit casting

Programmer explicitly requests the type conversion using cast operators.

* C++ facilitates the following four kinds of named casting.

<br>
<br>

### Based on direction

<br>

#### Up casting

Converting from a derived class to a base class (moving "up" the inheritance hierarchy).

* Always safe (derived "is-a" base).
* Can be implicit.
* Loses access to derived-specific members.
* Polymorphism-friendly.

<br>

#### Down casting

Converting from a base class to a derived class (moving "down" the inheritance hierarchy).

* Potentially unsafe (not all base objects are derived objects)
* Must be explicit.
* Requires runtime type checking for safety, check [dynamic cast operator](#dynamic-casting).
    

* Few possible reasons for necessity.
    * Accessing unique derived methods. Suppose we have a base class object `GameEntity` and we need to call `openInventory` method which is specific to `Player` derived class.
    * Hand written type checkers. Suppose in a collision system, there are two `PhysicsBody*` objects. There is a need to know if it is `TriggerZone` or `SolidWall` so as to be handled appropriately.
    * Interacting with GUI frameworks. Most libraries return generic pointers to "Object" or "Widget", one needs to cast it to specific widget for appropriate use.

<br>
<br>
<br>

## Types of named explicit casting operators.

<br>
<br>

### Static casting

Is used for performing conversions that are known at compile-time and can be checked for type consistency.

* It works with both polymorphic and non-polymorphic class hierarchies.
* It supports both upcasting and down casting.
* Static cast is "type safe" only in the sense that it prevents mathematically impossible conversions but it is "instance unsafe" as it doesn't check what the object actually is at the moment in memory.
* The static cast operator gives a compilation error if two types are completly unrelated.

    ```cpp
    #include <bits/stdc++.h>
    using namespace std;


    class Vehicle{
        std::string brand;
        std::string make;
    };

    class Animal{
        std::string name;
    };

    int main() {
        
        Vehicle* car = new Vehicle();
        Animal* dog = static_cast<Animal>(car);
    }
    ```

- The static cast operator does not perform any runtime check, it trusts the programmer which might lead to runtime crashes.

    ```cpp
    #include <bits/stdc++.h>
    using namespace std;


    class Vehicle{;
    };

    class Car : public Vehicle{
    };

    class Bus : public Vehicle{
    };


    int main() {
        
        Bus* bus = new Bus();
        Vehicle* car = static_cast<Vehicle*>(bus); //misleading bus is considered to be a car.
    }
    ```


<br>
<br>

### Dynamic casting

`dynamic_cast` is a C++ casting operator used for downcasting or side casting base classes that are polymorphic.

* It works only with polymorphic base classes, base classes that have atleast one virtual function.
* It is used mostly for down casting and side casting. Although upcasting is supported but it doesn't make sense as it is always safe to cast derived to base.


* When dealing with pointers, `dynamic_cast` returns a `nullptr`. Hence, the foolproof safe method is to perform the cast and immediately check for nullptr within a conditional scope.

    ```cpp
    // Base* ptr = getSomeObject();
    if (Derived* derivedPtr = dynamic_cast<Derived*(ptr)) {
        // SUCCESS: The pointer is definitely a 'Derived'type here.
        derivedPtr->specificFunction();
    } else {
        // FAILURE: ptr was either null or not a'Derived' type.
        // Handle the error gracefully.
    }
    ```
* When dealing with references, `dynamic_cast` throws an `std::bad_cast` exception. Hence, The foolproof way is to wrap it in try catch block.

    ```cpp
    try {
        Derived& d = dynamic_cast<Derived&>(baseRef);
        d.specificFunction();
    } catch (const std::bad_cast& e) {
        // Handle the fact that baseRef was not actuallya Derived type
        std::cerr << "Cast failed: " << e.what() <<std::endl;
    }
    ```


* When `dynamic_cast` is used, C++ 

    1. Follows the object's [vptr](../oops/02-cpp-polymorphism.md#virtual-method-table) to it's [vtable](../oops/02-cpp-polymorphism.md#polymorphic-internals).

    1. Looks up [RTTI](../oops/02-cpp-polymorphism.md#rtti) information stored there.

    1. Compares that type information against the type to cast to and based on the inhertiance check returns the result.

<br>
<br>

### Reinterpret casting

<br>
<br>

### Const casting