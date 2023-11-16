# useReducer hook

_**useReducer** facilitates an alternate way of setting state, ideally when component has a lot of states._

- It is likely used where useState is not enough to code the usecase such as:
  - Lot of states, spread across many event handlers all over the component.
  - When multiple state updates need to happen at the same time.
  - When updating one piece of state depends on one or multiple other pieces of state.

<br>
<br>

## Creating a state using useReducer

```jsx
//Note that reducer is not a react functional component!

function reducer(state, action) {
  return state + action; //Return value is the updated state
}

//following must be within a functional component.
const [state, dispatch] = useReducer(reducer, initialValue);
```

- `reducer` is a pure function (no side effects) that takes the current state and the action to return the next state. It is called when we use the dispatch function.
- `dispatch` function triggers the state update by sending actions to the reducer.
- `action` is an object that describes how to update the state.

<br>

- Consider this simple code which manages two states.

  ```jsx
  import { useState } from "react";

  export default function App() {
    const [count, setCount] = useState(0);
    const [step, setStep] = useState(1);

    const incr = () => {
      setCount((count) => count + step);
    };

    const decr = () => {
      setCount((count) => count - step);
    };

    const changeCount = (e) => {
      setCount(Number(e.target.value));
    };

    const changeStep = (e) => {
      setStep(Number(e.target.value));
    };

    return (
      <div>
        <input
          type="range"
          min="1"
          max="10"
          value={step}
          onChange={changeStep}
        ></input>
        <span>{step}</span>
        <div>
          <button onClick={decr}>-</button>
          <input value={count} onChange={changeCount}></input>
          <button onClick={incr}>+</button>
        </div>
      </div>
    );
  }
  ```

- The same functionality can be achieved using useReducer, where we can manage multiple states in a clean way.

  ```jsx
  import { useReducer } from "react";

  function reducer(state, action) {
    switch (action.type) {
      case "decr":
        return { ...state, count: state.count - state.step }; //The count state is updated here
      case "incr":
        return { ...state, count: state.count + state.step }; //The count state is updated here
      case "changeCount":
        return { ...state, count: action.payload }; //The count state is updated here using the payload!
      case "changeStep":
        return { ...state, step: action.payload }; //The step state is updated here using the payload!
    }
  }

  export default function App() {
    const [state, dispatch] = useReducer(reducer, { count: 0, step: 1 });

    const { count, step } = state; //destructure

    const incr = () => {
      dispatch({ type: "incr" });
    };

    const decr = () => {
      dispatch({ type: "decr" });
    };

    const changeCount = (e) => {
      dispatch({ type: "changeCount", payload: Number(e.target.value) });
    };

    const changeStep = (e) => {
      dispatch({ type: "changeStep", payload: Number(e.target.value) });
    };

    return (
      <div>
        <input
          type="range"
          min="1"
          max="10"
          value={step}
          onChange={changeStep}
        ></input>
        <span>{step}</span>
        <div>
          <button onClick={decr}>-</button>
          <input value={count} onChange={changeCount}></input>
          <button onClick={incr}>+</button>
        </div>
      </div>
    );
  }
  ```
