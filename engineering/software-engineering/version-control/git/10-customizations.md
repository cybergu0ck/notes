# Customizations

- Find the .gitconfig file in C:\Users\<user>\
- Open it in an editor and make it similar to the following file.

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
