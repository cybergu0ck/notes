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

1. `push_back()` : to append elements to the vector.
2. `size()` : The number of elements in the vector.

   ```cpp
   #include <iostream>
   #include <vector>

   int main(){
       std::vector <int> my_vec{1,2,3};
       std::cout << my_vec.size() << std::endl;
   }

   //3
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
