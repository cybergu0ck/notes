# STL Vector

A std::vector is a dynamic array.

- It is defined in the `<vector>` header.

<br>
<br>

## Initialisation

```cpp
#include<iostream>
#include<vector> //Library to be included

int main()
{
	std::vector<int> v1;                      // Default
	std::vector<int> v2(5);                   // Vector of size 5 with all elements initialized to 0
	std::vector<int> v3(5, 10);	              // Vector of size 5 with all elements initialized to 10
	std::vector<int> v4 = { 1, 2, 3, 4, 5 };  // Initialiser list
	std::vector<int> v5(v1);                  // Copy Initialisation
	std::vector<int> v6(std::move(v2));       // Move Initialisation
}
```

<br>
<br>

## Methods

<br>

### Appending Elements

```cpp
#include <iostream>
#include <vector>

int main()
{
    std::vector<int> vec;
    vec.push_back(1);
    vec.push_back(2);
}
```

<br>

### Inserting Elements

```cpp
#include <iostream>
#include <vector>

int main()
{
    std::vector<int> vec = {1,2,3};   //vec is {1,2,3}
    vec.insert(vec.begin(), 0);       //vec is {0,1,2,3}
    vec.insert(vec.begin()+2, 100);   //vec is {0,1,100,2,3}
    vec.insert(vec.end(), 200);       //vec is {0,1,100,2,3,200}
    vec.insert(vec.end()-1, 199);     //vec is {0,1,100,2,3,199,200}
    vec.insert(v.begin() + 1, 3, 99); //vec is {0, 99,99,99, 1,100,2,3,199,200}
}
```

<br>

### Accessing Elements

```cpp
#include <iostream>
#include <vector>

int main()
{
    std::vector<int> vec = {1,2,3};     //vec is {1,2,3}

    std::cout << vec.front() << '\n';   //Accessing the first element
    std::cout << vec.back() << '\n';    //Accessing the last element
    std::cout << vec[1] << '\n';        //Accessing element using index
}

//1
//2
//3
```

<br>

### Removing Elements

```cpp
#include <iostream>
#include <vector>

int main()
{
    std::vector<int> vec = {1,2,3,4,5};   //vec is {1,2,3,4,5}

    vec.erase(vec.begin());               //vec is {2,3,4,5}
    vec.erase(vec.begin() + 2);           //vec is {2,3,5}
    vec.pop_back();                       //vec is {2,3}
    vec.clear();                          //vec is {}
}
```

<br>

### Number of Elements

```cpp
#include <iostream>
#include <vector>

int main()
{
    std::vector<int> vec = {1,2,3,4,5};

    std::cout << vec.size() << '\n';	//Returns the number of elments in the vector
}
//5
```

<br>

### Empty Vector

```cpp
#include <iostream>
#include <vector>

int main()
{
    std::vector<int> vec = {1,2,3,4,5};

    std::cout << vec.empty() << '\n';	//Returns 1 if vector is empty else returns 0
}
//0
```

<br>

### Emplacing Element

- Emplacing an elment into the vector. Understand emplacement using the illustration below

  ```cpp
  #include<iostream>
  #include<vector> //Library to be included

  class MyClass {
  public:
      int number;
      std::string word;

      MyClass(int p1, std::string p2):number{p1}, word{p2}
      {
          std::cout << "constructor was called" << std::endl;
      }
      MyClass(const MyClass& source):number{source.number}, word{source.word}
      {
          std::cout << "copy constructor was called" << std::endl;
      }
      MyClass(const MyClass&& source) noexcept :number{source.number}, word{source.word}
      {
          std::cout << "move constructor was called" << std::endl;
      }
      ~MyClass() {}
  };
  ```

  ```cpp
  int main()
  {
      std::vector<MyClass> v;
      MyClass obj = MyClass(1, "a");
      v.push_back(obj);
  }

  //constructor was called
  //copy constructor was called
  ```

  ```cpp
  int main()
  {
      std::vector<MyClass> v;
      v.push_back(MyClass(1, "a"));
  }

  //constructor was called
  //move constructor was called
  ```

  ```cpp

  int main()
  {
      std::vector<MyClass> v;
      v.emplace_back(1,"a"); //Pass the paramters to construct the object directly in memory
  }

  //constructor was called
  ```
