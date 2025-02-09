# Creating arrays

```js
let fruits = ["banana", "apples", "oranges", 100];
console.log(fruits);

//['banana', 'apples', 'oranges', 100]
```

<br>
<br>

# Inserting elements into array

- Append an element at the end of the array using `push()`, also returns the new length.

  ```js
  let fruits = ["banana", "apples", "oranges", 100];
  let fruitsLen = fruits.push("strawberries");

  console.log(fruits);
  console.log(fruitsLen);

  //['banana', 'apples', 'oranges', 100, 'strawberries']
  //5
  ```

- Insert an element at the begining of the array using `unshift()`, also returns the new length.

  ```js
  let fruits = ["banana", "apples", "oranges", 100];
  let first_fruit = fruits.unshift("mangoes");

  console.log(first_fruit);
  console.log(fruits);

  //5
  // ['apples', 'oranges', 100]
  ```

- Modify the array using `splice()`

<br>
<br>

# Accesing array elements

- Access single element using `array[index]` notation, however negative indices are not supported.

- Access multiple elements using `slice()`.

  ```js
  let fruits = ["banana", "apples", "oranges", 100];
  console.log(fruits.slice(0, 2)); //end index is exclusive!

  //['banana', 'apples']
  ```

* Access the first element by deleting first element using `shift()`.

- Access the last element by popping it using `pop()`.

<br>
<br>

# Deleting array elements

- Delete and access the first element in the array using `shift()`. The indices are shifted left by 1 value.

  ```js
  let fruits = ["banana", "apples", "oranges", 100];
  let first_fruit = fruits.shift();

  console.log(first_fruit);
  console.log(fruits);

  //'banana'
  // ['apples', 'oranges', 100]
  ```

- Delete and ascess the last element in the array using `pop()`.

  ```js
  let fruits = ["banana", "apples", "oranges", 100];
  let doesNotBelong = fruits.pop();

  console.log(doesNotBelong);
  console.log(fruits);

  //100
  //['banana', 'apples', 'oranges']
  ```

- Delete elements using `delete` keyword and index, this leaves `undefined` holes in the array!

  ```js
  let fruits = ["banana", "apples", "oranges", 100];
  delete fruits[0];

  console.log(fruits);
  console.log(typeof fruits[0]);

  // [empty,'apples', 'oranges', 100]
  //undefined
  ```

- Clear the entire (delete all elements) array using `splice()`.

<br>
<br>

# Modifying elements in array

- Modifying elements using index

  ```js
  let fruits = ["banana", "apples", "oranges", 100];
  fruits[0] = "mangoes";

  console.log(fruits);
  //['mangoes', 'apples', 'oranges', 100]
  ```

- Insert/Delete elements using `splice()`

  - `splice()` overwrites the original array!
  - syntax : `array.splice(index, delete-count, items ...)`

  ```js
  let fruits = ["banana", "apples", "oranges", 100];
  fruits.splice(0, 0, "mangoes");
  console.log(fruits);

  //['mangoes', 'banana', 'apples', 'oranges', 100]
  ```

  ```js
  let fruits = ["banana", "apples", "oranges", 100];
  fruits.splice(1, 1, "mangoes", "watermelons"); // At index=1, delete 1 item and add 'mangoes' and 'watermelons'
  console.log(fruits);

  //['banana', 'mangoes', 'watermelons', 'oranges', 100]
  ```

<br>
<br>

# Sorting arrays

- Sort arrays alphabetically using `sort()`
- To sort an array in decreasing order, use `sort()` and then use `reverse()`.

  ```js
  let fruits = ["banana", "apples", "oranges"];
  fruits.sort(); //sorts the orginial array itself!

  console.log(fruits);
  //['apples', 'banana', 'oranges']
  ```

  ```js
  let my_variable = "zz plant";
  let fruits = ["banana", my_variable, "apples", "oranges"];
  fruits.sort();

  console.log(fruits);
  //['apples', 'banana', 'oranges', 'zz plant']
  ```

  ```js
  let my_variable = 990;
  let fruits = ["banana", my_variable, "apples", "oranges"];
  fruits.sort();

  console.log(fruits);
  //[990, 'apples', 'banana', 'oranges']
  ```

