# Exports

<br>
<br>

## Named Exports

**_Named Export_** is a way to export specific variables, functions, or classes form a module so that they can be imported and used in other modules.

<br>

### Syntax for exporting named export

```js
// modulea.js
export const myVariable = 42;
export function myFunction() {
  return "Hello, World!";
}
```

<br>

### Syntax for importing named export

```js
// moduleb.js
import { myVariable, myFunction } from "./modulea.js";
console.log(myVariable); // 42
console.log(myFunction()); // Hello, World!
```

<br>

### Running on node

#TODO - Move this section to node notes later

- Initialise the node project, make sure the above js files are housed in this!

  ```
  node init
  ```

- Add the type in package.json

  ```
  "type": "module",
  ```

- Add the entry point in the package.json

  ```
  "main": "moduleb.js",
  ```

- Run the project

  ```
  node moduleb.js
  ```

<br>

### Running on browser

- Use the following syntax in the html file that includes the script

  ```html
  <script type="module" src="moduleb.js"></script>
  ```

<br>
<br>

## Defeault Exports

_Default Export is a way to export a single variable or a function, or a class form a module so it they can be imported and used in other modules._

<br>

### Syntax for exporting default export

```js
// modulea.js
function myFunction() {
  return "Hello, World!";
}

export default myFunction;
```

<br>

### Syntax for importing default export

```js
import myFunction from "./modulea.js";

console.log(myFunction());
```
