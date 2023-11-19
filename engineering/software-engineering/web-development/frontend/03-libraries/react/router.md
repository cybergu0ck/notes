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

## Routes

```jsx
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Homepage from "./pages/Homepage";
import Product from "./pages/Product";
import Pricing from "./pages/Pricing";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Homepage></Homepage>}></Route>
        <Route path="product" element={<Product></Product>}></Route>
        <Route path="pricing" element={<Pricing></Pricing>}></Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
```

<br>
<br>

## Links

Use the `<Link/>` or `<NavLink/>` from react-router-dom

```jsx
import { Link } from "react-router-dom";

function Component() {
  return (
    <div>
      <Link to="/pricing">Pricing</Link>
    </div>
  );
}
```

> <br>
> Using an anchor tag with href reloads the entire page! <br> <br>
