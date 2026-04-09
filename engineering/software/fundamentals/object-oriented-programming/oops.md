# Contents

- [Object Oriented Programming](#object-oriented-programming)
  - [Encapsulation](#encapsulation)
  - [Abstraction](#abstraction)
  - [Inheritance](#inheritance)
  - [Polymorphism](#polymorphism)
    - [Difference between abstract class and interface](#difference-between-abstract-class-and-interface)

<br>
<br>
<br>




# Object Oriented Programming

<br>
<br>

## Encapsulation

Encapsulation is the concept of wrapping up information and behaviour and managing (allowing or restricting) access to it.

<br>
<br>

## Abstraction

Abstraction is the concept of hiding internal implementation logic and exposing only the necessary.

<br>
<br>
<br>

## Inheritance

Inheritance is the concept of building classes upon the characteristics and behavior of other classes by establishing a parent-child relationship.

<br>
<br>
<br>

## Polymorphism

Polymorphism is the concept of using different objects in a single, common way.

<br>
<br>

### Difference between abstract class and interface

| Abstarct class                                   | Interface                                            |
| ------------------------------------------------ | ---------------------------------------------------- |
| Represents base class with shared implementation | Represents a pure contract                           |
| Models an "is a" relation                        | Defines what a class "must do"                       |
| Contains partial implementation                  | Contains no implementation (purely abstract methods) |
| Objects can be instantiated                      | Objects cannot be instantiated                       |

<br>

- In C++
  - An interface is implemented as a class with only purely virtaul functions as it does not have a specific keyword for `interface`.
  * An abstract class is a class with at least one pure virtual function.
