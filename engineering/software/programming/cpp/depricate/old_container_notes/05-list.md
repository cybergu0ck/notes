# STL List

A std::list is a sequence container that allows non-contiguous memory allocation.

- It is implemented as a doubly linked list

## Initialisation

```cpp
#include <iostream>
#include <list>
#include <vector>

int main() {

    std::list<int> list1;               // Default Initialization
    std::list<int> list2(5);            // Initialization with Specific Size
    std::list<int> list3(5, 10);        // Initialization with Specific Size and Value
    std::list<int> list4 = {1, 2, 3, 4, 5};     // Initialization with an Initializer List

    std::list<int> originalList = {1, 2, 3};
    std::list<int> list5(originalList);         // Copy Initialization

    std::vector<int> vec = {1, 2, 3, 4, 5};
    std::list<int> list6(vec.begin(), vec.end());   // Range Initialization

    std::list<int> list7(std::move(originalList));  // Move Initialization


    std::list<int> list8;
    list8.assign(5, 10);    // Using `assign` Method
    return 0;
}
```

<br>
<br>

## Methods

### Adding Elements

The following display function is used to display the elments.

```cpp
void print(std::list<int>& numbers)
{
    for(const auto& num: numbers)
    {
        std::cout << num << "\t";
    }
}
```

1. Pushing elments to front and back.

   ```cpp
   int main()
   {
       std::list<int> numbers;
       numbers.push_back(2);
       numbers.push_back(3);
       numbers.push_front(1);
       print(numbers);
   }
   //1	2	3
   ```

2. Inserting elements.

   ```cpp
   int main()
   {
       std::list<int> numbers = {1,2,3};
       auto iterator = numbers.begin();
       std::advance(iterator, 2);
       numbers.insert(iterator, 20);
       print(numbers);
   }
   //1	2	20	3
   ```

3. Emplacing elments.

   ```cpp
   int main()
   {
       std::list<std::pair<int, int>> pairs;
       pairs.emplace_back(2,1);
       pairs.emplace_back(1,1);

       auto it = pairs.begin();
       std::advance(it, 1);
       pairs.emplace(it, 20,1);
   }
   ```

<br>

### Accessing Elements

<br>

### Finding Elements

<br>

### Removing Elements

<br>

### Number of Elements

<br>

### Emptyness

<br>
