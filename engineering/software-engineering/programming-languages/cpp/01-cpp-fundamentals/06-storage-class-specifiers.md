> Review this notes after having reviewd oops <br> <br>

# `extern` specifier

- When used in the context of global variables, `extern` is used to declare a variable that is defined in another source file or translation unit. It extends the visibility and linkage of the variable to multiple files, allowing them to access and share the same global variable.

  ```cpp
  //file1.cpp
  int a{10};
  ```

  ```cpp
  //file2.cpp
  #include <iostream>

  extern int a;

  int main()
  {
      std::cout << a << std::endl;  //10
  }
  ```

<br>
<br>
<br>

# `static` specifier

- The `static` keyword has multiple uses based on the context of how it is being used.

<br>

## local static variable (function scope)

- When static is used with a variable inside a function, it preserves the variable's value across multiple function calls. The variable is initialized only once and retains its value between function invocations.

* Static variables reside in the data segment of the process memory. As such, they are already present on the data segment even before the function is called.
* For integral type varibles like int, the default value that is used for initialisaton on the data segment is zero.

  ```cpp
  #include <iostream>

  void add_plot()
  {
      static int num_plots; //track the number of plots plotted
      num_plots++;
      //add plot logic
      std::cout << "total number of plots = " << num_plots << std::endl;
  }

  int main()
  {
      add_plot();
      add_plot();
      add_plot();
  }

  //total number of plots = 1
  //total number of plots = 2
  //total number of plots = 3
  ```

<br>

## global static variable (file scope)

- When static is used with a global variable, it limits the scope of the variable to the current translation unit (source file). The variable is not accessible from other translation units and has internal linkage.

  ```cpp
  //file1.cpp
  static int a{10};
  ```

  ```cpp
  //file2.cpp
  #include<iostream>
  extern int a;

  int main()
  {
    std::cout << a; //error
  }
  ```

<br>

## global static function

- When static is used with a global function, the compiler prohibits it's use in other files even if the declaration is put in that file.

* We can declare the function and use the definition from another translation unit.

  ```cpp
  //file1.cpp
  #include <iostream>

  void fun()
  {
    std::cout << "fun called";
  }
  ```

  ```cpp
  //file2.cpp

  void fun();

  int main()
  {
    fun();
  }

  //fun called
  ```

* However if we make a global function static, we wont be able to do this

<br>

## static data attribute

- Objects will only take responsibility of allocating memory for the non-static data members of the class because objects are created on the stack or heap while static members reside in the data segment.
- We can facilitate the static local variable behaviour for the data attribute of a class by using the static keyword and declaring(also initialise, if needed) that data attribute right after the class declaration.

  ```cpp
  #include <iostream>

  class MyClass
  {
  private:
    static int a;

  public:
    void increment()
    {
      a += 1;
      std::cout << a << std::endl;
    }
  };

  int MyClass::a;			//Initialised to zero by default
  //int MyClass::a =10;	//Custom Initialisation

  int main()
  {
    MyClass obj;
    obj.increment();
    obj.increment();
    obj.increment();
  }

  //1
  //2
  //3
  ```

<br>

## static member functions

- functions dealing only with static data can be qualified as static, as such it is possible to call this member function without any object.
- static member function donot support `this` pointer.

  ```cpp
  #include <iostream>

  class MyClass
  {
  private:
    static int a;

  public:
    static void increment()
    {
      a += 1;
      std::cout << a << std::endl;
    }
  };

  int MyClass::a;			//Initialised to zero by default
  //int MyClass::a =10;	//Custom Initialisation

  int main()
  {
    MyClass::increment();
    MyClass::increment();
  }

  //1
  //2
  ```
