# Terminology

- **Exception** : an object or primitive type that signals that an error has occurred.
- **Throwing an exception (Raising an exception)** : It is the code that detects an error that has(will) occurred(occur) but doesn't know how to handle it.
- **Catching an exception (Handling an exception)** : It is the code that handles the exception.

<br>
<br>

# C++ Exception Handling syntax

    ```
    try
    {
        //code here can potentially throw an exception!
    }

    catch (exception obj)
    {
        //code here is run only if the try block code throws an exception and that object mathches
        //the exception obj mentioned above.
    }
    ```

- An illustration without exception handling, a program that prints miles per gallon

  ```cpp
  int main()
  {
      int miles{ 100 };
      int gallons{ 0 };
      double miles_per_gallon;
      if (gallons != 0)
      {
          miles_per_gallon = miles / gallons;
          std::cout << "fuel economy is " << miles_per_gallon << endl;
      }
      else
      {
          std::cerr << "cannot divide by zero" << endl;
      }
  }
  ```

- The same program using exception handling

  ```cpp
  int main()
  {
      int miles{ 100 };
      int gallons{ 0 };
      double miles_per_gallon;

      try
      {
          if (gallons == 0)
              throw 0;
          miles_per_gallon = miles / gallons;
          std::cout << "fuel economy is " << miles_per_gallon << endl;
      }
      catch(int &ex)
      {
          std::cout << "cannot divide by zero" << endl;
      }
  }
  ```
