# Data Types

There are eight basic data types in js.

1. `Number` (contains `infinity` and `Nan`)
2. `String`
3. `Bigint`
4. `Boolean`
5. `null`
6. `undefined`
7. `object`
8. `symobol`


- All other datatypes except `object` and `symbol` are *primitive datatypes* because their values can contain only a single thing (be it a string or a number or whatever). In contrast, objects are used to store collections of data and more complex entities.
- Refer this article for good information [data-types](https://javascript.info/types)

<br>

## Boolean

- *Falsy values*: when used in conditionals, the values 0, "", null, undefined, NaN all become False.
- *Truthy values*: all other values become true.

<br>

# Creating Variables in js

1. using `let`, has block scope and can be modified later on.
2. using `const`, has block scope and cannot be modified later on.
3. using `var`, has gloabl scope and don't use this.
