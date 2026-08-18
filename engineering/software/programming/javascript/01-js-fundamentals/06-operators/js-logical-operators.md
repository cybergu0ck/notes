# Logical Operators

<br>
<br>

## `&&` Operator

- This is the logical "and" operator.
- It returns `true` if both the operands are true, and `false` otherwise.

  ```js
  const condition1 = true;
  const condition2 = true;

  if (condition1 && condition2) {
    console.log("both conditions are true");
  }

  // both conditions are true
  ```

<br>

### Short Circuiting with `&&` operator

```js
const myObject = {
  book: "alchemist",
  author: "paulo coelho",
  genre: "fiction",
};

const bookProp1 = myObject.book && "A property named book exists";
const bookProp2 = myObject.page && "No property named page";

console.log(bookProp1); //A property named book exists
console.log(bookProp2); //undefined
```

This operator checks theleft hand operand,

- If it is true it will return the value of right-hand operand.
- If it is false it will return the value of the left-hand operand and will not go to check the right-hand operand.

<br>
<br>

## `||` operator

- It is logical or operator
- It returns `true` if either one of the operands is true and false if both operands result in false.

<br>

### Short Circuiting with `||` operator

```js
const myObject = {
  book: "alchemist",
  author: "paulo coelho",
  genre: "fiction",
};

const bookProp1 = myObject.book || "A property named book exists";
const bookProp2 = myObject.page || "No property named page";

console.log(bookProp1); //alchemist
console.log(bookProp2); //No property named page
```

This operator checks the left-hand operand,

- If it is true it will return the value of it (left-hand operand) and will not go to check the second hand operator.
- If it is false it will return the value of the right-hand operand.

<br>
<br>

## `??` operator

- It is called as the **_"Nullish Coalescing Operator"_**.
- It returns the right-hand operand if the left hand operand is "null" or "undefined". Otherwise, it returns the left-hand operand.

- It is likely used to set default values, especially when working with user inputs.

  ```js
  const myObject = {
    book: "alchemist",
    author: "paulo coelho",
    genre: "fiction",
  };

  myObject.page = myObject.page ?? 163;
  console.log(myObject);

  /* 
    {
    book: 'alchemist',
    author: 'paulo coelho',
    genre: 'fiction',
    page: 163
    }
    */
  ```

<br>
<br>

## References

- Checkout [javascript.info](https://javascript.info/logical-operators) for information on logical operators.

<br>
<br>
