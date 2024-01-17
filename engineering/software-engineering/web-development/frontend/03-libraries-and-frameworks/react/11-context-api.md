# Context API

The Context API provides a way to pass data through the component tree without having to pass props down manually at every level.

- Essentially it is better solution against prop drilling.

- The concept of context API has three crucial things :

  - Provider: Provider is the construct that gives all the child components access to values.
  - Value : It is the data that is to be made available to the components.
  - Consumer : Consumer is the component that reads the provided context value.

- All consumers are automatically re-rendered whenever the context value is updated.

<br>
<br>

## Creating the Context

```jsx
import { createContext } from "react";
const NumberContext = createContext(); //The name of the variable must start with a capital letter as the convention for React Components.
```

<br>
<br>

## Providing the value to the Context

```jsx
<NumberContext.Provider
  value={{
    number: number,
    onClick: handleIncr,
  }}
>
  <MainContent number={number} onClick={handleIncr}></MainContent>
  <Footer number={number}></Footer>
</NumberContext.Provider>
```

<br>
<br>

## Consuming the Context

```jsx
import { useContext } from "react";
const contextValueObj = useContext(NumberContext);
// const {number, onClick} = useContext(NumberContext); //Destructuring is the preferred method.
```

- Here `contextValueObj` will be the object that we passed as value in the context Provider.

<br>
<br>

## Illustration

- Here, The three steps of creating the context, providing the value to it and consuming it are done.

  ```jsx
  import { createContext, useState, useContext } from "react";

  //#NOTE: 1. Creating the Context
  const NumberContext = createContext();

  //#NOTE: 2. Providing value to the context (see NumberContext.Provider)
  function App() {
    const [number, setNumber] = useState(0);

    function handleIncr() {
      setNumber((number) => number + 1);
    }
    return (
      <>
        <Header></Header>
        <NumberContext.Provider
          value={{
            number: number,
            onClick: handleIncr,
          }}
        >
          <MainContent></MainContent>
          <Footer></Footer>
        </NumberContext.Provider>
      </>
    );
  }

  function Header() {
    return (
      <div>
        <h1>Keep Incrementing</h1>
      </div>
    );
  }

  function MainContent() {
    return (
      <div>
        <Widget></Widget>
      </div>
    );
  }

  function Widget() {
    //NOTE: 3. Consuming the Context
    const contextValueObj = useContext(NumberContext);
    const { number, onClick } = contextValueObj;

    return (
      <div style={{ display: "flex" }}>
        <p>{number}</p>
        <button onClick={onClick}>+</button>
      </div>
    );
  }

  function Footer() {
    const { number } = useContext(NumberContext);

    return (
      <div>
        <h3>You pressed the increment button {number} many times.</h3>
      </div>
    );
  }

  export default App;
  ```

- The component tree for the above code is:

  ```

  App
  ├── Header
  └── Context.Provider
      ├── MainContent
      │     └── Widget
      └── Footer

  ```

- The Context API in React eliminates prop drilling, providing a cleaner code structure. In the example, values needed for `Widget` and `Footer` are directly accessed from the context, avoiding the need to pass them through every intermediate component (ex: `MainContent`). This enhances code simplicity and modularity.

<br>
<br>

- Creating components to abstract the above context creation and consumption.

  ```jsx
  //NumberProvider.jsx

  import { createContext, useState, useContext } from "react";

  //#NOTE: 1. Creating the Context
  const NumberContext = createContext();

  //#NOTE: 2. Providing value to the context (see NumberContext.Provider)
  function NumberProvider({ children }) {
    const [number, setNumber] = useState(0);

    function handleIncr() {
      setNumber((number) => number + 1);
    }

    return (
      <NumberContext.Provider
        value={{
          number: number,
          onClick: handleIncr,
        }}
      >
        {children}
      </NumberContext.Provider>
    );
  }

  //This is an Abstraction to encapsulate the useContext()
  function useNumber() {
    const context = useContext(NumberContext);
    return context;
  }

  export { NumberProvider, useNumber };
  ```

  ```jsx
  // App.jsx

  import { createContext, useState, useContext } from "react";
  import { NumberProvider, useNumber } from "./NumberProvider";

  function App() {
    return (
      <>
        <Header></Header>
        <NumberProvider>
          <MainContent></MainContent>
          <Footer></Footer>
        </NumberProvider>
      </>
    );
  }

  function Header() {
    return (
      <div>
        <h1>Keep Incrementing</h1>
      </div>
    );
  }

  function MainContent() {
    return (
      <div>
        <Widget></Widget>
      </div>
    );
  }

  function Widget() {
    //NOTE: 3. Consuming the Context
    const contextValueObj = useNumber();
    const { number, onClick } = contextValueObj;

    return (
      <div style={{ display: "flex" }}>
        <p>{number}</p>
        <button onClick={onClick}>+</button>
      </div>
    );
  }

  function Footer() {
    const { number } = useNumber();

    return (
      <div>
        <h3>You pressed the increment button {number} many times.</h3>
      </div>
    );
  }

  export default App;
  ```
