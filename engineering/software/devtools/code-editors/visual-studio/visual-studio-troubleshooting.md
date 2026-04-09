# Contents

- [Visual Studio Troubleshooting](#visual-studio-troubleshooting)
  - [How to toggle between solution view and Folder view in VS](#how-to-toggle-between-solution-view-and-folder-view-in-vs)
  - [Disable specific warning](#disable-specific-warning)
    - [Using the VS IDE and solution explorer](#using-the-vs-ide-and-solution-explorer)

<br>
<br>
<br>




# Visual Studio Troubleshooting

<br>
<br>

## How to toggle between solution view and Folder view in VS

- Look at the top answer in [stack overflow](https://stackoverflow.com/questions/54997800/solution-explorer-opens-in-folders-view)

<br>
<br>

## Disable specific warning

Can be done in multiple ways.

<br>

### Using the VS IDE and solution explorer

- Open the properties page by Project > Properties >
- Make sure to select the correct Configuration (Debug, Release) and correct Platform (Win32, x64...)
- Then find Configuration Properties > C/C++ > Advanced > Disable Specific warning
- Make sure to enable _Inherit from parent or project details option_
- Enter only the warning number!

<br>
<br>
