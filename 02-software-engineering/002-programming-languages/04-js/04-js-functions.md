# Syntax for writing functions in js

```js
// function definition
function foo(){
    console.log('Hi from foo');
}

//function call
foo(); 

//Hi from foo
```

> Function vs Methods <br> Functions that are part of objects are called methods.

<br>
<br>

# Function parameters


## Optional parameters

```js
const myArray = ['I', 'love', 'chocolate', 'frogs'];
const madeAString = myArray.join(' ');
console.log(madeAString);
// returns 'I love chocolate frogs'

const madeAnotherString = myArray.join();
console.log(madeAnotherString);
// returns 'I,love,chocolate,frogs'
```
<br>

## Default paramters

If you're writing a function and want to support optional parameters, we can specify default values by adding = after 
the name of the parameter, followed by the default value:

```js
function hello(name = 'Chris') {
  console.log(`Hello ${name}!`);
}

hello('Ari'); // Hello Ari!
hello();      // Hello Chris!
```

<br>
<br>


# Anonymous functions

functions without names are anonymous functions, we mostly see anonymous functions when a function expects to receive another function as a parameter. 

- Normal function definition,

  ```js
  function myFunction() {
    alert('hello');
  }
  ```
- Defining anonymously,

  ```js
  (function (){
    alert('hello');
    })
  ```
<br>

### Illustration of using anonymous fucntions as parameters

- Using normal definition,

  ```js
  function logKey(event) {
    console.log(`You pressed "${event.key}".`);
  }

  textBox.addEventListener('keydown', logKey);
  ```
- Using anonymous function,

  ```js
  textBox.addEventListener('keydown', function(event) {
    console.log(`You pressed "${event.key}".`);
  });
  ```

<br>
<br>

# Arrow functions

Used instead of anonymous functions, Instead of function(event), we write (event) =>

```js
textBox.addEventListener('keydown', (event) => {
    console.log(`You pressed "${event.key}".`);
  });

  
// if there is only single line of code inside the function we can skip the curly braces.
textBox.addEventListener('keydown', (event) => console.log(`You pressed "${event.key}".`));

// if we have a single parameter then we can skip the paranthesis.
textBox.addEventListener('keydown', event => console.log(`You pressed "${event.key}".`));

```
* If we have no parameters for the function then we have to use `() => {code};`

<br>
<br>





















