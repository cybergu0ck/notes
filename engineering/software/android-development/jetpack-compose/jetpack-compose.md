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

## LazyColumn

In Jetpack Compose, a scrollable list can be made using the LazyColumn composable. The difference between a LazyColumn and a Column is that a Column should be used when you have a small number of items to display, as Compose loads them all at once. A Column can only hold a predefined, or fixed, number of composables. A LazyColumn can add content on demand, which makes it good for long lists and particularly when the length of the list is unknown. A LazyColumn also provides scrolling by default, without additional code. Declare a LazyColumn composable inside of the AffirmationList() function. Pass the modifier object as an argument to the LazyColumn.

## Screen density

Screen density refers to how many pixels per inch or dots per inch (dpi) are on the screen. For a medium-density device (mdpi), there are 160 dots per inch on the screen, while an extra-extra-extra-high-density device (xxxhdpi) has 640 dots per inch on the screen.

Below is a list of [density qualifiers](https://developer.android.com/training/multiscreen/screendensities#TaskProvideAltBmp) on Android:

- mdpi - resources for medium-density screens (~160 dpi)
- hdpi - resources for high-density screens (~240 dpi)
- xhdpi - resources for extra-high-density screens (~320 dpi)
- xxhdpi - resources for extra-extra-high-density screens (~480 dpi)
- xxxhdpi - resources for extra-extra-extra-high-density screens (~640 dpi)
- nodpi - resources that are not meant to be scaled, regardless of the screen's pixel density
- anydpi - resources that scale to any density
