# The Prototype

- Every object in javascript has a _prototype_, which is essentially the parent of the object!
- _prototype_ is also an object!

<br>

## `[[Prototype]]`

- `[[Prototype]]` is a hidden private property that all objects have in Javascript, it holds a reference to the object’s _prototype_.

<br>

## `__proto__`

- The `__proto__ `property is a simple accessor property on `Object.prototype` (More on this eventually) consisting of a getter and setter function.
- This is the depricated way of accessing the `[[Prototype]]` of an object.

<br>

## `Object.getPrototypeOf()` and `Object.setPrototypeOf()`

- `Object.getPrototypeOf(obj)` returns the `[[Prototype]]` of obj.
- `Object.setPrototypeOf(obj, proto)` sets the `[[Prototype]]` of obj to proto.
- These are the modern ways to access the `[[Prototype]]`

<br>
<br>

# Setting a protoype

There are many ways to do this, here are few

## Using a constructor

- In JavaScript, all functions have a property named `prototype`(This is not to be confused with whatever `[[Property]]` refers to!). When you call a function as a constructor, this property is set as the prototype of the newly constructed object (by convention, in the property named `[[Property]]`).

  ```js
  //constructor function
  function Human(name) {
    this.name = name;
  }

  //new object
  let myGuy = new Human("steve");
  ```

  ![image](../_assets/proto1.jpg)

<br>

## Using `Object.create()`

> Fill Notes

<br>

## Using `Object.setPrototypeOf()`

- `Object.setPrototypeOf(obj, proto)` sets the `[[Prototype]]` of obj to proto.

  ```js
  let car = {
    wheels: 4,
    color: "red",
    type: "gasoline",
  };

  let telsa = {
    type: "electric",
  };

  Object.setPrototypeOf(tesla, car); //Sets "car" object as the [[Protoype]] of tesla.
  ```

  > Add Image

<br>
<br>

# Prototypal Inheritence

> Add Image

- A better way to create objects using functions.

  ```js
  //constructor definition
  function Player(name, marker) {
    //properties
    this.name = name;
    this.marker = marker;
    //method
    this.sayName = function () {
      console.log(name);
    };
  }

  //calling the constructor
  const player1 = new Player("steve", "X");
  player1.sayName(); //logs 'steve'

  const player2 = new Player("rogers", "X");
  player2.sayName(); //logs 'rogers'
  ```
