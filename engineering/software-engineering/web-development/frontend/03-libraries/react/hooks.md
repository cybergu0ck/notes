## `useEffect` hook

_A hook that facilitates actions that can be performed in response to the changes in the component's state or props._

```jsx
useEffect(
  () => {
    // execute side effect
    return () => {
      // cleanup function on unmounting or re-running effect
    };
  },
  // optional dependency array
  [
    /* 0 or more entries */
  ]
);
```

- It takes two arguments: a function to run the side effect and an array of dependencies.

  1. The function inside useEffect is the code you want to run when the component renders or when specific dependencies change.

  2. If the dependency array is not used, the side effect runs after every render. If it is empty, the side effect runs only once when the component is mounted. If it is filled with items, the side effect runs whenever any of the item changes in the compoenent.

- The side effect can return a cleanup function, which is useful for cleaning up resources or canceling subscriptions when the component unmounts.

<br>

- The following code logs the statement "useEffect hooked" every time the button is clicked (i.e. every time the state is changed i.e for every render)

  ```jsx
  import React, { useEffect, useState } from "react";

  export function Clock() {
    const [counter, setCounter] = useState(0);

    useEffect(() => {
      console.log(`useEffect hooked`);
    });

    const handleClick = () => {
      setCounter(counter + 1);
    };

    return (
      <div>
        <button onClick={handleClick}>+</button>
        <p>count is {counter}</p>{" "}
      </div>
    );
  }
  ```

- The following code logs the statement only when the component is mounted (first render). It logs twice at the first render.

  ```jsx
  import React, { useEffect, useState } from "react";

  export function Clock() {
    const [counter, setCounter] = useState(0);

    useEffect(() => {
      console.log(`useEffect hooked`);
    }, []);

    const handleClick = () => {
      setCounter(counter + 1);
    };

    return (
      <div>
        <button onClick={handleClick}>+</button>
        <p>count is {counter}</p>{" "}
      </div>
    );
  }
  ```

<br>
<br>
