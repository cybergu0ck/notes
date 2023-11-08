# Destructuring

It is a way to extract values from arrays and objects and assign them to variables in a more convinient way.

<br>
<br>

## Array Destructuring

We use square braces with any name for variables.

```js
const myArray = ["first", "second", "third", "fourth", "fifth"];

const [f1, f2] = myArray;

console.log(f1);
console.log(f2);

// first
// second
```

- Skipping values while destructuring.

  ```js
  const myArray = ["first", "second", "third", "fourth", "fifth"];

  const [f1, , f3] = myArray;

  console.log(f1);
  console.log(f3);

  // first
  // third
  ```

- Using [rest operator](rest-spread-operator.md#rest-operator-in-destructuring) to get the remaining values.

<br>
<br>

## Object Destructing

we use curly braces along with the names of the properties of the object we are destructuring.

```js
const myObject = {
  firstProp: 1,
  secondProp: 2,
  thirdProp: 3,
  fourthProp: 4,
};

const { firstProp, secondProp } = myObject;

console.log(firstProp);
console.log(secondProp);

// 1
// 2
```

- We can extract any property in any order.

  ```js
  const myObject = {
    firstProp: 1,
    secondProp: 2,
    thirdProp: 3,
    fourthProp: 4,
  };

  const { firstProp, fourthProp } = myObject;

  console.log(firstProp);
  console.log(fourthProp);

  // 1
  // 4
  ```

- We can provide default values for undefined properties.

  ```js
  const myObject = {
    firstProp: 1,
    secondProp: 2,
    thirdProp: 3,
    fourthProp: 4,
  };

  const { firstProp, fourthProp, newProp = "new value" } = myObject;

  console.log(firstProp);
  console.log(newProp);

  // 1
  // new value
  ```

- We can perform assignment whilst destructuring.

  ```js
  const myObject = {
    firstProp: 1,
    secondProp: 2,
    thirdProp: 3,
    fourthProp: 4,
  };

  const { firstProp: first, secondProp: second } = myObject;

  console.log(first);
  console.log(second);

  //1
  //2
  ```

- Destructuring is commonly used in function parameters.

  ```js
  function printFullName({ firstName, lastName }) {
    console.log(`${firstName} ${lastName}`);
  }

  const person = { firstName: "John", lastName: "Doe" };
  printFullName(person); // "John Doe"
  ```

- Complex destructuring using nesting

  ```js
  const nestedObject = {
    prop1: "value1",
    prop2: { prop3: "value2" },
  };
  const {
    prop1,
    prop2: { prop3 },
  } = nestedObject;

  console.log(prop1); // "value1"
  console.log(prop3); // "value2"
  ```