* Reverse an array using `reverse()`

  ```js
  let my_variable = 990;
  let fruits = ["banana", my_variable, "apples", "oranges"];
  fruits.reverse(); //Reverses the orginial array iself!

  console.log(fruits);
  //['oranges', 'apples', 990, 'banana']
  ```

* **_Fisher Yates Sort_** (or Fisher Yates Shuffle) it is the most correct way to shuffle an array.

  ```js
  const points = [40, 100, 1, 5, 25, 10];

  for (let i = points.length - 1; i > 0; i--) {
    let j = Math.floor(Math.random() * (i + 1));
    let k = points[i];
    points[i] = points[j];
    points[j] = k;
  }
  ```

* Checkout [w3schools](https://www.w3schools.com/js/js_array_sort.asp) for sorting numbers and objects.

<br>
<br>

## Array's `map` method

It returns a new array by applying the specified function to each element in the original array.

- The number of elements in the new array and the original array will be always same.
- A basic example of the map method.

  ```js
  const numbers = [1, 2, 3, 4, 5];
  const twosMultiples = numbers.map((num) => 2 * num);

  console.log(twosMultiples);

  // [ 2, 4, 6, 8, 10 ]
  ```

- An example of using map method involving objects.

  ```js
  const book1 = {
    author: "paulo coelho",
    title: "alchemist",
    genre: "fiction",
  };
  const book2 = {
    author: "scott adams",
    title: "gilberts principle",
    genre: "comedy",
  };
  const book3 = {
    author: "ernst hemmingway",
    title: "the old man and the sea",
    genre: "fiction",
  };

  books = [book1, book2, book3];

  const titles = books.map((book) => book.title);
  console.log(titles);

  // [ 'alchemist', 'gilberts principle', 'the old man and the sea' ]
  ```

- An example of map method returning objects in its logic. We cannot simply use curly to return objects because it is treated as the curly braces for arrow function!

  - We can explicitely use the return statement inside the arrow function's curly braces.

    ```js
    const book1 = {
      author: "paulo coelho",
      title: "alchemist",
      genre: "fiction",
    };
    const book2 = {
      author: "scott adams",
      title: "gilberts principle",
      genre: "comedy",
    };
    const book3 = {
      author: "ernst hemmingway",
      title: "the old man and the sea",
      genre: "fiction",
    };

    books = [book1, book2, book3];

    const essentialData = books.map((book) => {
      return { author: book.author, title: book.title };
    });
    console.log(essentialData);

    /*
    [
    { author: 'paulo coelho', title: 'alchemist' },
    { author: 'scott adams', title: 'gilberts principle' },
    { author: 'ernst hemmingway', title: 'the old man and the sea' }
    ]
    */
    ```

  - Or we can wrap the the object inside parenthesis (without using the return statement)

    ```js
    const essentialData = books.map((book) => ({
      author: book.author,
      title: book.title,
    }));
    ```

<br>
<br>

## Array's `filter` method

It returns a new array containing all elements from the original array that meet a certain condition, as determined by a provided callback function.

- The number of elements in the new array and the original array need not be the same.
- A basic example of the filter method.

  ```js
  const numbers = [1, 2, 3, 4, 5];
  const evenNums = numbers.filter((num) => num % 2 == 0);

  console.log(evenNums);

  // [ 2, 4 ]
  ```

- An example involving objects

  ```js
  const book1 = {
    author: "paulo coelho",
    title: "alchemist",
    genre: "fiction",
  };
  const book2 = {
    author: "scott adams",
    title: "gilberts principle",
    genre: "comedy",
  };
  const book3 = {
    author: "ernst hemmingway",
    title: "the old man and the sea",
    genre: "fiction",
  };

  books = [book1, book2, book3];

  const hemmingwayData = books.filter(
    (book) => book.author == "ernst hemmingway"
  );

  console.log(hemmingwayData);

  /* 
  [
  {
      author: 'ernst hemmingway',
      title: 'the old man and the sea',
      genre: 'fiction'
  }
  ]
  */
  ```

<br>

### Concept Clarity

```js
const numbers = [1, 2, 3, 4, 5];
const evenNums = numbers.filter((num) => num % 2);

console.log(evenNums);

// [ 1,3,5]
```

- At first glance we may thik that there is syntax error as we have not completed the condition (`num % 2` must be `num % 2 == 0`)
- However, the code returns odd numbers from the original array!
- This is because `num%2` here is checking for truthy and falsy values and whenever num%2 results to 0, which is a falsy value hence the condition is considered as false. In other cases where it doesn't result to 0, it will considered a truthy value and the condition is set to true.

<br>
<br>

## Array's `reduce` method

**It reduces the elements of an array to a single value by iterating over each element of the array, applying a provided function that is defined, and accumulating the result.**

- The syntax:

  ```
  array.reduce(callback[, initialValue]);
  ```

- A simple example:

  ```js
  const book1 = {
    author: "paulo coelho",
    title: "alchemist",
    genre: "fiction",
    pages: 163,
  };
  const book2 = {
    author: "scott adams",
    title: "gilberts principle",
    genre: "comedy",
    pages: 200,
  };
  const book3 = {
    author: "ernst hemmingway",
    title: "the old man and the sea",
    genre: "fiction",
    pages: 85,
  };

  books = [book1, book2, book3];

  const grandTotalPages = books.reduce(
    (accumulator, books) => accumulator + books.pages, //callback
    0 //initial value
  );

  console.log(grandTotalPages);

  //448
  ```

- A more complex example:

  ```js
  const book1 = {
    author: "paulo coelho",
    title: "alchemist",
  };
  const book2 = {
    author: "scott adams",
    title: "gilberts principle",
  };
  const book3 = {
    author: "ernst hemmingway",
    title: "the old man and the sea",
  };
  const book4 = {
    author: "paulo coelho",
    title: "Piligrimage",
  };

  books = [book1, book2, book3, book4];

  const booksWithUniqueauthors = books.reduce((acc, curr) => {
    if (acc.filter((b) => b["author"] === curr.author).length !== 0) return acc;
    else return [...acc, curr];
  }, []);

  console.log(booksWithUniqueauthors);

  /*
  [
    { author: 'paulo coelho', title: 'alchemist' },
    { author: 'scott adams', title: 'gilberts principle' },
    { author: 'ernst hemmingway', title: 'the old man and the sea' }
  ]
  */
  ```

<br>
<br>

# Other array methods

- Get the index of an element using `indexOf()`

  ```js
  let fruits = ["mangoes", "apples", "mangoes"];
  let mangoIndex = fruits.indexOf("mangoes");

  console.log(mangoIndex); //Note that it returns index of first occurance!

  //0
  ```

- Get the max number from an array (containing only numbers) using `Math.max.apply()`

  - Math.max.apply(null, [1, 2, 3]) is equivalent to Math.max(1, 2, 3).

  ```js
  let numbers = [1, 1000, 10, 69];
  let maximum = Math.max.apply(null, numbers);

  console.log(maximum);
  //1000
  ```

- Get the min number from an array (containing only numbers) using `Math.min.apply()`

- Combine two arrays and get a new array using `concat()` (original arrays are not modified)

  ```js
  let numbers = [1, 1000, 10, 69];
  let fruits = ["apples", "mangoes"];
  let merged = numbers.concat(fruits);

  console.log(numbers);
  console.log(fruits);
  console.log(merged);

  // [1, 1000, 10, 69]
  // ['apples', 'mangoes']
  // [1, 1000, 10, 69, 'apples', 'mangoes']
  ```

- Convert an array to string using `toString()`

  ```js
  let numbers = [1, 1000, 10, 69];
  let converted = numbers.toString();
  console.log(numbers);
  console.log(converted);

  //[1,1000,10,69]
  //'1,1000,10,69'
  ```

- convert an array to a string using custom seperator using `join()`.

  ```js
  let numbers = [1, 1000, 10, 69];
  let afterJoin = numbers.join();
  let customJoin = numbers.join(" * ");

  console.log(numbers);
  console.log(afterJoin);
  console.log(customJoin);

  //[1,1000,10,69]
  //'1,1000,10,69'
  //'1 * 1000 * 10 * 69'
  ```
