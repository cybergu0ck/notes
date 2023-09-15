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
git config --gloabl alias.lg "log --oneline --graph --all"  #global alias
got config --local alias.lg "log --oneline --graph --all"  #local alias
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
