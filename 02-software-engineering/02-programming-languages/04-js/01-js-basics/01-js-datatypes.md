# Variables

- A variable is a “named storage” for data and are defined using the `let` keyword.

  ```js
  let message; //declaration
  message = "Hello"; //assignment
  ```

- declaration and assignment can be made in one line, obviously.
- We can declare multiple variables in one line, however it is not recommended.

  ```js
  let user = 'john', age = 25, message = "hello';
  ```

<br>

## Variable naming

- There are two limitations on variable names in JavaScript:

  1. The name must contain only letters, digits, or the symbols $ and \_.
  1. The first character must not be a digit.

- When the name contains multiple words, **camelCase** is commonly used.

- There is a list of [reserved words](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#Keywords), which cannot be used as variable names because they are used by the language itself.

<br>
<br>

# Constants

- constants cannot be reassigned and are declared using thr `const` keyword.

  ```js
  const projectName = "SpookyFox';
  ```

<br>
<br>

# Data Types

There are eight basic data types in js.

1. `Number` (contains `infinity` and `Nan`)
2. `String`
3. `Bigint`
4. `Boolean`
5. `null`
6. `undefined`
7. `object`
8. `symbol`

- All other datatypes except `object` are _primitive datatypes_ because their values can contain only a single thing (be it a string or a number or whatever). In contrast, objects are used to store collections of data and more complex entities.
- Refer this article for good information [data-types](https://javascript.info/types)

<br>

## Boolean

- _Falsy values_: when used in conditionals, the values 0, "", null, undefined, NaN all become False.
- _Truthy values_: all other values become true.

<br>
<br>
