# Framework vs Library

- Both library and framework are reusable code written by developers.
- What distinguishes them is a term called _"Inversion of control"_. When using a library, the dev is in charge of the flow of the application (when and where to call the library). When using a framework, the framework is in charge of the flow.

<br>
<br>

# Why do Front-end Frameworks exists

An interactive webpage is all about handling the data and displaying the webpage accordingly. This means that the data and the UI must be in sync.

Using Vanilla Javascript (or JQuery) to do the above is not ideal for the following reasons:

1. Requires a lot of DOM manipulation and traversing (imperative).
2. Results in Spaghetti code!
3. Data is usually stored in the DOM (which is shared across the entire app), hard to reason and solve bugs.

In addition to solving the above mentioned drawbacks, the front-end frameworks provide:

1. A correct way of structuring and writing code.
2. Gives developers and teams a consistent way of building applications.
