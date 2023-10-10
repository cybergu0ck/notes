# ESLint

Linters are tools that scan code for bugs and errors, check for subjective, stylisitic preferences and report any errors that they find.

- ESLint is one among the linter tools.

<br>
<br>

## Setting up ESLint for VS Code Editor

The following steps are to integrate the ESLint with VSCode (NOT TO SETUP ESLINT FOR A PROJECT).

1.  Install the ESLint VSCode extension.
2.  Enable Formatting on save to automatically fix syntax and formatting issues,

    - Using command palette, open **Preferences: Open Workspace Settings (JSON)**
    - Write the following to settings.json file that will be opened.

      ```
      {
          "editor.codeActionsOnSave": {
              "source.fixAll.eslint": true
          },
          "eslint.validate": ["javascript"]
      }
      ```

3.  Customise ESLint rules

    - Open up the `.eslintrc.json` file.
    - Add rules in the key named "rules"

      ```json
      {
        //...
        "rules": { "no-console": "off" }
      }
      ```

<br>
<br>

## Setup ESLint (for a project)

1. Initialise the javacript project, this will create the pacakge.json file.

   ```bash
   npm init --yes
   ```

2. Setup ESLint, this will create ta directory named node_modules.

   ```bash
   npm install eslint --save-dev
   ```

3. Initialise the ESLint configuration for the project. Use any 1 of the following 2 commands.

   ```bash
   ./node_modules/.bin/eslint --init
   ```

   ```bash
   #or use this
   npm init @eslint/config
   ```

4. Answer the prompts.

<br>

### Creating the ESLint script

We can use this script to trigger the linting process.

1. In package.json, under "scripts" add the following:

   ```json
   {
     "lint": "eslint ./"
   }
   ```

2. To run the script command, use

   ```bash
   npm run lint
   ```

<br>
<br>

## Refrences

- [The Odin Project](https://www.theodinproject.com/lessons/node-path-javascript-linting) about linting and formatting.
- Follow this [documentation](https://www.digitalocean.com/community/tutorials/linting-and-formatting-with-eslint-in-vs-code).
