# Pointers

_**Pointers** are variables that store the memory addresses of other variables._

- They have a memory location where they are bound too, they have a value (an adress of a variable) and they have a type (the type of the variable that the pointer points to)

<br>
<br>

## Declaring Pointers

- Pointers are declared as follows:

  ```
  type *pointer_name;
  ```

* Uninitialised pointer contain garbage data and can point anywhere, Hence **always initialise pointers**.

<br>
<br>

## Initialising Pointers

- Initialising a pointer to zero or nullptr (C++11) means the pointer is pointing to nowhere.
- pointers can be initialised as follows:

  ```
  char* ptr1 {};		//null pointer, points to nothing
  int* ptr2{ nullptr }; //null pointer, points to nothing
  int* ptr3{ &num1 };	//pointer to an int, points to num1
  ```

<br>
<br>

## Storing address in pointers

- We can store an address of a varible (make the pointer point to that variable)

  ```cpp
  int main()
  {
      int num = 100;
      int* num_ptr = &num;

      cout << "The address of num is " << &num << endl;  //00BAFC3C
      cout << "num_ptr's value is " << num_ptr << endl;  //00BAFC3C

  }
  ```

- pointer to a pointer

  ```cpp
  int num = 10;
  int * ptr = &num;
  // int * ptr = &ptr  // a value of type int** cannot be used to initialize an entity of type int*
  int ** ptr_ptr = &ptr;
  ```

<br>
<br>

## Accessing Address of the pointer

- pointer's address should not be confused with it's value! pointer's value is the address of the variable that it points to.

* & is the address operator and can be used to get the address of any variable.

  ```cpp
  int main()
  {
      int* p;
      cout << "The address of the pointer p is : " << &p << endl;
  }

  //The address of the pointer p is : 010FF974
  ```

<br>
<br>

## `sizeof` operator on pointers

- sizeof operator, when used on pointers is not referring to the size of what the pointer is pointing to.
- all pointers in a program have the same size (that is the size of the address that they store)

  ```cpp
  int main()
  {
      int num = 10;
      long long bigger_num = 1000;

      int* p1 = &num;
      long long* p2 = &bigger_num;

      cout << sizeof p1 << endl; //4 (means 4 bytes)
      cout << sizeof p2 << endl; //4

  }
  ```

<br>
<br>

## Dereferencing the Pointer

_**Dereferencing** means accessing the data the pointer is pointing to._

- Note that \* is used both in pointer declaration and also in pointer dereferencing! Once a pointer is declared then \* used on that pointer is for dereferencing.

  ```cpp
  int main()
  {
      int num = 100;
      int* num_ptr = &num;
      cout << " num (using pointer deferencing) is " << *num_ptr << endl;
  }

  //num (using pointer deferencing) is 100
  ```

* when \* is used on the left side of the equation, it becomes lvalue (location value). Hence in the below code, \* num_ptr refers to the address of the num_ptr and hence we can modify the data in whatever pointer points to.

  ```cpp
  int main()
  {
      int num = 100;
      int* num_ptr = &num;

      *num_ptr = 200;
      cout << num;  //200
  }
  ```

<br>
<br>

## `const` and pointers

- There are several ways to qualify pointers using `const`.
  1. pointers to constants
  1. constant pointers
  1. constant pointers to constants

<br>

### pointers to constants

- If the pointer is to point to a constant type, then the pointer must be const qualified (this is pointer to constant and not const pointers)
- Here, The data pointed to by the pointers is constant and connot be changed however the pointer itself can change and point to something else.

  ```cpp
  int main()
  {
    const int num1 = 10;
    int num2 = 60;
    const int* ptr{ &num1 };  //pointer to const int
    *ptr = 500; //error
    ptr = &num2;  //ptr now points to num2 (even though num2 is not const qualified)
    cout << *ptr << endl;
  }
  ```

- We can const qualify varibales uisng pointers

  ```cpp
  int main()
  {
    int num1 = 10;
    const int* ptr{ &num1 };  //pointer to const int
    *ptr = 1000; //error
  }
  ```

<br>

### const pointers

- the data pointed to by the pointer can be changed but the pointer itself cannot.

  ```cpp
  int main()
  {
    int num1 = 10;
    int* const ptr{ &num1 }; //const pointer to an int

    ptr = nullptr; //error
  }
  ```

<br>

### constant pointers to constants

- The data pointed to by the pointer as well as the pointer itself cannot change.

  ```cpp
  int main()
  {
    int num1 = 1000;
    const int* const ptr{ &num1 };
    *ptr = 800;   //error
    ptr = nullptr; //error
  }
  ```

<br>
<br>

## Pointers with functions

### Passing pointers to functions (Pass by reference)

- pass by reference can be done by using pointer parameters.
- The function paramter is a pointer.
- the argument can be a pointer or address of a variable.

  ```cpp
  void double_data(int* int_ptr);

  int main()
  {
    int value{ 10 };
    int* ptr{ &value };
    double_data(ptr);  //or double_data(&value);
    cout << value << endl;	//20
  }

  void double_data(int* int_ptr) {
    *int_ptr *= 2; // *int_ptr = *int_ptr * 2;
  }
  ```

