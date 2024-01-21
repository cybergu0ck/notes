# Function

_**Function** are reusable logically self-contained code that facilitates modularization of program._

- Illustration of a C++ function

  ```cpp
  #include <iostream>
  int add_numbers(int, int);		//function prototype
  int main()
  {
      int a{ 10 }, b{ 20 };
      int result{ 0 };
      result = add_numbers(a, b);		//function call
      std::cout << a << " + " << b << " equals " << result << std::endl;
  }
  int add_numbers(int num1, int num2) {	//function defintion
      return num1 + num2;
  }
  ```

<br>
<br>

## Function Definition

_**Function definition** provides the actual implementation of the function, defining what the function does when it is called._

```
return_type function_name(type parameter...){
    //body
}
```

<br>
<br>

## Function Prototype (Forward Declaration)

_**Function prototype** tells the compiler all it needs to know about a function._

- The compiler must know the function details before it is called, becuase it must know if the number of arguments and it's types are matching that of the parameter list.

  ```cpp
  int main()
  {
      sayHello();  //error: sayHello identifier not found
  }

  void sayHello() {
      cout << "hello" << endl;
  }
  ```

- Function prototype for the above code is

  ```cpp
  void sayHello();
  ```

- These are generally written at the beginning of the program (for smaller programs) and are wriiten in header files (.h files) in case of larger programs.
- The compiler doesn't care about the names of the parameters, it only cares about it's type.
  ```cpp
  int foo(int a, int b);  //ok
  int foo(int, int);      //ok
  ```
- Function prototypes are really helpful when two functions call each other.

<br>
<br>

## Function Call

- functions can be called from main or from within functions.

  ```cpp
  void sayHello() {
      cout << "hello" << endl;
  }

  int main()
  {
      sayHello();  //ok: compiler has seen the definiton of sayHello
  }
  ```

<br>
<br>

## Activation Records (Function Stack Frame)

In C++, whenever a function is called and it is handled in a 3 step process: prolog, business-logic and epilog.

![acti](../_assets/activation-record.png)

- Functions use the **_function call stack_** of the memory, which follows LIFO (last in first out)
- Each time a function is called, a new **_stack frame_** (**_activation record_**) is created and pushed to the stack. When the function terminates, the activation record is popped and returns the control to the function that called it.
- The prolog instructions are written by the compiler and will be present in the exe.
- Local variables and function parameters are stored on the stack.

<br>
<br>

## Function Parameters

_**Parameters** refer to the data that is passed into a funciton when it is called._

- parameters and arguments must match in _number, order and type_.

<br>

### Formal and Actual parameters

- Formal parameters (parameters) are the parameters defined in the function definiton or prototype.
- Actual parameters (arguments) are the parameters used in the function call, the arguments.

- In C++, the actual paramters are passed by value i.e. the actual parameters are copied to the formal parameters.

<br>
<br>

### Pass by Value

_When arguments are **passed by value**, the copy of the actual arguments is passed to the function._

- In C++, when we pass arguments normally it is passed by value.
- When we modify the parameter that is passed by value, we are modifying the copy and the original argument doesn't change.

  ```cpp
  void modify(int );

  int main()
  {
      int a{ 0 };
      modify(a);
      cout << "value of 'a' after modify() is " << a << endl;

  }

  void modify(int num)
  {
      num = 100;
  }

  //value of 'a' after modify() is 0
  ```

<br>
<br>

### Pass by Reference

_When arguments are **passed by reference**, the actual argument is passed to the function, via a reference._

- In C++, when we pass arguments by reference, they are passed as reference.
- Here, the formal parameters are aliases for the actual parameters.
- When we modify the parameter that is passed by reference, we are modifying the original argument.

  ```cpp
  void modify(int& );

  int main()
  {
      int a{ 0 };
      modify(a);
      cout << "value of 'a' after modify() is " << a << endl;

  }

  void modify(int &num)
  {
      num = 100;
  }

  //value of 'a' after modify() is 100
  ```

<br>

- It is efficient to pass long vectors or arrays by reference to save memory (as this avoids making copy), but if we donot want to modify the data (because pass by reference will modify the original argument), we must use `const` qualifier in the parameter list of the function

<br>
<br>

### Default Argument Values

_**Default arguments** are values that are assigned to function parameters if no arguments are passed to the function when it is called._

- It is ideal to set default arguments in the function declaration (h file) and not in definition (cpp file), keeping [developer-consumer approach](../../programming.md#developer-consumer-approach) in mind

  ```cpp
  float calculate_total_cost(float cost, float = 0.06); //good practice

  int main()
  {
      float cost{ 200 };
      cout << "total is " << calculate_total_cost(cost) << endl;
  }

  float calculate_total_cost(float cost, float tax_rate )
  {
      return cost * (1 + tax_rate);
  }
  ```

* Default arguments must not be followed by normal formal parameters.

  ```cpp
  void fun(int a = 10, int b);  //error
  void fun(int b, int a = 10); //ok
  ```

* When overloading a function that has default arguments, it's signature must not clash with the function having default arguments

  ```cpp
  #include <iostream>

  void fun(int a, int b = 10) {
  }

  void fun(int) {
  }

  int main()
  {
      fun(10);     //error because of ambiguity
  }
  ```

<br>
<br>

## Passing Arrays to Functions

- When we pass an array to a function, we are actually passing the memory address of the first element of the array (pointer pointing to the first element of the array)

  ```cpp
  #include <iostream>

  void print_array(int arr[]);

  int main()
  {
      int arr[3]{ 10,20,30 };
      print_array(arr);
  }

  void print_array(int arr[])   //the arr parameter here is a pointer!
  {
      std::cout << *arr << std::endl;
  }

  //10
  ```

- Therefore, there is no way of knowing (from the function) how many elements are there in the array! Hence, we usually pass the size of the array as the accompanying argument.

  ```cpp
  void print_array(int arr[], size_t size);

  int main()
  {
      int arr[3]{ 10,20,30 };
      print_array(arr, 3);
  }

  void print_array(int arr[], size_t size)
  {
      for (int i{ 0 }; i < size; i++) {
          cout << arr[i] << '\t';
      }
  }

  //10    20  30
  ```

- Since a pointer is being passed when an array is passed into a function, they are **_passed by reference_**, and hence the original argument (i.e. array) will be modified if we modify the parameter in the function.

  ```cpp
  void make_zero(int arr[], size_t size);

  int main()
  {
      int arr[3]{ 10,20,30 };
      make_zero(arr, 3);

      int size = sizeof(arr) / sizeof(arr[0]);

      for (int i{ 0 }; i < size; i++) {
          cout << arr[i] << "\t";
      }
  }

  void make_zero(int arr[], size_t size)
  {
      for (int i{ 0 }; i < size; i++) {
          arr[i] = 0;
      }
  }

  //0   0   0
  ```

<br>
<br>

## Passing Vectors into functions

- Passing vectors by reference

  ```cpp
  #include <iostream>
  #include <vector>
  using namespace std;

  void print_vector(vector <int> &vec)
  {

      for (int i = 0; i < vec.size(); i++) {
          vec[i] = 0;
      }

      /*
      we need to use reference (&) inside the range for to modify the original vector!

      for (auto &item: vec) {
          item = 0;
      }
      */

  }

  int main()
  {
      vector<int> my_vec{ 10,20,30 };
      int arr[3]{ 10,20,30 };

      print_vector(my_vec);


      for (auto item : my_vec) {
          cout << item << '\t';
      }
  }

  //0     0       0
  ```

<br>
<br>

## Function Overloading

_**Function Overloading** is a concept of having two or more functions with same name but different parameter list._

- Function Overloading is a form of Polymorphism.

  ```cpp
  void display(int );
  void display(string);

  int main()
  {
      display(10);
      display("Hey");
  }

  void display(int num)
  {
      cout << "Displaying the number: " << num << endl;
  }

  void display(string str)
  {
      cout << "Displaying the string: " << str << endl;
  }

  //Displaying the number: 10
  //Displaying the string: Hey
  ```

- functions cannot be overloaded based on return types!

  ```cpp
  int get_value();     //error
  double get_value();  //error

  int main()
  {
      display(10);
      display("Hey");
  }

  int get_value()
  {
      return 10;
  }

  double get_value()
  {
      return 10.00;
  }
  ```

  <br>
  <br>

## Inline Functions

Inline Function is a function that is expanded at the point of it's invocation rather than generating the function call (in assembly file).

```cpp
//wether a function is inlined by the compiler can be verified in asm file, however at this time I am not sure how to get this done in Visual Studio

inline int add(int a, int b) {
    return a + b;
}
```

- [prolog and epilog](#activation-records-function-stack-frame) adds overhead when the function is called, which is avoided by using inline functions.
- Inline functions would enhance execution speed. At the same time it would increase the size of the executable file.
