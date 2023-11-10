# State

_"**State**" refers to an internal data structure that allows a component to store and manage data that can change over time._

- It enables components to re-render and update their user interfaces in response to changes in the data.
- Each component has and manages its own state.
- The state of a component is isolated from the state of other components. i.e. change in the state of one component doesn't affect the states of other components.

<br>
<br>

## Hook

_"**Hook**" is a special function that allows addition of stateful logic to functional components._

- They are called "hooks" because they allow developers to "hook into" React state and lifecycle features from functional components, which were traditionally stateless.
- Never update the state manually. React will never know if the state is updated other than the setState function.

<br>

### Rules for utilizing hooks.

1. Hooks must always be called in the same order.

   - Hence we can't use hooks indside conditional statements, loops.
   - As such it is ideal to place the hook at the top level of a functional component.

1. Hooks must be called from react functions.
   - They can't be called from functions inside react component.

<br>
<br>

## `useState` hook

- _**useState** hook is a hook that facilitates defining the state in a functional component._

  ```jsx
  const [stateValue, setStateValue] = useState(initialValue);
  ```

  - It takes in an initial value as a parameter and returns an array with two elements.
  - The two elements are [destructured](../../../../programming-languages/javascript/01-js-fundamentals/js-features/destructuring.md#array-destructuring) to get:
    1. The current state value.
    2. A function to update the state value.

- The following is an example code illustrating the use of state using useState hook.

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
<br>

## State vs Prop

| State                                        | Prop                                                    |
| -------------------------------------------- | ------------------------------------------------------- |
| State is used to make components interactive | Prop is used by parent to configure the child component |
| Internal data, owned by the component        | External data, owned by parent component                |
| Mutable                                      | Immutable                                               |

Whenever a state variable is passed as a prop to child component and the state variable changes in the parent component, then the child component also undergoes rerendering with the parent.
