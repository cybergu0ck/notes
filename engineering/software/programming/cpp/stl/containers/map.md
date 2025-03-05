# stl maps

stl maps are associative containers that store key value pairs.

<br>
<br>

## types

1. **map** : an stl map is an associative container that stores key-value pairs with unique keys in a _sorted order by key._
2. **multi map** : a multimap is an associative container that stores key-value pairs, allowing multiple values to be associated with the same key (i.e., duplicate keys), in a _sorted order by key._
3. **unordered map** : an unordered map is an associative container that stores key-value pairs with unique keys _without maintaining any specific order of the elements._
4. **unordered multimap** : an unordered multimap is an associative container that stores key-value pairs, allowing multiple values to be associated with the same key (i.e., duplicate keys) _without maintaining any specific order of the elements._

<br>

|                | std::map       | std::mulitmap  | std::unordered_map | std::unordered_multimap |
| -------------- | -------------- | -------------- | ------------------ | ----------------------- |
| Unique keys    | true           | false          | true               | false                   |
| Order          | true           | true           | false              | false                   |
| Header file    | `<map>`        | `<map>`        | `<unordered_map>`  | `unordered_map`         |
| Implementation | Red Black Tree | Red Black Tree | Hash Table         | Hash Table              |

<br>

### time complexities

|           | std::map   | std::mulitmap | std::unordered_map  | std::unordered_multimap |
| --------- | ---------- | ------------- | ------------------- | ----------------------- |
| Insertion | $O(log n)$ | $O(log n)$    | $\theta(1)$, $O(n)$ | $\theta(1)$, $O(n)$     |
| Deletion  | $O(log n)$ | $O(log n)$    | $\theta(1)$, $O(n)$ | $\theta(1)$, $O(n)$     |
| Search    | $O(log n)$ | $O(log n)$    | $\theta(1)$, $O(n)$ | $\theta(1)$, $O(n)$     |

- For the unordered variants the time complexity is $\theta(1)$ i.e. average case and $O(n)$ i.e. worst case (when the exisiting hash is generated, rare).

<br>

### space Complexities

|     | std::map | std::mulitmap | std::unordered_map | std::unordered_multimap |
| --- | -------- | ------------- | ------------------ | ----------------------- |
|     | $O(n)$   | $O(n)$        | $O(n)$             | $O(n)$                  |

<br>
<br>

## initialisation

<br>
<br>

## methods

<br>

### access

1. `T operator[](size_t pos)`

   - returns the object at pos _without bounds checking_.
   - has $O(1)$ time complexity.
   - no exception is thrown if the key is not found.

     ```cpp
     int main()
     {
         std::map<int, std::string> myMap;
         myMap[1] = "value1";            // Inserts key 1 with value "value1"
         std::string value = myMap[2];   // Inserts key 2 with default value ""

         display(myMap);
     }

     //1 : value1
     //2 :
     ```

<br>

1. `T at(size_t pos)`

   - returns the object at pos _with bounds checking_.
   - has $O(1)$ time complexity.
   - If the non-existing key is used with the `at` method, it will throw an `std::out_of_range` exception.

     ```cpp
     int main()
     {
         std::map<int, std::string> myMap;
         myMap[1] = "value1";
         try {
             std::string value = myMap.at(1);  // Accesses value for key 1
             std::string missingValue = myMap.at(2);  // Throws std::out_of_range
         }
         catch (const std::out_of_range& e) {
             std::cout << "Key not found" << std::endl;
         }

         display(myMap);
     }

     //"Key not found"
     //1 : value1
     ```

<br>

<br>

### search

- searching an key in a map is done with `find` method.

  ```cpp
  int main()
  {
      std::map<int, std::string> myMap = { {1, "larry"}, {2, "harry"} };

      auto iter = myMap.find(2);
      if (iter != myMap.end())
      {
          std::cout << "Key-value pair found, key = " << iter->first << " and value = " << iter->second << "\n";
      }
  }

  //Key-value pair found, key = 2 and value = harry
  ```

<br>

### insertion

- if a non exisiting key is used in the operator, it will create a new key in the map with either the given value or a default constructed one.

<br>

