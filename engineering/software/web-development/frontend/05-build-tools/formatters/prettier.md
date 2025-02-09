# Prettier

Prettier automatically formats javascript code to a set of rules.

- Prettier is an opinionated code formatter.
- Unlike a linter, it is not looking for style errors, but specifically targeting the layout of the code and making intelligent decisions about things like spaces, indentation levels and line-breaks.

<br>
<br>

## Setting up Prettier for VS Code Editor

1. Install the Prettier VSCode extension.
2. Enable format on save in settings.

<br>
<br>

## Using ESLint with Prettier

Using ESLint and Prettier together causes conflicts.

To turnoff ESLint rules that are unnecessary or conflicting with Prettier:

1. Install eslint-config-prettier

   ```bash
   npm install --save-dev eslint-config-prettier
   ```

2. Add eslint-config-prettier to your ESLint configuration (eslintrc in our case). Make sure to put "prettier" last, so it gets the chance to override other configs.

   ```
   {
   "extends": [
       "some-other-config-you-use",
       "prettier"
   ]
   }
   ```

- Checkout the [official documentation](https://github.com/prettier/eslint-config-prettier#installation) for eslint-config-prettier.

<br>
<br>

## References

- [About](https://prettier.io/docs/en/) prettier.

- Watch this [video](https://www.youtube.com/watch?v=cQqvoUxKIYQ&ab_channel=TuomoKankaanp%C3%A4%C3%A4) to install and use prettier for simple projects.
- [webdev simplified's video](https://www.youtube.com/watch?v=DqfQ4DPnRqI&ab_channel=WebDevSimplified), He shows how to setup prettier for advanced project involving colaboration, ignoring files, setting it with eslint.
