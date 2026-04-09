# Contents

- [LazyColumn](#lazycolumn)
- [Screen density](#screen-density)

<br>
<br>
<br>




## LazyColumn

In Jetpack Compose, a scrollable list can be made using the LazyColumn composable. The difference between a LazyColumn and a Column is that a Column should be used when you have a small number of items to display, as Compose loads them all at once. A Column can only hold a predefined, or fixed, number of composables. A LazyColumn can add content on demand, which makes it good for long lists and particularly when the length of the list is unknown. A LazyColumn also provides scrolling by default, without additional code. Declare a LazyColumn composable inside of the AffirmationList() function. Pass the modifier object as an argument to the LazyColumn.

<br>
<br>
<br>

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
