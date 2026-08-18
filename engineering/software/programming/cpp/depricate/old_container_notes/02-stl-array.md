# STL Array

**A std::array is a static array.**

- It is defined in the `<array>` header.

<br>
<br>

## Initialisation

```cpp
#include <array>

int main()
{
    std::array<int, 4> arr1;      //Elements are randomly initialised with garbage values; arr1 = [0 , 0 , 445436,453666];
    arr1.fill(10);                //All elements are 10 now; arr1 = [0 , 0 , 0, 0];

    std::array<int,4> arr2{};     //Elements are initialised to zero using Default constructor; arr2 = [0 , 0 , 0, 0];
    std::array<int,4> arr3 = {};  //Elements are initialised to zero using Default constructor; arr3 = [0 , 0 , 0, 0];

    std::array<int, 4> arr4 = {1};  //arr4 = [1, 0, 0, 0];
    std::array<int, 4> arr5 = {1,2,3,4};  //arr4 = [1, 2, 3, 4];

    return 0;
}
```

<br>
<br>

## Methods

### Set Value

fill() method sets the given value to all the elements in the array.

```cpp
#include <array>

int main()
{
    std::array<int, 4> arr1;      //Elements are randomly initialised with garbage values; arr1 = [0 , 0 , 445436,453666];
    arr1.fill(10);                //All elements are 10 now; arr1 = [0 , 0 , 0, 0];

    return 0;
}
```
