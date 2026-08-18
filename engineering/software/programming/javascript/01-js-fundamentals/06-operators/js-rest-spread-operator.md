# Rest Operator

- `...` can be either the rest operator or spread operator based on how it is used.

- The rest operator is used for [destructuring](destructuring.md#destructuring).

<br>
<br>

## Rest operator in destructuring

```js
const myArray = ["first", "second", "third", "fourth", "fifth"];

const [f1, f2, ...others] = myArray;

console.log(f1);
console.log(f2);
console.log(others);

// first
// second
// [ 'third', 'fourth', 'fifth' ]
```

<br>
<br>

# Spread Operator

<br>
<br>

## Spreading Arrays

- Using an array variable inside another array would result in something like this.

  ```js
  const myArray = [1, 2, 3];
  const updatedArray = [myArray, 4, 5, 6];
  console.log(updatedArray);

  // [ [ 1, 2, 3 ], 4, 5, 6 ]
  ```

- We can spread the values of the array inside another array using the spread operator.

  ```js
  const myArray = [1, 2, 3];
  const updatedArray = [...myArray, 4, 5, 6];
  console.log(updatedArray);
  // [ 1, 2, 3, 4, 5, 6 ]
  ```

- Unlike the rest operator which should be used at the end while destructuring, spread operator can be used anywhere.

  ```js
  const myArray = [1, 2, 3];
  const updatedArray = [4, 5, ...myArray, 6];
  console.log(updatedArray);

  // [ 4, 5, 1, 2, 3, 6 ]
  ```

<br>
<br>

## Spreading Objects

```js
const myObject = {
  title: "alchemist",
  author: "paulo coelho",
  genre: "fiction",
  pages: 1000,
};

const updatedObject = { ...myObject, rating: 5 };

console.log(updatedObject);

/* 
{
  title: 'alchemist',
  author: 'paulo coelho',
  genre: 'fiction',
  pages: 1000,
  rating: 5
} 
*/
```

- Properties can be overwritten if the existing property is added after the spread operator.

  ```js
  const myObject = {
    title: "alchemist",
    author: "paulo coelho",
    genre: "fiction",
    pages: 1000,
  };

  const updatedObject = { ...myObject, pages: 163 };

  console.log(updatedObject);

  /* 
  {
    title: 'alchemist',
    author: 'paulo coelho',
    genre: 'fiction',
    pages: 163,
  } 
  */
  ```
