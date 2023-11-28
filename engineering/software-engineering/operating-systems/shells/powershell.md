# Powershell

<br>
<br>

## Powershell Scripting

<br>

### Adding multi line commands in a script

- Follow [powershell - How to enter a multi-line command - Stack Overflow](https://stackoverflow.com/questions/3235850/how-to-enter-a-multi-line-command), However I haven't been able to get this done using backtick.

<br>

### Adding multiple commands in a single line in a script

- I followed [syntax - Can I get "&&" or "-and" to work in PowerShell? - Stack Overflow](https://stackoverflow.com/questions/563600/can-i-get-or-and-to-work-in-powershell), Using semicolon ; after every command seems to get the job done for me.

  ```powershell
  cd E:\3Library\Notes ; git add . ; git commit -m " Automated git push" ; git push -u origin main
  ```

<br>

### Getting Date and time

```powershell
"Date and time is: $((Get-Date).ToString())"
```
