# Synchronous

_Synchronous refers to programming concept where code is executed sequentially, one statement at a time, from top to bottom._

- Each operation **_blocks_** the execution of the subsequent code until it's completed. If an operation takes a long time, the entire program appears to freeze.

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

_Asynchronous refers to programming concept where code is not executed sequentially and certain operations occur independently of the main program flow._

- asynchronous code does not block the execution of subsequent code. Instead, it allows other tasks to run while it waits for the asynchronous operation to complete.

- Examples of a asynchronous code.

  1. Data fetching
  2. Calling Backend API
  3. Loading files
  4. timers and intervals

- Here, setTimeout is an asynchronous function. When the orderPizza is called, the setTimeout function will start executing asynchronously meaning the rest of the code in orderPizza function will be executed without waiting for setTimeout to finish. Hence the pizza is not defined in the rest of the code.

  ```js
  let pizza;
  function orderPizza() {
    console.log("Pizza was ordered");
    setTimeout(() => {
      //simulating the time taken to prepare pizza
      pizza = "Margherita";
    }, 2000);
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
    console.log("Pizza was ordered");
    setTimeout(() => {
      //simulating the time taken to prepare pizza
      pizza = "Margherita";
      callback(); //The callback is called inside the asynchronous function
    }, 2000);
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
