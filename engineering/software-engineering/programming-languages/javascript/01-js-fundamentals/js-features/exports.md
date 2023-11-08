# Exports

## Named Exports

**_Named Exports_** is a way to export specific variables, functions, or classes form a module so that they can be imported and used in other modules.

```js
// modulea.js
export const myVariable = 42;
export function myFunction() {
  return "Hello, World!";
}
```

```js
// moduleb.js
import { myVariable, myFunction } from "./modulea.js";
console.log(myVariable); // 42
console.log(myFunction()); // Hello, World!
```

#### Running the above on node

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

#### Running the above on browser

- Use the following syntax in the html file that includes the script

  ```html
  <script type="module" src="moduleb.js"></script>
  ```

<br>
<br>

## Defeault Exports
