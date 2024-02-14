# References

<br>

## lvalue

- An lvalue refers to an expression that identifies a specific object or variable in memory.
- Hence, lvalues are addressable and modifiable/assignable.
- lvalues can appear on the left-hand side of an assignment operator (=) because they represent addressable objects.
- Examples of lvalues include variables, non-const references, and dereferenced pointers.

  ```cpp
  int main()
  {
      int num;
      num = 100; //num is a lvalue
  }
  ```

<br>
<br>

## rvalue

- An rvalue refers to an expression that produces a temporary or intermediate value. (Anything that is not a lvalue is a rvalue)
- Hence, rvalues are not addressable and non-modifiable/non-assignable.
- rvalues can appear on the right-hand side of an assignment operator but cannot be assigned a new value directly.
- Examples of rvalues include literals (e.g., 5, "hello"), temporary objects, and the results of computations.

<br>

- rvalues can be assigned to lvalues explicitely

  ```cpp
  int main()
  {
      int x{ 1 }, y{ 0 };
      y = 100; // a temporary variable (r value) having a value 100 is assigned to y
      x = x + y;  // a temporary variable (r value) having the value x+y is assigned to x
  }
  ```

<br>
<br>

## lvalue reference (&)

- Introduced in earlier versions of C++.
- Binds to lvalues (addressable objects or storage locations).
- Can extend the lifetime of the object it refers to.
- Used for aliasing.

  ```cpp
  #include <iostream>
  int main()
  {
      int a{ 10 };     // a is a lvalue
      int& lref {a};   // lref is an lvalue reference
      lref = 200;      // valid: a is now 200

      std::cout << lref << std::endl;   //200
      std::cout << a << std::endl;      //200
      std::cout << &lref << std::endl; //006BFBAC
      std::cout << &a << std::endl;	//006BFBAC
  }
  ```

* Once a reference is bound to a variable, it cannot be binded to a new variable.

  ```cpp
  int main()
  {
      int a{ 10 };     // a is a lvalue
      int b{ 50 };     // a is a lvalue
      int& lref {a} ;   // lref is an lvalue reference
      lref = b;	     //assigns a with the value of b

      std::cout << lref << std::endl;   //50
      std::cout << a << std::endl;      //50
      std::cout << &lref << std::endl; //006BFBAC
      std::cout << &a << std::endl;	//006BFBAC
  }
  ```

* Used to pass by reference and avoid copying of objects for every function call.

  ```cpp
  #include <iostream>
  using namespace std;

  void foo(int& num)
  {
      cout << "The value of parameter num = " << num << " and address is " << &num << endl;
  }

  int main()
  {
      int x{ 10 };
      cout << "The value of argument x = " << x << " and address is " << &x << endl;
      foo(x);
      foo(10);	//error: 100 is a rvalue
  }

  //The value of argument x = 10 and address is 000000494751F5F4
  //The value of parameter num = 10 and address is 000000494751F5F4
  ```

- In a range based for loop, the variable is a copy of the orginal iterable, hence we get the following result:

  ```cpp
  int main()
  {
      vector<string> stooges{ "larry", "moe","curly" };

      for (auto name : stooges) {
          name = "funny";
      }

      for (auto name : stooges) {
          cout << name << endl;
      }
  }

  //larry
  //moe
  //curly
  ```

- When we use lvalue references (see inside range based for loop)

  ```cpp
  int main()
  {
      vector<string> stooges{ "larry", "moe","curly" };

      for (auto &name : stooges) {
          name = "funny";
      }

      for (auto name : stooges) {
          cout << name << endl;
      }
  }
  //funny
  //funny
  //funny
  ```

<br>

### const correctness with lvalue references

- a lvalue reference to a const datatype must also be const.

  ```cpp
  int main()
  {
      const int a{ 10 };
      int& ref1{ a };        //error
      const int& ref2{ a };  //ok
  }
  ```

<br>
<br>

## rvalue reference (&&)

- Introduced in C++11 and later.
- Binds to rvalues (temporary values or expressions without persistent memory locations).
- Typically used to enable move semantics and perfect forwarding.
- Used for efficient resource transfer and optimization.

  ```cpp
  int main()
  {
      int a{ 10 };            // a is a l value
      int b{ 20 };            // b is a l value

      int&& rref = 50;        // rref is an r value reference
      int&& rref2 = a;        // error, a is a l value and connot be used to define r value reference!

      rref = b;               // rref now stores the value of b i.e. 20
      rref = 60;              // rref now stores 60

      cout << rref << endl;   // 60
      cout << a << endl;      // 10
      cout << b << endl;      // 20
      cout << &rref << endl;  // 0060FD0C
  }
  ```

- The same concept applies to functions with r value reference parameters

  ```cpp
  #include <iostream>
  using namespace std;

  void foo(int&& para)
  {
      cout << para << endl;     //10
      cout << &para << endl;    //0039FD88
      cout << &&para << endl;   //error
  }


  int main()
  {
      int x{ 10 };
      foo(x);     //error: x is a l value
      foo(10);	//valid
  }
  ```

<br>
<br>

## lvalue and rvalue with functions

### Function returning rvalue

- When a function returns by value (i.e., not a reference), the return value is treated as an rvalue.
- The returned rvalue can be used in expressions but cannot be directly modified.

  ```cpp
  #include <iostream>

  int num{ 5 };

  int indirect()
  {
    return num;
  }

  int main()
  {
    num = indirect() + 10; //can be used in expressions
    std::cout << num << std::endl;

    //indirect() = 10; //error, rvalue cannot be assigned


    //The following code can be used to check if something is lvalue or rvalue (However this is from GPT3)
    if (std::is_lvalue_reference<decltype(indirect())>::value) {
      std::cout << "The returned type is an lvalue\n";
    }
    else {
      std::cout << "The returned type is is an rvalue\n";
    }
  }

  //15
  //The returned type is is an rvalue
  ```

* A function with return type of a pointer (to a data type) is returned as rvalue.

  ```cpp
  #include <iostream>

  int num{ 5 };
  int another{ 20 };

  int* indirect()
  {
      return &num;
  }

  int main()
  {
      //indirect() = &another; //error, indirect() returns pointer as rvalue
      *indirect() = 10; //dereferencing the pointer gives lvalue
      std::cout << num <<std::endl;


      //The following code can be used to check if something is lvalue or rvalue (However this is from GPT3)
      if (std::is_lvalue_reference<decltype(indirect())>::value) {
          std::cout << "The returned type is an lvalue\n";
      }
      else {
          std::cout << "The returned type is an rvalue\n";
      }
  }

  //10
  //The returned type is an rvalue
  ```

<br>

### Function returning lvalue

- Functions with return type with reference returns lvalue.
- Returning an lvalue reference from a function allows the caller to use the returned value as an lvalue and potentially modify it.

  ```cpp
  #include <iostream>

  int num{ 5 };

  int& indirect()
  {
    return num;
  }

  int main()
  {
    indirect() = 10;    //here
    std::cout << num << std::endl;

      //The following code can be used to check if something is lvalue or rvalue (However this is from GPT3)
      if (std::is_lvalue_reference<decltype(indirect())>::value) {
          std::cout << "The returned type is an lvalue\n";
      }
      else {
          std::cout << "The returned type is an rvalue\n";
      }
  }

  //10
  //The returned type is an lvalue
  ```
