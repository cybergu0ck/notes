# The System Font Stack

- If the font specified is not installed in the user's machine, then it'll be defaulted to default html font, which is mostly ugly.

- The following code will try using the default font of the system’s user interface. It will go through each of those fonts until it finds one that is installed on the system, and then use that.

  ```css
  body {
    font-family: system-ui, "Segoe UI", Roboto, Helvetica, Arial, sans-serif,
      "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
  }
  ```

<br>
<br>

# Online Font Libraries

- We can use fonts from [google font](https://fonts.google.com/) or [font library](https://fontlibrary.org/)

- To use a font from one of these libraries, we have to select a font and then copy a snippet from the website to import that font from their server into our website. Importing can be done in 2 ways.

* The import will make it available for us to use in our CSS:

  ```css
  body {
    font-family: "Roboto Mono", monospace;
  }
  ```

<br>

## 1.Using `<link>`

- We can import by using the `<link>` tag to put in your HTML like so

  ```css
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto+Mono:ital,wght@1,300&display=swap" rel="stylesheet">
  ```

<br>

## 2.Using `@import`

- Or use the `@import` tag that can be dropped at the top of a CSS file.

  ```css
  @import url("https://fonts.googleapis.com/css2?family=Roboto+Mono:ital,wght@1,300&display=swap");
  ```

<br>
<br>

# Text Styles

<br>

## font-style

```css
h1 {
  font-style: italic;
}
```

<br>

## letter-spacing

- Without letter spacing

  ```css
  p {
    font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
    letter-spacing: 0.5rem;
  }
  ```

  ![image](./_assets/spacing1.png)

- With letter spacing

  ```css
  p {
    font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
    letter-spacing: 0.5rem;
  }
  ```

  ![image](./_assets/spacing2.png)

<br>

## line height

- line-height property

  ```css
  p#left {
    font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  }

  p#right {
    font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.5;
  }
  ```

  ![image](./_assets/lineheight.png)

<br>

## text-transform

- Text transform simply changes the case of the given text.

<br>

## text-shadow

- `text-shadow` adds a shadow around the text in the selected element. This one is best used sparingly, but can be used to great effect in headings or other presentational text.

<br>

## ellipsis

- This one isn’t a single property, With the `text-overflow` property, you can truncate overflowing text with an ellipsis. Making an overflow happen, however, requires the use of a couple other properties because the default behavior of text simply printing outside its container isn’t technically considered an `overflow`
