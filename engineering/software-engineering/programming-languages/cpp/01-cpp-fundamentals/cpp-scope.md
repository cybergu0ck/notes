# Scope

_**Scope** is the region in the program where a name is visible._

- There are 3 types of scopes in C++:

    <ol type="1">
        <li><strong>Global scope:</strong> This is the outermost scope in a program. Variables declared in the global scope are visible to all other scopes in the program.</li>
        <li><strong>Function scope:</strong> This is the scope of a function. Variables declared within a function are only visible within that function.</li>
        <li><strong>Block scope:</strong> This is the scope of a block of code ({//block}). Variables declared within a block of code are only visible within that block of code.
    - function parameters have block scope.</li>

    </ol>

<br>

- with nested blocks inner blocks can 'see' but outer blocks cannot 'see'.

  ```cpp
  int main()
  {
      int num = 100;
      {
          int inner_num = -45;
      }
      cout << inner_num << endl;  //error
  }
  ```

- the name is first searched inside the scope, it starts searching outer scopes only if it is not found in the current scope.

  ```cpp
  int main()
  {
      int num = 100;
      {
          int num = -45;
          cout << num << endl;
      }
  }
  //-45
  ```

- gloabl varibles are preserved between function calls and local varibales are not.

  ```cpp
  int global_num{ 10 };

  void doubler() {
      int local_num{ 10 };
      global_num *= 2;
      local_num *= 2;
      cout << "global num is : " << global_num << " and local num is : " << local_num << endl;

  }

  int main()
  {
      doubler();  //global num is : 20 and local num is : 20
      doubler();  //global num is : 40 and local num is : 20
  }
  ```

- using `static`, we can preserve the values and it must be noted that static variables have block scope.

  ```cpp
  int global_num{ 10 };

  void doubler() {
      static int local_num{ 10 };
      global_num *= 2;
      local_num *= 2;
      cout << "global num is : " << global_num << " and local num is : " << local_num << endl;

  }

  int main()
  {
      doubler();  //global num is : 20 and local num is : 20
      doubler();  //global num is : 40 and local num is : 40
  }
  ```

> - The static keyword in C++ is used to declare variables, functions, and classes. It has different effects depending on the context in which it is used. (to declare variable, function or class)
> - When used to declare a variable, the static keyword tells the compiler that the variable should be allocated in static storage. This means that the variable will exist for the lifetime of the program, even after all the objects have been destroyed. Static variables are initialized only once, when the program starts.

<br>
<br>
