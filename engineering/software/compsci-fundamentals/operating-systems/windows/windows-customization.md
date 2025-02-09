# To create a custom shortcut key

- Use the following as shortcut value in the properties tab of an custom made exe. (My exe was in `C:\Windows\System32`)

  ```
  C:\Windows\System32\rundll32.exe powrprof.dll,SetSuspendState 0,1,0
  ```

<br>
<br>
<br>

# Custom powershell script to push git

- Create a txt file with the suitable name
- Add the commands (For example)

  ```ps1
  cd E:\03-library\01-notes ; git add . ; git commit -m "git pushed using script at $((Get-Date).ToString())" ; git push -u origin main ;
  ```

- Save the txt file with `ps1` extension.
- Run powershell as adminstrator and Type the following command.

  ```ps1
  Set-ExecutionPolicy RemoteSigned
  ```

  <br>
  <br>
  <br>

# How to Make Microsoft Edge Always Start in InPrivate Mode

[How to Make Microsoft Edge Always Start in InPrivate Mode (groovypost.com)](https://www.groovypost.com/howto/make-microsoft-edge-always-start-in-inprivate-mode/)

<br>
<br>
<br>

# Set the default startup location in git bash terminal

- Refer this ![website](https://www.shellhacks.com/git-bash-change-default-directory/)
- Basically,
  - Open the properties of the git bash shortcut.
  - Change the "Start in" option. The default will be `%HOMEDRIVE%%HOMEPATH%`
  - Remove the `--cd-to-home` from the Target field.

<br>
<br>
<br>
