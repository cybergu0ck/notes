# Steps to create a powershell script to sync a local repo

- create a txt file with the suitable name
- Add the commands (For example)

```ps1
cd E:\03-library\01-notes ; git add . ; git commit -m "git pushed using script at $((Get-Date).ToString())" ; git push -u origin main ;
```

- Save the txt file with `ps1` extension.
- Run powershell as adminstrator.
- Type the following command.

```ps1
Set-ExecutionPolicy RemoteSigned
```
