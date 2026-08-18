# Installing WSL on Windows 11

To install default version of WSL (which comes with ubuntu)

```powershell
wsl --install
```

Refer [official documentation](https://learn.microsoft.com/en-us/windows/wsl/install)

<br>
<br>

# To open linux directories in windows file explorer

1. open file explorer
2. search `\\wsl$`

<br>
<br>

## WSL fails to launch code

- Throws an error saying Invalid argument
- Open Powershell and run the command:
  ```psl
  wsl --shutdown
  wsl
  ```
