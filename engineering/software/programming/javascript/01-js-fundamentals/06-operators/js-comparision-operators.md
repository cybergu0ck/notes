# Comparison Operators

| Operator | Name                     | Description                                                              |
| -------- | ------------------------ | ------------------------------------------------------------------------ |
| ===      | Strict equality          | Tests whether the left and right values are identical to one another     |
| !==      | Strict-non-equality      | Tests whether the left and right values are not identical to one another |
| <        | Less than                |                                                                          |
| >        | Greater than             |                                                                          |
| <=       | Less than or equal to    |                                                                          |
| >=       | Greater than or equal to |                                                                          |

<br>
<br>

## Difference between `==` and `===` in javascript

The == test whether the values are the same but not whether the values' datatypes are the same.

The ===, strict versions test the equality of both the values and their datatypes. The strict versions tend to result in fewer errors, so it is recommended.

<br>
<br>

## Comparison with null and undefined

- With scrict equality check,

  ```js
  alert(null === undefined); // false
  ```

- With strict-not equality,

  ```js
  alert(null == undefined); // true
  ```

<br>
<br>

## Strange results: null vs 0

```js
alert(null > 0); // (1) false
alert(null == 0); // (2) false
alert(null >= 0); // (3) true
```

- The reason is that an equality check == and comparisons > < >= <= work differently. Comparisons convert null to a number, treating it as 0. That’s why (3) null >= 0 is true and (1) null > 0 is false.

- On the other hand, the equality check == for undefined and null is defined such that, without any conversions, they equal each other and don’t equal anything else. That’s why (2) null == 0 is false.

<br>
<br>

## References

- Checkout [javascript.info](https://javascript.info/comparison) for comparision operators.
