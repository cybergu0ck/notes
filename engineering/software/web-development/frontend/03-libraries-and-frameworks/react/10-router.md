# Single Page Application

A single page application (SPA) is a web application that interacts with the user by dynamically rewriting the current page rather than loading entire new pages from the server.

<br>

## Routing

It is the process of matching different URLs to different UI views (react components)

<br>
<br>
<br>

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

- _NavLink is very much like Link, however it adds an "active" class to the rendered element when it's `to` prop mathces the current location._ This class can be used in CSS to specifically highlight the current state.

- Using an anchor tag `<a>` for linking reloads the entire page but Link and NavLink doesn't.
  ```jsx
  <a href="/pricing">Pricing</a> <!-- Reloads the page! -->
  ```

<br>

### `to` prop

- A Link component with the `to` prop leading with a '/' will not append to the existing root url. For illustration, assume the current URL is root/home/app and then the following link is accessed, now the url will be root/login.

  ```
  <Link to="/login">
  ```

- A Link component with the `to` prop without any '/' will append to the existing url. Considering the previous illustration, now when the following link is accessed, the url will be root/home/app/login.

  ```
  <Link to="/login">
  ```

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
      <Outlet></Outlet>{" "}
      {/* This is where the child routes will be rendererd. */}
    </div>
  );
}

export default AppPage;
```

- The `Outlet` component is used to define where child routes should be rendered within a parent route. In our case, the child routes (tab1 and tab2) will be rendered in the AppPage.
- The location is set to the `Route` with the `index` prop whenever the children path's are not used. (Basically the default for the parent of the nested routes)

<br>
<br>

## Route with Parameters

_Parameters are placeholders in the URL that facilitates the state to be stored directly in the URL._

//TODO - Link to the notes on storing state in the URL present in state management.

Consider the following code for the explanation.

```jsx
//App.jsx

import { BrowserRouter, Routes, Route } from "react-router-dom";
import HomePage from "./components/HomePage";
import UserProfile from "./components/UserProfile";
import AppPage from "./components/AppPage";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage></HomePage>}></Route>
        <Route path="app" element={<AppPage></AppPage>}></Route>
        <Route path="app/:user" element={<UserProfile></UserProfile>}></Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
```

```jsx
//HomePage.jsx

import { Link } from "react-router-dom";

function HomePage() {
  return (
    <Link to="app">
      <button>Go to App</button>
    </Link>
  );
}

export default HomePage;
```

```jsx
//AppPage.jsx

import { Link } from "react-router-dom";

function AppPage() {
  const user1 = { name: "TerranceHill", role: "Deputy" };
  const user2 = { name: "BudSpencer", role: "Sherif" };

  return (
    <div>
      <Link to={`${user1.name}`}>
        <button>Terrance Hill</button>
      </Link>
      <Link to={`${user2.name}`}>
        <button>Bud Spencer</button>
      </Link>
    </div>
  );
}

export default AppPage;
```

```jsx
//UserProfile.jsx

import { useParams } from "react-router";

function UserProfile() {
  const { user } = useParams();

  return (
    <div>
      <h1>Name: {user}</h1>
    </div>
  );
}

export default UserProfile;
```

<br>

### Setting up the Route

The following syntax is used to setup the parameter, here `user` is the name of the parameter.

```jsx
<Route path="/:user" element={<UserProfile></UserProfile>}></Route>
```

<br>

### Linking to the Route containg Parameters

The route is linked using the Link component and it's `to` prop. In this code, when the button is cliked, `user1.name` is the value for the parameter `user`. The value of the parameter is appended to the exisiting URL, hence the URL changes from `.../app` to `.../app/<value of the parameter>`. This url will be picked up by the router and the associated component will be loaded (`<UserProfile>` in this case).

```jsx
<Link to={`${user1.name}`}>
  <button>Terrance Hill</button>
</Link>
```

- It is important that the value for `to` doesn't include `/` as the start.

<br>

### Accessing the Parameters

The `useParams` function facilitates the access to the parameters from the current route.

```jsx
const { user } = useParams(); //The name of the variable must be the name of the parameter!
```

<br>
<br>

## Route with Queries

_Queries are key-value pairs in the URL that facilitates the state to be stored directly in the URL._

Consider the following code.

```jsx
//App.jsx
import { BrowserRouter, Routes, Route } from "react-router-dom";
import HomePage from "./components/HomePage";
import UserProfile from "./components/UserProfile";
import AppPage from "./components/AppPage";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage></HomePage>}></Route>
        <Route path="app" element={<AppPage></AppPage>}></Route>
        <Route path="app/:user" element={<UserProfile></UserProfile>}></Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
```

```jsx
//HomePage.jsx

import { Link } from "react-router-dom";

function HomePage() {
  return (
    <Link to="app">
      <button>Go to App</button>
    </Link>
  );
}

export default HomePage;
```

```jsx
//AppPage.jsx

import { Link } from "react-router-dom";

