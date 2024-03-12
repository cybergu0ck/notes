# Scope

_**Scope** is the region in the program where a name is visible._

<br>
<br>

## Type of Scopes

<br>

### Global Scope

Global scope is the outer most scope in a program.

- Variables declared in this scope are visible to all other scopes in the program.
- Variables declared in this scope have the lifetime of the executable.

- When working on a multi-file codebase in C++, the variables declared outside classes and functions are visible in that translational unit only. To access them from other translational units, [`extern`](./09-storage-class-specifiers.md#extern-specifier) must be used.

<br>

### Block Scope

Block scope is the local scope of a block of code.

- Variables declared in this scope are visible only within that block.
- Variables declared in this scope have the lifetime of the block. They are automatically destroyed when the block exits.
- function blocks, conditional blocks and simple blocks are all block scopes.

<br>

### Class Scope

<br>

### Namespace Scope

<br>
<br>

## Misc

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

## Automatic Object Destruction

- When the scope of the variable ends the memory allocated for that variable is released automatically. This memory is typically managed using the stack.The variable's value becomes undefined once its scope ends, and accessing it after its scope ends leads to undefined behavior.

- When a pointer variable's scope ends, only the pointer itself (i.e., the memory allocated for the pointer variable) is released.
  - The memory it points to, if allocated on the stack will be automatically released by the stack when it goes out of scope.
  - The memory it points to, if dynamically allocated will not be automatically released unless explicitly freed using `delete`.
