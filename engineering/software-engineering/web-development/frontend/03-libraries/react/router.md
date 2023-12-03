# React Router

_**React Router** is a popular library for handling navigation and routing in React applications._

<br>
<br>

## Installing the Package

```bash
npm i react-router-dom
```

<br>
<br>

## Pages

The pages and the file structure that is used in the illustration for this section is as shown here.

```
src
 ├───assets
 └───pages
        ├───HomePage.jsx
        ├───Login.jsx
        └───Pricing.jsx
     App.jsx

```

```jsx
function HomePage() {
  return (
    <div>
      <p> This is the App</p>
    </div>
  );
}

export default HomePage;
```

```jsx
function Login() {
  return (
    <div>
      <p>Login Page</p>
    </div>
  );
}

export default Login;
```

```jsx
function Pricing() {
  return (
    <div>
      <p>Pricing Page</p>
    </div>
  );
}

export default Pricing;
```

<br>
<br>

## Routes

_Route is a component provided by the React Router library that enables the rendering of UI components based on the current URL or location of the application._

```jsx
//App.jsx

import { BrowserRouter, Routes, Route } from "react-router-dom";
import HomePage from "../src/pages/HomePage";
import Login from "../src/pages/Login";
import Pricing from "../src/pages/Pricing";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage></HomePage>}></Route>
        <Route path="login" element={<Login></Login>}></Route>
        <Route path="pricing" element={<Pricing></Pricing>}></Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
```

- There must always be a Route with `path="/"`, This is the default path that will be loaded first.

<br>
<br>

## Links

- _The Link component is a basic navigation component used to create links between different routes in a React application._

  ```jsx
  //HomePage.jsx (Modifying the original file)

  import { Link, NavLink } from "react-router-dom";

  function HomePage() {
    return (
      <div>
        <p> This is Home Page of the application</p>
        <ul>
          <li>
            <Link to="login">Login</Link>
          </li>
          <li>
            <Link to="pricing">Pricing</Link>
          </li>
        </ul>
      </div>
    );
  }

  export default HomePage;
  ```

- _NavLink is very much like Link, however it adds an "active" class to the rendered element when it's `to` prop mathces the current location._

- Using an anchor tag `<a>` for linking reloads the entire page but Link and NavLink doesn't.

<br>
<br>

## Nested Routes

Nested routes provides the feel for nesting pages.

```jsx
//App.jsx

import { BrowserRouter, Routes, Route } from "react-router-dom";
import AppPage from "./pages/AppPage";
import Login from "../src/pages/Login";
import Pricing from "../src/pages/Pricing";
import HomePage from "./pages/HomePage";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage></HomePage>}></Route>
        <Route path="login" element={<Login></Login>}></Route>
        <Route path="pricing" element={<Pricing></Pricing>}></Route>
        <Route path="app" element={<AppPage></AppPage>}>
          <Route index element={<p>default for app page</p>}></Route>
          <Route path="tab1" element={<p>This is tab1</p>}></Route>
          <Route path="tab2" element={<p>This is tab2</p>}></Route>
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
```

```jsx
//AppPage.jsx

import { NavLink, Outlet } from "react-router-dom";

function AppPage() {
  return (
    <div>
      <ul>
        <li>
          <NavLink to="tab1">Tab 1</NavLink>
        </li>
        <li>
          <NavLink to="tab2">Tab 2</NavLink>
        </li>
      </ul>
      <Outlet></Outlet>
    </div>
  );
}

export default AppPage;
```

- The `Outlet` component is used to define where child routes should be rendered within a parent route. In our case, the child routes (tab1 and tab2) will be rendered in the AppPage.
- The location is set to the `Route` with the `index` prop whenever the children path's are not used. (Basically the default for the parent of the nested routes)
