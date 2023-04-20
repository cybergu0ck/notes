# If Else statement

```js
let num = 2;

if (num%2 === 0){
    console.log(`${num} is an even number.`)
}
else {
    console.log(`${num} is an odd number.`)
}

//2 is an even number.
```

<br>
<br>

# Else if statement

```js
let num = 3;

if (num%2 === 0){
    console.log(`${num} is an even number.`)
}
else if (num%2 !== 0){
    console.log(`${num} is an odd number.`)
}

//3 is an odd number.
```

<br>
<br>

> We can use logical operators like && (and) and || (or) inside paranthesis of if and else if conditions.

<br>
<br>

# Switch statement

> Add notes

<br>
<br>


# Using the ternary operator for if-else

```js
let num = 10;
let res = num%2 === 0 ? `${num} is an even number.`: `${num} is an odd number.`;
console.log(res);

//10 is an even number.
```

<br>

### Multiple ?

```js
let age = 2;

let greeting =  age < 5 ? `Hi baby` :
                age < 18 ? `Hello!` :
                age < 100 ? 'Greetings': 
                'Wow, going strong';

console.log(greeting)
//Notice how it terminates after a condition is satisfied.

// Hi baby
```
<br>
<br>

# Reference

- https://javascript.info/comparison
- https://javascript.info/logical-operators
- https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/conditionals
- https://javascript.info/ifelse
- https://www.digitalocean.com/community/tutorials/how-to-use-the-switch-statement-in-javascript
