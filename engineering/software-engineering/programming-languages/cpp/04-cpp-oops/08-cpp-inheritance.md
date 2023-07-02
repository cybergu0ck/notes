# Inheritance

- Creating new classes by using the code present in already defined classes, extending the data.
- Inheritance facilitates **_IS-A relationship_**, A Derived object IS A Base object.

* The construction of an derived class object will always be the sum of the sizes of all non-static data members of the base class and the sum size of all non-static data members of the derived class. It does not matter which access specifier we are using at the time of inheritance.
* The Derived Class has all the data members of the Base class and Access Specifiers deals with only access to those data.

<br>
<br>

# Types of Inheritance

- Different behaviour of inheritance is facilitated using the access specifiers in C++.

## Private Inheritance

- syntax: `class Derived : private Base`

<br>

- The base class private members are not accessible in the derived class.
- The protected and public members of the base, if any are accessible in the derived class as 'private' members.

<br>
<br>

## Protected Inheritance

- syntax: `class Derived : protected Base`

<br>

- The base class private members are not accessible in the derived class.
- The protected and public members of the base, if any are accessible in the derived class as 'protected' members.

<br>
<br>

## Public Inheritance

- syntax: `class Derived : public Base`

<br>

- The base class private members are not accessible in the derived class.
- The protected members of the base, if any are accessible in the derived class as 'protected' members.
- The public members of the base, if any are accessible in the derived class as 'public' members.

<br>
<br>

# Constructors and Destructors in regard to Inheritance

- The constructor and destructor methods are not inheritable.
- The derived class object when created, will implicitely invoke only the Derived Class Constructor. The Base class Constructor has to be explicitely called (if needed).
- The derived class object when dying, will implicitely invoke only the Derived Class Destructor. The Base class Destructor has to be explicitely called (if needed).
