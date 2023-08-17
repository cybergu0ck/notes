# Lambdas

Lambdas in C++ are a way to define anonymous functions inline, often used for short, one-off functions that don't need to be named separately.

- The basic structure of a lambda expression is

  ```
  []()-> return_type specifiers {};
  ```

  - [] is the capture list
  - () is the parameter list
  - `-> return_type` can be skipped if the return type is void, More over the compiler will mostly deduce the return type.

* Calling lambda

  ```cpp
  #include <iostream>

  int main() {
      []() {std::cout << "Hello"; }();	//A function object is instantiated and called.
  }

  //Hello
  ```

  ```cpp
  #include <iostream>

  int main() {
      auto l = []() {std::cout << "Hello"; };	//Creating a lambda
      l();	//calling the lambda
  }

  //Hello
  ```

* References can also be passed as parameters in lambda functions.

  ```cpp
  #include <iostream>

  int main() {
      int num{ 10 };
      std::cout << num << std::endl;
      auto l = [](int& x) {x = x*x; };
      l(num);
      std::cout << num << std::endl;	//We can see that the original parameters are modified!
  }

  //10
  //100
  ```

* Pointers can also be used in lambda parameters.

  ```cpp
  #include <iostream>

  int main() {
      int num{ 10 };
      auto l = [](int* ptr) { *ptr = 100; };
      l(&num);
      std::cout << num << std::endl; //100
  }
  ```

<br>
<br>
<br>

# Stateless lambda

A "stateless lambda" refers to a lambda function that does not capture any variables from its surrounding scope.
