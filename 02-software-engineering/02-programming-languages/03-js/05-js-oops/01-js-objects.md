- While primitive datatype's values have only one thing, objects are used to store keyed collections of various data and more complex entities.

<br>
<br>

# Creating Objects using Literals

- An object can be created with figure brackets {…} with an optional list of **properties**. A property is a _“key: value” pair_, where key is a string (also called a “property name”), and value can be anything.

- An empty object can be created using one of two syntaxes (Generally Object Literal Syntax is used):

  ```js
  let user = new Object(); // "object constructor" syntax
  let user = {}; // "object literal" syntax
  ```

- Creating objects with **Object Literal Syntax**.

  ```js
  let user = {     // an object
  name: "John",  // by key "name" store value "John"
  age: 30        // by key "age" store value 30
  "likes chocolates" : false //mult-word properties must be enclosed with ""
  };
  ```

  <br>

## Setting Properties

- Setting properties using dot notation and assignment operator:

  ```js
  user.isCool = true;
  ```

- Setting multiword properties using quotes and square brackets:

  ```js
  user["likes birds"] = true;
  ```

  <br>

## Accessing Properties

- We can access property values using dot notation:

  ```js
  console.log(user.name); //John
  console.log(user.age); //30
  ```

- We can access multiword properties using square brackets:
  ```js
  console.log(user["likes chocolates"]);
  ```

<br>

## Deleting Properties

- We can delete property using `delete` operator:

  ```js
  delete user.age;
  ```

- deleting multiword properties:

  ```js
  delete user["likes birds"];
  ```

<br>
<br>

# Creating objects using Constructors

- Constructors are functions, we can create objects by calling the constructors with the `new` keyword.

  ```js
  //constructor definition

  function Player(name, marker) {
    this.name = name;
    this.marker = marker;

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

  <br>
  <br>

# Property Value shorthand

- In real code, we often use existing variables as values for property names.

  ```js
  function makeUser(name, age) {
    return {
      name: name,
      age: age,
      // ...other properties
    };
  }

  let user = makeUser("John", 30);
  console.log(user.name); // John
  ```

- We can use the _property value shorthand_ to make the above code shorter:

  ```js
  function makeUser(name, age) {
    return {
      name,
      age,
    };
  }
  ```

- We can use both normal property and shorthands in the same object!

  ```js
  function makeUser(name, age) {
    return {
      name,
      age: 99,
    };
  }
  ```

<br>
<br>

# Property names limitations

Propery names (the key's) of Objects have no limitations (language reserved keyword can be used)

<br>
<br>

# Property existence test, `in` opertaor

- Reading a non-existing property just returns `undefined`.

  ```js
  let user = { name: "John", age: 30 };
  console.log("age" in user); //true
  ```

  <br>
  <br>

# The "for..in" loop

- To walk over all keys of an object, there exists a special form of the loop: **for..in**.

  ```js
  let user = {
    name: "John",
    age: 30,
    "likes chocolates": false,
  };

  for (key in user) {
    console.log(key);
  }

  //name
  //age
  //likes chocolates
  ```

<br>
<br>

# Object references and copying

One of the fundamental differences of objects versus primitives is that objects are stored and copied **_“by reference”_**, whereas primitive values: strings, numbers, booleans, etc – are always copied **_“as a whole value”_**.

<br>

## Illustration

- From the snippet below, we have two independent variables, each one storing the string "Hello!".
  ```js
  let message = "Hello!";
  let phrase = message;
  ```

> Add image

- **_A variable assigned to an object stores not the object itself, but its “address in memory” – in other words “a reference” to it._**

  ```js
  let user = {
    name: "John",
  };
  ```

* The object is stored somewhere in memory while the `user` variable has a 'reference" to it.

* **_When an object variable is copied, the reference is copied, but the object itself is not duplicated._**

  ```js
  let user = { name: "John" };
  let admin = user; // copy the reference
  ```

> add image

```js
let user = { name: "John" };
let admin = user;
admin.name = "Pete"; // changed by the "admin" reference
alert(user.name); // 'Pete', changes are seen from the "user" reference
```

> Fill Notes
