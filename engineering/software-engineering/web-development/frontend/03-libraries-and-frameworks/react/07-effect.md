# Effect

Effect is an action (which is not directly related to rendering) that can be performed in response to rendering (changes in the component's state or props.)

- Effect is also known as Side Effect in React.
- Examples of side effects are:
  - Data fetching
  - Setting up subscriptions
  - Setting up timers
  - DOM manipulation

<br>
<br>

## Difference between State and Effect

| State                                                                                                                        | Effect                                                                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| "**State**" refers to an internal data structure that allows a component to store and manage data that can change over time. | "**Effect**" is an action (which is not directly related to rendering) that can be performed in response to rendering (changes in the component's state or props.) |

<br>
<br>

## `useEffect` hook

_It is a hook that triggers the side effects._

```jsx
useEffect(() => {}, []);
```

- It takes two arguments:

  <ol type="1">

    <li> Callback (Reference to a function) </li>
    <li> Dependency Array </li>
  </ol>

<br>

### Callback in useEffect

_It contains the logic for the side effect._

- The side effect can optionally return a cleanup function, which is useful for cleaning up resources or canceling subscriptions when the component unmounts.

  ```jsx
  useEffect(() => {
    //side effect logic
    return ()={
      //clean up logic
    }
  }, []);
  ```

<br>

### Dependency Array in useEffect

_If specifies when the side effect must be executed._

1. If the dependency array is not used, the side effect is executed after every render.

   ```jsx
   import { useState, useEffect } from "react";

   export default function App() {
     return (
       <div>
         <MyComponent></MyComponent>
       </div>
     );
   }

   function MyComponent() {
     const [likes, setLikes] = useState(0);
     const [disLikes, setDisLikes] = useState(0);

     useEffect(() => {
       console.log("Simulating a side effect!");
     });

     return (
       <div>
         <div style={{ display: "flex" }}>
           <p>{likes} 👍</p>{" "}
           <button onClick={() => setLikes(likes + 1)}>Like</button>
         </div>
         <div style={{ display: "flex" }}>
           <p>{disLikes} 👎</p>{" "}
           <button onClick={() => setDisLikes(disLikes + 1)}>Dislike</button>
         </div>
       </div>
     );
   }
   ```

1. If it is empty, the side effect is executed only once, when the component is mounted.

   ```jsx
   import { useState, useEffect } from "react";

   export default function App() {
     return (
       <div>
         <MyComponent></MyComponent>
       </div>
     );
   }

   function MyComponent() {
     const [likes, setLikes] = useState(0);
     const [disLikes, setDisLikes] = useState(0);

     useEffect(() => {
       console.log("Simulating a side effect!");
     }, []);

     return (
       <div>
         <div style={{ display: "flex" }}>
           <p>{likes} 👍</p>{" "}
           <button onClick={() => setLikes(likes + 1)}>Like</button>
         </div>
         <div style={{ display: "flex" }}>
           <p>{disLikes} 👎</p>{" "}
           <button onClick={() => setDisLikes(disLikes + 1)}>Dislike</button>
         </div>
       </div>
     );
   }
   ```

1. If it is filled with items, the side effect runs whenever any of the item changes in the compoenent.

   ```jsx
   import { useState, useEffect } from "react";

   export default function App() {
     return (
       <div>
         <MyComponent></MyComponent>
       </div>
     );
   }

   function MyComponent() {
     const [likes, setLikes] = useState(0);
     const [disLikes, setDisLikes] = useState(0);

     useEffect(() => {
       console.log("Simulating a side effect!");
     }, [likes]);

     return (
       <div>
         <div style={{ display: "flex" }}>
           <p>{likes} 👍</p>{" "}
           <button onClick={() => setLikes(likes + 1)}>Like</button>
         </div>
         <div style={{ display: "flex" }}>
           <p>{disLikes} 👎</p>{" "}
           <button onClick={() => setDisLikes(disLikes + 1)}>Dislike</button>
         </div>
       </div>
     );
   }
   ```

<br>

---

<br>
<br>

# Data Fetching

Data fetching is a side effect.

```jsx
import { useEffect, useState } from "react";

const API_KEY = "8e43a241";
const query = "Interstellar";

export default function App() {
  const [movie, setMovie] = useState({});

  useEffect(() => {
    fetch(`http://www.omdbapi.com/?apikey=${API_KEY}&s=${query}`)
      .then((response) => response.json())
      .then((data) => {
        console.log(data.Search.at(0));
        setMovie(data.Search.at(0));
      });
  }, []);

  return (
    <div>
      <p>Making API request... </p>
      <MovieBoard movie={movie}></MovieBoard>;
    </div>
  );
}

function MovieBoard({ movie }) {
  return (
    <div>
      <p>
        {`Found a ${movie.Type} named ${movie.Title} which was released in ${movie.Year}.`}
      </p>
    </div>
  );
}
```

<br>
<br>

## Handling loading while data fetching

```jsx
import { useEffect, useState } from "react";

const API_KEY = "8e43a241";
const query = "Interstellar";

export default function App() {
  const [movie, setMovie] = useState({});
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    setIsLoading(true);

    fetch(`http://www.omdbapi.com/?apikey=${API_KEY}&s=${query}`)
      .then((response) => response.json())
      .then((data) => {
        console.log(data.Search.at(0));
        setMovie(data.Search.at(0));
        setIsLoading(false);
      });
  }, []);

  return (
    <div>
      <p>Making API request... </p>
      <MovieBoard movie={movie} isLoading={isLoading}></MovieBoard>;
    </div>
  );
}

function MovieBoard({ movie, isLoading }) {
  return (
    <div>
      {isLoading ? (
        <p>Loading...</p>
      ) : (
        <p>
          {`Found a ${movie.Type} named ${movie.Title} which was released in ${movie.Year}.`}
        </p>
      )}
    </div>
  );
}
```

<br>
<br>

## Handling errors while data fetching

```jsx
import { useEffect, useState } from "react";

const API_KEY = "8e43a241";
const query = "Interstellar";

export default function App() {
  const [movie, setMovie] = useState({});
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    try {
      setIsLoading(true);
      fetch(`http://www.omdbapi.com/?apikey=${API_KEY}&s=${query}`)
        .then((response) => {
          if (!response.ok) {
            throw new Error("Network failed to fetch.");
          }
          return response.json();
        })
        .then((data) => {
          if (data.Response !== "True") {
            throw new Error("No response for the given Query");
          }
          setMovie(data.Search.at(0));
        });
    } catch (error) {
      console.log(error);
    } finally {
      setIsLoading(false);
    }
  }, []);

  return (
    <div>
      <p>Making API request... </p>
      <MovieBoard movie={movie} isLoading={isLoading}></MovieBoard>;
    </div>
  );
}

function MovieBoard({ movie, isLoading }) {
  return (
    <div>
      {isLoading ? (
        <p>Loading...</p>
      ) : (
        <p>
          {`Found a ${movie.Type} named ${movie.Title} which was released in ${movie.Year}.`}
        </p>
      )}
    </div>
  );
}
```
