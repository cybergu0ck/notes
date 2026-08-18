# React Components

<br>

## Component

_**"Component"** is a blueprint for creating independent reusable building blocks that enables the composition of UI._

- Components describe what the UI should look like and how it should behave.
- Components can be class-based components or functional components.
- Class based components are depricating and are not preferred.

<br>

### Functional Component

_"**Functional Component**" is a javascript function that return JSX._

```jsx
function MyButton() {
  return <button>Click Me</button>; //This is JSX!
}
```

- The name of the function must always start with a capital letter.
- Components must be pure in terms of props and state. See [immutability of props](04.props.md#immutability-of-props)

<br>
<br>

## Component Instance

_***"Component instance"*** is a specific occurrence or instantiation of a component._

- Component is the blueprint and component instance is an instance of the component that is created from that blueprint.
- However "_component_" and "_component instance_" are used interchangebly.
- Each component instance can have its own set of props and state, making it self-contained.

<br>
<br>

## React Element

_A "***React element***" is a plain JavaScript object that represents a description of what is to be rendered on the screen._

- Component Instances (specifically the JSX) are converted to react elements using the `React.createElement()` function.
- It is this react element that will be converted to actual DOM elements in the html.

<br>
<br>

## Guidelines for creating components

- Code components such that they follow:

  <ol type="1">
    <li>Logical Seperation of content/layout.</li>
    <li>Reusability.</li>
    <li>Minimal Responsibilty (if not single responsibility).</li>
    <li>Personal Coding Style.</li>
  </ol>

- Name the components according to what it does or displays.
- Longer names are okay.
- When in doubt, start with a big component and then split into smaller components when necessary.
- A large component containing a lot of elements or components wrapped inside is bad.
- Similar is the case of having a lot of very small sized components.

<br>

### Seperation of concerns

- Traditionally, a web application is seperated by **_one technology per file_**. We seperate HTML, CSS and Javascript into different files although they are tightly coupled.
- With react, a web application is seperated by **_one component per file_**. We seperate the Components into different files which have JSX (HTML, CSS and Javascript) in them, which are also tightly coupled.

<br>

---

<br>
