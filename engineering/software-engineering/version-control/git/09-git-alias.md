# Creating alias

- alias can be created to simplify the commands. It allows to define custom shorthand commands.
- For example, creating an alias for git `log --oneline --all --graph` command.

  ```bash
  git config --gloabl alias.lg "log --oneline --graph --all"  #global
  got config --local alias.lg "log --oneline --graph --all"  #local
  ```

- Using the alias

  ```bash
  git lg
  ```

<br>
<br>
<br>

# Deleting alias

```bash
git config --global --unset alias.lg    #global
git config --unset alias.lg #local
```
