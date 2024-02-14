# Promise

Promise is a built-in object that represents the eventual completion (or failure) of an asynchronous operation and allows the handling of its result when it becomes available.

- Handling asynchronous code using Promise objects involves:

  - The _promise maker_ : The function that makes a promise object and returns it.
  - The _promise receiver_ : Recevies the promise object from the maker and does something with it.

- The promise objects takes a single function (called executor) with two parameters "resolve" and "reject".

  ```js
  function someAsynchronousFunction() {
    //This is the promise maker
    return new Promise(function (resolve, reject) {
      //code
      //resolve or reject
    });
  }
  ```

- The 3 states of the promise object.

  1. Pending : The promise is not yet resolved nor rejected, It represents that the asynchronous operation is still ongoing and the result is not available yet.
  2. Resolved: The promise is fullfilled..
  3. Rejected: The promise is not fullfilled.

- Using promises for the pizza illustration.

  ```js
  let pizza;
  function orderPizza() {
    console.log("Pizza was ordered");
    return new Promise(function (resolve, reject) {
      setTimeout(() => {
        //simulating the time taken to prepare pizza
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

  const orderNumber = orderPizza(); //orderNumber is a Promiseobject!
  orderNumber.then(eatPizza); //If the promise is resolved eatPizza will be called

  // orderPizza().then(eatPizza);     //cleanedup code instead of the above 2 lines
  callRavi();

  // Pizza was ordered
  // calling Ravi...
  // Eating Margherita
  ```

<br>
<br>
<br>

# Handling Reject

The rejection of the promise at the maker end can be handled in 2 ways by the receiver.

<br>

## Second parameter in the `then` method

The rejected object is passed as the parameter to the second function in the then method.

```js
let pizza;
function orderPizza() {
  console.log("Pizza was ordered");
  return new Promise(function (resolve, reject) {
    setTimeout(() => {
      //simulating the time taken to prepare pizza
      //   resolve("Margherita");
      reject("No Pizza");
    }, 2000);
  });
}

function eatPizza(pizza) {
  console.log(`Eating ${pizza}`);
}

function noPizza(error) {
  console.log(error);
}

function callRavi() {
  console.log("calling Ravi...");
}

orderPizza().then(eatPizza, noPizza); //If the promise is rejected noPizza will be called.
callRavi();

// Pizza was ordered
// calling Ravi...
// No Pizza
```

<br>
<br>

## catch method

The rejected object is passed as the parameter to the function present in the catch method.

```js
let pizza;
function orderPizza() {
  console.log("Pizza was ordered");
  return new Promise(function (resolve, reject) {
    setTimeout(() => {
      //simulating the time taken to prepare pizza
      //   resolve("Margherita");
      reject("No Pizza");
    }, 2000);
  });
}

function eatPizza(pizza) {
  console.log(`Eating ${pizza}`);
}

function noPizza(error) {
  console.log(error);
}

function callRavi() {
  console.log("calling Ravi...");
}

orderPizza().then(eatPizza).catch(noPizza); //rejected result is passed as parameter to noPizza
callRavi();

// Pizza was ordered
// calling Ravi...
// No Pizza
```

<br>
<br>
<br>

# Chaining

- We can chain as many promise objects using the `then` and `catch` methods.
- The function (First function if it has two) in the `then` block gets only the resolved object as the parameter and the function in the `catch` method gets only the rejected object as the parameter.

```js
//toggle reject in orderPizza and observe the output

let pizza;
function orderPizza() {
  console.log("Pizza was ordered");
  return new Promise(function (resolve, reject) {
    setTimeout(() => {
      //simulating the time taken to prepare pizza
      resolve("Margherita");
      //   reject("No Pizza");
    }, 2000);
  });
}

function callRavi() {
  console.log("calling Ravi...");
}

function eatPizza(pizza) {
  console.log(`Eating ${pizza}`);
  return new Promise((resolve, reject) => {
    resolve(true);
  });
}

function noPizza(error) {
  console.log(error);
  return new Promise((resolve, reject) => {
    reject(true);
  });
}

function giveGoodRating(rating) {
  if (rating) {
    console.log(`Rating the Pizza 9`);
  }
}

function giveBadRating(rating) {
  if (rating) {
    console.log(`Rating the pizza 0`);
  }
}

orderPizza()
  .then(eatPizza)
  .catch(noPizza)
  .then(giveGoodRating)
  .catch(giveBadRating);
callRavi();

// Pizza was ordered
// calling Ravi...
// Eating Margherita
// Rating the Pizza 9
```

<br>
<br>
<br>

# finally method

- It is used to specify a callback function that will be executed regardless of whether the Promise is resolved (fulfilled) or rejected.

- It allows you to perform cleanup or finalization tasks that should occur no matter what the outcome of the Promise is.

```js
let pizza;
function orderPizza() {
  console.log("Pizza was ordered");
  return new Promise(function (resolve, reject) {
    setTimeout(() => {
      //simulating the time taken to prepare pizza
      resolve("Margherita");
      //   reject("No Pizza");
    }, 2000);
  });
}

function callRavi() {
  console.log("calling Ravi...");
}

function eatPizza(pizza) {
  console.log(`Eating ${pizza}`);
  return new Promise((resolve, reject) => {
    resolve(true);
  });
}

function noPizza(error) {
  console.log(error);
  return new Promise((resolve, reject) => {
    reject(true);
  });
}

function giveGoodRating(rating) {
  if (rating) {
    console.log(`Rating the Pizza 9`);
  }
}

function giveBadRating(rating) {
  if (rating) {
    console.log(`Rating the pizza 0`);
  }
}

function goToBed() {
  console.log(`Going to Sleep`);
}

orderPizza()
  .then(eatPizza)
  .catch(noPizza)
  .then(giveGoodRating)
  .catch(giveBadRating)
  .finally(goToBed);
callRavi();

// Pizza was ordered
// calling Ravi...
// Eating Margherita
// Rating the Pizza 9
// Going to Sleep
```

<br>
<br>
<br>

# Advantages of promises over callbacks

1. We donot have to pass the functions. we can call the functions using the promise objects.
2. Better readability as it avoids the "callback hell" or "pyramid of doom" by providing chaining feature.

<br>
<br>
<br>
