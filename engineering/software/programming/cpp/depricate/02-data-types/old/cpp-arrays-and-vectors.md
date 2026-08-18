# Arrays

Characteristics of arrays are:

- Fixed size.
- Elements are all the same type.
- Stored contiguously in memory.

<br>

## Declaring Arrays

- arrays are declared using following syntax:

  ```
  type name [number of elements];
  ```

* Examples :

  ```cpp
  int test_scores[10];

  const int nums {20};
  int arr [nums];
  ```

<br>

## Initialising Arrays

- arrays are intialised using
  ```
  type name[size] {values};
  ```

* Different kinds of initialisation :

  ```cpp
  int results[3]{99,100,75};
  int high_scores [10] {50,70}; //rest of the elements are 0's
  int lazyness [365]{} //all elements are 0's
  int power [365] {100} //first element is 100, rest are 0's
  int another_arr [] {1,2,3} //size is calculated automatically
  ```

## Accessing array elements

- In C++, the name of the array refers to (pointer) the first element (at index 0) in the array.
- array elements are accessible using the index as `name[index]` notation.

  ```cpp
  int main()
  {
      int arr[5]{ 1,2,3,4,5 };
      cout << arr[4];
      return 0;
  }

  //5
  ```

<br>
<br>

## Array Decay

There are 2 problems related to arrays in C (not C++).

1. When array is passed into a function, copying all the elements every time is expensive.

   ```cpp
   #include <iostream>

   void printElementZero(int arr[1000]) //array of size 1000
   {
       std::cout << arr[0];
   }

   int main()
   {
       int x[1000] { 5 }; //array of size 1000
       printElementZero(x);
       return 0;
   }
   ```

1. We want to be able to write a single function that can accept array arguments of different lengths.

   ```cpp
   #include <iostream>

   void printElementZero(int arr[1000]) //array of size 1000
   {
     std::cout << arr[0];
   }

   int main()
   {
     int x[7] { 5 }; //array of size 7
     printElementZero(x);
     return 0;
   }
   ```

Therefore, C-style array will be implicitly converted into a pointer to the element type and initialized with the address of the first element (with index 0) under certain circumstances.

1. Passing an array to a function: When you pass an array as an argument to a function, it decays into a pointer to its first element. This means the function receives a pointer, not the entire array.

1. Using the array name in an expression: Except when used with the sizeof operator or the & operator, the array name decays to a pointer to its first element.

- In the following code, The type of the variable `array` is `int[10]`. But when it is used in expressions it decays to a `int *`.

  ```cpp
  #include <iostream>
  using namespace std;

  int main()
  {
      int arr[10]{ 9, 7, 5, 3, 1 };
      cout << *arr << endl; //9, arr is decaying here

      auto ptr{ arr }; // evaluation causes arr to decay, type deduction should deduce type int*
      cout << *ptr << endl; //9

      return 0;
  }
  ```

<br>
<br>

# Multi-dimensional arrays

## declaring multidimensional arrays

- multidimensional arrays are declared like these (Here 2D array is shown, similarly N dimensional arrays can be created as limited by the compiler)

  ```
  type name [dim1_size][dim2_size]
  ```

* Example:

  ```cpp
  int main()
  {
      const int rows{ 3 };
      const int cols{ 4 };
      int table[rows][cols];
      return 0;
  }
  ```

<br>

## Initialising multidimensional array

- multidimensional arrays are initialised using this syntax

  ```
  type name [dim1_size][dim2_size] { {values}, {values},....}
  ```

* Example :

  ```cpp
  int table[3][4] {
          {1,2,3,4},
          {5,6,7,8},
          {9,10,11,12}
      };
  ```

<br>

## Accessing multidimensional array

- multidimensional array elements are accessible using the index as `name[dim1_index][dim2_index]` notation.

<br>
<br>
<br>

# Vectors

- vectors are dynamic arrays that can grow and shrink in size at execution.
- vectors are objects hence have useful methods like sort, max, min etc.

<br>

## Declaring vectors

- syntax:

  ```cpp
  #include <vector>

  std::vector <type> name;
  ```

- example:

  ```cpp
  #include <vector>
  using namespace std;

  int main()
  {
      vector <int> test_score;
      return 0;
  }
  ```

<br>

## Initialising vectors

- Different kinds of initialisation :

  ```cpp
  std::vector <int> test_score{98,88,60,30};
  std::vector <int> my_vector(5); //vector of size = 5 and all are 0's
  std::vector <int> postiveness(100, 56); // 100 is the size and all elements are 56
  std::vector <char> vowels{'a','e', 'i','o','u'};
  ```

<br>

## Accessing elements of vectors

1. using index and `name[index]` notation.
2. using at method. ex : `name.at(index)`

<br>

## Vector methods

<br>

### Getting the Number of Elements

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> numbers{1,2};
    std::cout << numbers.size() << std::endl;
    return 0;
}

//2
```

<br>

### Appending an element

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> numbers{1,2};
    numbers.push_back(3);

    for(int num: numbers){
        std::cout << num << "\t";
    }

    return 0;
}

//1 2 3
```

<br>

### Inserting an element

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> numbers{1,2};
    numbers.insert(numbers.begin(),0);  //Insert an elment at 0 index
    numbers.insert(numbers.begin()+1,9);  //Insert an elment at 1 index

    for(int num: numbers){
        std::cout << num << "\t";
    }
    return 0;
}
//0	9	1	2
```

<br>

### Poping the last element

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> numbers{1,2,3};
    numbers.pop_back();

    for(int num:numbers){
        std::cout << num << "\t";
    }
    return 0;
}

//1	2
```

<br>

### Removing a specific element

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> numbers{1,2,3};
    numbers.erase(numbers.begin()+1);  //Removes the element at index 1

    for(int num:numbers){
        std::cout << num << "\t";
    }
    return 0;
}
// 1	3
```

<br>

## Clear the vector

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> numbers{1,2,3};
    numbers.clear();  //Removes the element at index 1
    std::cout << numbers.size() << std::endl;
    return 0;
}

//0
```

<br>

## Swap two vectors

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> numbers{1,2,3};
    std::vector<int> vector{100,200,300};
    numbers.swap(vector);

    for(int num: numbers){
        std::cout << num << "\t";
    }
    std::cout << "\n";
    for(int num: vector){
        std::cout << num << "\t";
    }
    return 0;
}

// 100	200	300
// 1	2	3
```

<br>
<br>

# Multi-dimensional vectors

- The concept is similar to that of multidimenional arrays but applied for vectors.

## Declaration

- syntax:

  ```
  std::vector <std::vector <type>> name;
  ```
