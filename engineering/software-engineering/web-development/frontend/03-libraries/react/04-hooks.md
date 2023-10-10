# State

"State" refers to an internal data structure that allows a component to store and manage data that can change over time.

It enables components to re-render and update their user interfaces in response to changes in the data.

<br>

### Working of state in react

In React, when a component’s state or props change, the component is **_destroyed_** and **_recreated_** from scratch.

- This includes the variables, functions, and React nodes. The entire component is recreated but this time the latest state value will be returned from useState. This process is called **_rerendering_**. Rerendering is a key feature of React that enables it to efficiently update the user interface in response to changes in the underlying data.

<br>
<br>

## Hook

Hooks are special functions that allows addition of stateful logic to functional components.

- They are called "hooks" because they allow developers to "hook into" React state and lifecycle features from functional components, which were traditionally stateless.
- Rules for utilizing hooks.
  1. Hooks can only be called from the top level of a functional component.
  1. Hooks can’t be called from inside loops or conditions.

<br>
<br>

### useState hook

- It is a hook that facilitates to define the state in a functional component.
- It takes in an initial value as a parameter and returns an array with two elements.
- The two elements are destructured to get:

1. The current state value.
1. A function to update the state value.

```jsx
const [stateValue, setStateValue] = useState(initialValue);
```

- Adding more state variables should be as easy as adding more useState calls.

```jsx
import { useState } from "react";

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
  const COLORS = ["red", "green", "blue"];
  const [bgColor, setBgColor] = useState(COLORS[0]);

  const clickEvent = (color) => () => {
    setBgColor(color);
  };

  /* 
  function clickEvent(color) {
    function innerFunc() {
      setBgColor(color);
    }
    return innerFunc;
  }
  */

  return (
    <div style={{ backgroundColor: bgColor }}>
      {COLORS.map((color) => {
        return (
          <MyButton
            color={color}
            text={color}
            fontSize="15"
            handleClick={clickEvent(color)}
            key={color}
          ></MyButton>
        );
      })}
    </div>
  );
}
```
