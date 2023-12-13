# State Management

<br>
<br>

## Types of State

Based on the accessibility of the state:

1. Local State : A State that is needed by only one or few components.
2. Global State : A State that is needed by many components.

<br>

Based on the domain of the state:

1. Remote State : Application data loaded from a remote server (API).
2. UI State : Data other than Remote State (theme, list filters, form data etc.)

<br>
<br>

## State Placement Options

| Option              | Tools                                | Use Case                            |
| ------------------- | ------------------------------------ | ----------------------------------- |
| Local Component     | useState, useReducer, useRef         | Local State                         |
| Parent Component    | useState, useReducer, useRef         | Lifting up State                    |
| Context             | Context API + useState, useReducer   | Global State (preferably UI state)  |
| Third party library | Redux, React Query, SWR, Zustand etc | Gloabl State (Remote or UI)         |
| URL                 | React Router                         | Global State, passing between pages |
| Browser             | Local Storage, Session Storage etc.  | Storing data in user's browser      |

<br>

|              | Local State                             | Global State                                                                               |
| ------------ | --------------------------------------- | ------------------------------------------------------------------------------------------ |
| UI State     | useState, useReducer, useRef            | context API + useState/useReducer; Redux, Zustand, Recoil etc; React Router                |
| Remote State | fetch + useEffect + useState/useReducer | context API + useState/useReducer; Redux, Zustand, Recoil etc; React Query; SWR; RTK Query |
