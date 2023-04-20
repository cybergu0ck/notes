
# Arithmetic Operators

| Operator | Operation |
|---|---|
| + | Addtion |
| - | Subtraction |
| * | Multiplication |
| / | Division |
| % | Modulo (Remainder) |
| ** | Exponent |

<br>

## Operator Precedence

Operator precedence in JavaScript is the same as is taught in math classes in school — multiply and divide are always done first, then add and subtract (the calculation is always evaluated from left to right).

<br>


## Increment and Decrement operators

> We canot appy these operatores directly on numbers!

```js
3++; // Results in syntax error
```
<br>

## Prefix and Postfix

- In Prefix increment/decrement happens first and then the assignment. Hence the operation occurs first and the value (new in this case) is returned.

- In Postfix assignment happens first and then the increment/decrement. Hence the value (old in this case) is returned and then the operation occurs.

<br>
<br>

# Logical Operators

https://javascript.info/logical-operators

<br>
<br>

# Assignment Operators

| Operator | Name | Description |
| --- | --- |--- |
| += | Addition Assignment | myInt += 1 is equvivalent to myInt = myInt + 1 |
| -= | Subtraction Assignment | myInt -= 1 is equvivalent to myInt = myInt - 1 |
| *= | Multiplication Assignment | myInt *= 1 is equvivalent to myInt = myInt * 1 |
| /= | Division Assignment | myInt /= 1 is equvivalent to myInt = myInt / 1 |

<br>
<br>

# Comparison Operators


| Operator | Name | Description |
| --- | --- |--- |
| === | Strict equality | Tests whether the left and right values are identical to one another |
| !== | Strict-non-equality | Tests whether the left and right values are not identical to one another|
| < | Less than | | 
| > | Greater than | | 
| <= | Less than or equal to | | 
| >= | Greater than or equal to | | 

<br>

> Difference between == and === in js <br><br>
> The == test whether the values are the same but not whether the values' datatypes are the same. The ===, strict versions test the equality of both the values and their datatypes. The strict versions tend to result in fewer errors, so it is recommended.

<br>

> Add string comparison
> Strings are compared letter-by-letter in the “dictionary” order.

<br>

## Comparison with null and undefined

- With scrict equality check,

    ```js
    alert( null === undefined ); // false
    ```
- With strict-not equality,

    ```js
    alert( null == undefined ); // true
    ```

<br>

## Strange results: null vs 0

```js
alert( null > 0 );  // (1) false
alert( null == 0 ); // (2) false
alert( null >= 0 ); // (3) true
```

- The reason is that an equality check == and comparisons > < >= <= work differently. Comparisons convert null to a number, treating it as 0. That’s why (3) null >= 0 is true and (1) null > 0 is false.

- On the other hand, the equality check == for undefined and null is defined such that, without any conversions, they equal each other and don’t equal anything else. That’s why (2) null == 0 is false.


<br>
<br>

# References

https://javascript.info/comparison