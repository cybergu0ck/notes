# Operator Overloading

- Operator overloading is a feature in C++ that allows programmers to redefine the meaning of operators for user-defined data types. This can make code more concise and readable, and can also improve the flexibility and expressiveness of a program.
- The following operators cannot be overloaded

  | Operator             | Symbol |
  | -------------------- | ------ |
  | Scope Resolution     | ::     |
  | Conditional Operator | :?     |
  | pointer to a member  | .\*    |
  | dot operator         | .      |
  | Size Of              | sizeof |

* Basic rules while overloading operators

  - precedence and associativity of operators cannot be changed.
  - 'arity' cannot be changed (ex: unary operators cannot be made binary)
  - cannot overload operators for primitive type (ex: int, double, etc)
  - cannot create new operators
  - [], (), ->, and the assignment operator must be declared as member methods while other operators can be declared as member or global methods.

<br>
<br>

# Assignment Operator Overloading

- overloaded assignment operator is called whenever an object is assigned to another object, If an overloaded assignment operator is not defined, then the compiler will generate one and perform member wise copy.

  ```cpp
  #include <iostream>

  class MyClass
  {
  private:
      int a;

  public:
      MyClass(int x = 2): a{x}{}
      MyClass& operator=(MyClass& x);		//overloaded assignment operator declaration

      void modify()
      {
          a = 10;
      }

      void print_a()
      {
          std::cout << "data attribute a = " << a << std::endl;
      }
  };

  MyClass& MyClass::operator=(MyClass& x)
  {
      std::cout << "overloaded assignment operator called" << std::endl;
      this->a = x.a;
      return *this;
  }

  int main()
  {

      MyClass obj1;
      //MyClass obj2 = obj1;  //This is not assignment, It is equivalent to MyClass obj2{obj1}
      MyClass obj2;
      obj1.modify();
      obj2 = obj1;		// obj2.operator=(obj1)
      obj2.print_a();
  }

  //overloaded assignment operator called
  //data attribute a = 10
  ```

<br>
<br>

# Stream Operator Overloading
