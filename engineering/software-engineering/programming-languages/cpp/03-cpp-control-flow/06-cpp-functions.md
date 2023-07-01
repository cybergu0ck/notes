# Functions

- Functions allow us to modularise our program by creating logical self-contained code that can be reused.
- The syntax of creating and calling functions are as follows:

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

# Function Definition

```
return_type function_name(type parameter...){
    //body
}
```

## function name

- the name of the function must be appropriate and should be meaningful to what the function does.

<br>

## parameter list

- parameter list is the list of variables that are to be passed when the function is called.
- the types of the parameters must be specified.

<br>

## return type

- It is the type of the data that is returned from the function.

<br>

## function body

- The statements that are executed when the function is called, it is present within {}.

<br>
<br>

# Function Call

- The compiler must know the function details before it is called, becuase it must know if the number of arguments and it's types are mathcing that of the parameter list.
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

  ```cpp
  int main()
  {
      sayHello();  //error: sayHello identifier not found
  }

  void sayHello() {
      cout << "hello" << endl;
  }
  ```

<br>

# How does function call work?

- functions use the **_function call stack_** of the memory, which follows LIFO (last in first out)
- each time a function is called, a new **_stack frame_** (**_activation record_**) is created and pushed to the stack. When the function terminates, the activation record is popped and returns the control to the function that called it.
- local variables and function parameters are stored on the stack.
- stack size is finite, hence stack overflow may occur.

<br>
<br>

# Function Prototype (Forward Declaration)

> We cannot always rely on defining a function before it is being used, for instance two functions calling eachother.

- Function prototypes tell the compiler all it needs to know about a function.
- This enables us to define a function anywhere in our program.
- These are written at the beginning of the progeam (for smaller programs) and are wriiten in header files (.h files) in case of larger programs
- The compiler doesn't care about the names of the parameters, it only cares about it's type.
  ```cpp
  int foo(int a, int b);  //ok
  int foo(int, int);      //ok
  ```

<br>
<br>

# Function Parameters

- parameters refer to the data that is passed into a funciton when it is called.
- In the function call, they are called **arguments**.
- In the function definition, they are called **parameters**.
- parameters and arguments must match in _number, order and type_.

<br>

## Formal and Actual parameters

- formal parameters (parameters) are the parameters defined in the function definiton or prototype.
- actual parameters (arguments) are the parameters used in the function call, the arguments.

- In C++, the actual paramters are passed by value i.e. the actual parameters are copied to the formal parameters.

<br>
<br>
<br>
<br>

# Pass by Value

- In C++, when we pass data it is _passed by value_. what this means is that the compiler makes a copy of the data and that copy is passed into the function.
- When we modify the data that is passed by value, we are modifying the copy and the original argument doesn't change.

- Illustration:

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

# Pass by Reference

- pass by reference is used when we want to change/ modify the actual parameters(arguments) from within the function.
- We do this by creating reference parameters, the formal parameter will now be an alias for the actual parameter.

- Illustration:

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

# Default Argument Values

- default arguments are values that are assigned to function parameters if no arguments are passed to the function when it is called.
- It is ideal to set default arguments in the function declaration (h file) and not in definition (cpp file) as the h files will be text based and human readable while the cpp files will get compiled to binary and users cannot see the default arguments if needed (think in terms of library author and user relationship)
- default values must be at the tail end of the parameter list. i.e. normal parameters cannot follow defualt parameters.

  ```cpp
  float calculate_total_cost(float cost, float = 0.06);

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

* The default arguments must not be followed by normal formal parameters.

  ```cpp
  void fun(int a = 10, int b);  //error
  void fun(int b, int a = 10); //ok
  ```

* When overloading a function that has default arguments, it's signature must not clash with the default arguments

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

# Passing Arrays to Functions

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

# Passing Vectors into functions

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

# Function Overloading

- We can have functions with different parameter list that have the same name, this is called function overloading.
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

# Scope

- Scope is the region in the program where a name is visible.

- There are three types of scopes in C++:

  1. Global scope: This is the outermost scope in a program. Variables declared in the global scope are visible to all other scopes in the program.
  1. Function scope: This is the scope of a function. Variables declared within a function are only visible within that function.
  1. Block scope: This is the scope of a block of code ({//block}). Variables declared within a block of code are only visible within that block of code.
     - function parameters have block scope.

<br>

- with nested blocks inner blocks can 'see' but outer blocks cannot 'see'.

  ```cpp
  int main()
  {
      int num = 100;
      {
          int inner_num = -45;
      }
      cout << inner_num << endl;  //error
  }
  ```

- the name is first searched inside the scope, it starts searching outer scopes only if it is not found in the current scope.

  ```cpp
  int main()
  {
      int num = 100;
      {
          int num = -45;
          cout << num << endl;
      }
  }
  //-45
  ```

- gloabl varibles are preserved between function calls and local varibales are not.

  ```cpp
  int global_num{ 10 };

  void doubler() {
      int local_num{ 10 };
      global_num *= 2;
      local_num *= 2;
      cout << "global num is : " << global_num << " and local num is : " << local_num << endl;

  }

  int main()
  {
      doubler();  //global num is : 20 and local num is : 20
      doubler();  //global num is : 40 and local num is : 20
  }
  ```

- using `static`, we can preserve the values and it must be noted that static variables have block scope.

  ```cpp
  int global_num{ 10 };

  void doubler() {
      static int local_num{ 10 };
      global_num *= 2;
      local_num *= 2;
      cout << "global num is : " << global_num << " and local num is : " << local_num << endl;

  }

  int main()
  {
      doubler();  //global num is : 20 and local num is : 20
      doubler();  //global num is : 40 and local num is : 40
  }
  ```

> - The static keyword in C++ is used to declare variables, functions, and classes. It has different effects depending on the context in which it is used. (to declare variable, function or class)
> - When used to declare a variable, the static keyword tells the compiler that the variable should be allocated in static storage. This means that the variable will exist for the lifetime of the program, even after all the objects have been destroyed. Static variables are initialized only once, when the program starts.

<br>
<br>

# Inline functions

- Function call in C++ occurs as prolog (compiler generated), business logic (our code) and epilog(compiler generated) phases. prolog and epilog will consume some amount of time, If we want to avoid this we can create **inline funcitons**.
- Inline function is a request to the compiler to replace the function call with only the business logic of the function (thus avoiding prolog and epilog)
- Inline functions would enhance execution speed. At the same time it would increase the size of the executable file.

```cpp
//wether a function is inlined by the compiler can be verified in asm file, however at this time I am not sure how to get this done in Visual Studio

inline int add(int a, int b) {
    return a + b;
}
```
