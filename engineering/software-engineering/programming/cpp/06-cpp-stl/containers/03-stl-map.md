# STL Map

A std::map is an associative STL container that stores key-value pairs in a sorted order by key.

- Defined in the `<map>` header.

<br>
<br>

## Initialisation

```cpp
#include <iostream>
#include <string>
#include <map>

int main()
{
    std::map<int, std::string> map1;                                //default constructor
    std::map<int, std::string> map2{ {1, "larry"} };                //Initialiser list; the elments in the list must be pairs.
    std::map<int, std::string> map3{ {1, "mr"}, {2, "bean"} };      //Initialiser list; the elments in the list must be pairs.

    //using copy constructor
    //using move constructor
}
```

<br>
<br>

## Methods

<br>

### Adding Elements

- Adding key-value pairs to a map.

  - Using the `[]` operator.

    ```cpp
    #include <iostream>
    #include <string>
    #include <map>
    int main()
    {
        std::map<int, std::string> map1;
        map1[1] = "larry";
        map1[1] = "elison";        //overwrites the value "elison" for the key 1.
    }
    ```

    - This method will overwrite the value if the key already exists.

  - Using `insert` method.

    ```cpp
    #include <iostream>
    #include <string>
    #include <map>
    int main()
    {
        std::map<int, std::string> map1;
        map1.insert({ 1, "larry" });
        auto result_pair = map1.insert({ 1, "elision" }); //Doesn't overwrite; Hence the value for key 1 isstill "larry"
        //insert method returns a pair, first elment is the iterator and the second is a bool value.
        if (result_pair.second)
            std::cout << "Insertion sucessful";
        else
            std::cout << "Key already exists";
    }
    ```

    - This method will not overwrite the value if the key already exists.

<br>

### Accessing Elements

- Accessing the elements

  - Using `[]` operator.

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

    - If a non exisiting key is used in the operator, it will create a new key in the map with either the given value or a default constructed one.
    - No exception is thrown if the key is not found.

  - Using `at` method.

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

    - If the non-existing key is used with the `at` method, it will throw an `std::out_of_range` exception.

<br>

### Finding Elements

- Finding an element in the map.

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

### Removing Elements

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

### Number of Elements

```cpp
int main()
{
    std::map<int, std::string> myMap;
    myMap[1] = "a";
    myMap[2] = "b";
    myMap[1] = "c";

    std::cout << myMap.size();
}
//2
```

<br>

### Emptyness

```cpp
int main()
{
    std::map<int, std::string> myMap;

    std::cout << myMap.empty();  //returns 1 if the map is empty else returns 0
}
//1
```

<br>
<br>

## Types of STL Maps

1. **Map** : _An STL map is an associative container that stores key-value pairs with unique keys in a sorted order by key._
2. **Multi Map** : _A multimap is an associative container that stores key-value pairs, allowing multiple values to be associated with the same key (i.e., duplicate keys), in a sorted order by key._
3. **Unordered Map** : _An unordered map is an associative container that stores key-value pairs with unique keys without maintaining any specific order of the elements._
4. **Unordered Multimap** : _An unordered multimap is an associative container that stores key-value pairs, allowing multiple values to be associated with the same key (i.e., duplicate keys) without maintaining any specific order of the elements._

<br>

### Illustration

|             | std::map | std::mulitmap | std::unordered_map | std::unordered_multimap |
| ----------- | -------- | ------------- | ------------------ | ----------------------- |
| Unique keys | true     | false         | true               | false                   |
| Order       | true     | true          | false              | false                   |
| Header file | `<map>`  | `<map>`       | `<unordered_map>`  | `unordered_map`         |

<br>

### Implementation Details

|                | std::map       | std::mulitmap  | std::unordered_map | std::unordered_multimap |
| -------------- | -------------- | -------------- | ------------------ | ----------------------- |
| Implementation | Red Black Tree | Red Black Tree | Hash Table         | Hash Table              |

<br>

### Time Complexities

|           | std::map   | std::mulitmap | std::unordered_map  | std::unordered_multimap |
| --------- | ---------- | ------------- | ------------------- | ----------------------- |
| Insertion | $O(log n)$ | $O(log n)$    | $\theta(1)$, $O(n)$ | $\theta(1)$, $O(n)$     |
| Deletion  | $O(log n)$ | $O(log n)$    | $\theta(1)$, $O(n)$ | $\theta(1)$, $O(n)$     |
| Search    | $O(log n)$ | $O(log n)$    | $\theta(1)$, $O(n)$ | $\theta(1)$, $O(n)$     |

- For the unordered variants the time complexity is $\theta(1)$ i.e. average case and $O(n)$ i.e. worst case, when the exisiting hash is generated (rare).

<br>

### Space Complexities

|     | std::map | std::mulitmap | std::unordered_map | std::unordered_multimap |
| --- | -------- | ------------- | ------------------ | ----------------------- |
|     | $O(n)$   | $O(n)$        | $O(n)$             | $O(n)$                  |
