# Looping through a collection

## 1.for...of loop

* We can loop through a collection like an array
    ```js
    let fruits = ['mangoes', 'apples', 'melons', 'berries']

    for(const fruit of fruits){
        console.log(fruit);
    }

    //'mangoes'
    //'apples'
    //'melons'
    //'berries'
    ```

<br>

## 2.map

* `map()` is used to do something to each item in a collection and create a new collection containing the changed items.

    ```js
    function toUpper(string){
        return string.toUpperCase();
    }

    const fruits = ['apples', 'oranges'];
    const FRUITS = fruits.map(toUpper);
    console.log(FRUITS);

    //['APPLES', 'ORANGES']
    ```

    ```js
    //Using arrow functions
    const FRUITS = fruits.map(string => string.toUpperCase());
    ```

<br>

## 3.filter

* We can use `filter()` to test each item in a collection, and create a new collection containing only items that match:

    ```js
    const fruits = ['apples', 'oranges', 'bananas', 'berries'];
    const fruitsStartingWithB = fruits.filter(string=>string.startsWith('b'));  //Note that it is case-sensitive!
    console.log(fruitsStartingWithB);

    //['bananas', 'berries']
    ```

<br>
<br>

# Standard for loop

* Syntax is as show here:

    ```js
    for (initializer; condition; final-expression) {
    // code to run
    }
    ```

* Example:
  ```js
  for (let i=0; i < 10; i++){
  //code
  }
  ```

<br>
<br>

# Break statement

* `break` is used to exit the ongoing loop.

    ```js
    //log fruit until lemon
    const fruits = ['mangoes','bananas', 'lemon', 'berries'];

    function containsLemon(arr){
        for (const item of arr){
            if (item === 'lemon'){
                break;
            }
            console.log(item);
            }
        }

    containsLemon(fruits);

    //mangoes
    //bananas
    ```

<br>
<br>

# Continue statement

* `continue` is used to skip an iteration in the ongoing loop.

    ```js
    //log fruits except lemon
    const fruits = ['mangoes','bananas', 'lemon', 'berries'];

    function containsLemon(arr){
        for (const item of arr){
            if (item === 'lemon'){
                continue;
            }
            console.log(item);
            }
        }

    containsLemon(fruits);

    //mangoes
    //bananas
    //berries
    ```

<br>
<br>

# While and do-while

* syntax of while loop is as shown here

    ```js
    initializer
    while (condition) {
    // code to run

    final-expression
    }
    ```


    ```js
    const fruits = ['mangoes','bananas', 'lemon', 'berries'];

    let index = 0

    while (index <= fruits.length -1){
        console.log(fruits[index]);
        index++;
    }

    //'mangoes'
    //'bananas'
    //'lemon'
    //'berries'
    ```

* syntax of do-while is as shown here

    ```js
    initializer
    do {
    // code to run

    final-expression
    } while (condition)
    ```

> The main difference between a do...while loop and a while loop is that the code inside a do...while loop is always executed at least once.
