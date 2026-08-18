# Standard

<br>
<br>
<br>

## Headings

- The name of the topic should be the `#` heading.

  - At one point, file names represented the topic and `#` started with sub topics. This is not good if markdown is converted to pdf as filename won't be in the body of the pdf.

- The addition of `#` and the `<br>` should be 5.
  - A single `#` heading should be preceeded by four `<br>`.
  - A single `####` heading should be preceeded by one `<br>`.

* Only first letter of the heading must be capital.

  - Prefer `# Storing resource file` over `# Storing Resource File`.

* Try to use only letters in the headings and avoid special characters like `.` `-` etc.

  - Reson : linking topics in markdown becomes easy.

* Do not use code in heading names. Example : If the subtopic is about methods,

  - Prefer the following (Reason : linking topics in markdown becomes easy)

    ```
    # Accessing the values of the map

    1. Using `[]` operator

    1. Using `at` method
    ```

  - Instead of

    ```
    # Accessing values of the map using `[]` oepator

    # Accessing values of the map using `at` oepator
    ```

<br>
<br>
<br>

## Storing resource files

- `_resources` will be the standard name of the directory.
- Stick to "Locality of behaviour" and place the directory in the same level as the markdown file which uses the resource files.

  - Reason : The links will be relative and if and when the directory is moved the \_resources directory will also be moved and links don't break.

- Use the following segregation based on resource file types.

  ```
  _resources
      * images (.jpg, .jpeg, .png)
      * videos (.mp4, .avi, .mov)
      * drawings (.drawio, .excalidraw, or .psd)
      * documents (.pdf, .doc, .xlsx, .ppt)
  ```
