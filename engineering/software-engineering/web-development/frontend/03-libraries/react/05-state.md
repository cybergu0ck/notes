# State

_"State" refers to an internal data structure that allows a component to store and manage data that can change over time._

- It enables components to re-render and update their user interfaces in response to changes in the data.

<br>

### Working of state in react

In React, when a component’s state changes, the component is **_destroyed_** and **_recreated_** from scratch.

- This includes the variables, functions, and React nodes. The entire component is recreated but this time the latest state value will be returned from useState. This process is called **_rerendering_**. Rerendering is a key feature of React that enables it to efficiently update the user interface in response to changes in the underlying data.

<br>

### Points on state

1. Each component has and manages its own state.
2. The state of a component is isolated from the state of other components. i.e. change in the state of one component doesn't affect the states of other components.

<br>
<br>

## Hook

_"Hooks" are special functions that allows addition of stateful logic to functional components._

- They are called "hooks" because they allow developers to "hook into" React state and lifecycle features from functional components, which were traditionally stateless.

<br>

### Rules for utilizing hooks.

1. Hooks can only be called from the top level of a functional component. i.e. In the scope of the react component.

   - Hooks can’t be called from inside loops or conditions.
   - They can't be called from functions inside react component.

2. Never update the state manually. React will never know if the state is updated other than the setState function.

<br>
<br>

## `useState` hook

- _A hook that facilitates defining the state in a functional component._

  ```jsx
  const [stateValue, setStateValue] = useState(initialValue);
  ```

  - It takes in an initial value as a parameter and returns an array with two elements.
  - The two elements are [destructured](../../../../programming-languages/javascript/01-js-fundamentals/js-features/destructuring.md#array-destructuring) to get:
    1. The current state value.
    2. A function to update the state value.

- Adding more state variables should be as easy as adding more useState calls.

```js
import { useState } from "react";

export function Counter() {
  const [count, setCount] = useState(0); //Initial value of count is set to 0.

  const increment = () => {
    setCount(count + 1);
  };

  const decrement = () => {
    setCount(count - 1);
  };

  return (
    <div>
      <button onClick={decrement}>-</button>
      <p>Current Count = {count}</p>
      <button onClick={increment}>+</button>
    </div>
  );
}
```

<br>

### Updating a state based on current state

- React will not update the state twice for the following code. _The setCount method is asynchronous, meaning react will not update the state immediately!_ Hence the state will have the same value second time aswell.

  ```js
  const increment = () => {
    setCount(count + 1); //count is a state variable and setCount is the setter accordingly
    setCount(count + 1);
  };
  ```

- A better way would be to adhere to the below syntax when updating a state based on the current state.

  ```js
  const increment = () => {
    setCount((count) => count + 1); //Better than setCount(count + 1);
  };
  ```

<br>
<br>

## Lifting Up State

_Moving the state that needs to be shared between components to a common ancestor component and then pass down that state as props to the child components that need it._

- Data always flows downwards from parent to children components in react. If we need to share the data with components in the same hierarchy, we have to use this concept.

- In the code below, we have lifted the states to the parent MyApp component, so that the state variables can be shared by both the children components (which are in same level in terms of hierarchy).

  ```js
  import { useState } from "react";

  export function MyApp() {
    const [inputText, setInputText] = useState("");
    const [outputText, setOutputText] = useState("");

    function handleInputText(text) {
      setInputText(text);
    }

    function handleClick() {
      //clear the input field
      setInputText("");
      // change state of output
      setOutputText((outputText) =>
        !outputText ? outputText + inputText : outputText + "\n" + inputText
      );
    }

    return (
      <>
        <InputPanel
          inputText={inputText}
          handleInputText={handleInputText}
          handleClick={handleClick}
        />
        <OutputPanel outputText={outputText} />
      </>
    );
  }

  function InputPanel({ inputText, handleInputText, handleClick }) {
    return (
      <>
        <input
          value={inputText}
          onChange={(e) => handleInputText(e.target.value)}
        ></input>
        <button onClick={handleClick}>Submit</button>
      </>
    );
  }

  function OutputPanel({ outputText }) {
    return (
      <>
        <div
          style={{
            border: "2px solid black",
            width: "165px",
            height: "200px",
            whiteSpace: "pre-line",
          }}
        >
          {outputText}
        </div>
      </>
    );
  }
  ```

<br>
<br>

## Inverse data flow

- If there is a usecase such that the child component has to update the prop (that is received from the parent), this can be done using the setState method that must also be got from the parent!

<br>

### Understanding the rendering

```jsx
import { useState } from "react";

export function Counter() {
  const [count, setCount] = useState(0); //Initial value of count is set to 0.

  const increment = () => {
    console.log(`The value of the count before setCount is ${count}`);
    setCount(count + 1);
    console.log(`The value of the count after setCount is ${count}`);
  };

  console.log(`The value of count is ${count}`); //This will run every time react renders the page.

  return (
    <div>
      <button onClick={increment}>+</button>
      <p>Current Count = {count}</p>
    </div>
  );
}
```

The control flow for the above code is briefly explained here:

- When the page loads, the console is logged twice with the count value as 0.

  ![state1](./_assets/state-1.png)

- When the increment button is pressed, it calls the increment function, the first console log statement in that function is logged with the count value of 0, the setState increments the count value, However this happens asynchronously (non-blocking code) hence the next console log statement logs the count value of 0 aswell. When the asynchronous function finishes setting the count value, it re-renders the page and thus count value of 1 is logged twice.

  ![state1](./_assets/state-2.png)

<br>
<br>

## State vs Prop

| State                                        | Prop                                                    |
| -------------------------------------------- | ------------------------------------------------------- |
| State is used to make components interactive | Prop is used by parent to configure the child component |
| Internal data, owned by the component        | External data, owned by parent component                |
| Mutable                                      | Immutable                                               |

Whenever a state variable is passed as a prop to child component and the state variable changes in the parent component, then the child component also undergoes rerendering with the parent.
