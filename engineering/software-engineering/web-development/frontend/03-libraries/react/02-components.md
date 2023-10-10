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

<br>
<br>

## JSX

JSX is a syntax extension for javascript that allows HTML-like markup inside javascript file.

- JSX is syntactic sugar for react `createElement` function.
- JSX compiles down to plain javascript objects.
- Rules to follow when using JSX

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

  3. **_camelCase most things._** JSX turns into Javascript, hence we cannot use dash or reserved keywords. Example: use strokeWidth instead of stroke-width.

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

- Javacript can be used inside JSX with the help of curly braces.

  ```jsx
  function MyButton() {
    const btnTitle = "Click";
    return <button>{btnTitle}</button>;
  }
  ```

- Passing javascript object using double curly braces. Generally used in inline CSS styles in JSX.

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

## Keys

- keys are unique identifiers, something like id attribute in html.
- As long as keys remain consistent and unique, React can handle the DOM effectively and efficiently.
- It is important to define keys when creating react components.

<br>
<br>

## Props

In React, "props" is short for "properties," and it's a mechanism for passing data from a parent component to a child component.

```jsx
//MyApp.jsx

function MyButton(props) {
  //storing all the properties as an object
  const buttonStyle = {
    color: props.color,
    fontSize: props.fontSize + "px",
  };

  return <button style={buttonStyle}> {props.text}</button>;
}

export function MyApp() {
  return <MyButton color="red" fontSize="15" text="Click Here" />;
}
```

```jsx
//main.jsx

import React from "react";
import ReactDOM from "react-dom/client";
import { MyApp } from "./MyApp.jsx";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <MyApp />
  </React.StrictMode>
);
```

<br>

### Prop Destructuring

Props destructuring is essentially object destructuring from JavaScript applied to the props object passed to a React functional component.

```jsx
function MyButton({ color, fontSize, text }) {
  //storing all the properties as an object
  const buttonStyle = {
    color: color,
    fontSize: fontSize + "px",
  };

  return <button style={buttonStyle}> {text}</button>;
}

export function MyApp() {
  return <MyButton color="Red" fontSize="15" text="Click Here" />;
}
```

<br>

### Default Props

Default props is a way to specify default values for the props of a component.

```jsx
function MyButton({ color, fontSize, text }) {
  //storing all the properties as an object
  const buttonStyle = {
    color: color,
    fontSize: fontSize + "px",
  };

  return <button style={buttonStyle}> {text}</button>;
}

MyButton.defaultProps = {
  color: "Green",
  fontSize: "15px",
  text: "defaultClick",
};

export function MyApp() {
  return (
    <>
      <MyButton color="Red" fontSize="15" text="Click Here" />
      <MyButton />
    </>
  );
}
```

- We can combine default props and prop destructuring as follows:

  ```jsx
  function MyButton({
    color = "Green",
    fontSize = "15px",
    text = "defaultClick",
  }) {
    //storing all the properties as an object
    const buttonStyle = {
      color: color,
      fontSize: fontSize + "px",
    };

    return <button style={buttonStyle}> {text}</button>;
  }

  export function MyApp() {
    return (
      <>
        <MyButton color="Red" fontSize="15" text="Click Here" />
        <MyButton />
      </>
    );
  }
  ```

<br>

### Function as props

```jsx
function MyButton({
  color = "Green",
  fontSize = "15px",
  text = "defaultClick",
  handleClick,
}) {
  //storing all the properties as an object
  const buttonStyle = {
    color: color,
    fontSize: fontSize + "px",
  };

  return (
    <button style={buttonStyle} onClick={handleClick}>
      {text}
    </button>
  );
}

export function MyApp() {
  function ClickEvent() {
    console.log("Clicked.");
  }

  return (
    <>
      <MyButton
        color="Red"
        fontSize="15"
        text="Click Here"
        handleClick={ClickEvent}
      />
    </>
  );
}
```
