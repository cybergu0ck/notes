### Operator Overloading

- Operator overloading is a feature in C++ that allows programmers to redefine the meaning of operators for user-defined data types. This can make code more concise and readable, and can also improve the flexibility and expressiveness of a program.
- The following operators cannot be overloaded

  | Operator             | Symbol |
  | -------------------- | ------ |
  | Scope Resolution     | ::     |
  | Conditional Operator | ?:     |
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

#### Assignment Operator Overloading

- Note that copy elision doesn't apply for assignments and is pertinant to constructions. As such, it is typically not possible to implicitely eliminate copy or move assignments and hence can be critical for performance.

<!-- //TODO - Link to copy elision notes -->

<br>

#### Copy Assignment

Checkout [rule of five](../polymorphism/rule-of-five.md#copy-assignment)

<br>

#### Move Assignment

Checkout [rule of five](../polymorphism/rule-of-five.md#move-assignment)

<br>

#### Stream Operator Overloading

- cin s a global object of istream class and >> opertaor is a member function of istream class. (similarly cout and ostream). As such we cannot try to overload them in their class (becuase it is a standard library). We cannot overload them within our class because by doing so, the cin and cout objects (belonging to their respective classes) cannot call the member functions of our class. Hence we do it globally and use `friend`.

  ```cpp
  #include <iostream>

  class MyClass
  {
      int a;
      friend std::istream& operator>>(std::istream& input, MyClass& obj); //if this is not done, then this function won't have access to 'a'.
      friend std::ostream& operator<<(std::ostream& output, MyClass& obj);
  };


  std::istream& operator>>(std::istream & input, MyClass & obj)
  {
      std::cout << "Enter a number for data attribute a" << std::endl;
      input >> obj.a;
      return input;
  }

  std::ostream& operator<<(std::ostream& output, MyClass& obj)
  {
      output << obj.a;
      return output;
  }


  int main()
  {
      MyClass obj1;
      std::cin >> obj1;
      std::cout << "The value of obj1.a is " << obj1;

  }

  //Enter a number for data attribute a
  //12
  //The value of obj1.a is 12
  ```

<br>

#### Unary Operator Overloading

<!-- //REVIEW - Needs Review -->

- Unary operator can have prefix notation and postfix notation, we can faciliate both in unary operator overloading.

  ```cpp
  #include <iostream>

  class MyClass
  {
  private:
      int a;

  public:
      MyClass(int x = 2) : a{ x } {}
      MyClass& operator++();		//prefix implementation
      MyClass operator++(int);    //postfix implementation
      int get_a()
      {
          return a;
      }
  };

  MyClass& MyClass::operator++()  //return by reference
  {
      ++a;
      return *this;
  }



  MyClass MyClass::operator++(int)   //return by value as the object being returned is local object
  {
      MyClass temp{ *this };
      this->a++;
      return temp;
  }

  int main()
  {
      MyClass obj1;
      MyClass res1;
      res1 = ++obj1;
      std::cout << "-----prefix example-----" << std::endl;
      std::cout << "The value of obj1 after prefix increment is " << obj1.get_a() << std::endl;
      std::cout << "The value of res1 after prefix increment is " << res1.get_a() << std::endl;
      std::cout << "\n";
      std::cout << "-----postfix example-----" << std::endl;
      MyClass obj2;
      MyClass res2;
      res2 = obj2++;
      std::cout << "The value of obj2 after prefix increment is " << obj2.get_a() << std::endl;
      std::cout << "The value of res2 after prefix increment is " << res2.get_a() << std::endl;

  }

  //---- - prefix example---- -
  //The value of obj1 after prefix increment is 3
  //The value of res1 after prefix increment is 3
  //
  //---- - postfix example---- -
  //The value of obj2 after prefix increment is 3
  //The value of res2 after prefix increment is 2
  ```

<br>

#### Arrow Assignment Overloading

<!-- //REVIEW - Needs Review -->

- Find a good case for using this (I don't think the following code is a good use case), However checkout arrow operator overloading in PIMPL model.

  ```cpp
  #include <iostream>

  class MyClass
  {
  private:
      int a;

  public:
      MyClass(int x = 2) : a{ x } {}
      MyClass* operator->();		//overloaded arrow operator declaration

      void print_a()
      {
          std::cout << "data attribute a = " << a << std::endl;
      }
  };

  MyClass* MyClass::operator->()
  {
      return this;
  }


  int main()
  {
      //allocate an array of MyClass objects on the heap
      MyClass* arr = new MyClass[5];

      arr[0].print_a();   //arr[0] is a MyClass object hence we need not use ->

      //If we wanted to use ->, for code readability we must provide an overloaded operator
      arr[1]->print_a();  //Here arr[1] is a MyClass object
  }

  //data attribute a = 2
  //data attribute a = 2
  ```

<br>
<br>
<br>
