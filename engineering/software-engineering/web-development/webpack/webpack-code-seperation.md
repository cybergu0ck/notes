# Code Seperation using Webpack

- Refer to this [video](https://www.youtube.com/watch?v=IZGNcSuwBZs&t=446s&ab_channel=TraversyMedia)

- In a terminal, run

  ```
  npm init -y
  ```

- Install webpack as dev dependancy, this will update the package.json file

  ```
  npm i -D webpack webpack-cli
  ```

- Edit the package.json's script part, to add the build command.

  ```
  "scripts": {
      "build": "webpack --mode production"
  }
  ```

- Now, we can build the code using `npm run build`.
