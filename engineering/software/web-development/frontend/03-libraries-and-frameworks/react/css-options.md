# Styling Options in React

| Styling Option    | Scope             |
| ----------------- | ----------------- |
| Inline CSS        | Local Scope       |
| CSS or Sass File  | Global Scope      |
| CSS Modules       | Component Scope   |
| CSS in JS         | Component Scope   |
| Utility First CSS | JSX Element Scope |

<br>
<br>

## CSS Module

- CSS Modules comes along with the both create-react-app and vite.
- Here we have a CSS file per component.
- The convention of file naming is `<componentname.module.css>`.
- Class names must be used in the css module file.
- It is bad practice to use element selectors as shown below in css modules as it can apply styling globally.

  ```
  ul{
      <!-- styles -->
  }
  ```

- To apply to styling to the component import the style from the respective css module file and use it as className withing the component.

### illustration

Say we have two components `LeftPanel` and `RightPanel` used in the `App.jsx`. `LeftPanel.module.css` and `RightPanel.module.css` are the css module files for respective components. Notice that even though the same classnames are being used in both the css files, react internally mangels the classnames to make it different so that these classnames are specific to the component!

```
//LeftPanel.module.css
.panel {
  background-color: aquamarine;
}
```

```jsx
// LeftPanel.jsx
import styles from "./LeftPanel.module.css";

function LeftPanel() {
  return <div className={styles.panel}>Left Side</div>;
}

export default LeftPanel;
```

```
//RightPanel.module.css
.panel {
  background-color: aquamarine;
}
```

```jsx
// RightPanel.jsx
import styles from "./RightPanel.module.css";

function RightPanel() {
  return <div className={styles.panel}>Right Side</div>;
}

export default RightPanel;
```

```jsx
//App.jsx
import LeftPanel from "./components/LeftPanel";
import RightPanel from "./components/RightPanel";

function App() {
  return (
    <div>
      <LeftPanel></LeftPanel>
      <RightPanel></RightPanel>
    </div>
  );
}

export default App;
```

- To apply a style globally but using the css module file,

  ```css
  :global(.banner) {
    background-color: blueviolet;
  }
  ```

  - In this case, we can use the text directly in the classname `<div className="banner">Right Side</div>`
