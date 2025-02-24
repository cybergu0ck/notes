# Generic Programming with macros

- This is not a good practice but must be known to deal with legacy C++ code (a lot of it is out there)

* macros begin with a # sign and all directives that begin with # are preprocessor directives.
* Preprocessor directives doesn't know C++, it just replaces the stuff wherever it is used! (i.e. simple substitution)

* There is no type assocaiated with macros, the preprocessor is doing simple substituition

  ```cpp
  #include <iostream>

  #define PI 3.16

  int main()
  {
      double radius{ 1 };
      double area = PI * radius * radius; //the preprocessor just replaces the PI with 3.16 here
      std::cout << area << std::endl;
  }
  ```

* An illustrative example of why it is bad practice to use this

  ```cpp
  #include <iostream>

  #define SQUARED 5*5

  int main()
  {
      double wrong_ans = 100 / SQUARED;  //we expect 4 but preprocessor just replaces it and we get 100 / 5* 5
      std::cout << wrong_ans << std::endl;  //but we get 100;
  }
  ```

* macros with arguments are even more prone to bugs

  ```cpp
  #include <iostream>

  #define SQUARE(a) a*a

  //#define SQUARE(a) (a*a) is better!

  int main()
  {
      int two_squared = SQUARE(2);
      std::cout << two_squared << std::endl;  //4
  }
  ```

<br>
<br>
<br>

# Generic Programming with Function Templates

- C++ templates are like blueprints and the compiler generates the appropriate functions/class from the templates.
- A function template is useful, when the business logic (code inside the function) remains the same, irrespective of the input data-type.
- Example showcasing the use of function templates.

  ```cpp
  #include <iostream>

  template <typename T1, typename T2>

  void Add(T1 x, T2 y)
  {
    std::cout << x << " + " << y << " = " <<  x+y << std::endl;
  }

  int main()
  {
    Add(10, 20);		//int parameters
    Add(1.1f, 1.1f);	//float parameters
    Add(1, 1.2);		//An int and a double
  }


  //10 + 20 = 30
  //1.1 + 1.1 = 2.2
  //1 + 1.2 = 2.2
  ```

<br>

> Confusion reagrding using templates vs function overloading <br> <br>
> A function template must be preffered, when the business logic remains the same, irrespective of the input data-type and function overloading must be preffered, when the business-logic of the function keeps changing, with change in input-datatype.

<br>

- When the template is used, the appropriate code is instantiated and it is this code that goes into the binary and not the template code itself. Hence the code with tempaltes must be shared as text files i.e. cpp and h files and not obj or lib file. (this is evident in stl library)

* We can specialise the function template for a particular type. In the following code, Add function template is specialised for char data types.

  ```cpp
  #include <iostream>

  template <typename T>
  void Add(T x, T y)
  {
    T res;
    res = x + y;
    std:: cout << x << " + " << y << " = " << res << std::endl;
  }

  template<>
  void Add(char x, char y)
  {
    std::cout << "cannot add characters" << std::endl;
  }

  int main()
  {
    Add('x', 'y');		//will call the specialised function template
  }

  //cannot add characters
  ```

* Explicit instantiation of function templates

  ```cpp
  #include <iostream>

  template <typename T1, typename T2, typename T3>

  T3 Add(T1 x, T2 y)
  {
    T3 res = x + y;
    return res;
  }

  int main()
  {

    std::cout << Add<float, int, float>(1.2, 5) << std::endl;
  }

  //6.2
  ```

* If we are dealing with code where the return type of function template is typename, it is good discipline to maintain the order, i.e. keep the typename that would be used for return type in first place (see code) so that we have to explicitely mention only one type, the return type.

  ```cpp
  #include <iostream>
  using namespace std;

  template < typename T1, typename T2, typename T3>
  T1 Add(T2 x, T3 y)
  {
    return x + y;
  }

  int main()
  {
    float result1;
    result1 = Add<float>(50.5, 50); //explicit instantiation with the discipline
    cout << result1 << endl;
  }
  ```

* If we want to use user defined classes with template funcitons, we must make sure that it supports the opeations and methods

  ```cpp
  #include <iostream>
  #include <string>

  template <typename T>

  T min(T a, T b)
  {
      return (a < b) ? a : b;  //return a if a < b else return b
  }


  struct Person
  {
      std::string name;
      int age;

      //overloaded assignment operator
      bool operator<(const Person& rhs)const
      {
          return this->age < rhs.age; //this takes care of the (a<b) in the template function!
      }
  };


  int main()
  {
      Person p1{ "Curly", 19};
      Person p2{ "Moey", 25 };
      Person p3 = min(p1, p2);
      std::cout << p3.name << std::endl;  //Curly
  }
  ```

