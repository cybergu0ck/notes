# Creating arrays 

```js
let fruits = ['banana', 'apples', 'oranges', 100];
console.log(fruits);

//['banana', 'apples', 'oranges', 100]
```

<br>
<br>

# Inserting elements into array

*  Append an element at the end of the array using `push()`, also returns the new length. 

    ```js
    let fruits = ['banana', 'apples', 'oranges', 100];
    let fruitsLen = fruits.push('strawberries')

    console.log(fruits);
    console.log(fruitsLen);

    //['banana', 'apples', 'oranges', 100, 'strawberries']
    //5
    ```

* Insert an element at the begining of the array using `unshift()`, also returns the new length.

    ```js
    let fruits = ['banana', 'apples', 'oranges', 100];
    let first_fruit = fruits.unshift('mangoes');

    console.log(first_fruit);
    console.log(fruits);

    //5
    // ['apples', 'oranges', 100]
    ```


* Modify the array using `splice()`


<br>
<br>

# Accesing array elements 

- Access single element using `array[index]` notation, however negative indices are not supported.

- Access multiple elements using `slice()`.

    ```js
    let fruits = ['banana', 'apples', 'oranges', 100];
    console.log(fruits.slice(0,2));   //end index is exclusive!

    //['banana', 'apples']
    ```

* Access the first element by deleting first element using `shift()`.

- Access the last element by popping it using `pop()`.


<br>
<br>

# Deleting array elements 

- Delete and access the first element in the array using `shift()`. The indices are shifted left by 1 value.

    ```js
    let fruits = ['banana', 'apples', 'oranges', 100];
    let first_fruit = fruits.shift();

    console.log(first_fruit);
    console.log(fruits);

    //'banana'
    // ['apples', 'oranges', 100]
    ```

- Delete and ascess the last element in the array using `pop()`.

    ```js
    let fruits = ['banana', 'apples', 'oranges', 100];
    let doesNotBelong = fruits.pop();

    console.log(doesNotBelong);
    console.log(fruits);

    //100
    //['banana', 'apples', 'oranges']
    ```

- Delete elements using `delete` keyword and index, this leaves `undefined` holes in the array!

    ```js
    let fruits = ['banana', 'apples', 'oranges', 100];
    delete fruits[0]

    console.log(fruits);
    console.log(typeof fruits[0])

    // [empty,'apples', 'oranges', 100]
    //undefined
    ```

- Clear the entire (delete all elements) array using `splice()`.

<br>
<br>

# Modify elements in array

- Modifying elements using index

    ```js
    let fruits = ['banana', 'apples', 'oranges', 100];
    fruits[0] = 'mangoes';

    console.log(fruits)
    //['mangoes', 'apples', 'oranges', 100]
    ```

- Insert/Delete elements using `splice()`

    - `splice()` overwrites the original array!
    - syntax : `array.splice(index, delete-count, items ...)`

    ```js
    let fruits = ['banana', 'apples', 'oranges', 100];
    fruits.splice(0, 0, 'mangoes')
    console.log(fruits);

    //['mangoes', 'banana', 'apples', 'oranges', 100]
    ```

    ```js
    let fruits = ['banana', 'apples', 'oranges', 100];
    fruits.splice(1, 1, 'mangoes', 'watermelons') // At index=1, delete 1 item and add 'mangoes' and 'watermelons' 
    console.log(fruits);

    //['banana', 'mangoes', 'watermelons', 'oranges', 100]
    ```

<br>
<br>

# Sorting arrays 

- Sort arrays alphabetically using `sort()`
- To sort an array in decreasing order, use `sort()` and then use `reverse()`.

    ```js
    let fruits = ['banana', 'apples', 'oranges'];
    fruits.sort() //sorts the orginial array itself!

    console.log(fruits)
    //['apples', 'banana', 'oranges']
    ```

    ```js
    let my_variable = 'zz plant'
    let fruits = ['banana', my_variable, 'apples', 'oranges'];
    fruits.sort()

    console.log(fruits)
    //['apples', 'banana', 'oranges', 'zz plant']
    ```

    ```js
    let my_variable = 990
    let fruits = ['banana', my_variable, 'apples', 'oranges'];
    fruits.sort()

    console.log(fruits)
    //[990, 'apples', 'banana', 'oranges']
    ```

* Reverse an array using `reverse()`

    ```js
    let my_variable = 990
    let fruits = ['banana', my_variable, 'apples', 'oranges'];
    fruits.reverse()  //Reverses the orginial array iself!

    console.log(fruits)
    //['oranges', 'apples', 990, 'banana']
    ```

* ***Fisher Yates Sort*** (or Fisher Yates Shuffle) it is the most correct way to shuffle an array. 

    ```js
    const points = [40, 100, 1, 5, 25, 10];

    for (let i = points.length -1; i > 0; i--) {
    let j = Math.floor(Math.random() * (i+1));
    let k = points[i];
    points[i] = points[j];
    points[j] = k;
    }
    ```

* Checkout [w3schools](https://www.w3schools.com/js/js_array_sort.asp) for sorting numbers and objects.


<br>
<br>

# Array methods


* Get the index of an element using `indexOf()`
    ```js
    let fruits = ['mangoes', 'apples', 'mangoes']
    let mangoIndex = fruits.indexOf('mangoes')

    console.log(mangoIndex); //Note that it returns index of first occurance!

    //0
    ```

* Get the max number from an array (containing only numbers) using `Math.max.apply()`
    * Math.max.apply(null, [1, 2, 3]) is equivalent to Math.max(1, 2, 3).

    ```js
    let numbers = [1,1000,10,69];
    let maximum = Math.max.apply(null, numbers);

    console.log(maximum);
    //1000
    ```

* Get the min number from an array (containing only numbers) using `Math.min.apply()`

* Combine two arrays and get a new array using `concat()` (original arrays are not modified)

    ```js
    let numbers = [1,1000,10,69];
    let fruits = ['apples', 'mangoes']
    let merged = numbers.concat(fruits);

    console.log(numbers);
    console.log(fruits);
    console.log(merged);

    // [1, 1000, 10, 69]
    // ['apples', 'mangoes']
    // [1, 1000, 10, 69, 'apples', 'mangoes']
    ```

* Convert an array to string using `toString()`
    ```js
    let numbers = [1,1000,10,69];
    let converted = numbers.toString();
    console.log(numbers);
    console.log(converted);

    //[1,1000,10,69]
    //'1,1000,10,69'
    ```

* convert an array to a string using custom seperator using `join()`.
    ```js
    let numbers = [1,1000,10,69];
    let afterJoin = numbers.join();
    let customJoin = numbers.join(' * ')

    console.log(numbers);
    console.log(afterJoin);
    console.log(customJoin);

    //[1,1000,10,69]
    //'1,1000,10,69'
    //'1 * 1000 * 10 * 69'
    ```

