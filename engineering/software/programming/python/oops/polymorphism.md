[← Back to oops](./contents.md)

# Contents

- [Polymorphism](#polymorphism)
  - [2.a Polymorphisim of Operators](#2a-polymorphisim-of-operators)
  - [2.b Polymorphism of Functions (Overloading Functions)](#2b-polymorphism-of-functions-overloading-functions)

<br>
<br>
<br>




[← Back to oops](./contents.md)

# Polymorphism

- Polymorphism is the ability of a variable, function, or object to take on multiple forms.
- It refers to the use of a single type entity (method, operator or object) to represent different types in different scenarios.

<br/>

## 2.a Polymorphisim of Operators

Another kind of built-in polymorphism in Python is the ability to override an operator in Python depending upon the operands used.

- '+' is used for arithmetic addition when used with numbers and as concatination when used with strings.

<br/>

## 2.b Polymorphism of Functions (Overloading Functions)

Overloading Built in functions :

- len() can be used with different data types like list, tuple, string

Overloading User Defined Functions :

- Python doesn't support conventional C++ function overloading, it considers the latest function signatures.
  1.  the workaround for that is to use default arguments with "None".

      ```python
      class Student:
          def hello(self, name=None):
              if name is not None:
                  print('Hey ' + name)
              else:
                  print('Hey ')


      std = Student()

      std.hello()

      std.hello('Nicholas')  #same function but diff behaviour

      #>Hey
      #Hey Nicholas
      ```

  2.  function overloading using different classes (Illusration 2)

      ```python
      class Dog:
          def speak(self):
              print('Woof Roof')

      class Cat:
          def speak(self):
              print('Meow')

      myDog = Dog()
      myCat = Cat()

      for animal in (myDog, myCat):
          animal.speak()

      #>Woof Roof
      #>Meow
      ```

  3.  method overloading using inheritence (Illustration 3)

      ```python
      class Parent:
          def foo(self):
              print ('Coming hot from Parent Class')

      class Child(Parent):
          def foo(self):
              print('coming hot from Child class')

      parentObj = Parent()
      parentObj.foo()

      childObj = Child()
      childObj.foo()

      #Coming hot from Parent Class
      #coming hot from Child class
      ```
