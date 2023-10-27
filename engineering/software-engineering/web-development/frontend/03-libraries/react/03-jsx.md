# JSX

_"JSX" is a syntax extension for javascript that allows HTML-like markup within javascript._

- JSX is short for Javascript XML.
- JSX compiles down to plain javascript objects.
- JSX is a superset of Javascript. Hence, all JSX code is javascript but the reverse is not true.

<br>
<br>

## JSX Rules

1. **_Return a single root element._**

   - If multiple elements are to be returned in a component then wrap them in a `<div>` or react fragment i.e. `<></>`.

2. **_Close all tags._**

   - Self closing html tags must also be explicitly closed.

     ```jsx
     //input tag is a self closing html tag
     <input type="text" />
     ```

3. **_camelCase most things._**

   - JSX turns into Javascript, hence we cannot use dash or reserved keywords.

   - `class` is reserved keyword in javascript, hence we use `className` in JSX.
   - Example: use strokeWidth instead of stroke-width.

     ```html
     <circle
       class="myCircles"
       cx="50"
       cy="50"
       r="40"
       fill="blue"
       stroke-width="2"
     />
     ```

     ```jsx
     <circle
       className="myCircles" //Notice class is invalid in JSX
       cx="50"
       cy="50"
       r="40"
       fill="blue"
       strokeWidth="2"
     />
     ```

<br>
<br>

## Using javascript in JSX

- Javacript can be used inside JSX with the help of curly braces.

  ```jsx
  function MyButton() {
    const btnTitle = "Click";
    return <button>{btnTitle}</button>;
  }
  ```

<br>

### Using conditional statements in JSX.

- Statements (if/else, for, switch) are not allowed within JSX!

  ```js
  //ERROR
  function Footer() {
    const hour = new Date().getHours();
    const openHour = 12;
    const closeHour = 22;
    const isOpen = hour >= openHour && hour <= closeHour;

    return (
      <footer>
        {
          if(!isOpen)
            return ( <p> We're currently closed</p>)
        }
      </footer>
    )
  //ERROR
  ```

- We can use javascript if/else conditions in the component but it must be outside JSX.

  ```js
  function Footer() {
    const hour = new Date().getHours();
    const openHour = 12;
    const closeHour = 22;
    const isOpen = hour >= openHour && hour <= closeHour;

    if (!isOpen) return <p>We're currently closed.</p>;

    return (
      <footer className="footer">
        <div className="order">
          <p>We're open until {closeHour}:00. Come visit us or order online.</p>
          <button className="btn">Order</button>
        </div>
      </footer>
    );
  }

  //This is for illustration only, this is bad code as the footer will not be generated in the early return!
  ```

<br>
<br>

## Using CSS in JSX

- Writing Inline CSS in JSX with double curly braces.

  ```jsx
  export function MyApp() {
    return (
      <div
        style={{
          backgroundColor: "red",
          color: "yellow",
        }}
      >
        <MyButton></MyButton>
      </div>
    );
  }
  ```

- We can also define a javascript object containg the styles and then use the javascript mode (single curly brace) to declare the CSS.

  ```jsx
  export function MyApp() {
    const divStyle = {
      backgroundColor: "red",
      color: "yellow",
    };
    return (
      <div style={divStyle}>
        <MyButton></MyButton>
      </div>
    );
  }
  ```

- Checkout [official docs](https://react.dev/learn/javascript-in-jsx-with-curly-braces#using-curly-braces-a-window-into-the-javascript-world) to understand the usage of curlies in JSX.

<br>
<br>

## Setting classes conditionally in JSX

- Based on the prop we need to set the class using [template literals](../../../../programming-languages/javascript/01-js-fundamentals/js-features/template-literals.md#template-literals).
  and [conditional ternary opertor](../../../../programming-languages/javascript/03-js-control-flow/01-js-conditionals.md#ternary-conditional-operator)

  ```js
  function MyApp({ abnormal }) {
    return <div className={`${abnormal ? "abnormal" : "normal"}`}></div>;
  }
  ```

- Setting multiple classes ("status" and "normal" in this code) for the same element.

  ```js
  function MyApp() {
    return <div className="status normal"></div>;
  }
  ```

- Setting multiple classes for the same element, conditionally.
  ```js
  function MyApp({ abnormal }) {
    return <div className={`status ${abnormal ? "abnormal" : "normal"}`}></div>;
  }
  ```

<br>
<br>

## Setting text conditionally in JSX

```js
function MyApp({ isSoldOut }) {
  return (
    <p>
      {isSoldOut ? "the items are sold out" : " Select authentic items here. "}
    </p>
  );
}
```

<br>
<br>

## React fragment

- When we wrap multiple elements with a div element, that div element will be present in the DOM.
- When we wrap multiple elements with a react fragment, the react fragment will not be present in the DOM, it will look like the multiple elements are not wrapped at all in the DOM.

  ```js
  function App() {
    return (
      <>
        <h1>Authetic Header</h1>
        <p>lorem epsum salz..</p>
      </>
    );
  }
  ```

- If we want to use key's for react fragments,

  ```js
  //Make sure to import React!
  function App() {
    return (
      <React.Fragment key="value">
        <h1>Authetic Header</h1>
        <p>lorem epsum salz..</p>
      </React.Fragment>
    );
  }
  ```

<br>
<br>

## Displaying a list of elements in JSX

This is done by embedding expressions inside the JSX with curly braces.

```jsx
function App() {
  const animals = ["Lion", "Cow", "Snake", "Lizard"];

  return (
    <div>
      <h1>Animals: </h1>
      <ul>
        {animals.map((animal) => (
          <li key={animal}>{animal}</li>
        ))}
      </ul>
    </div>
  );
}
```

<br>
<br>

## Conditional Rendering

Rendering JSX based on a conditional expression.

- Rendering in this context means displaying
- Rendering should not be confused for the react's rendering process which is a different altogether.

<br>

### Conditional rendering using the ternary operator

```jsx
function List(props) {
  return (
    <ul>
      {props.animals.map((animal) => {
        return animal.startsWith("L") ? <li key={animal}>{animal}</li> : null;
      })}
    </ul>
  );
}

function App() {
  const animals = ["Lion", "Cow", "Snake", "Lizard"];

  return (
    <div>
      <h1>Animals: </h1>
      <List animals={animals} />
    </div>
  );
}
```

<br>

### Conditional rendering using the `&&` operator

```jsx
function List(props) {
  return (
    <ul>
      {props.animals.map((animal) => {
        return animal.startsWith("L") && <li key={animal}>{animal}</li>;
      })}
    </ul>
  );
}

function App() {
  const animals = ["Lion", "Cow", "Snake", "Lizard"];

  return (
    <div>
      <h1>Animals: </h1>
      <List animals={animals} />
    </div>
  );
}
```

<br>

### Conditional rendering using `if`, `if/else` and `switch` statments

- We can use these statements for conditional rendering.

<br>

### Falsy values in JSX (A common pitfall)

- In JSX, values like `null`, `undefined`, and `false` do not render anything, even though they are falsy values.

- However, value like 0 or an empty string doesn't do the same thing. l. They are valid in JSX and will be rendered completely fine, so be sure to be aware of that!
