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

## Route with parameters

Parameters in the route are placeholders in the URL that capture values and make them accessible to the components.

```jsx
<Router>
  <Route path="cities/:city_id" element={MyComponent} />
</Router>
```

- Generally the parameter will be the value of a variable or a state in which case the state is being stored in the URL.

<br>

### Setting the parameters

We can set the parameters using the Link component and it's `to` prop.

```jsx
//id here can be any variable
<Link to={${id}}>{/* children components goes here*/}</Link>
```

- When we are in the route "cities" and we click the element having the above link, the url becomes "cities/{value of the variable "id"}".
- This will match the Route having the path "cities/:city_id" and the corresponding element will be loaded.

<br>

### Accessing the parameters

The `useParams` function facilitates the access to the parameters from the current route.

```jsx
import { useParams } from "react-router-dom";
const { city_id } = useParams(); //Here city_id will have the value of the variable "id"
```

<br>
<br>

## Route with Queries

Queries are set in the Link component's to prop.

```jsx
//position is a variable

<Link
  className={styles.cityItem}
  to={`cities?lat=${position.lat}&{position.lng}`}
></Link>
```

- When the element with the above link is clicked, The Router tries to match the Route containing ".../cities" and then loads the element corresponding to that route.
- It also appends the above queries in the URL. It looks something like:

  ```
  http://localhost:5173/app/cities?lat=38.727881642324164&lng=-9.140900099907554
  ```

- The usefullness of queries is that we save some data directly in the URL hence when the URL is shared, the data is also shared, which means that the webpage will be loaded to exact state when it is shared.

<br>

### Accessing and Setting the queries

```jsx
import { useSearchParams } from "react-router-dom";
const [searchParams, setSearchParams] = useSearchParams();
```

- The queries in the active url can be accessed by calling the get method on the searchParams object with the name of the query as the parameter.

  ```jsx
  const lat = searchParams.get("lat");
  ```

- The queries can be set by passing a new object containing the values for the queries as a parameter to the setSearchParams function.

  ```jsx
  setSearch({ lat: 23, lng: 50 });
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
