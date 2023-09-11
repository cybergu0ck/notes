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

# Promise

- The promise maker is the function that makes a promise object and returns it.
- The promise receiver calls the maker and does something with the promise object.

<br>

## Promise Object

- The Promise object in JavaScript represents the eventual completion (or failure) of an asynchronous operation and allows you to handle its result when it becomes available.

- It takes a single function (called executor) with two parameters "resolve" and "reject".
- The 3 states of the promise object.
  1. Pending : The promise is not yet resolved nor rejected, It represents that the asynchronous operation is still ongoing and the result is not available yet.
  2. Resolved: The promise is fullfilled..
  3. Rejected: The promise is not fullfilled.

* The advantage of Promise over callback is that we donot have to pass the functions. we can call the functions using the promise objects.

  ```js
  let pizza;
  function orderPizza() {
    console.log("Pizza was ordered");
    return new Promise(function (resolve, reject) {
      setTimeout(() => {
        resolve("Margherita");
        //   reject("No Pizza");
      }, 2000);
    });
  }

  function eatPizza(pizza) {
    console.log(`Eating ${pizza}`);
  }

  function callRavi() {
    console.log("calling Ravi...");
  }

  const orderNumber = orderPizza(); //orderNumber is a Promise object, it is like the orderNumber with which we can collect our pizza later!
  orderNumber.then(
    function (data) {
      pizza = data;
      eatPizza(pizza);
    },
    function (error) {
      console.log(`${error}`);
    }
  );

  callRavi();

  // Pizza was ordered
  // calling Ravi...
  // Eating Margherita
  ```

* The promise object's then method actually takes 2 functions as parameters. One for promise resolution and one for promise rejection.

  ```js
  let pizza;
  function orderPizza() {
    console.log("Pizza was ordered");
    return new Promise(function (resolve, reject) {
      setTimeout(() => {
        //   resolve("Margherita");
        reject("No Pizza");
      }, 2000);
    });
  }

  function eatPizza(pizza) {
    console.log(`Eating ${pizza}`);
  }

  function callRavi() {
    console.log("calling Ravi...");
  }

  const orderNumber = orderPizza(); //orderNumber is a Promise object, it is like the orderNumber with which we can collect our pizza later!
  orderNumber.then(
    function (pass_data) {
      pizza = pass_data;
      eatPizza(pizza);
    },
    function (fail_data) {
      console.log(`${fail_data}`);
    }
  );

  callRavi();

  // Pizza was ordered
  // calling Ravi...
  // No Pizza
  ```

- A cleaned up version of the above code:

  ```js
  let pizza;
  function orderPizza() {
    console.log("Pizza was ordered");
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        resolve("Margherita");
        //   reject("No Pizza");
      }, 2000);
    });
  }

  function eatPizza(pizza) {
    console.log(`Eating ${pizza}`);
  }

  function callRavi() {
    console.log("calling Ravi...");
  }

  function onSucess(data) {
    pizza = data;
    eatPizza(pizza);
  }

  function onError(error) {
    console.log(`${error}`);
  }

  orderPizza().then(onSucess, onError);

  callRavi();

  // Pizza was ordered
  // calling Ravi...
  // Eating Margherita
  ```
