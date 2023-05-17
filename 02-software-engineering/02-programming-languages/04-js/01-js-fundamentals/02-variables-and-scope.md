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

## The old `var`

- The `var` declaration is similar to `let`, However has following differences:

### 1. `var` has no block scope

- Variables, declared with var, are either _function-scoped_ or _global-scoped_. **They are visible through blocks.**

  ```js
  if (true) {
    var num = 100;
    let another = 2;
  }

  console.log(num); //100
  console.log(another); // Reference error another is not defined
  ```

* If a code block is inside a function, then var becomes a function-level variable:

  ```js
  function foo() {
    if (true) {
      var num = 99;
    }
    console.log(num); //logs 99 when foo is called
  }

  foo();
  console.log(num); //Reference error num is not defined
  ```

<br>

### 2. `var` tolerates redeclarations

- If we declare the same variable with `let` twice in the same scope, that’s an error:

  ```js
  let user;
  let user; // SyntaxError: 'user' has already been declared
  ```

* But that is not the case with `var`

  ```js
  var user = "Pete";
  var user = "John";
  alert(user); // John
  ```

<br>

### 3. `var` is Hoisted

- JavaScript Hoisting refers to the process whereby the interpreter appears to move the declaration of functions, variables or classes to the top of their scope, prior to execution of the code.

  ```js
  phrase = "Hi";
  console.log(phrase); //Even though phrase is declared down inside the if block, this logs "Hi"

  if (false) {
    var phrase;
  }

  /* 
  The above code is same as :
    var phrase;
    phrase = "Hi";
    console.log(phrase); // Hi
  */
  ```

* It is important to note that **Declarations are hoisted, but assignments are not.**

  ```js
  console.log(phrase); //undefined

  var phrase = "Hey there";

  /*
  
  The declaration is processed at the start of function execution (“hoisted”), but the assignment always works at the place where it appears. So the code works essentially like this:
  
  var phrase;
  console.log(phrase);
  phrase = "Hi";
  
  */
  ```

<br>
<br>

# Constants

- constants are essentially variables that cannot be reassigned and are declared using thr `const` keyword.

```js
const projectName = "SpookyFox';
```

<br>

## Uppercase constants

- There is a widespread practice to use constants as aliases for difficult-to-remember values that are known prior to execution.

  ```js
  const COLOR_RED = "#F00";
  let color = COLOR_RED;
  alert(color);
  ```

<br>
<br>

# Scope

- In JavaScript, scope refers to the visibility of a variable or how it can be used after it is declared. The scope of a variable depends on the keyword that was used to declare it.
- The three types of Scope are _Global Scope_, _Block Scope_ and _Function Scope_.
- Before ES6 (2015), JavaScript had only Global Scope and Function Scope with the var keyword. ES6 introduced let and const which allow Block Scope in JavaScript.

<br>

1. Global Scope

   - Variables declared outside any function or curly braces ’{}’ have Global Scope, and can be accessed from anywhere within the same Javascript code.
   - **var**, **let** and **const** all provide this Scope.

<br>

2. Function Scope

   - Variables declared within a function can only be used within that same function. Outside that function, they are undefined.
   - **var**, **let** and **const** all provide this Scope.

<br>

3. Block Scope

   - A block is any part of JavaScript code bounded by ’{}‘. Variables declared within a block can not be accessed outside that block.
   - This Scope is only provided by the **let** and **const** keywords. If you declare a variable within a block using the **var** keyword, _it will NOT have Block Scope_.
