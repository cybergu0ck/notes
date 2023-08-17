# Lambdas

Lambdas in C++ are a way to define anonymous functions inline, often used for short, one-off functions that don't need to be named separately.

- The basic structure of a lambda expression is

  ```
  []()-> return_type specifiers {};
  ```

  - [] is the capture list
  - () is the parameter list
  - `-> return_type` can be skipped if the return type is void, More over the compiler will mostly deduce the return type.

<br>
<br>
<br>

# Instatiation and Call

- Instantiating and calling the lambda in place.

  ```cpp
  #include <iostream>
  #include <string>

  int main() {
      []() {std::cout << "Hello"; }();	//lambda with nothing in capture list and no parameters.
      std::cout << std::endl;
      [](std::string text) {std::cout << text << std::endl; }("Hey enzo"); //lambda with nothing in capture list and 1 parameter
  }

  //Hello
  //Hey enzo
  ```

- Storing the lambda function in a variable.

  ```cpp
  #include <iostream>

  int main() {
      auto l = []() {std::cout << "Hello"; };	//Creating a lambda
      l();	//calling the lambda
  }

  //Hello
  ```

<br>
<br>
<br>

# Parameter list

- References can also be passed as parameters in lambda functions.

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

- Pointers can also be used in lambda parameters.

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

# Lambas in functions

- Lambdas themselves can be passed as parameters

  ```cpp
  #include <iostream>
  #include <functional>

  //Supported in C++ 14
  void foo_1(std::function<void(int)> lambda) //Here: "void" is the return type and "int" is the parameter type
  {
    lambda(11);
  }

  //Supported in C++ 14
  void foo_2(void(*lambda)(int)) //Here: "void" is the return type and "int" is the parameter type
  {
    lambda(11);
  }

  //Supported in C++ 20
  void foo_3(auto lambda) {
    lambda(11);
  }

  int main() {
    auto display = [](int x) {std::cout << x << std::endl; };
    foo_1(display);
    foo_2(display);
    foo_3(display);
  }

  //11
  //11
  //11
  ```

- Returning lambdas from functions

  ```cpp
  #include <iostream>
  #include <vector>
  #include <functional>

  #include <iostream>
  #include <functional>

  std::function<void(int)> make_lambda() {
    return [](int x) {std::cout << x; };
  }


  /*
  *
  //legacy
  void (*foo())(int) {
    return [](int x) {std::cout << x; };
  }

  //modern
  auto foo() {
    return [](int x) {std::cout << x; };
  }
  */

  int main() {
    std::function<void(int)> l = make_lambda();
    l(11);
  }

  //11
  ```

<br>
<br>
<br>

# Stateless lambda

A "stateless lambda" refers to a lambda function that does not capture any variables from its surrounding scope.

<br>
<br>
<br>

# Predicate Lambda

- It's a type of lambda function that returns a boolean value based on certain conidtion (generally takes some parameters to perform this calculation).

  ```cpp
  #include <iostream>
  #include <vector>
  #include <functional>

  void filter(std::vector<int> vec, std::function<bool(int)> func) {
    for (auto i : vec) {
      if (func(i)) {
        std::cout << i << std::endl;
      }
    }
  }

  int main() {
    auto l = [](int x) {return x > 10; };
    std::vector my_vec{1, 10, 3, 13, 20};

    std::cout << "values greater than 10 are as follows: " << std::endl;
    filter(my_vec, l);

    std::cout << "values less than 10 are as follows: " << std::endl;

    //defining the lambda inline
    filter(my_vec, [](int x) {return x < 10; });
  }

  //values greater than 10 are as follows :
  //13
  //20
  //values less than 10 are as follows :
  //1
  //3
  ```
