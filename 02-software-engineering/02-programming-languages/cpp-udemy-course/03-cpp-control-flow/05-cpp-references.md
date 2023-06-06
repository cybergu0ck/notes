# References

- A reference in C++ is a special type of variable that cannot be assigned a new value. It can only refer to an existing object.
- References are declared using the & symbol.
- Reference cannot be null.

<br>
<br>

# References as Alias

- Reference can an alias for a variable.
  ```cpp
  int main()
  {
      int num{ 10 };
      int& my_num{ num };
      my_num = 100;
      cout << num << endl;  //100
  }
  ```

<br>
<br>

# Reference to avoid copying objects

- References are typically used to avoid copying objects. For example, if you have a function that takes an object as a parameter, you can use a reference to avoid copying the object. This can improve performance, especially if the object is large.
- In a range based for loop, the variable is a copy of the orginal iterable, hence we get the following reult:

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

- When we use references (see inside range based for loop)

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
<br>

# l-value

- An l-value is an object that occupies location in memory and is addressable.
- objects are addressable when they can be used on the left hand side of an assignment statement.

  ```cpp
  int main()
  {
      int num;
      num = 100; //num is a lvalue
  }
  ```

<br>
<br>

# r-value

- Anything that is not an lvalue is an rvalue, hence rvalues are non addressable and non assignable.
- Usually,

  - rvalues are on the right hand side of the assignment
  - literals are rvalues
  - ravlues can be temporary variables(inteneded to be non modifiable)

<br>

- rvalues can be assigned to lvalues explicitely

  ```cpp
  int main()
  {
      int x{ 1 }, y{ 0 };
      y = 100; // a temporary varible (r value) having a value 100 is assigned to y
      x = x + y;  // a temporary varible (r value) having the value x+y is assigned to x
  }
  ```

<br>
<br>

# references as l-value

- Concept clarity for l value references:

  ```cpp
  int main()
  {
    int a{10};       // a is a l value
    int b{20};       // b is a l value

    int& lref = a;   // lref is an l value reference
    int& lref = 10;  // error: 10 is an r value and cannot be used to define l value reference

    lref = b;        // valid: a has the value of b i.e. 20
    lref = 200;      // valid: a is now 200


    cout << lref << endl;   //200
    cout << a << endl;      //200
    cout << b << endl;      //20
    cout << &lref << endl; //006BFBAC
  }
  ```

- The same concept applies to functions with l value reference parameters

  ```cpp
  #include <iostream>
  using namespace std;

  void foo(int& num)
  {
      cout << num << endl;     //10
      cout << &num << endl;    //00B5FB30
  }

  int main()
  {
      int x{ 10 };
      foo(x);
      foo(10);	//error: 100 is a rvalue
  }
  ```

<br>
<br>

# references as r value

- Concept clarity for r value references:

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
