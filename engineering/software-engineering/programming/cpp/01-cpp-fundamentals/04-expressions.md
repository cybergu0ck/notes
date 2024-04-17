# Expressions

_An expression is a composition of operands and operators and yields a result when evaluated._

- Examples:

  - literals are expressions as they are values.

    ```cpp
    char letter = 'x';  //x is an expression
    ```

  - variables are expressions.
  - arithmetic operations (1.2 + 2)
  - relational opertions (a > b)

- A C++ expression can either be a **lvalue** or a **xvalue** or a **prvalue**.

  ![img](../_assets/expressions1.png)

<br>
<br>

## glvalue

*A glvalue is an expression whose evaluation determines the identity of an object or function*

- glvalue refers to “generalized lvalue".
- gvalue occupy data storage.

<br>
<br>

## rvalue

*An rvalue is essentially an expression that can be moved in memory.*

<br>
<br>

## lvalue

_An lvalue is an expression not nearing it's end of lifetime and whose evaluation determines the identity of an object or function._

- It is common to define lvalue as *An lvalue is a glvalue that is not an xvalue.*
- lvalue is a glvalue but not a rvalue. Hence,
  - lvalues can be accessed in memory.
  - lvalues cannot be moved in memory.
- lvalues can be modifiable or non-modifiable.
- Examples of lvalues include variables, references, and dereferenced pointers.

  ```cpp
  int main()
  {
      int num = 100; //num is a lvalue
      int *ptr = &num; 
      *ptr = 200; //referenced pointer is a lvalue
      int &ref = num; //ref is a lvalue
  }
  ```

- Historically, lvalues could be present on the left hand side of the assignment operation. Technically,  Modifiable lvalues can appear on the left hand side of the assignment operator.

  ```cpp
  int main()
  {
	int num{ 100 };
	num = 200; //num is a modifiable lvalue
  }
  ```

  ```cpp
  int foo()
  {	
    int random_number = 69; //assume this is generated reandomly
    return random_number;
  }

  int goo()
  {
    return 1;
  }

  int main()
  { 
      const int num{ 100 };
      num = 200; //error: expression must be modifiable lvalue
      foo = goo;  //error: expression must be modifiable lvalue
  }
  ```

- lvalue can be used in a context where an rvalue is expected. The process called "lvalue to rvalue conversion" takes place.

  ```cpp
  int main()
  {
    int num{ 100 };
    int another = num;  //num is an lvalue and can be used on the right hand side
  }
  ```

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


## prvalue

_An prvalue is an expression whose evaluation doesnt determine the identity of an object or function and whose resources can be reused._

- prvalues refers "pure rvalue".
- prvalue is a rvalue and not a glvalue. Hence,
  - prvalue cannot be accessed in memory.
  - prvalue can be moved in memory.
- prvalues cannot be present on the left hand side of an assignment.
- Examples of prvalues are literals.
- post
- A function call or an overloaded operator expression, whose return type is non-reference is a prvalue. 

  ```cpp
  #include <iostream>

  int doesNothing()
  {	
    return 96;;
  }

  int main()
  {
    int res = std::move(doesNothing()); //doesNothing() is a prvalue
  } 
  ```

- A function call whose return type is a pointer is a prvalue as it is non-reference.

  ```cpp
  #include <iostream>

  int special{ 100 };

  int* getSpecial()
  {	
    return &special;
  }

  int main()
  {
    getSpecial() = 10; //Error: expression must be modifiable lvalue; getSpecial() is a prvalue
    *getSpecial() = 10; //Valid as derefencing a non-const pointer is a modifiable lvalue
  } 
  ```

<br>
<br>

## xvalue

_An xvalue is an expression nearing it's end of lifetime, whose evaluation determines the identity of an object or function and whose resources can be reused._

- xvalue refers to "expiring value".
- xvalue is both glvalue and rvalue. Hence,
  - xvalue can be accessed in memory.
  - xvalue can be moved in memory.

<br>
<br>

### Temporary Materialisation Conversion 

A prvalue of any complete type T can be converted to an xvalue of the same type T. This conversion initializes a temporary object of type T from the prvalue by evaluating the prvalue with the temporary object as its result object, and produces an xvalue denoting the temporary object.

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

# Statements

- A statement is a complete line of code that performs some action.
- statements are usually terminated with a semicolon and usually contain expressions.



<br>
<br>

## References

- The left hand side of an assignment operator must be a modifiable lvalue.