function AppPage() {
  const user1 = { name: "TerranceHill", role: "Deputy" };
  const user2 = { name: "BudSpencer", role: "Sherif" };

  return (
    <div>
      <Link to={`${user1.name}?role=${user1.role}&is_good=${true}`}>
        <button>Terrance Hill</button>
      </Link>
      <Link to={`${user2.name}?role=${user1.role}&is_good=${false}`}>
        <button>Bud Spencer</button>
      </Link>
    </div>
  );
}

export default AppPage;
```

```jsx
//UserProfile.jsx

import { useParams } from "react-router";
import { useSearchParams } from "react-router-dom";

function UserProfile() {
  const { user } = useParams();

  const [searchParams, setSearchParams] = useSearchParams();
  const role = searchParams.get("role");
  const is_good = searchParams.get("is_good");

  return (
    <>
      <div style={{ display: "flex" }}>
        <div style={{ marginRight: "30px" }}>
          <h3>Name: {user}</h3>
          <h3>Role: {role}</h3>
          <h3>Good: {is_good}</h3>
        </div>

        <table border="1">
          <thead>
            <tr>
              <th>Folks present</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>{role}</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div style={{ marginTop: "30px" }}>
        <button
          onClick={() => setSearchParams({ role: "Boss", is_good: "Always" })}
        >
          Change Role
        </button>
      </div>
    </>
  );
}

export default UserProfile;
```

<br>

### Linking the Query

Queries need not be set in the Route but are directly linked using the following syntax.

```jsx
<Link to={`${user1.name}?role=${user1.role}&is_good=${true}`}>
  <button>Terrance Hill</button>
</Link>
```

- multiple queries can be used using `&`.
- Queries can be used without Parameters (unlike the above code).
- Queries get appended to the existing URL just like parameters.

<br>

### Accessing and Setting the queries

```jsx
import { useSearchParams } from "react-router-dom";
const [searchParams, setSearchParams] = useSearchParams();
```

- The queries in the active url can be accessed by calling the get method on the searchParams object with the name of the query as the parameter.

  ```jsx
  const role = searchParams.get("role");
  const is_good = searchParams.get("is_good");
  ```

- The queries can be set by passing a new object containing the values for the queries as a parameter to the setSearchParams function.

  ```jsx
  setSearchParams({ role: "Boss", is_good: "Always" });
  ```

<br>
<br>

## Programmatic Navigation

<br>

### Imperative Method

This is acheived using `useNavigate` hook from the "react-router-dom".

```jsx
import { useNavigate } from "react-router-dom";
const navigate = useNavigate(); //navigate is a function that is to be used to redirect the url.
```

- Here when the component is clicked the url will be routed to ".../form".

  ```jsx
  <Button
    onClick={() => {
      navigate("form");
    }}
  />
  ```

- Navigating backwards :

  ```jsx
  <Button
    onClick={() => {
      navigate(-1);
    }}
  />
  ```

<br>

### Declarative Method

This is acheived by using `Navigate` component from the "react-router-dom".

- Here, when the url lands on "app", It displays Tab1 component because of the Route component having the `index` prop. However it is important to observe that the url is not directed to "app/tab1".

  ```jsx
  import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
  import AppPage from "./pages/AppPage";
  import Login from "../src/pages/Login";
  import Pricing from "../src/pages/Pricing";
  import HomePage from "./pages/HomePage";
  import Tab1 from "./pages/Tab1";
  import Tab2 from "./pages/Tab2";

  function App() {
    return (
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<HomePage></HomePage>}></Route>
          <Route path="login" element={<Login></Login>}></Route>
          <Route path="pricing" element={<Pricing></Pricing>}></Route>
          <Route path="app" element={<AppPage></AppPage>}>
            <Route index element={<Tab1></Tab1>}></Route>
            <Route path="tab1" element={<Tab1></Tab1>}></Route>
            <Route path="tab2" element={<Tab2></Tab2>}></Route>
          </Route>
        </Routes>
      </BrowserRouter>
    );
  }

  export default App;
  ```

- Here, the `Navigate` component redirects the route itself. Hence changing the url with it.

  ```jsx
  import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
  import AppPage from "./pages/AppPage";
  import Login from "../src/pages/Login";
  import Pricing from "../src/pages/Pricing";
  import HomePage from "./pages/HomePage";
  import Tab1 from "./pages/Tab1";
  import Tab2 from "./pages/Tab2";

  function App() {
    return (
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<HomePage></HomePage>}></Route>
          <Route path="login" element={<Login></Login>}></Route>
          <Route path="pricing" element={<Pricing></Pricing>}></Route>
          <Route path="app" element={<AppPage></AppPage>}>
            <Route index element={<Navigate to="tab1"></Navigate>}></Route>
            <Route path="tab1" element={<Tab1></Tab1>}></Route>
            <Route path="tab2" element={<Tab2></Tab2>}></Route>
          </Route>
        </Routes>
      </BrowserRouter>
    );
  }

  export default App;
  ```

- Without the `replace` prop in the `Navigate` component, navigating backward is not possible. [The `replace` prop, when set to true, replaces the current entry in the navigation history with the new location. This means that the current entry will be removed from the history stack, and navigating back will not go to the replaced entry.]

<br>
