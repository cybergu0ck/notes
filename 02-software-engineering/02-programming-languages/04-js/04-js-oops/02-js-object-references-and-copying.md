- One of the fundamental differences of objects versus primitives is that objects are stored and copied **_“by reference”_**, whereas primitive values: strings, numbers, booleans, etc – are always copied **_“as a whole value”_**.

<br>

## Illustration

- From the snippet below, we have two independent variables, each one storing the string "Hello!".
  ```js
  let message = "Hello!";
  let phrase = message;
  ```

> Add image

- **_A variable assigned to an object stores not the object itself, but its “address in memory” – in other words “a reference” to it._**

  ```js
  let user = {
    name: "John",
  };
  ```

* The object is stored somewhere in memory while the `user` variable has a 'reference" to it.

* **_When an object variable is copied, the reference is copied, but the object itself is not duplicated._**

  ```js
  let user = { name: "John" };
  let admin = user; // copy the reference
  ```

> add image

```js
let user = { name: "John" };
let admin = user;
admin.name = "Pete"; // changed by the "admin" reference
alert(user.name); // 'Pete', changes are seen from the "user" reference
```