<br>
<br>

### Returning a pointer from a function

- The return type of a function can be a pointer.

  ```cpp
  int* largest(int* int_ptr1, int* int_ptr2);

  int main()
  {
    int a{ 100 }, b{ 200 };
    int* ptr_largest = largest(&a, &b);
    cout << *ptr_largest << endl;	//200
  }

  int* largest(int* int_ptr1, int* int_ptr2) {
    if (*int_ptr1 >= *int_ptr2) {
      return int_ptr1;
    }
    else {
      return int_ptr2;
    }
  }
  ```

- Never return pointer to local varibales in a function!

  ```cpp
  vector <int>* never_do(int* int_ptr1, int* int_ptr2) {
    vector <int> local_variable(5);  //vector of size = 5 and all are 0's
    vector <int>* ptr{ &local_variable };
    return ptr;					//NEVER DO THIS
    //return &local_variable	//OR THIS
  }
  ```

<br>
<br>

## Common Pitfalls with pointers

### Uninitialised pointers

- Modern IDE will throw an error and prevent this (which is a good thing)

  ```cpp
  int main()
  {
    int* ptr;   //UNINITIALISED!!
    *ptr = 100;
    cout << *ptr;
  }
  ```

<br>

### Dangling pointers

- dangling pointers are created when a pointer points to a memory that is invalid (or no longer valid)
- When a function returns a pointer to a local varible, it's a dangling pointer.
- When two pointers point to the same data and one of the pointer releases the data with delete, the other pointer now access the released data (can be invalid), resulting in dangling pointers.

<br>

### Not checking if `new` failed

- An exception is thrown if `new` fails to allocate memory on the heap.
- If exceotion handling is not done here, it'll point to nullptr and dereferencing a null ptr can make the program crash.

<br>

### Memory Leaks

- memory leaks occur when we forget to release the allocated heap memory using `delete`.
- it can also occur if we loose the pointer to the allocated heap memory (say reassigning the pointer), now we have no way to access or release that allocated heap memory, which is still considered in-use by C++.

<br>
<br>

## Pointer Arithmetic

Pointer arithmetic only makes sense with raw arrays.

### `++` and `--`

- `++` increments a pointer to point to the next array element. `int_ptr++;`
- `--` decrement a pointer to point to the previous array element. `int_ptr--;`

<br>

### `+` and `-`

- `+` increments the pointer by "n \* sizeof(type)".

  ```cpp
  int_ptr += n; //or int_ptr = int_ptr + n;
  ```

* similar can be said for `-`

<br>

### Subracting two pointers pointing to same datatype

- the subtraction of two pointers (must point to same datatype) gives the number of elements between them.

  ```cpp
  int main()
  {
      int num1 = 10;
      int num2 = 20;
      int* p1 = &num1;
      int* p2 = &num2;

      cout << p1 << endl;  //0135FA38
      cout << p2 << endl;  //0135FA2C
      cout << p2 - p1 << endl; //-3
      cout << (p2+3) << endl;  //0135FA38
      cout << "This is a dummy expression so that debugger stays here while I view memory." << endl;
  }
  ```

  - p1 and p2+3 point to the same address! <br> <br>

  ![](../_assets/p1.png)

  - In the above image showing memory, we can see hex 0a (decimal 10) at 0x0135FA38 and we can see 0x0135FA2C containing hex 14 (decimal 20) at 3rd memory block behind.

<br>
<br>

## Pointers and Arrays

- The value of the array name is the first element in the array. (essentially it's a pointer ig)

  ```cpp
  int arr[5]{ 100,200};
  cout << arr << endl;  //004FFE8C
  cout << *arr << endl; //100
  ```

* If we initialise a pointer with the above array, we can see that the value of the pointer is the same as that of the array.

  ```cpp
  int* arr_ptr = arr;   // int* arr_ptr = &arr gives error!
  cout << arr_ptr << endl;   //004FFE8C
  cout << *arr_ptr << endl;  //100
  ```

* Hence we can use both array name and pointers interchangebaly.

  ```cpp
  int arr[5]{ 100,200}; //[100,200,0,0,0]
  int* arr_ptr = arr;
  cout << arr_ptr[0] << endl; //100
  cout << arr_ptr[1] << endl; //200
  cout << arr_ptr[2] << endl; //0
  ```

* Checkout pointer arithmetics to understand the following, we can access the data stored in an array using _subscript notation_ (like above) or using _offset notation_ (shown below)
* Notice the paranthesis in the following code.
* when 1 is added to a memory address (it addes 4 bytes as array is storing integers having 4 bytes of memory and shows the adjacent memory location).

  ```cpp
  int arr[5]{ 100,200}; //[100,200,0,0,0]
  int* arr_ptr = arr;
  cout << *arr_ptr << endl; //100
  cout << *(arr_ptr+1) << endl; //200
  cout << *(arr_ptr+2) << endl; //0
  ```

<br>
<br>
