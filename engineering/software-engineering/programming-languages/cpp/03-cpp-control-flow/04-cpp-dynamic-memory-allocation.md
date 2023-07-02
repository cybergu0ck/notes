# Dynamic Memory Allocation

Dynamic memory allocation refers to the process of allocating memory at runtime, rather than at compile time.

<br>
<br>

# Dynamic Memory Allocation in C vs C++

- The difference is listed here
  | C | C++ |
  | ------- | --------------------------------- |
  | malloc | new , new(nothrow), placement new |
  | calloc | new[ ] |
  | realloc | - |
  | free | delete, delete[ ] |

<br>

- It is efficient to use malloc and free (over new and delete) to allocate and deallocate dynamic memory for standard types and C structs.
- It is ideal to use new and delete (over malloc and free) to allocate and deallocate dynamic memory for class objects and C++ structs as they will implicitely call the constructor and destructor (respectively) if any.

<br>
<br>

## Allocating heap memory using new keyword

- When we allocate something on the heap, there is no name to that so the only way to access that is using the pointer, if we loose the pointer (due to scope or reassignment), then we loose the accesss to that and this causes memory leak.

- When we are done using the storage, we must deallocate it so that it is available for the rest of the program.

  ```cpp
  int main()
  {
      int* int_ptr;
      int_ptr = new int;  //allocate an integer on the heap

      cout << int_ptr << endl;  //00FECC00
      cout << *int_ptr << endl; //- 842150451 (garbage)

      *int_ptr = 100;

      cout << int_ptr << endl;  ////00FECC00
      cout << *int_ptr << endl;  //100

      delete int_ptr;  //deallocation
  }
  ```

- Allocating contigious memory

  ```cpp
  int main()
  {
      int* array_ptr{ nullptr };
      int size{ 10 };
      array_ptr = new int[size]; //allocating an array on the heap

      delete[] array_ptr; //free the allocated storage
  }
  ```

<br>
<br>

# Returning dynamically allocated memory from a function

- Note that returning a pointer type is returned as a rvalue.

  ```cpp
  int* create_array(int size, int default_value);

  int main()
  {
    int* my_array = create_array(100, 5); //create an array on heap with 100 items, each having value as 5
    delete[] my_array;   //always free up the heap!
  }


  int* create_array(int size, int default_value = 0) {

    int* new_storage = new int[size];

    for (int i{ 0 }; i < size; i++) {
      *(new_storage + i) = default_value;
    }

    return new_storage;
  }
  ```
