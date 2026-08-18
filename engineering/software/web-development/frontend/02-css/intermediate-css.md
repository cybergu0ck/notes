# Intermediate CSS

- Checkout [CSS Cheat sheet](https://htmlcheatsheet.com/css/)

<br>
<br>

# Default Styles

The default style sheets are used to reduce browser inconsistencies in things like default line heights, margins and font sizes of headings, and so on.

- [The Meyer Reset](https://meyerweb.com/eric/tools/css/reset/) is most popular, it removes all default styles.
- [Normalize.css](https://nicolasgallagher.com/about-normalize-css/) is another popular one. It’s a little different in that it doesn’t remove all the default styles, but tweaks them slightly to ensure that browsers are consistent.

<br>
<br>

# CSS Units

## Absolute Units

- Absolute units are those that are always the same in any context.
- `px` is the only absolute unit you should be using for web projects.

<br>

## Relative Units

- Relative units are units that can change based on their context.
- `em` and `rem` both refer to a font size, though they are often used to define other sizes in CSS, but as a rule-of-thumb, prefer `rem`.
- **`1em`** is the font-size of an **element** (or the element’s parent if you’re using it to set font-size).
  - So, for example, if an element’s font-size is 16px, then setting its width to 4em would make width 64px (16 \* 4 == 64).
- `1rem` is the font-size of the **root element** (either :root or html).

  - The math works the same with rem as it did with em, but without the added complexity of keeping track of the parent’s font size. Relying on em could mean that a particular size could change if the context changes, which is very likely not the behavior you want.

- The units `vh` and `vw` relate to the size of the viewport. Specifically, 1vh is equal to 1% of the viewport height and 1vw is equal to 1% of the viewport width. (Google this for more info)
