# Syntax for writing functions in js

```js
// function definition
function foo() {
  console.log("Hi from foo");
}

//function call
foo();

//Hi from foo
```

> Function vs Methods <br> Functions that are part of objects are called methods.

<br>
<br>

# Function parameters

## Optional parameters

```js
const myArray = ["I", "love", "chocolate", "frogs"];
const madeAString = myArray.join(" ");
console.log(madeAString);
// returns 'I love chocolate frogs'

const madeAnotherString = myArray.join();
console.log(madeAnotherString);
// returns 'I,love,chocolate,frogs'
```

<br>

## Default paramters

If you're writing a function and want to support optional parameters, we can specify default values by adding = after
the name of the parameter, followed by the default value:

```js
function hello(name = "Chris") {
  console.log(`Hello ${name}!`);
}

hello("Ari"); // Hello Ari!
hello(); // Hello Chris!
```

<br>
<br>

# Anonymous functions

functions without names are anonymous functions, we mostly see anonymous functions when a function expects to receive another function as a parameter.

- Normal function definition,

  ```js
  function myFunction() {
    alert("hello");
  }
  ```

- Defining anonymously,

  ```js
  (function () {
    alert("hello");
  });
  ```

  <br>

### Illustration of using anonymous fucntions as parameters

- Using normal definition,

  ```js
  function logKey(event) {
    console.log(`You pressed "${event.key}".`);
  }

  textBox.addEventListener("keydown", logKey);
  ```

- Using anonymous function,

  ```js
  textBox.addEventListener("keydown", function (event) {
    console.log(`You pressed "${event.key}".`);
  });
  ```

<br>
<br>

# Arrow functions

An example of a regular javascript function.

```js
function greet(message) {
  const greeting = `The AI says ${message}`;
  return greeting;
}

const greetingFromAI = greet("hello");
console.log(greetingFromAI);

// The AI says hello
```

An example of javascript arrow function.

```js
// Javascript Arrow Functions
const greet = (message) => {
  const greeting = `The AI says ${message}`;
  return greeting;
};

const greetingFromAI = greet("hello");
console.log(greetingFromAI);

// The AI says hello
```

- Arrow functions without curly braces _"returns"_ the single line statement.

  ```js
  const greet = (message) => `The AI says ${message}`;

  const greetingFromAI = greet("hello");
  console.log(greetingFromAI);

  // The AI says hello
  ```

- If the arrow function takes in a single parameter, we can skip the parenthesis.

  ```js
  const greet = (message) => `The AI says ${message}`;

  const greetingFromAI = greet("hello");
  console.log(greetingFromAI);
  ```

- If the arrow funciton takes no parameters, then we have to use an empty parenthesis.

  ```js
  const greet = () => `The AI says Hey there`;

  const greetingFromAI = greet("hello");
  console.log(greetingFromAI);

  // The AI says Hey there
  ```

- Arrow functions can return back functions which can be arrow functions!

  ```js
  const res = greet();
  console.log(res); // [Function (anonymous)]
  console.log(typeof res); // function

  greet()(); //arrow function speaking

  // res(); //same as greet()()
  ```

<br>
<br>
