* While primitive datatype's values have only one thing, objects are used to store keyed collections of various data and more complex entities.

<br>
<br>

# Literals and Properties

* An object can be created with figure brackets {…} with an optional list of **properties**. A property is a *“key: value” pair*, where key is a string (also called a “property name”), and value can be anything.

* An empty object can be created using one of two syntaxes (Generally Object Literal Syntax is used):

    ```js
    let user = new Object(); // "object constructor" syntax
    let user = {}; // "object literal" syntax
    ```
* Creating objects with properties (key:value pairs).

    ```js
    let user = {     // an object
    name: "John",  // by key "name" store value "John"
    age: 30        // by key "age" store value 30
    "likes chocolates" : false //mult-word properties must be enclosed with ""
    };
    ```
<br>

## Setting Properties

* Setting properties using dot notation and assignment operator:

    ```js
    user.isCool = true;
    ```
* Setting multiword properties using quotes and square brackets:

    ```js
    user["likes birds"] = true;
    ```
<br>

## Accessing Properties

* We can access property values using dot notation:

    ```js
    console.log(user.name); //John
    console.log(user.age);  //30
    ```

* We can access multiword properties using square brackets:
    ```js
    console.log(user["likes chocolates"])
    ```

<br>

## Deleting Properties
    
* We can delete property using `delete` operator:

    ```js
    delete user.age;
    ```
* deleting multiword properties:

    ```js
    delete user["likes birds"];
    ```
<br>
<br>

# Property Value shorthand

* In real code, we often use existing variables as values for property names.
    ```js
    function makeUser(name, age) {
    return {
        name: name,
        age: age,
        // ...other properties
    };
    }

    let user = makeUser("John", 30);
    console.log(user.name); // John
    ```

* We can use the *property value shorthand* to make the above code shorter:

    ```js
    function makeUser(name, age) {
    return {
        name,
        age,
    };
    }
    ```
* We can use both normal property and shorthands in the same object!

    ```js
    function makeUser(name, age) {
        return {
            name,
            age:99,
        };
        }
    ```

<br>
<br>

# Property names limitations

Propery names (the key's) of Objects have no limitations (language reserved keyword can be used)

<br>
<br>

# Property existence test, `in` opertaor

* Reading a non-existing property just returns `undefined`.

    ```js
    let user = { name: "John", age: 30 };
    console.log("age" in user);  //true
    ```
<br>
<br>

# The "for..in" loop

* To walk over all keys of an object, there exists a special form of the loop: **for..in**.

    ```js
    let user = {
        name: "John",
        age:30,
        "likes chocolates": false,
    }

    for (key in user){
        console.log(key);
    }

    //name
    //age
    //likes chocolates
    ```