[← Back to git](./contents.md)

# Contents

- [Customizations](#customizations)
  - [git config](#git-config)
  - [Alias](#alias)
    - [Creating alias](#creating-alias)
    - [Using alias](#using-alias)
    - [Deleting alias](#deleting-alias)

<br>
<br>
<br>



# Customizations

<br>
<br>

## git config

- Find the .gitconfig file in C:\Users\<user>\
- Open it in an editor and make it similar to the following file (text editor, difftool, mergetool etc).

```
[user]
	name = <name>
	email = <email>
[init]
    defaultBranch = main
[filter "lfs"]
	process = git-lfs filter-process
	required = true
	clean = git-lfs clean -- %f
	smudge = git-lfs smudge -- %f
[alias]
	lg = log --oneline --graph --all
[core]
      editor = code --wait
[merge]
        tool = vscode
[mergetool "vscode"]
         cmd = code --new-window --wait --merge $REMOTE $LOCAL $BASE $MERGED
[diff]
        tool = vscode
[difftool "vscode"]
        cmd = code --new-window --wait --diff $LOCAL $REMOTE
```

<br>
<br>

## Alias

alias can be created to simplify the commands. It allows to define custom shorthand commands.

<br>

### Creating alias

For example, creating an alias for git `log --oneline --all --graph` command.

```bash
git config --global alias.lg "log --oneline --graph --all"  #global alias
git config --local alias.lg "log --oneline --graph --all"  #local alias
git config --global alias.pp '!git pull && git push' #Note that ! is needed here. The ! at the start tells Git to execute the alias as a shell command rather than a built-in Git subcommand.
```

<br>

### Using alias

```bash
git lg
```

<br>

### Deleting alias

```bash
git config --global --unset alias.lg    #global
git config --unset alias.lg #local
```
