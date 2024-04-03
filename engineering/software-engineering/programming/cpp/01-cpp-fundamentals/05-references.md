# Lvalue Reference

_An lvalue reference defines an alternative name (Alias) for an object._


<br>
<br>

## Basics of Lvalue Reference


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

- const lvalue references can bind to xvalues, This is because of [temporary materialisation conversion](#temporary-materialisation-conversion) but never to a prvalue. 


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

- Once an lvalue reference is bound to an lvalue or xvalue, they cannot be binded to any other. Hence they must be initialised when they are created! 
  ```cpp
  int main()
  {
      int a{ 10 };    
      int b{ 50 };    
      int& lref {a} ; 
      lref = b;	      //assigns a with the value of b
  }
  ```

<br>
<br>

## Const Correctness with Lvalue References


- lvalue references to constant lvalues must be const references.
  ```cpp
  int main()
  {
    const int num{ 100 };
    const int &ref = num; //Or int const &ref = num; both are same
  }
  ```

- const lvalue references can bind to non-const lvalues.

  ```cpp
  int main()
  {
    int num{ 100 };
    const int &ref = num;
  }
  ```

<br>
<br>

## Lvalue References as Function Arguments

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
    number *= 2;	//here
  }

  int main()
  {
    int num{ 100 };
    doubler(num);  //error: expression must be a modifiable lvalue
    std::cout << num; 
  }
  ```


<br>
<br>

## Lvalue References as Return Type

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

### Temporary Materialisation Conversion (move this to lvalue and rvalue notes)


```cpp
#include <iostream>
using namespace std;

void foo(const int& num)
 {
    cout << "The value of parameter num = " << num << " and address is " << &num << endl;
 }

int main()
{
  int& ref = 10; //error: initial value of reference to non-const must be an lvalue; 10 is a prvalue
  int const &  ref1 = 100;  //Because of temporary materialisation conversion; prvalue is converted to an xvalue;
  foo(10); //now 10 is an xvalue
}
```


<br>
<br>
<br>

# Rvalue Reference (Complete this)

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






