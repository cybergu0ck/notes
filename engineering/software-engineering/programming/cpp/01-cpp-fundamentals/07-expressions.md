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


## glvalue

*A glvalue is an expression whose evaluation determines the identity of an object or function*

- glvalue refers to “generalized” lvalue.

<br>
<br>

## rvalue


*rvalue is an expression that is either a prvalue or a xvalue.*

<br>
<br>


## lvalue

*An lvalue is a glvalue that is not an xvalue.*

- lvalues are addressable.
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

<br>
<br>




## prvalue

*A prvalue is an expression that doesnt occupy data storage. Another way to define it is a value that is not associated with an object.*

- prvalues means "pure rvalue".
- prvalues are not addressable and non modifiable.
- prvalues cannot be present on the left hand side of an assignment.
- Examples of prvalues are literals, The result of calling a function whose return type is not a reference. 

  ```cpp
  int foo()
  {	
    int random_number = 69; //assume this is generated reandomly
    return random_number;
  }

  //foo() is a prvalue
  ```

<br>
<br>


## xvalue

A xvalue is a temporary expression that does occupy data storage.



<br>
<br>

### Left Hand Side of an assignment operator


### Return types (Complete this)

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

# Statements

- A statement is a complete line of code that performs some action.
- statements are usually terminated with a semicolon and usually contain expressions.

* ## Examples:
