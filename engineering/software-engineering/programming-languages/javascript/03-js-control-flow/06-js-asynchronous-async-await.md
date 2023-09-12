# async await

- Simplifies working with asynchronous code and promises by allowing to write it in a more synchronous-like fashion.

- Async/await is built on top of promises and is often used with functions that return promises.

- An `async` function is a function that is defined using the async keyword. It returns a promise implicitly.

- The `await` keyword can be used **_only_** inside an async function to pause the execution until a promise is settled (either resolved or rejected).

```js
function orderPizza() {
  console.log("Pizza was ordered");
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      //simulating the time taken to prepare pizzas
      resolve("Margherita");
      //   reject("Got No Pizza");
    }, 2000);
  });
}

async function eatPizza() {
  const pizza = await orderPizza();
  console.log(`Eating ${pizza}`);
}

function callRavi() {
  console.log("calling Ravi...");
}

eatPizza();
callRavi();

// Pizza was ordered
// calling Ravi...
// Eating Margherita
```

<br>
<br>

## Handling rejection of promise

- It is ideal to use the await inside a try block and use a catch block to catch errors

  ```js
  function orderPizza() {
    console.log("Pizza was ordered");
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        //simulating the time taken to prepare pizzas
        //   resolve("Margherita");
        reject("Got No Pizza");
      }, 2000);
    });
  }

  async function eatPizza() {
    try {
      const pizza = await orderPizza();
      console.log(`Eating ${pizza}`);
    } catch (error) {
      console.log(error);
    }
  }

  function callRavi() {
    console.log("calling Ravi...");
  }

  eatPizza();
  callRavi();

  // Pizza was ordered
  // calling Ravi...
  // Got No Pizza
  ```
