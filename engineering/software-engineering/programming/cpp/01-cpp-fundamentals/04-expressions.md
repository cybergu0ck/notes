# Expressions

_An expression is composed of one or more operands and yields a result when it is evaluated._

- Examples:

  - literals are expressions as they are values.

    ```cpp
    char letter = 'x';  //x is an expression
    ```

  - variables are expressions.

  - arithmetic operations (1.2 + 2)
  - relational opertions (a > b)
  - assignments (a = b)

- A C++ expression can either be a **lvalue** or a **xvalue** or a **prvalue**.

  ![img](../_assets/expressions1.png)

<br>
<br>

## lvalue

_An lvalue refers to an expression that yields an object or a function._

- When objects are used as lvalue, the object's identity (it's location in memory) is being used.
- lvalues are addressable and modifiable/assignable.
- lvalues can appear on the left-hand side of an assignment operator (=) because they represent addressable objects.
- Examples of lvalues include variables, non-const references, and dereferenced pointers.

  ```cpp
  int main()
  {
      int num;
      num = 100; //num is a lvalue
  }
  ```

- lvalue can be used in a context where an rvalue is expected.

  ```cpp
  int main() {
      int x = 5;
      int y = 10;

      int z = x + y; // Here, x and y are lvalues, but the expression expects rvalues

      int& ref = x;
      cout << "Value of ref: " << ref << endl; // Here, ref is an lvalue, but cout expects an rvalue

      return 0;
  }
  ```

<br>
<br>

## rvalue

An rvalue refers to an expression that produces a temporary or intermediate value.

- When objects are used as rvalue, the object's value (it's contents) is being used.
- Anything that is not a lvalue is a rvalue.
- rvalues are not addressable and non-modifiable/non-assignable.
- rvalues can appear on the right-hand side of an assignment operator and cannot be assigned a new value directly.
- Examples of rvalues include literals (e.g., 5, "hello"), temporary objects, and the results of computations.

- rvalues cannot be used in the context where lvalues are required.

  ```cpp
  #include <iostream>

  int main() {
      int* ptr2 = &5; // Error: Cannot take the address of an rvalue
      return 0;
  }
  ```

<br>
<br>

<br>
<br>
<br>

# Statements

- A statement is a complete line of code that performs some action.
- statements are usually terminated with a semicolon and usually contain expressions.

* ## Examples:
