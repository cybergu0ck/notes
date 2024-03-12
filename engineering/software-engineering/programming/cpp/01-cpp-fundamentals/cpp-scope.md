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

<br>

### Class Scope

Class scope is the scope within the class.

- Member variables, member functions, and nested classes within a class have class scope.
- Class scope also applies to static data members and static member functions of a class.

<br>

### Namespace Scope

Names declared within a namespace have namespace scope.

- Namespaces provide a way to organize code into logical groups and avoid naming conflicts.
- variables with namespace scope are accessible using the scope resolution operator `::`.

<br>
<br>

## Name Resolution

The name is first searched inside the scope, it starts searching outer scopes only if it is not found in the current scope.

```cpp
int main(){
    int num = 100;
    {
        int num = -45;
        cout << num << endl;
    }
}
//-45
```

<br>
<br>

## Automatic Object Destruction

//TODO - Review this notes and update it if needed

- When the scope of the variable ends the memory allocated for that variable is released automatically. This memory is typically managed using the stack.The variable's value becomes undefined once its scope ends, and accessing it after its scope ends leads to undefined behavior.

- When a pointer variable's scope ends, only the pointer itself (i.e., the memory allocated for the pointer variable) is released.
  - The memory it points to, if allocated on the stack will be automatically released by the stack when it goes out of scope.
  - The memory it points to, if dynamically allocated will not be automatically released unless explicitly freed using `delete`.

<br>
<br>

## References

- Checkout [static](./09-storage-class-specifiers.md#static-specifier) keyword
