# Smart Pointer

- They are objects that can only point to heap-allocated memory.
- They automatically call delete when no longer needed.
- They adhere to RAII principles.
- There are different kind of smart pointers

  - Unique Pointers (unique_ptr)
  - Shared Pointers (shared_ptr)
  - Weak Pointers (weak_ptr)
  - Auto Pointers (auto_ptr) : Depricated! hence must not be used.

  * We can use dereference (\*) and member selection (->) like raw pointers however we cannot use pointer arithmetic.

<br>
<br>

# Unique Pointer

- Unique pointers point to objects on the heap and there can be _only_ one unique pointer pointing to that object on the heap.
- Unique pointers:
  - cannot be copied.
  - cannot be assigned.
  - can be moved.
- **_When the pointer goes out of scope, the pointer will be destroyed and the object that is pointed is automatially destroyed._**

* The syntax is as follows

  ```cpp
  #include <iostream>
  #include <memory>  //Don't forget this

  using namespace std;

  int main()
  {

      std::unique_ptr<int> my_ptr{ new int{100} };
      cout << *my_ptr << endl;            //100
      *my_ptr = 200;
      cout << *my_ptr << endl;            //200
  }
  ```

* get() method returns the address of the object in heap memory that the unique pointer points to.

  ```cpp
  cout << my_ptr << endl;             //015C5DC8
  cout << my_ptr.get() << endl;       //015C5DC8
  ```

* reset() method sets the pointer to nullptr.

  ```cpp
  my_ptr.reset();                     //makes the pointer nullptr
  cout << my_ptr << endl;             //00000000
  ```

* Understand the following code to understand the concept.

  ```cpp
  #include <iostream>
  #include <memory>
  #include <vector>
  using namespace std;

  int main()
  {
      std::vector <std::unique_ptr <int>> my_vec;
      std::unique_ptr <int> num_on_heap{ new int{1} };
      my_vec.push_back(num_on_heap);              //error: copy not allowed
      my_vec.push_back(std::move(num_on_heap));   //valid
  }
  ```

* C++ 14 standard brought a new way to initialise unique_ptrs without `new` keyword!

  ```cpp
  std::unique_ptr<int> p1 = make_unique<int>(100);
  std::unique_ptr<Account> = make_unique<Account>("Curly", 5000);
  ```

<br>
<br>

# Shared Pointer

- Shared pointers also point to objects on the heap but unlike unique pointers there can be many shared pointers pointing to the same object on the heap.
- Shared pointers:
  - can be copied.
  - can be assigned.
  - can be moved.

* When the use count is zero, the managed object on the heap is destroyed.

  ```cpp
  #include <iostream>
  #include <memory>
  using namespace std;

  int main()
  {
      std::shared_ptr <int> p1{ new int {99} };
      std::cout << *p1 << std::endl;		//99
      *p1 = 55;
      std::cout << *p1 << std::endl;		//55
  }
  ```

* use_count() method can be used to see how many shared pointers are managing that object on the heap.
* reset() method will nullify it and decrement the use_count to zero!

  ```cpp
  #include <iostream>
  #include <memory>
  using namespace std;

  int main()
  {
      std::shared_ptr <int> p1{ new int {99} };
      std::cout << p1.use_count() << std::endl;		//1

      std::shared_ptr <int> p2{ p1 };
      std::cout << p1.use_count() << std::endl;		//2

      p2.reset();		//p2 lost ownership of the object on the heap, which is now managed only by p1
      std::cout << p1.use_count() << std::endl;		//1
  }
  ```

* Understand the following code to understand the concept.

  ```cpp
  #include <iostream>
  #include <memory>
  #include <vector>
  using namespace std;

  int main()
  {
      std::vector <std::shared_ptr <int>> my_vec;
      std::shared_ptr <int> num_on_heap{ new int{59} };
      my_vec.push_back(num_on_heap);              //valid: copy allowed
      cout << num_on_heap.use_count() << endl;    //2, one is the num_on_heap and the other is the copy that is in the vector!
  }
  ```

* This is the best way to initialise a shared pointer
  ```cpp
  std::shared_ptr <int> p1 = std::make_shared<int>(99);
  ```

<br>
<br>

# Weak Pointers

- Weak pointers are pointers created from shared pointers but do not participate in owning (managing) relationship.

* they donot increment or decrement the reference use count.

* In the below program, the class A contains an attribute that is a shared pointer of type B and similarly class B contains an attribute that is a shared pointer of type A. In the main program we set the appropriate values for these 2 attributes. However there is a memory leak in this program (which is evident from the console output, we can see that no destructors are called even after main has ended!).

* Explanation (circular reference), since shared pointers are used (for attributes), the class A and class B on the heap have attributes (the shared pointers inside the class) with reference use count as they are pointing to eachother. when the scope of main ends the shared pointers in main are deleted but when it tries to delete the objects (class A and B) on the heap, they see that they have shared pointers in them with non zero use count, hence those heap objects (class A and B) are not deleted and the cause for the leak!

  ```cpp
  #include <iostream>
  #include <memory>
  #include <vector>
  using namespace std;


  class B;   //forward declaration; a forward declaration is a way to declare a class, function, or variable before providing its complete definition.

  class A {
      std::shared_ptr<B> b_ptr;
  public:
      void set_b(std::shared_ptr<B>& b) {
          b_ptr = b;
      }

      A() {
          cout << "constructor of A" << endl;
      }
      ~A() {
          cout << "destructor of A" << endl;
      }
  };


  class B {

      std::shared_ptr<A> a_ptr;     //fix: std::weak_ptr<A> a_ptr;

  public:
      void set_a(std::shared_ptr<A>& a) {
          a_ptr = a;
      }

      B() {
          cout << "constructor of B" << endl;
      }

      ~B() {
          cout << "destrcutor of B" << endl;
      }
  };

  int main() {
      std::shared_ptr<A> a = std::make_shared<A>();
      std::shared_ptr<B> b = std::make_shared<B>();
      a->set_b(b);
      b->set_a(a);
  }

  //constructor of A
  //constructor of B
  ```

* The fix for the problem faced above is using a weak reference for any one of the class attribute. (As shown in the comment above)

<br>
<br>

# Custom Deleter

- C++ smart pointers allows custom deleters, with which we can perform more than just destroying the object on the heap.
- This can be acheived using function or lambdas (other methods must also be there)

## Using a function

- We write a function with a parameter being a raw pointer to the smart pointer and then when we instantiate the smart pointer, we pass the custom deleter.

  ```cpp
  #include <iostream>
  #include <memory>
  using namespace std;

  class Test {
      int data;
  public:
      Test(int data=0)//constructor
      {
          this->data = data;
          cout << "Test object with the data value of " << this->data << " has been instatiated " << endl;
      }
      ~Test() {}	//destructor

  };

  void my_custom_deleter(Test* ptr)
  {
      cout << "my_custom_deleter function is run" << endl;
      delete ptr;
  }

  int main()
  {
      std::shared_ptr<Test> s_ptr{new Test{69}, my_custom_deleter};
  }


  //Test object with the data value of 69 has been instatiated
  //my_custom_deleter function is run
  ```

* We can do the same using lambda functions!