### deletion

1. `iterator erase(const_iterator pos);`

```cpp
int main()
{
    std::map<int, std::string> myMap{ {1, "a"}, {2, "b"}, {3, "c"} };
    myMap.erase(1);                 //myMap is {2 : "b", 3 : "c"}
    myMap.erase(0);                 //No errors, nothing is removed

    myMap.erase(myMap.begin());     //myMap is {3 : "c"}
    myMap.erase(myMap.begin()+1);   //Error as map iterators are bidirectional, not random access iterators!
    myMap.erase(myMap.end());       //Error: Can't erase using out of bound iterators

    myMap.clear();                  //Clears the entire map
}
```

<br>
<br>

### modification

<br>

#### sorting

- maps, ordered variants are already sorted!

- it doesn't make sense to sort unordered maps but even then sorting an unordered map is not intuitive. unordered map provides only forward iterators and not random iterators and sort function needs random iterators to jump around quickly and perform sorting. hence we need to use a vector to sort an unordered map!

  ```cpp
  #include <iostream>
  #include <unordered_map>
  #include <vector>
  #include <algorithm>

  int main() {
      std::unordered_map<int, int> freq {{2,3},{1,2}, {3,10}};

      std::vector<std::pair<int, int>> temp_vec;
      for(const auto& pair:freq){
      temp_vec.push_back(pair);
      }

      std::sort(temp_vec.begin(), temp_vec.end(), [](std::pair<int,int> a, auto b){ return a.second < b.second;}); //Use greater than operator to sort the other way.

      for(const auto& pair : temp_vec){
      std::cout << pair.first << ":" << pair.second << "\n";
      }

      return 0;
  }

  // 1:2
  // 2:3
  // 3:10
  ```

- to have a map order the keys in a custom manner, see the following example:

  ```cpp
  #include <iostream>
  #include <string>
  #include <vector>
  #include <algorithm>
  #include <map>

  struct custom_comparator{
  bool operator()(const std::string& a, const std::string&b)const{
  return a>b;
  }
  };

  int main()
  {
      std::map<std::string, int> freq1 {{"abc",3},{"a",1}, {"abcd",4}};
      std::map<std::string, int, custom_comparator> freq2 {{"abc",3},{"a",1}, {"abcd",4}};

      for(const auto& pair : freq1){
      std::cout << pair.second << '\t';
      }

      std::cout << '\n';
      for(const auto& pair : freq2){
      std::cout << pair.second << '\t';
      }

      return 0;
  }

  //1 3 4
  //4 3 1
  ```

  - std::map's template parameter for the comparator (Compare) expects a type that provides a function object (something that can be called like a function) and not a function itself.
  - This is usually done using a struct or class that overloads the operator().
  - the operator() overload makes the struct/class act like a function. This allows the std::map to use it to compare keys.
  - the operator() should be const because it shouldn't modify the comparator object itself during the comparison.

<br>

### miscallaneous

1.  `size_t size()`

    - returns the number of objects.
    - has $O(1)$ time complexity.

<br>

1. `bool empty()`

   - returns true or 1 if vector is empty else returns false or 0.

<br>

1. `bool operator==(map T);`

   - `==` returns true only if the two maps being compared have exactly same keys with exactly same values.

   - example :

     ```cpp
     #include <iostream>
     #include <unordered_map>

     void compare_maps(std::unordered_map<char, int> map1,
                     std::unordered_map<char, int> map2) {
         if (map1 == map2) {
             std::cout << "true" << "\n";
         } else {
             std::cout << "false" << '\n';
         }
     }

     int main() {
         std::unordered_map<char, int> map1{{'a', 1}, {'b', 1}};
         std::unordered_map<char, int> map2{{'a', 1}, {'b', 1}};
         std::unordered_map<char, int> map3{{'a', 1}, {'b', 10}};

         compare_maps(map1, map2);
         compare_maps(map1, map3);
     }

     // true
     // false
     ```

<br>

1. `size_t count(const T& key)`

   - For set and unordered set, it returns 1 if the key exists otherwise returns 0.
   - For multiset and unordered multiset, it returns the number of elements having the key as the parameter.
