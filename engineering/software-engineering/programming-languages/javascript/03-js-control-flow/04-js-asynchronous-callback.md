# Synchronous

<br>

## Illustration

- Illustartion of synchronous code. We have 3 functions orderPizza, callRavi and eatPizza that does exactly what it sounds like. We can see that The code is executed line by line.

  ```js
  let pizza;
  function orderPizza() {
    pizza = "Margherita";
    console.log("Pizza was ordered");
  }

  function eatPizza(pizza) {
    console.log(`Eating ${pizza}`);
  }

  function callRavi() {
    console.log("calling Ravi...");
  }

  orderPizza();
  callRavi();
  eatPizza(pizza);

  // Pizza was ordered
  // calling Ravi...
  // Eating Margherita
  ```

<br>
<br>
<br>

# Asynchronous

- "asynchronous" refers to a programming paradigm that allows certain operations to occur independently of the main program flow.
- Examples of a asynchronous code.
  1. Data fetching
  2. Calling Backend API
  3. Loading files
  4. timers and intervals

<br>

## Illustration

- Here, setTimeout is an asynchronous function. When the orderPizza is called, the setTimeout function will start executing asynchronously meaning the rest of the code in orderPizza function will be executed without waiting for setTimeout to finish. Hence the pizza is not defined in the rest of the code.

  ```js
  let pizza;
  function orderPizza() {
    setTimeout(() => {
      pizza = "Margherita";
    }, 2000);
    console.log("Pizza was ordered");
  }

  function eatPizza(pizza) {
    console.log(`Eating ${pizza}`);
  }

  function callRavi() {
    console.log("calling Ravi...");
  }

  orderPizza();
  callRavi();
  eatPizza(pizza);

  // Pizza was ordered
  // calling Ravi...
  // Eating undefined
  ```

<br>
<br>
<br>

# Callback

- A callback is a function that you pass as an argument to another function, and it gets executed when the asynchronous operation is complete.
- Callbacks are often used with functions like setTimeout, setInterval, and when making asynchronous requests using methods like fetch or handling events.

  ```js
  let pizza;
  function orderPizza(callback) {
    setTimeout(() => {
      pizza = "Margherita";
      callback(pizza);
    }, 2000);
    console.log("Pizza was ordered");
  }

  function eatPizza(pizza) {
    console.log(`Eating ${pizza}`);
  }

  function callRavi() {
    console.log("calling Ravi...");
  }

  orderPizza(eatPizza);
  callRavi();

  // Pizza was ordered
  // calling Ravi...
  // Eating Margherita
  ```

<br>
<br>
<br>
