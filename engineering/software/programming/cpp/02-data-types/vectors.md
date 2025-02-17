# std::vectors

A std::vector is a class that represents a dynamic arrays.

- It is defined in the `<vector>` header.

<br>
<br>

## initialization

- Different kinds of initialisation :

  ```cpp
  //default initialisation
  std::vector <int> empty_vec;

  //uniform initialisation
  std::vector <int> test_score{98,88,60,30};
  std::vector <char> vowels = {'a','e', 'i','o','u'}; //using an initaliser list

  //fill initialisation
  std::vector <int> my_vector(5); //using only size; 5 elements with default values 0;
  std::vector <int> postiveness(100, 56); //using size and value; 100 elements with value 56
  ```

<br>
<br>

## arrays vs std::vetors

| array                    | std::vector                  |
| ------------------------ | ---------------------------- |
| fixed size               | dynamic size                 |
| manual memory management | automatic memory managements |

<br>
<br>

## methods

<br>

### access

1. _T operator[](size_t pos)_

   - returns the object at pos _without bounds checking_.
   - has $O(1)$ time complexity.

1. _T at(size_t pos)_

   - returns the object at pos _with bounds checking_.
   - has $O(1)$ time complexity.

<br>

### search

- searching an element in a vector is done with the help of algorithm's find function.
- example :

  ```cpp
  #include <iostream>
  #include <vector>
  #include <algorithm>

  int main() {
      std::vector<int> v = {10, 20, 30, 20, 40};
      auto it = std::find(v.begin(), v.end(), 20);

      if (it != v.end()) {
          std::cout << "Found 20 at index: " << std::distance(v.begin(), it) << std::endl;
      } else {
          std::cout << "20 not found" << std::endl;
      }

      return 0;
  }
  //Found 20 at index: 1
  ```

<br>

### insertion

1. _void push_back(T obj)_

   - append a object obj to _\*this_.
   - has amortised $O(1)$ time complexity, average is $O(1)$ and is $O(n)$ in case of relocation.

<br>

1. _iterator insert(const_iterator pos, T obj);_

   - insert obj at pos.
   - has amortised $O(n)$ time complexity, average is $O(n)$ and is $O(n+m)$ in case of relocation.
   - example :

     ```cpp
     #include <iostream>
     #include <vector>

     int main() {
         std::vector<int> numbers{1,2};
         numbers.insert(numbers.begin(),0);  //Insert an elment with value 0 at 0 index
         numbers.insert(numbers.begin()+1,9);  //Insert an elment with value 9 at 1 index

         for(int num: numbers){
             std::cout << num << "\t";
         }
         return 0;
     }
     //0 9 1 2
     ```

<br>

1. _void emplace_back(args ...)_

   - to emplace an element means to construct an object directly in the container instead of copying or moving it.

   - understand using the following illustration:

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

<br>

### deletion

1.  _void pop_back();_

- removes the last element from the vector.
- doesn't return anything.
- has $O(1)$ time complexity.
- example:

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

1. _iterator erase(const_iterator pos);_

   - erase the element at pos.
   - returns the iterator.
   - has $O(n)$ time complexity.
   - example :

   ```cpp
   #include <iostream>
   using namespace std;
   #include <vector>

   int main()
   {
       std::vector<int> nums{1,2,3};
       std::vector<int>::iterator it = nums.erase(nums.begin()+1);

       std::cout << "value of the erased element is " << *it;

       std::cout << '\n';
       for(int num:nums){
           std::cout << num << "\t";
       }

       return 0;
   }

   //value of the erased element is 3
   //1	3
   ```

<br>

1. _void clear();_

   - erase the entire vector.
   - has $O(n)$ time complexity.

<br>

### modification

- can be done using the access methods in combination with the assignment operator.

<br>

### miscallaneous

1.  _size_t size()_

    - returns the number of objects.
    - has $O(1)$ time complexity.

<br>

1. _bool empty()_

- returns true or 1 if vector is empty else returns false or 0.

<br>

1. _void swap(std::vector<T>& other);_

   - swap `*this` and other with each other.
   - has $O(1)$ time complexity.
   - example :

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

<!-- TODO - write about iterators -->
