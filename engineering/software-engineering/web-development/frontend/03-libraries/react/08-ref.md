# Ref

_A "**ref**" is a way to reference a React components and DOM elements._

- Like state, ref is also persistant across renders.
- Like state, we must not read/write ref in render logic.
- Unlike state, ref is mutable.
- Ref is usally written in event handlers (handler functions) and effects and not in JSX.

<br>
<br>

## Creating Ref

- Create a ref using the useRef hook and then bind it to the DOM element by passing it.

  ```jsx
  import { useEffect, useState, useRef } from "react";

  export default function App() {
    const inputElement = useRef(null);

    return <input ref={inputElement}></input>;
  }
  ```

<br>
<br>

## Accesing and Modifying Ref

- the `current` property of the Ref gives us access to the element or component that it is referring to.

  ```jsx
  import { useEffect, useState, useRef } from "react";

  export default function App() {
    const inputElement = useRef(null);

    useEffect(() => {
      inputElement.current.focus(); //Accessing
    }, []);

    return <input ref={inputElement}></input>;
  }
  ```

<br>
<br>

#TODO - Add usecases here, setting focus, keeping track of number of state changes.

<br>
<br>
## Difference between State and Ref

| State                              | Ref                                      |
| ---------------------------------- | ---------------------------------------- |
| State is immutable                 | Ref is mutable                           |
| Updating a state causes re-render. | Updating a ref doesn't cause a re-render |
| State updates are asynchronous     | Ref updates are synchronous              |

<br>
<br>
