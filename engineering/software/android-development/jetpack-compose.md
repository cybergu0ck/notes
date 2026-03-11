# Jetpack compose

Jetpack Compose is a modern toolkit for building Android UIs.

- Compose simplifies and accelerates UI development on Android with less code, powerful tools, and intuitive Kotlin capabilities.
- With Compose, you can build your UI by defining a set of functions, called composable functions, that take in data and describe UI elements.

<br>
<br>
<br>

## Composable functions

Composable functions are the basic building block of a UI in Compose.

- A composable function:
  - Describes some part of your UI.
  - Doesn't return anything.
  - Takes some input and generates what's shown on the screen.

<br>
<br>
<br>

## Annotations

Annotations are means of attaching extra information to code.

- Annotations help tools like the Jetpack Compose compiler, and other developers understand the app's code.
- Annotations is part of Kotlin language syntax.

* Examples :

  ```kotlin
  // Example code, do not copy it over

  @Json
  val imgSrcUrl: String

  @Volatile
  private var INSTANCE: AppDatabase? = null
  ```

* Annotations can have parameters.

  ```kotlin
  @Preview(
    showBackgroung = true,
    name = "My Preview")
  @Composable
  fun GreetingPreview(){
      HappyBirthdayTheme {
          Greeting(name : "Android")
      }
  }
  ```

<br>
<br>
<br>

## Composable annotation

Composable annotation annotation informs the Compose compiler that this function is intended to convert data into UI.

```kt
@Composable
fun Greeting(name: String) {
    Text(text = "Hello $name!")
}
```

- Jetpack Compose is built around composable functions.
- Composable functions define the app's UI programmatically by describing how it should look, rather than focusing on the process of the UI's construction.

<br>
<br>

### Composable function rules

- Compose function should return nothing.
- It should have `@Composable` annotation.
- It must be named in Pascal case. (not camelCase).
- The name must be a noun and not a verb, preposition, adjective, adverb but may be prefixed by adjectives.
  - `DoneButton()` is valid as it is a noun.
  - `RoundIcon()` is valid as it a noun prefixed by an adjective.
  - `DrawTextField()` is invalid name as it is a verb.
  - `TextFieldWithLink()` is invalid as it has preposition.
  - `Bright()` is invalid as it is an adjective.
  - `Outside()` is invalid as it is an adverb.

<br>
<br>
<br>

## State

State refers to any data that can change and affect the UI.

<br>
<br>

### Composition

The Composition is a description of the UI built by Compose when it executes composables.

- Compose apps call composable functions to transform data into UI.

<br>
<br>

### Recomposition

Recomposition is a process where upon a state change Compose re-executes the affected composable functions and updates the UI.

- The only way to modify the Composition is through recomposition.
- To achieve this Compose needs to know the states to be tracked so that it can schedule the recomposition when it receives an upate. The trackable state is known as [Observable state](#observable-state).

<br>
<br>

### Observable state

Observable state is a state that is tracked by Compose.

- Observable state can be immutable (read only).
- Observable state can be mutable, Example : `mutableStateOf()`, t receives an initial value as a parameter that is wrapped in a State object, which then makes its value observable.
