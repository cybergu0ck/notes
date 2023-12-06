# ESLint

Linters are tools that scan code for bugs and errors, check for subjective, stylisitic preferences and report any errors that they find.

- ESLint is one among the linter tools.
- It is ideal and preferred to setup ESLint local to the projects (instead of global setup), check references.

<br>
<br>

## ESLint setup for VSCode (Not Globally)

1. Make sure the javscript project is initialised. If not, use:

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

4. Answer the prompts according to the project.

5. Make sure ESLint extension is installed in VSCode so that error highlighting starts to kick in the code editor.

<br>
<br>

## Triggering Formatting

<br>

### Formatting manually using script

1. In `package.json`, under "scripts" add the following:

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

### Formatting on save

1. Using command palette, open **Preferences: Open Workspace Settings (JSON)**
2. Write the following to `settings.json` file that will be opened.

   ```json
   {
     "editor.codeActionsOnSave": {
       "source.fixAll.eslint": true
     },
     "eslint.validate": ["javascript"]
   }
   ```

<br>
<br>

## Customizing ESLint rules

Rules can be found in `eslintrc` file. If it's in JSON format, then add the rules as shown here:

```json
{
  "rules": { "no-console": "off" }
}
```

<br>

### Disabling props validation during linting for react

- Add the following to .eslintrc file in the root directory of project.

  ```bashrc
  {
  "plugins": [
     "react"
  ],
  "rules": {
     "react/prop-types": 0
  }
  }
  ```

- To enforce this setting globally in VS code, add the following in the settings.json file of VS Code.

  ```json
  "eslint.options": {
     "rules": {
        "react/prop-types": "off"
     }
  }
  ```

<br>
<br>

## References

- [The Odin Project](https://www.theodinproject.com/lessons/node-path-javascript-linting) about linting and formatting.
- Follow this [documentation](https://www.digitalocean.com/community/tutorials/linting-and-formatting-with-eslint-in-vs-code) for setting up ESLint.
- [Downsides](https://stackoverflow.com/questions/66694306/any-downsides-to-installing-eslint-globally) of setting ESLint globally.
