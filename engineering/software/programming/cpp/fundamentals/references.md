# References

<br>
<br>
<br>

## Lvalue Reference

_An lvalue reference defines an alternative name (Alias) for an object._

<br>
<br>

### Basics of Lvalue Reference

- What C++03 calls reference is lvalue reference in Modern C++.
- lvalue refernces can bind to lvalues, once binded they act as aliases.

  ```cpp
  int main()
  {
    int num{ 100 };
    int&  ref = num; //num is a lvalue
    ref = 50; //assigns 50 to num
    std::cout << num << std::endl;   //50
    std::cout << ref << std::endl;   //50
    std::cout << &num << std::endl;	//006BFBAC
    std::cout << &ref << std::endl; //006BFBAC
  }
  ```

- lvalues references are not objects!

  ```cpp
  int main()
  {
    int num{ 100 };
    int&  ref = num; //num is a lvalue
    std::cout << &num << std::endl;	//006BFBAC
    std::cout << &ref << std::endl; //006BFBAC //Here &ref simply means &num
  }
  ```

- Once an lvalue reference is bound, they cannot be binded again. Hence they must be initialised when they are created!

  ```cpp
  int main()
  {
      int a{ 10 };
      int b{ 50 };
      int& lref {a} ;
      lref = b;	      //assigns a with the value of b
  }
  ```

- The type of the lvalue reference must match the type of the object to which it refers. Except for two exceptions:

  1. We can bind a lvalue reference to a prvalue using the const qualifier because of [temporary materialisation conversion](./07-expressions.md#temporary-materialisation-conversion-move-this-to-lvalue-and-rvalue-notes).

     ```cpp
     int main()
     {
         int num{ 100 };
         const int& ref1 = 69; //ok because of temporary materialisation conversion
         int& ref2 = 42; //Error: Initial value of reference to non const must be lvalue
         int& ref3 = num * 2; //Error: Initial value of reference to non const must be lvalue
     }
     ```

  1. We can bind a lvalue refernce to a Child class using the type of Base class in the case of inheritance.

<br>
<br>

### Const Correctness with Lvalue References

<br>

#### Reference to const

- Although there is no concept of "constant reference" as reference is not an object, it is commonly okay to refer to "reference to const" as "constant reference".

- lvalue references to constant lvalues must be refernance to const.

  ```cpp
  int main()
  {
    const int num{ 100 };
    const int &ref = num; //Or int const &ref = num; both are same
  }
  ```

- A reference to const cannot be used to bind a non-const one.

  ```cpp
  #include <iostream>

  int main()
  {
    const int num{ 100 };
    const int& ref = num;
    int& ano_ref = ref; //error: binding a reference of type "int &" to an initializer of type "const int"
  }
  ```

- reference to const can bind to non-const lvalues. Hence, binding a reference to const to an object says nothing about whether the underlying object itself is const.

  ```cpp
  int main()
  {
    int num{ 100 };
    const int &ref = num;
    num = 200; //ok
    ref = 98; //error
  }
  ```

<br>
<br>

### Lvalue References as Function Arguments

- A non const lvalue reference parameter is used to pass the argument by reference instead of pass by value and the argument is modifiable.

  ```cpp
  #include <iostream>

  void doubler(int & number)
  {
    number *= 2;
  }

  int main()
  {
    int num{ 100 };
    doubler(num);
    std::cout << num; //200
  }
  ```

- A const lvalue reference parameter is used to pass the argument by reference instead of pass by value and the argument is non-modifiable.

  ```cpp
  #include <iostream>

  void doubler(const int & number)
  {
    number *= 2;	//error: expression must be a modifiable lvalue
  }

  int main()
  {
    int num{ 100 };
    doubler(num);  //Passing a non const variable is not an error
    std::cout << num;
  }
  ```

<br>
<br>

### Lvalue References as Return Type

- Function returning an non-const lvalue reference returns a modifiable lvalue.

  ```cpp
  #include <iostream>

  int& doesNothing(int& number)
  {
    return number;
  }

  int main()
  {
    int num{ 100 };
    doesNothing(num) = 200; //doesNothing() is a modifiable lvalue
    std::cout << num << "\n";	//200
  }
  ```

<br>
<br>
<br>

## Rvalue Reference

- Introduced in C++11.
- Binds to rvalues (temporary values or expressions without persistent memory locations).
- Used to enable move semantics, perfect forwarding, efficient resource transfer and optimization.

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
