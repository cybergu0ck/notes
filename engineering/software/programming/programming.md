# Programming Paradigms

<br>

## Procedural Programming

- procedural programming is basically a collection of functions, where data (usually declared seperately) are manipulated.
- limitations:
  - functions need to know the structure of data, if structure of the data is changed, then the function must also change for it to work.
  - as programs get large, it is difficult to understand, maintain, reuse, debug, extend.

<br>
<br>

## Object Oriented Programming

- Object-oriented programming (OOP) is a programming paradigm that uses "objects" – data structures consisting of data fields and methods together with their interactions – to design applications and computer programs.
- OOP in C++ is based on the concept of classes. A class is a blueprint for an object. It defines the data that an object will hold and the methods that an object will have.
- When you create an object, you are creating an instance of a class. The object will have its own copy of the data that is defined in the class, and it will be able to call the methods that are defined in the class.

- Advantages:

  - Abstraction : Abstraction is a process of hiding the implementation details of a system from the user, and only the functional details will be available to the user end.
  - Encapsulation: Encapsulation is a method of wrapping up the data and code acting on the data into a single unit.
  - Inheritence : Creating new classes by using the code present in already defined classes, extending the data.
  - Polymorpism : Polymorphism is the ability to use the same code to operate on different types of objects. This makes the code more flexible.

<br>

- Limitations:
  - OOP is not a panacea, it will bad code even worse XD
  - complicated design
  - slower and larger in size

<br>
<br>

## Generic Programming

- Generic programming is a programming paradigm that focuses on writing code that is reusable across different data types. It allows you to create algorithms and data structures that can operate on a variety of types without the need for separate implementations for each type.

- Templates are the primary mechanism for achieving generic programming in C++. Function templates and class templates allow you to write code that can work with different types by using template parameters.

<br>
<br>
<br>

# Websites ranking programming langauages

- [TIOBE index](https://www.tiobe.com/tiobe-index/)
- [PYPL ranking](https://pypl.github.io/PYPL.html)
- [IEEE spectrum ranking](https://spectrum.ieee.org/top-programming-languages-2022)
- [Redmonk ranking](https://redmonk.com/sogrady/2022/10/20/language-rankings-6-22/)

<br>
<br>
<br>

# Developer-Consumer Approach

_The approach of developing code with the consumer in mind._

- Developer is the entity that facilitates the code.
- Consumer is the entity that uses the code.
- It is important that the developper exposes only meaningful and useful code to the consumer while abstracting most of the implementation.

- In C++, the header files (text files) are exposed to the consumer of the C++ library. The C++ library developper must facilitate all the necessary data in the header files while hiding away the implementation in library files (.lib).

<br>
<br>
<br>

## Difference between Error and Exception

_An error in general refers to any deviation from the expected or intended behavior of a program that can happen either during compile time or run time._

- Errors needs to be fixed.

<br>

_Errors detected during execution (Run Time) are called exceptions and are not unconditionally fatal._

- Exceptions can be handled.

<br>
<br>
<br>

# Naming conventions

<br>
<br>

## Hungarian Notation

Naming convention where a prefix is included mostly indicating the variable's data type.

- Examples are "icount", "fvalue" etc.

<br>
<br>

## Camel Case

Naming convention where compound words are joined together and each word's initial letter, except for the first one, is capitalised.

- Examples are "camelCase", "totalAmount", "firstName" etc.

<br>
<br>

## Pascal Case

Naming convention where compound words are joined together and each word's initial letter, even for the first one, is capitalised.

- Examples are "PascalCase", "TotalAmount", "FirstName" etc.

<br>
<br>

## Snake Case

Naming convention where compound words are joined together using underscores and typically lower case is used.

- Examples are "snake_case", "total_amount", "first_name" etc.
