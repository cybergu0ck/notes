# Terminology

- **Exception** : an object or primitive type that signals that an error has occurred.
- **Throwing an exception (Raising an exception)** : It is the code that detects an error that has(will) occurred(occur) but doesn't know how to handle it.
- **Catching an exception (Handling an exception)** : It is the code that handles the exception.

<br>
<br>

# C++ Exception Handling syntax

    ```
    try
    {
        //code here can potentially throw an exception!
    }

    catch (exception obj)
    {
        //code here is run only if the try block code throws an exception and that object mathches
        //the exception obj mentioned above.
    }
    ```

- An illustration without exception handling, a program that prints miles per gallon

  ```cpp
  int main()
  {
      int miles{ 100 };
      int gallons{ 0 };
      double miles_per_gallon;
      if (gallons != 0)
      {
          miles_per_gallon = miles / gallons;
          std::cout << "fuel economy is " << miles_per_gallon << endl;
      }
      else
      {
          std::cerr << "cannot divide by zero" << endl;
      }
  }
  ```

- The same program using exception handling

  ```cpp
  #include <iostream>

  int main()
  {
      int miles{ 100 };
      int gallons{ 0 };
      double miles_per_gallon;

      try
      {
          if (gallons == 0)
              throw 0;
          miles_per_gallon = miles / gallons;
          std::cout << "fuel economy is " << miles_per_gallon << std::endl;
      }
      catch (int& ex)
      {
          std::cout << "cannot divide by zero" << std::endl;
      }
  }
  ```

<br>
<br>

## Throwing an exception from a function

- It is similar to throwing exception normally

  ```cpp
  #include <iostream>

  double calculate_mpg(int miles, int gallons) {
      if (gallons == 0)
          throw 0;
      return static_cast<double> (miles) / gallons;
  }

  int main()
  {
      int miles{ 100 };
      int gallons{ 0 };
      double miles_per_gallon;

      try
      {
          miles_per_gallon = calculate_mpg(miles, gallons);
          std::cout << "fuel economy is " << miles_per_gallon << std::endl;
      }
      catch (int& ex)
      {
          std::cout << "cannot divide by zero" << std::endl;
      }
  }

  //cannot divide by zero
  ```

<br>
<br>
<br>

# Handling Multiple Exceptions

```cpp
#include <iostream>

double calculate_mpg(int miles, int gallons) {
    if (gallons == 0)
        throw 0;
    if (miles < 0 || gallons < 0)
        throw std::string{ "Negative value error" };
    return static_cast<double> (miles) / gallons;
}

int main()
{
    int miles;
    int gallons;
    std::cout << "Enter miles: ";
    std::cin >> miles;
    std::cout << "Enter gallons: ";
    std::cin >> gallons;
    std::cout << std::endl;

    double miles_per_gallon;

    try{
        miles_per_gallon = calculate_mpg(miles, gallons);
        std::cout << "fuel economy is " << miles_per_gallon << std::endl;
    }
    catch (int& ex){
        std::cerr << "cannot divide by zero" << std::endl;
    }
    catch (std::string& ex) {
        std::cerr << ex << std::endl;
    }
}
```

<br>
<br>

## Catch All block

- In C++ exception handling, a "catch-all" block refers to a catch block that can catch exceptions of any type.
- he catch-all block is typically used as a last resort to handle any exceptions that were not caught by more specific catch blocks.

```cpp
catch (...) {
        std::cerr << "Unkown Error" << std::endl;
    }
```

<br>
<br>
<br>

# Exception Handling in the context of Stack Unwinding

- Normal unwinding of the stack

  ```cpp
  #include <iostream>

  void func2(); //forward declaration
  void func3(); //forward declaration

  void func1() {
      std::cout << "func1 started..." << std::endl;
      func2();
      std::cout << "func1 executed." << std::endl;
  }

  void func2() {
      std::cout << "func2 started..." << std::endl;
      func3();
      std::cout << "func2 executed." << std::endl;
  }

  void func3() {
      std::cout << "func3 started..." << std::endl;
      //code
      std::cout << "func3 executed." << std::endl;
  }

  int main()
  {
      std::cout << "main started..." << std::endl;
      func1();
      std::cout << "main executed." << std::endl;
  }

  //main started...
  //func1 started...
  //func2 started...
  //func3 started...
  //func3 executed.
  //func2 executed.
  //func1 executed.
  //main executed.
  ```

