# Factory Functions

The factory function pattern is similar to constructors, but instead of using `new` to create an object, factory functions simply set up and return the new object when you call the function.

```js
const personFactory = (name, age) => {
  const sayHello = () => console.log(`${name} says Hello.`);
  return { name, age, sayHello };
};

let myGuy = personFactory("steve", 69);

console.log(myGuy.sayHello()); // steve says Hello.
```

- line 3 in the above code is a shorthand for `return {name: name, age: age, sayHello: sayHello};`

<br>
<br>

# Closure

- In JavaScript, closure is a feature that allows a function to remember and access its lexical scope even when it's executed outside that scope.

* A closure is created when a function is defined inside another function and the inner function references variables from the outer function. The inner function _"closes over"_ the outer function's variables, meaning that it has access to those variables even after the outer function has finished executing.

  ```js
  const personFactory = (name, age) => {
    const sayHello = () => console.log(`${name} says Hello.`);

    const secret = "123!@#";
    const gotSecret = () => {
      if (secret) {
        return true;
      } else {
        return false;
      }
    };

    return { name, age, sayHello, gotSecret };
  };

  let myGuy = personFactory("steve", 69);

  console.log(myGuy.gotSecret()); //true
  console.log(myGuy.secret); //undefined
  ```

* In the above code, we can see that we donot have the access to the constant `secret`. However, we have access to the gotSecret function (which has access to `secret` because of **_closure_**)
* We can create private variables, constants and functions using closure.

* To understand the crux of this and the lexical environment, head over to [javascript.info](https://javascript.info/closure)

<br>
<br>

# Inheritence with Factories

- factory functions do not utilise the prototypes.
- In order to use inheritence with factory functions we must do this:

  ```js
  const Person = (name) => {
    const sayName = () => console.log(`my name is ${name}`);
    return { sayName };
  };

  const Nerd = (name) => {
    // simply create a person and pull out the sayName function with destructuring assignment syntax!
    const { sayName } = Person(name);
    const doSomethingNerdy = () => console.log("nerd stuff");
    return { sayName, doSomethingNerdy };
  };

  const jeff = Nerd("jeff");

  jeff.sayName(); // my name is jeff
  jeff.doSomethingNerdy(); // nerd stuff
  ```

<br>
<br>

# The module pattern

- This is related to IIFE (Immediately invoked function expression) and not ES6 javascript modules!

- It offers encapsulation.

- The concepts are exactly the same as the factory function. However, instead of creating a factory that we can use over and over again to create multiple objects, the module pattern wraps the factory in an IIFE

* The syntax is something like:

  ```
  const moduleName = (factoryFucntion)();
  ```

* Example:

  ```js
  const calculator = (() => {
    const add = (a, b) => a + b;
    const sub = (a, b) => a - b;
    const mul = (a, b) => a * b;
    const div = (a, b) => a / b;

    return { add, sub, mul, div };
  })();

  console.log(calculator.add(10, 20)); //30
  ```
