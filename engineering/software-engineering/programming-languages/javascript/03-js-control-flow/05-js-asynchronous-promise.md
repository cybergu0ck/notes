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
const orderNumber = orderPizza(); //orderNumber is a Promiseobject, it is like the orderNumber with which we can collect ourpizza later!
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

- The promise object's then method actually takes 2 functions as parameters. One for promise resolution and one for promise rejection.

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

* A cleaned up version of the above code:

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

  orderPizza().then(eatPizza, onError);
  //orderPizza().then(onSucess, onError);     //we can just pass the eatPizza function directly instead of onSucess!

  callRavi();

  // Pizza was ordered
  // calling Ravi...
  // Eating Margherita
  ```

<br>
<br>
<br>

# Chaining

- We can chain as many promise objects using the `then` method.

  ```js
  let pizza;
  function orderPizza() {
    console.log("Pizza was ordered");
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        //simulating the time taken to prepare pizzas
        resolve("Margherita");
        //   reject("No Pizza");
      }, 2000);
    });
  }

  function eatPizza(pizza) {
    console.log(`Eating ${pizza}`);
    return new Promise((resolve, reject) => {
      //simulating the time taken to eat the pizza
      setTimeout(() => {
        resolve(7);
      }, 2000);
    });
  }

  function ratePizza(rating) {
    console.log(`Rated it ${rating}`);
  }

  function callRavi() {
    console.log("calling Ravi...");
  }

  function onError(error) {
    console.log(`${error}`);
  }

  orderPizza().then(eatPizza, onError).then(ratePizza);

  callRavi();

  // Pizza was ordered
  // calling Ravi...
  // Eating Margherita
  // Rated it 7
  ```

<br>
<br>

## catch method

- The rejection of the promise at the maker end can be handled in 2 ways by the receiver.

1. Use second parameter in the `then` method (as seen in above illustrations)
2. Use the catch method.

<br>

The `catch` method is used to handle any errors or rejections that occur in the promise chain.

```js
let pizza;
function orderPizza() {
  console.log("Pizza was ordered");
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      //simulating the time taken to prepare pizzas
      // resolve("Margherita");
      reject("Got No Pizza");
    }, 2000);
  });
}

function eatPizza(pizza) {
  console.log(`Eating ${pizza}`);
  return new Promise((resolve, reject) => {
    //simulating the time taken to eat the pizza
    setTimeout(() => {
      resolve(7);
    }, 2000);
  });
}

function callRavi() {
  console.log("calling Ravi...");
}

function noPizza(error) {
  console.log(`${error}`);
  return new Promise((resolve, reject) => {
    reject(0);
  });
}

function ratePizza(rating) {
  console.log(`Rated it ${rating}`);
}

function badRating(rating) {
  console.log(`Rated it ${rating}`);
}

orderPizza().then(eatPizza).catch(noPizza).then(ratePizza).catch(badRating);

callRavi();

// Pizza was ordered
// calling Ravi...
// Got No Pizza
// Rated it 0
```

<br>
<br>

## finally method

- It is used to specify a callback function that will be executed regardless of whether the Promise is resolved (fulfilled) or rejected.

- It allows you to perform cleanup or finalization tasks that should occur no matter what the outcome of the Promise is.

```js
let pizza;
function orderPizza() {
  console.log("Pizza was ordered");
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      //simulating the time taken to prepare pizzas
      // resolve("Margherita");
      reject("Got No Pizza");
    }, 2000);
  });
}

function eatPizza(pizza) {
  console.log(`Eating ${pizza}`);
  return new Promise((resolve, reject) => {
    //simulating the time taken to eat the pizza
    setTimeout(() => {
      resolve(7);
    }, 2000);
  });
}

function callRavi() {
  console.log("calling Ravi...");
}

function noPizza(error) {
  console.log(`${error}`);
  return new Promise((resolve, reject) => {
    reject(0);
  });
}

function ratePizza(rating) {
  console.log(`Rated it ${rating}`);
}

function badRating(rating) {
  console.log(`Rated it ${rating}`);
}

function goToBed() {
  console.log("Going to bed");
}

orderPizza()
  .then(eatPizza)
  .catch(noPizza)
  .then(ratePizza)
  .catch(badRating)
  .finally(goToBed);

callRavi();

// Pizza was ordered
// calling Ravi...
// Got No Pizza
// Rated it 0
// Going to bed
```

<br>
<br>
<br>

# Advantages of promises over callbacks

1. We donot have to pass the functions. we can call the functions using the promise objects.
2. Better readability as it avoids the "callback hell" or "pyramid of doom" by providing chaining feature.

<br>
<br>