* When an exception is thrown within a function's scope, the program seeks a relevant catch block in the same scope to address the exception. If found, the control shifts to that catch block, and after handling the exception, execution continues. If no appropriate catch block is present, the function's scope is abruptly terminated (skipping the rest of the code in that function), and the program proceeds to unwind the call stack, searching for relevant catch blocks in higher scopes. If a suitable catch block is encountered until main, the exception is managed, otherwise, the program ends with an error, typically through the abort() function. This hierarchical process allows for structured error handling, enabling recovery or orderly program termination.

  ```cpp
  #include <iostream>

  void func2(); //forward declaration
  void func3(); //forward declaration

  void func1() {
      std::cout << "func1 started..." << std::endl;
      func2();
      //code  //skipped
      std::cout << "func1 executed." << std::endl;  //skipped
  }

  void func2() {
      std::cout << "func2 started..." << std::endl;
      func3();
      //code  //skipped
      std::cout << "func2 executed." << std::endl;  //skipped
  }

  void func3() {
      std::cout << "func3 started..." << std::endl;
      throw(100);
      //code  //skipped
      std::cout << "func3 executed." << std::endl;  //skipped
  }

  int main()
  {
      std::cout << "main started..." << std::endl;
      func1();
      //code  //skipped
      std::cout << "main executed." << std::endl;  //skipped
  }

  //main started...
  //func1 started...
  //func2 started...
  //func3 started...
  //<run time error>
  ```

  ```cpp
  #include <iostream>

  void func2(); //forward declaration
  void func3(); //forward declaration

  void func1() {
      std::cout << "func1 started..." << std::endl;
      func2();
      std::cout << "func1 executed." << std::endl;
  }

  void func2() {
      std::cout << "func2 started..." << std::endl;
      try {
          func3();
      }
      catch (int& ex) {
          std::cerr << "caught exception" << std::endl;
      }
      std::cout << "func2 executed." << std::endl;
  }

  void func3() {
      std::cout << "func3 started..." << std::endl;
      throw(100);
      //code                                          //skipped
      std::cout << "func3 executed." << std::endl;    //skipped
  }

  int main()
  {
      std::cout << "main started..." << std::endl;
      func1();
      std::cout << "main executed." << std::endl;
  }

  //main started...
  //func1 started...
  //func2 started...
  //func3 started...
  //caught exception
  //func2 executed.
  //func1 executed.
  //main executed.
  ```

<br>
<br>
<br>

# User Defined Exception Class

- It is best practice to
  - throw an object instead of a primitive type.
  - throw an object by value.
  - catch an object by reference (or const reference).

```cpp
#include <iostream>

class DivideByZeroError {
};

class NegativeValueError {
};

double calculate_mpg(int miles, int gallons) {
    if (gallons == 0)
        throw DivideByZeroError();
    if (miles < 0 || gallons < 0)
        throw NegativeValueError();
    return static_cast<double> (miles) / gallons;
}

int main()
{
    int miles;
    int gallons;
    std::cout << "Enter miles: ";
    std::cin >> miles;
    std::cout << "Enter gallons: ";
    std::cin >> gallons;
    std::cout << std::endl;

    double miles_per_gallon;

    try {
        miles_per_gallon = calculate_mpg(miles, gallons);
        std::cout << "fuel economy is " << miles_per_gallon << std::endl;
    }
    catch (const DivideByZeroError &ex) {
        std::cerr << "cannot divide by zero" << std::endl;
    }
    catch ( const NegativeValueError &ex) {
        //std::cerr << ex << std::endl;  //Need to provide overloaded stream insertion operator in the class
        std::cerr << "miles or gallons can not be negative" << std::endl;
    }
}
```

<br>
<br>
<br>

# Class Level Exceptions

- Do not throw exceptions from a class destructor. (destructors are `noexcept`)
- Exceptions can be thrown from class constructor methods.

<br>
<br>
<br>

# The C++ std::exception Class Hierarchy

> make notes from the udemy course

<br>
<br>
<br>
