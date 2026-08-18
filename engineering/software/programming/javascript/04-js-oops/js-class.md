# The `class` syntax

- The basic syntax is

  ```js
  class MyClass {
    //class methods
    constructor() {
      //code
    }

    method1() {
      //code
    }

    method2() {
      //code
    }
  }

  const obj = new MyClass();
  ```

- Illustration:

  ```js
  class User {
    constructor(name) {
      this.name = name;
    }

    sayHi() {
      alert(this.name);
    }
  }

  // Usage:
  let user = new User("John");
  user.sayHi();
  ```

* What class User {...} construct really does is:

  1. Creates a function named User, that becomes the result of the class declaration. The function code is taken from the constructor method (assumed empty if we don’t write such method).
  1. Stores class methods, such as sayHi, in User.prototype.

<br>
<br>

# Not just syntactic sugar

- Sometimes people say that class is a “syntactic sugar” (syntax that is designed to make things easier to read, but doesn’t introduce anything new), because we could actually declare the same thing without using the class keyword at all.
- However, there are important differences.

  1. First, a function created by class is labelled by a special internal property `[[IsClassConstructor]]`: true. So it’s not entirely the same as creating it manually.The language checks for that property in a variety of places. For example, unlike a regular function, it must be called with `new`.

  1. Class methods are non-enumerable. A class definition sets enumerable flag to false for all methods in the "prototype".

     - That’s good, because if we "for..in" over an object, we usually don’t want its class methods.

  1. Classes always use strict. All code inside the class construct is automatically in strict mode.

<br>
<br>

# Class Expressions

- classes like functions can be defined inside another expression, passed around, returned, assigned etc.

```js
let user = class {
  sayHi() {
    alert("Hi");
  }
};
```

<br>
<br>

# Class Fields

- Previously, our classes only had methods.
- “Class fields” is a syntax that allows to add any properties.

  ```js
  class User {
    name = "john";

    sayHi() {
      alert("HI");
    }
  }

  let user = new User();
  console.log(user.name);
  ```

* **_The important difference of class fields is that they are set on individual objects, not `User.prototype`_**

<br>
<br>

# Making bound methods with class fields

> Fill notes

<br>
<br>
