# HTML Fundamentals

<br>
<br>

## DOCTYPE

- It is short for Document Type Declaration.
- It specifies the type and version of the HTML being used in a web document.
- The primary purpose of a DOCTYPE declaration is to inform web browsers and other user agents about the version of HTML or XML that a web page is written in.

- Different versions of HTML have their own DOCTYPE declarations. The choice of DOCTYPE depends on the version of HTML you are using. The following is for HTML5.

  ```html
  <!DOCTYPE html>
  <html>
    ...
  </html>
  ```

- Older versions are not simplified, for example HTML 4.01 Strict uses `<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">`
- It is self closing (doesn't have a closing tag)

<br>
<br>

## Fundamental Tags

<br>

### `<html>`

- The `<html>` tag is the root element of an HTML document. It encloses all other HTML elements on the page.
- It typically contains two main sections: the `<head>` section and the `<body>` section.

<br>

### `<head>`

- The `<head>` element contains meta-information about the HTML document, such as the document's title, character encoding, and links to external resources like stylesheets and scripts.
- It does not directly display any content on the web page itself.

<br>

### `<title>`

The `<title>` element is used within the `<head>` section to define the title of the web page. This title is displayed in the browser's title bar or tab.

<br>

### `<meta>`

The `<meta>` element is used to provide metadata about the HTML document, such as character encoding, author information, and keywords for search engines.

<br>

### `<link>`

The `<link>` element is used to link external resources to the HTML document. It is commonly used to link stylesheets (CSS) to control the page's visual presentation.

<br>

### `<style>`

`<style>` tag is used to define inline css.

<br>

### `<script>`

The `<script>` element is used to include JavaScript code within an HTML document.

<br>
<br>

## Comments

```html
<!--  Comment -->
```

<br>
<br>
