# React

- React is a library and technically not a framework.
- React is non opinionated, meaning there is no force to follow any specific design patterns, structure or logic.

- A function that returns a jsx and whose name starts with a capital letter is a component.

## Library vs Framework

- Both library and framework are reuable code written by developers.
- What distinguishes them is a term called _"Inversion of control"_. When using a library, the dev is in charge of the flow of the application (when and where to call the library). When using a framework, the framework is in charge of the flow.

## Creating a React app

```bash
npm create vite@latest <app-name> -- --template react -y
```

- Follow the mentioned steps

  - `cd <app-name>`
  - `npm install`
  - `npm run dev`

## Components

react enables to break the UI into independent reusable chunks called components.

<br>

### Creating react components

They are as easy as creating javascript funcitons returning JSX.

```jsx
export function Greeting() {
  return <h1> Hey, Hello </h1>;
}
```

- Remeber to export them using default export or named export.

## JSX

- JSX is a syntax extension for javascript that lets you write HTML-like markup inside a Javascript file.

- Rules to follow when using JSX

1. **_Return a single root element._** If multiple elements are to be returned in a component the wrap them in a `<div>` or react fragment `<></>`.
2. **_Close all tags._** Self closing html tags must also be explicitly closed.
3. **_camelCase most things._** JSX turns into Javascript, hence we cannot use dash or reserved keywords. Example: use strokeWidth instead of stroke-width.

## Keys

- keys are unique identifiers, something like id attribute in html.
- As long as keys remain consistent and unique, React can handle the DOM effectively and efficiently.

## props

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
  return <MyButton color="Red" fontSize="15" text="Click Here" />;
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

## Default Props

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

## Function as props

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
      {" "}
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

## State

## useState hook

- It is a hook that facilitates to define the state in a functional component.
- It takes in an initial value as a parameter and returns an array with two elements.
- The two elements are destructured to get:

1. The current state value.
1. A function to update the state value.

```jsx
const [stateValue, setStateValue] = useState(initialValue);
```

- Adding more state variables should be as easy as adding more useState calls.

### Working of state in react

In React, when a component’s state or props change, the component is **_destroyed_** and **_recreated_** from scratch.

- Yes, you heard that right: destroyed. This includes the variables, functions, and React nodes. The entire component is recreated but this time the latest state value will be returned from useState. This process is called rerendering. Rerendering is a key feature of React that enables it to efficiently update the user interface in response to changes in the underlying data.
