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
