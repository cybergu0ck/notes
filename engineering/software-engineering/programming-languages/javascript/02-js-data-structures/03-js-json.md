# JSON

- JSON stands for _Javascript Object Notation_ and is one of the data representation format (similar to xml or yaml)
- It is light weight to transfer and is easy to read hence used in API's and config.
- JSON is a subset of javascript and hence all JSON is javascript.

<br>

# JSON data types

- JSON supports following data types:

  1. Objects {...}
  2. Arrays [...]
  3. Primitives:
     - strings
     - numbers
     - booleans
     - null

<br>
<br>

# JSON.stringify()

- generally JSON is passed as a string.
- To convert a JSON object to string we use the stringify function.

  ```js
  let user = {
    name: "Kyle",
    age: 10,
    isCool: true,
    hobbies: ["weight lifting", "Bowling", "seeing"],
  };

  let stringed = JSON.stringify(user);

  console.log(stringed); //{"name":"Kyle","age":10,"isCool":true,"hobbies":["weight lifting","Bowling","seeing"]}
  console.log(typeof stringed); //string
  ```

<br>
<br>

# JSON.pasrse()

- We use this to convert a string to a JSON object.

  ```js
  let data = `[
    {
      "name": "Kyle",
      "age": 10
    },
    {
      "name": "John",
      "age": 99
    }
  ]
  `;

  let json_obj = JSON.parse(data);

  console.log(json_obj); //[ { name: 'Kyle', age: 10 }, { name: 'John', age: 99 } ]
  console.log(typeof json_obj); //object
  ```
