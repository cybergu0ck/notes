# STL Set

A set is an associative container that stores unique elements, typically without a specific order.

- Defined in the `<set>` header.
- Part of `std` namespace.
- The above defintion is specific to `std::set`, checkout the [types](#types) of sets.

<br>
<br>

## Types

1. **Set** : A set is an associative container that stores unique elements in sorted order.
2. **Multi Set** : A multiset is an associative container that stores elements (allows duplicates) in sorted order.
3. **Unordered Set** : An unordered is an associative container that stores unique elements in un-sorted order.
4. **Unordered Multiset** : An unordered_multiset is an associative container that stores elements (allows duplicates) in un-sorted order.

<br>

|                 | std::set       | std::muliset   | std::unordered_set | std::unordered_multset |
| --------------- | -------------- | -------------- | ------------------ | ---------------------- |
| Unique elements | true           | false          | true               | false                  |
| Order           | true           | true           | false              | false                  |
| Header file     | `<set>`        | `<set>`        | `<unordered_set>`  | `<unordered_set>`      |
| Implementation  | Red Black Tree | Red Black Tree | Hash Table         | Hash Table             |

<br>

### Time complexities

|           | std::set   | std::mulitset | std::unordered_set  | std::unordered_multiset |
| --------- | ---------- | ------------- | ------------------- | ----------------------- |
| Insertion | $O(log n)$ | $O(log n)$    | $\theta(1)$, $O(n)$ | $\theta(1)$, $O(n)$     |
| Deletion  | $O(log n)$ | $O(log n)$    | $\theta(1)$, $O(n)$ | $\theta(1)$, $O(n)$     |
| Search    | $O(log n)$ | $O(log n)$    | $\theta(1)$, $O(n)$ | $\theta(1)$, $O(n)$     |

- For the unordered variants the time complexity is $\theta(1)$ i.e. average case and $O(n)$ i.e. worst case, when the hash function is poor causing collisions (rare).

<br>

### Space complexities

|     | std::set | std::mulitset | std::unordered_set | std::unordered_multiset |
| --- | -------- | ------------- | ------------------ | ----------------------- |
|     | $O(n)$   | $O(n)$        | $O(n)$             | $O(n)$                  |

<br>
<br>

## Initialisation

```cpp
//Default initialisation
std::set<int> set1;  //default constructor invoked

//
std::set<int> set3{5, 4, 3, 2, 1};  //
std::set<int> set2 = {1, 2, 3, 4, 5};

//Intialise a set using another set
std::set<int> set4 = set2; //copy constructor invoked
std::set<int> set5(set2);  //copy constructor invoked
std::set<int> set6 = std::move(set2);  //move constructor invoked

//Initialise a set using a vector
std::vector<int> vec = {10, 20, 30, 40};
std::set<int> set7(vec.begin(), vec.end()); //overloaded range constructor
```

<!-- TODO vaidate (by creating a class implementation for a string and then checking different forms of initialisation) and mostly rewrite the different form of intialisation and the specific constructor invoked -->

<br>
<br>

## Methods

<br>

### Access

Sets do not have `at` or `operator[]` unlike vectors, as elements are not indexed.

1. `std::set<T>::iterator begin()`

   - Returns an itertor to the first element.
   - Time complexity is $O(1)$ .

     ```cpp
     #include <iostream>
     #include <set>

     int main(){
     std::set<int> nums = {1,2,3};
     auto iter = nums.begin();
     std::cout << *iter << '\n';
     }

     //1
     ```

<br>

1. `std::set<T>::iterator end();`

   - Returns an itertor to the last element.
   - Time complexity is $O(1)$ .
   - Example is similar to `begin` method.

<br>

### Search

1. `std::set<T>::iterator find(const T& value);`

   - Returns the iterator to the element having value same as that of parameter else returns "end" iterator.
   - Time complexity is $O(n * log(n))$ .

     ```cpp
     #include <iostream>
     #include <set>

     int main(){
         std::set<int> nums = {1,2,3};
         auto is_found = nums.find(2);
         if(is_found != nums.end())
             std::cout << "Found : " << *is_found << '\n';
         else
             std::cout << "Element not found" << '\n';
     }

     //Found : 2
     ```

<br>

### Insertion

1. `insert` method has various overloads

   - The time complexity of the basic form of insert is $O(1)$ on average and $O(n)$ in the worst case due to hash collisions.
   - Illustration of important form of insertions.

     ```cpp
     #include <iostream>
     #include <set>
     #include <vector>

     int main(){
         std::set<int> nums = {1,2,3};

         nums.insert(4);

         nums.insert({5,6,7});

         std::vector<int> vec{8,9,10};
         nums.insert(vec.begin(), vec.end());

         for(const auto& num : nums){
             std::cout << num << "\t";
         }
     }

     //1	 2	3	4	5	6	7	8	9	10
     ```

<br>

### Deletion

1. `erase` method has different overloads.

   - The time complexity of the basic form of erase is $O(log(n))$
   - Illustration of important form of erase.

     ```cpp
     #include <iostream>
     #include <set>

     int main(){
         std::set<int> nums = {1,2,3};

         nums.erase(2);  //using value

         auto it = nums.find(3);
         if(it != nums.end())
             nums.erase(it);   //using iterator

         for(const auto& num : nums){
             std::cout << num << "\t";
         }
     }

     //1
     ```

<br>

1. `void clear();`

   - Erase the entire set.

     ```cpp
     #include <iostream>
     #include <set>

     int main(){
         std::set<int> nums = {1,2,3};

         nums.clear();

         for(const auto& num : nums){
             std::cout << num << "\t";
         }
     }
     ```

<br>

### Modification

<br>

### Miscallaneous

<br>

1.  `size_t size();`

    - Returns the number of elements.
    - Time complexity is $O(1)$.

<br>

1. `bool empty();`

   - Returns true or 1 if vector is empty else returns false or 0.

<br>

<br>
