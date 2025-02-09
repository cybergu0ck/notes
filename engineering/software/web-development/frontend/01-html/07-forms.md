# HTML Forms

<br>
<br>

## `<label>`

The `<label>` element in HTML is used to associate a label with an input element.

```html
<label for="<id-of-input>"> </label>
```

<br>
<br>

## `<input>`

It is used to create various types of input fields where users can enter data or make selections.

<br>

### `type` attribute

- **text**: Creates a single-line text input field.
- **password**: Creates a password input field where the entered text is masked.
- **email**: Creates an email input field with built-in validation for email addresses.
- **number**: Creates a numeric input field.
- **checkbox**: Creates a checkbox for binary choices.
- **radio**: Creates a radio button for selecting from multiple options in a group.
- **date**: Creates a date input field for selecting a date from a calendar.
- **file**: Creates a file upload input field for uploading files.
- **submit**: Creates a submit button for submitting a form.
- **button**: Creates a generic button.

<br>

### `name` attribute

This attribute provides a name for the input field, which is used when submitting a form. It's essential for identifying the data on the server-side.

- The name attribute identifies the input value if it is sent to a server via a traditional GET or POST of a form.
- Checkout [stackoverflow](https://stackoverflow.com/questions/26061651/what-is-the-purpose-of-the-html-name-attribute) to understand this.

<br>

### `value` attribute

Specifies the default value for the input field. For example, you can pre-fill a text input with a default value.

<br>

### `placeholder` attributre

This attribute provides a short hint or example of the expected input format. It's displayed in the input field before the user enters any text.

<br>

### `disabled` attribute

If set to "disabled," it prevents the user from interacting with the input field. It's often used for read-only or inactive fields.

<br>
<br>

## `<textarea>`

The `<textarea>` element is an HTML form control that allows users to input multiple lines of text.

<br>

### `name`, `id`, `placeholder`, `disabled` attributes

Same functionality as above.

<br>
<br>

## `rows` and `cols`
