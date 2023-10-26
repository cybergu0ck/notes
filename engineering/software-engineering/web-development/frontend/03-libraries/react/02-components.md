# Components

_***"components"*** are blueprints for creating independent reusable building blocks that enables up to compose the UI._

- Components are defined using class-based components or function components in React.
- Components describe what the UI should look like and how it should behave.

<br>
<br>

## Functional Components

They are as easy as creating javascript funcitons returning JSX.

```jsx
function MyButton() {
  return <button>Click Me</button>;
}
// Remember to export them (if needed) using default export or named export.
```

- React components can be class components or functional components, the former is depricated and is not prefered.
- The name of the function must always start with a capital letter.
- Components must be pure in terms of props and state. See [immutability of props](./03.props.md#immutability-of-props)

<br>
<br>

## Component Instances

_***"Component instances"*** are specific occurrences or instantiation of a React components within the application._

- Component instances are what actually get rendered and displayed in your application.
- It is created from a component and represents a single, independent unit in your user interface.
- Each component instance can have its own set of props and state, making it unique and self-contained.

<br>
<br>

## React Element

_A "***React element***" is a plain JavaScript object that represents a description of what is to be rendered on the screen._

- Component Instances (specifically the JSX) are converted to react elements using the `React.createElement()` function.
- It is this react element that will be converted to actual DOM elements in the html.

<br>
<br>

## Seperation of concerns

- Traditionally, a web application is seperated by **_one technology per file_**. We seperate HTML, CSS and Javascript into different files although they are tightly coupled.
- With react, a web application is seperated by **_one component per file_**. We seperate the Components into different files which have JSX (HTML, CSS and Javascript) in them, which are also tightly coupled.

<br>
<br>

## Guidelines for splitting the UI into components

- A large component containing a lot of elements or components wrapped inside is bad. Similar is the case of having a lot of very small sized components.

- Code components such that they follow:

  1. Logical Seperation of content/layout.
  2. Reusability.
  3. Minimal Responsibilty (if not single responsibility).
  4. Personal Coding Style.

- Name the components according to what it does or displays.
- Longer names are okay.
- When in doubt, start with a big component and then split into smaller components when necessary.

<br>
<br>
