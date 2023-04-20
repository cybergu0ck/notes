- js has only one data type for numbers called `number`, both integers and decimal.


<br>
<br>

## Adding number and string dataypes in js

- Addiding numbers and strings results in string concatination.
    ```js
    let num1 = "499";
    let num2 = 1;
    let res = num1 + num2;
    console.log(res); 

    //4991
    ```
- The above behaviour is only for `+` operation.

    ```js
    let num1 = "499";
    let num2 = 1;
    let res = num1 - num2;
    console.log(res); 

    //498
    ```
- Using unary `+` before the variable converts the string to the number.

    ```js
    let num1 = "499";
    let num2 = 1;
    let res = +num1 + num2;
    console.log(res); 

    //500
    ```

<br>
<br>

# Type casting 

- To type cast strings into number datatypes use `Number()`.

```js
let inString = '69';
console.log(typeof Number(inString)); 
//number
```

<br>
<br>


# `number` methods

| method | Description |
|---|---|
| `toFixed()` | to round your number to a fixed number of decimal places |


<br>
<br>



