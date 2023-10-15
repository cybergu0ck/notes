# Components

React enables to break the UI into independent reusable chunks called _components_.

<br>
<br>

## Creating react components (Functional components)

They are as easy as creating javascript funcitons returning JSX.

```jsx
function MyButton() {
  return <button>Click Me</button>;
}
// Remember to export them (if needed) using default export or named export.
```

- React components can be class components or functional components, the former is depricated and is not prefered.
- The name of the function must always start with a capital letter.
- Components must be pure in terms of props and state. See [immutability of props](./03.props.md#immutability-of-props)

<br>
<br>

## JSX

JSX is a syntax extension for javascript that allows HTML-like markup inside javascript file.

- JSX is syntactic sugar for react `createElement` function.
- JSX compiles down to plain javascript objects.

<br>

### Rules for writing JSX

1. **_Return a single root element._** If multiple elements are to be returned in a component then wrap them in a `<div>` or react fragment i.e. `<></>`.
2. **_Close all tags._** Self closing html tags must also be explicitly closed.

   ```html
   <!-- This is an input tag in HTML, it is self closing -->
   <input type="text" />
   ```

   ```jsx
   //This is an input tag in JSX, we must self close it.
   <input type="text" />
   ```

3. **_camelCase most things._** JSX turns into Javascript, hence we cannot use dash or reserved keywords.

   - class is reserved keyword in javascript, hence we use className in JSX.
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

### Using javascript within JSX

- Javacript can be used inside JSX with the help of curly braces.

  ```jsx
  function MyButton() {
    const btnTitle = "Click";
    return <button>{btnTitle}</button>;
  }
  ```

- Statements (if/else, for, switch) are not allowed within JSX!

```js
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
```

- We can use it outside JSX in the javascript, like:

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

### Using inline CSS within JSX

Traditionally, we use `script: "<style attributes>"` but in JSX we have to wrap our CSS object with curly braces (hence double curlies).

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

```jsx
//Same code but note that we are not using double curly braces explicitely
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

## Seperation of concerns

- Traditionally, a web application is seperated by **_one technology per file_**. We seperate HTML, CSS and Javascript into different files although they are tightly coupled.
- With react, a web application is seperated by **_one component per file_**. We seperate the Components into different files which have JSX (HTML, CSS and Javascript) in them, which are also tightly coupled.

<br>
<br>

## Keys

- keys are unique identifiers, something like id attribute in html.
- As long as keys remain consistent and unique, React can handle the DOM effectively and efficiently.
- It is important to define keys when creating react components.

<br>
<br>
