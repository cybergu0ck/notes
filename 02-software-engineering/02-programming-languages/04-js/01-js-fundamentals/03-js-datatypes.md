# Data Types

- There are eight basic data types in js:

1. primitive datatypes:

   1. `Number` (contains `infinity` and `Nan`)
   1. `String`
   1. `Bigint`
   1. `Boolean`
   1. `null`
   1. `undefined`
   1. `symbol`

<br>

2. non-primitive datatypes:

   1. `object`

- All other datatypes except `object` are _primitive datatypes_ because their values can contain only a single thing (be it a string or a number or whatever). In contrast, objects are used to store collections of data and more complex entities.
- Refer this article for good information [data-types](https://javascript.info/types)

<br>
<br>

# string

## String concatenation

- Using _template literal_

  ```js
  const name = "Chris";
  const greeting = `Hello, ${name}`;
  console.log(greeting); // "Hello, Chris"
  ```

- Using `+`

  ```js
  const greeting = "Hello";
  const name = "Chris";
  console.log(greeting + ", " + name); // "Hello, Chris"
  ```

<br>

## String methods

| method            | description                                                                                                  | Example                          |
| ----------------- | ------------------------------------------------------------------------------------------------------------ | -------------------------------- |
| toLowerCase()     |                                                                                                              |                                  |
| toUpperCase()     |                                                                                                              |                                  |
| length (property) | Returns the length of the string <br> Note that this is a propery, not a method so donot use it as length()  |                                  |
| includes()        | check (returns bool) if the subtring is present inside the string                                            | myString.includes('substring')   |
| startsWith()      | check (returns bool) if the subtring starts with a particular substring.                                     | myString.startsWith('subString') |
| endsWith()        | check (returns bool) if the subtring ends with a particular substring.                                       | myString.startsWith('subString') |
| indexOf()         | Finding the position of a substring in the string                                                            | myString.indexOf('subString')    |
| slice()           | Extracting a substring from the string using start and end index                                             | Check Below                      |
| substr()          | similar to slice() only difference is that the second parameter specifies the length of the extracted part.  | Check Below                      |
| substring()       | similar to slice() only difference is that start and end values less than 0 are treated as 0 in substring(). |                                  |
| replace()         | Replace one substring inside a string with another substring                                                 | Check below                      |

<br>
<br>

```js
const myString = "This is a wonderful game.";
console.log(myString.slice(10, 20));

//wonderful
```

```js
let myString = "This is Beautiful.";
console.log(myString.substr(8, 9));
//Beautiful
```

```js
const browserType = "mozilla";
const updated = browserType.replace("moz", "van");

console.log(updated); // "vanilla"
console.log(browserType); // "mozilla"
```

<br>
<br>
