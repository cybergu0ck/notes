# stl array

- Unlike raw arrays, `std::array` doesn't decay to the pointer to the first element of the array when we pass it as arguments.
- Prefer `std:array` over raw arrays whenever possible!

> <br> Use https://en.cppreference.com/w/ for cpp reference!

- The type has to be specified in the parameter of the function

  ```cpp
  #include <iostream>
  #include<array>

  void display(std::array<int, 5> arr) {
      for ( auto& i : arr) {
          std::cout << i << " ";
      }
  }

  int main(){
      std::array<int, 5> arr1{ 1,2,3 };	//the remaining elements are intialised to zero.
      display(arr1);
  }

  //1 2 3 0 0
  ```

<br>
<br>

# useful functions

## using [ ] to get the value at the index

- This does not perform bounce checking. Hence when an index out of bound is used the code will compile fine but fail at run time.

  ```cpp
  #include <iostream>
  #include<array>

  int main(){
      std::array<int, 5> arr1{ 1,2,3 };
      arr1[10] = 100;	//this will compile successfully!
  }

  //run time error
  ```

<br>
<br>

## at() to get the value at the index

- Get the value for the specified index. This method will perform bounce checking! i.e. raises an exception at compile time itself.

  ```cpp
  #include <iostream>
  #include<array>

  int main(){
      std::array<int, 5> arr1{ 1,2,3 };
      arr1.at(10) = 20;	//this also compiled successfully tho lol
  }

  //abort will be called!
  ```

<br>
<br>

## fill()

- Fills up the entire array with the provided value.

  ```cpp
  #include <iostream>
  #include<array>

  void display(std::array<int, 5> arr) {
      for (const auto& i : arr) {
          std::cout << i << " ";
      }
  }

  int main(){
      std::array<int, 5> arr1{ 1,2,3 };
      arr1.fill(69);	//makes every element 69
      display(arr1);
  }

  //69 69 69 69 69
  ```

<br>
<br>

## swap()

- swaps two arrays.

  ```cpp
  #include <iostream>
  #include<array>

  void display(std::array<int, 5> arr) {
      for (const auto& i : arr) {
          std::cout << i << " ";
      }
      std::cout << std::endl;
  }

  int main(){
      std::array<int, 5> arr1{ 1,2,3 };
      std::array<int, 5> arr2{ 0,0,0 };
      arr1.swap(arr2);		//swaps both the arrays!
      display(arr1);
      display(arr2);
  }

  //0 0 0 0 0
  //1 2 3 0 0
  ```

<br>
<br>

## data()

- Returns the pointer to the first element of the `std::array`

  ```cpp
  #include <iostream>
  #include<array>

  int main(){
      std::array<int, 5> arr1{ 10,2,3 };
      int* first_elem = arr1.data();
      std::cout << *first_elem << std::endl;    //dereferencing
  }

  //10
  ```

<br>
<br>

## begin() and end()

- Since these are stl stuff, it supports iterators!

  ```cpp
  #include <iostream>
  #include<array>
  #include <algorithm>

  void display(std::array<int, 5> arr) {
      for (const auto& i : arr) {
          std::cout << i << " ";
      }
      std::cout << std::endl;
  }

  int main(){
      std::array<int, 5> arr1{ 10,2,3 };
      std::sort(arr1.begin(), arr1.end());	//sort is a stl algorithm
      display(arr1);

      std::array<int, 5>::iterator min_value_ptr = std::min_element(arr1.begin(), arr1.end());  //min_element is a stl algorithm to find min element
      auto max_value_ptr = std::max_element(arr1.begin(), arr1.end());		//auto comes clutch in these situations

      std::cout << "The minimum value in arr1 is " << *min_value_ptr << std::endl;
      std::cout << "The maximum value in arr1 is " << *max_value_ptr << std::endl;
  }

  //0 0 2 3 10
  //The minimum value in arr1 is 0
  //The maximum value in arr1 is 10
  ```
