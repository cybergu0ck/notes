# Type Conversions

## String Conversion

- String conversion happens when we need the string form of a value.
- To explicitely convert a valur to string, we use `String(value)`.

  ```js
  let my_var = String(100);
  console.log(typeof my_var); //string
  ```

<br>

## Numeric Conversion

- Numeric conversion in mathematical functions and expressions happens automatically.

  ```js
  alert("6" / "2"); // 3, strings are converted to numbers
  ```

- We can use the `Number(value)` function to explicitly convert a value to a number.

  ```js
  let str = "123";
  let num = Number(str);
  console.log(typeof num); //number
  ```

* Numeric conversion rules:

  | Value     | Becomes                                                                                                                                                                                                                          |
  | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | undefined | NaN                                                                                                                                                                                                                              |
  | null      | 0                                                                                                                                                                                                                                |
  | string    | Whitespaces (includes spaces, tabs \\t, newlines \\n etc.) from the start and end are removed. <br> If the remaining string is empty, the result is 0. <br> Otherwise, the number is “read” from the string. An error gives NaN. |

<br>
<br>

## Boolean Conversion

- It happens in logical operations but can also be performed explicitly with a call to `Boolean(value)`.

* the values 0, "", null, undefined, NaN all become False.
* all other values become true.

<br>
<br>

# Type Coersion

- Addiding numbers and strings results in string concatination.
  ```js
  let a = 7;
  let b = "6";
  let res = a + b;
  console.log(res); //76
  console.log(typeof res); //string
  ```

* The above behaviour is only for `+` operation.

  ```js
  let a = 7; //or let a = "7"
  let b = "6";
  let res = a - b;
  console.log(res); //1
  console.log(typeof res); //number
  ```

* Using unary `+` before the variable converts the string to the number.

  ```js
  let num1 = "499";
  let num2 = 1;
  let res = +num1 + num2;
  console.log(res); //500
  ```