<br>
<br>
<br>

# Generic programming with class templates

- We can use templates to create class objects. The syntax can be difficult to remember, so keep reviewing:

  ```cpp
  #include <iostream>

  template <typename T=int>
  class MyClass
  {
    T a;
  public:
    MyClass(T);
    void add_one();
  };

  template <typename T> MyClass<T>::MyClass(T x) : a{ x }
  {
    //check out the syntax for defining the functions outside the decalration!
  }

  template <typename T> void MyClass<T>::add_one()
  {
    std::cout << "The data attribute " << a  << " is of type " << typeid(T).name() << ". Adding 1 results in " << a + 1 << std::endl;
  }


  int main()
  {
    MyClass<double> obj1{ 69.69 };
    obj1.add_one();

    MyClass<> obj2{ 21 };	//int is default, see the template declaration line at the top
    obj2.add_one();

    MyClass obj3{ 12.4f };	//C++17 standard
    obj3.add_one();

  }

  //The data attribute 69.69 is of type double.Adding 1 results in 70.69
  //The data attribute 21 is of type int.Adding 1 results in 22
  //The data attribute 12.4 is of type float.Adding 1 results in 13.4
  ```

* We can specalise a member function for a specific data type like we did with function templates.

  ```cpp
  #include <iostream>

  template <typename T=int>
  class MyClass
  {
    T a;
  public:
    MyClass(T);
    void add_one();
  };

  template <typename T> MyClass<T>::MyClass(T x) : a{ x }
  {
    //check out the syntax for defining the functions outside the decalration!
  }

  template <typename T> void MyClass<T>::add_one()
  {
    std::cout << "The data attribute " << a  << " is of type " << typeid(T).name() << ". Adding 1 results in " << a + 1 << std::endl;
  }


  //specialised member function for char type
  template<> void MyClass<char>::add_one()
  {
    std::cout << " Cannot use this method for char type" << std::endl;
  }


  int main()
  {
    MyClass<double> obj1{ 69.69 };
    obj1.add_one();

    MyClass<char> obj2{ 'x' };
    obj2.add_one();

  }

  //The data attribute 69.69 is of type double.Adding 1 results in 70.69
  //Cannot use this method for char type
  ```

* We can specialise the entire class for a specific data type. Note the block comment in the code.

  ```cpp
  #include <iostream>

  template <typename T=int>
  class MyClass
  {
    T a;
  public:
    MyClass(T);
    void add_one();
  };

  template <typename T> MyClass<T>::MyClass(T x) : a{ x }
  {
    //check out the syntax for defining the functions outside the decalration!
  }

  template <typename T> void MyClass<T>::add_one()
  {
    std::cout << "The data attribute " << a  << " is of type " << typeid(T).name() << ". Adding 1 results in " << a + 1 << std::endl;
  }

  /*
  - The entire class can be specialised for a specific data type.
  - This class template can have entirely new data attributes and member functions. (It's like an new class)
  - Creating a seperate new class doesn't make sense as we need the above class to support a data type.
  - The definition and declaration must be inside the class itself.
  */

  template <>
  class MyClass<char>
  {
    char c;
  public:
    MyClass(char x) : c{ x }
    {
      //definition and declartion must be inside this class only when specialising entire class!
    }

    void specialised_foo()
    {
      std::cout << "specialised foo called" << std::endl;
    }
  };


  int main()
  {
    MyClass<double> obj1{ 69.69 };
    obj1.add_one();

    MyClass<char> obj2{ 'x' };
    obj2.specialised_foo();

  }

  //The data attribute 69.69 is of type double.Adding 1 results in 70.69
  //specialised foo called
  ```

* We can forbid the class template to support a given type. In traditional C++, it is done by making the constructor in the specialised class as private. With Modern C++, we can use the delete keyword.

  ```cpp
  #include <iostream>

  template <typename T=int>
  class MyClass
  {
    T a;
  public:
    MyClass(T);
    void add_one();
  };

  template <typename T> MyClass<T>::MyClass(T x) : a{ x }
  {
    //check out the syntax for defining the functions outside the decalration!
  }

  template <typename T> void MyClass<T>::add_one()
  {
    std::cout << "The data attribute " << a  << " is of type " << typeid(T).name() << ". Adding 1 results in " << a + 1 << std::endl;
  }


  template <>
  class MyClass<char>
  {
    char c;
  public:
    MyClass() = delete;   //This is Modern C++
  };


  int main()
  {
    MyClass<double> obj1{ 69.69 };
    obj1.add_one();

    //MyClass<char> obj2{ 'x' };	//error
  }
  ```
