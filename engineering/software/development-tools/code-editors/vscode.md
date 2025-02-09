# VS Code

<br>
<br>

## VS Code Key Bindings

- Set these keybindings for all code editors (Shortcuts with mouse clicks are not modifiable)

  | Shortcut                                         | Key Binding               |
  | ------------------------------------------------ | ------------------------- |
  | Selected Multi-cursor (VS Code Specific)         | Alt + Mouse Click         |
  | Continous Multi-cursor (VS Code Specific)        | Alt + Shift + Mouse Click |
  | Markdown: Open Preview                           | Ctrl + Shift + V          |
  | Move Line Up/Down                                | Alt + Up/Down             |
  | Copy Line Up                                     | Alt + Shift + Up/Down     |
  | Go to File                                       | Ctrl + P                  |
  | Add Selection to Find Next Match                 | Ctrl + D                  |
  | Cursor Undo                                      | Ctrl + U                  |
  | Select Entire Line                               | Ctrl + L                  |
  | Find                                             | Ctrl + F                  |
  | Replace                                          | Ctrl + H                  |
  | Go to a Line                                     | Ctrl + G                  |
  | Toggle Line Comment                              | Ctrl + /                  |
  | Toggle Block Comment                             | Ctrl + Shift + /          |
  | View:Open Previous Recently Used Editor in Group | Ctrl + Tab                |
  | Remove All Breakpoints                           | Ctrl + Shift + F9         |
  | Toggle Primary Side Bar (Left Bar)               | Alt + B                   |
  | Toggle Pannel (Bottom, terminal...)              | Alt + J                   |
  | Delete Line                                      | Ctrl + Shift + K          |
  | Format Document                                  | Shift + Alt + L           |
  | Format Selection                                 | Ctrl + K and Ctrl + F     |

  <br>
  <br>

## Snippets

- The following snippets are used for writing react code.
  ```
  {
    "reactComponent": {
      "prefix": "rfc",
      "scope": "javascript,typescript,javascriptreact",
      "body": [
      "function ${1:${TM_FILENAME_BASE}}() {",
      "\treturn (",
      "\t\t<div>",
      "\t\t\t$0",
      "\t\t</div>",
      "\t)",
      "}",
      "",
      "export default ${1:${TM_FILENAME_BASE}}",
      ""
      ],
      "description": "React component"
    },
    "importCSSModule": {
      "prefix": "csm",
      "scope": "javascript,typescript,javascriptreact",
      "body": ["import styles from './${TM_FILENAME_BASE}.module.css'"],
      "description": "Import CSS Module as `styles`"
      },
    "ClassName with formated string": {
      "prefix": "cla",
      "body": [
          "className = {${1:}}"
      ],
      "description": "ClassName with formated string"
    } ,
  }
  ```

## Extensions

<br>

### Prettier

To set up prettier:

1. Download the prettier extension.
2. Head to user settings (can be found by searching on command pallete Shift + Ctrl + P)
3. Search "Default Formatter" settings and make Prettier as the default formatter.
4. Search "Format on Save" settings and toggle it on.

<br>
<br>

## Miscallaneous

<br>

### Setting default shell for integrated terminal

1. Open Terminal ( Ctrl + `)
1. Click on the drop down present in the top right side beside the name of the shell.
1. Select "Select Default Profile" option
1. Select the shell to be made default.

<br>

### Setting custom font size for the Integrated Terminal

1. Open settings.JSON using command Pallete (Ctrl + Shift + P)
2. Add the line `"terminal.integrated.fontSize": 25,` with the desired font size.

<br>
<br>

### Configuring default C++ formatter

- To configure default C++ formatter to use K&R style of braces, follow this [stack overflow](https://stackoverflow.com/questions/45823734/visual-studio-code-formatting-for) thread.
