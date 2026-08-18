# Forms

- The _form_ element wraps all of the inputs a user will interact with on a form.

* The form element accepts two essential attributes:

  - `action` attribute which takes a URL value that tells the form where it should send its data to be processed.
  - `method` attribute which tells the browser which HTTP request method it should use to submit the form.

    - We use `GET` when we want to retrieve something from a server.
    - `POST` is used when we want to change something on the server

  ```html
  <form action="example.com/path" method="post"></form>
  ```

<br>
<br>

# Form control elements

## The input element

- It accepts a `type` attribute which tells the browser what type of data it should expect and how it should render the input element.
- It accepts a `placeholder` attribute, which will display the placeholder text as the defualt value in the input.
- The `name` attribute serves as a reference to the data inputted into a form control after submitting it. You can think of it as a variable name for the input. Form input should always have a name attribute; otherwise, it will be ignored when the form is submitted. (This is needed for backend to process the data)

  ```html
  <form action="example.com/path" method="post">
    <input type="text" placeholder="Bob..." name="first_name" />
  </form>
  ```

<br>

### email input

- Email inputs are specialized text inputs just for email addresses.
- To create an email input, we use an input element with `type` attribute of _“email”_:

  ```html
  <label for="user_email">Email Address:</label>
  <input
    type="email"
    id="user_email"
    name="email"
    placeholder="you@example.com"
  />
  ```

<br>

### password input

- Password inputs are another specialized text input. They mask the inputted data.

* A password input can be created using an `input` element with a type of “password”:
  ```html
  <label for="user_password">Password:</label>
  <input type="password" id="user_password" name="password" />
  ```
  <br>

### date input

- It provides a better user experience for choosing dates by rendering a simple date picker calendar
- To create a date input, we use the input element with a `type` attribute of “date”:

  ```html
  <label for="dob">Date of Birth:</label>
  <input type="date" id="dob" name="dob" />
  ```

## Labels

- `labels` are used along side input elements to inform the user what type of data are they expected to enter.
- Labels accept a `for` attribute, which associates it with a particular input. The input we want to associate with a label needs an id attribute with the same value as the label’s for attribute.
  ```html
  <form action="example.com/path" method="post">
    <label for="first_name">First Name:</label>
    <input type="text" id="first_name" placeholder="Bob..." name="first_name" />
  </form>
  ```

<br>

## Using httpbin

- It is a service that will send back a response which will let us view what data was submitted. The JSON output of the following html code is as shown below

  ```html
  <form action="https://httpbin.org/post" method="post">
    <label for="first_name">First Name</label>
    <input type="text" name="first_name" id=" " first_name />
  </form>
  ```

  ```JSON
  "form": {
      "first_name": "GODZILLA"
  }
  ```

<br>

## Text Area

- The text area element provides an input box that can accept text that spans multiple lines like user comments and reviews.
- It can also be resized by clicking and dragging the bottom right corner to make it bigger or smaller.

* To create a text area, we use the `<textarea>` element:

  ```html
  <textarea></textarea>
  ```

<br>

## Select Dropdown

- To create a select dropdown, we use the `<select>` element. Any options we want to display within the select element are defined using `<option>` elements:
- All the option elements should(otherwise the text content inside is used) have a `value` attribute. This value will be sent to the server when the form is submitted.
- We can set one of the options to be the default selected element when the browser first renders the form by giving one of the options the `selected` attribute:

  ```html
  <select name="Car">
    <option value="mercedes">Mercedes</option>
    <option value="tesla">Tesla</option>
    <option value="volvo" selected>Volvo</option>
  </select>
  ```

* We may also split the list of options into groups using the `<optgroup>` element. The optgroup element takes a label attribute which the browser uses as the label for each group:

  ```html
  <select name="Car">
    <optgroup label="gasoline">
      <option value="mercedes">Mercedes</option>
      <option value="volvo">Volvo</option>
    </optgroup>
    <optgroup label="electic">
      <option value="tesla">Tesla</option>
    </optgroup>
  </select>
  ```

<br>
<br>

# Organising form elements

## Fieldset Element

- The fieldset element is a container element that allows us to group related form inputs into one logical unit.

  ```html
  <fieldset>
    <label for="first_name">First Name</label>
    <input type="text" id="first_name" name="first_name" />

    <label for="last_name">Last Name</label>
    <input type="text" id="last_name" name="last_name" />
  </fieldset>
  ```

<br>

## Legend

The legend element is used to give field sets a heading or caption so the user can see what a grouping of inputs is for.

<br>

# Form Validation

- Validations allow us to set specific constraints or rules that determine what data users can enter into an input. When a user enters data that breaks the rules, a message will appear, providing feedback on what was wrong with the entered data and how to fix it.

<br>

## Required Validation

- To make a field required, we simply add the `required` attribute to it:
- To ensure a good user experience and to meet accessibility guidelines, we should always indicate which fields are required. This will often be done by adding an asterisk(\*) to the required field label

<br>

## Text Length Validations

- To add the minimum length validation, we give the form control a `minlength` attribute with an integer value that represents the minimum amount of characters we want to allow in the form control:

```html

```

- To add a maximum length validation, we give the form control a maxlength attribute with an integer value which represents the maximum amount of characters we want to allow in the form control:

```html

```

<br>

## Number Range Validation

- To add a minimum value validation, we give the form control a `min` attribute with an integer value which represents the minimum number we want the form control to accept:

```html

```

- To add a maximum value validation, we give the form control a max attribute with an integer value which represents the maximum number we want the form control to accept:

```html

```

<br>

## Pattern Validations

> Fill Notes

## Styling Vaidation

> Fill Notes
