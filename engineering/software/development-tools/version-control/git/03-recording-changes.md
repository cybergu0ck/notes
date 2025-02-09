# Git Recording changes

<br>
<br>

## Vewing changes

The status of the repo can be checked by checking the state of the files. use:

```bash
git status
```

<br>

### States of a file

A file can be in different state in VCS.

1. Untracked : An untracked file is a file that is not yet recognized by Git. It means Git is not monitoring changes to this file. Untracked files are typically new files, renamed files etc that haven't been added to the staging area or committed yet.
1. Tracked: A tracked file is a file that is recognized by git.
   1. Staged : A staged file is a modified file that has been marked for inclusion in the next commit. These changes are in the staging area.
   1. Modified : A modified file is a file that was previously committed but has been changed since the last commit.
   1. Deleted : A deleted file is a file that existed in the previous commit but has been deleted from the working directory.
1. Ignored : Ignored files are files that match patterns specified in a .gitignore file.

<br>
<br>

## Staging the changes

- Staging refers to the process of adding the changes in the working directory to the staging area, to include these updates in the next commit.
- The following command is used

  ```bash
  git add <file/directory>
  ```

<br>
<br>

## Commiting the changes

```bash
git commit -m "commit message goes here"
```

<br>

### Ammending previous commits

View [in undoing changes notes](06-undoing-changes.md#ammend-commit).

<br>
<br>

## Stashing the Changes

```bash
git stash
```

- The stash command will take uncommitted changes (both staged and unstaged) and saves them away for later use.
- **_The stash command will not stash untracked files._**
- To include the untracked files in the stash, use :

  ```bash
  git stash -u
  ```

<br>

### Multiple Stashes

Git supports multiple stashes, It stacks the stashes on top of eachother.

- By default it uses the current commit SHA as a stash message.

  ```
  stash@{1}: WIP on main: bac2a64 added file
  stash@{2}: WIP on main: bac2a64 added file
  ```

- `git stash save "<message>"` adds a stash message for our convenience.

  ```
  stash@{0}: On main: Final Fix, brain says
  stash@{1}: WIP on main: bac2a64 added file
  stash@{2}: WIP on main: bac2a64 added file
  ```

<br>

### View the Stash

```bash
git stash list
```

<br>

### Reapplying the Stashed Changes

The `pop` and `apply` git commands are used to apply the stashed changes back to the working directory, The major difference is that after re-applying the changes, `pop` command will remove the changes from the stash while `apply` will keep the changes in the stash.

- To re-apply the latest stashed change, use :

  ```bash
  git stash pop
  ```

- To re-apply a specific stashed change, use :

  ```bash
  git stash pop stash@{<number>}
  ```

<br>

### Dropping Stashed Changes

- To drop a specific stashed change, use :

  ```bash
  git stash drop stash@{<number>}
  ```

- To drop the entire stash, i.e delete all the stashed changes, use :

  ```bash
  git stash clear
  ```

<br>

## Tags

- A tag is a reference/label attached to a specific commit.
- There are 2 types of tags:
  1. Lightweight : A simple reference to a commit
  2. Annoted tag : A full git object that references a commit
- Like other references we can use tags instead of SHA-1 values in git commands.

<br>

### Creating a light weight tag

```bash
git tag <tagname> [commit]
```

Setting a tag called header for the commit where we defined a module level header and then viewing the log

```
$ git tag header HEAD

$ git log --oneline
1edd0b1 (HEAD -> master, tag: header) Added module header
f9a6285 created moviedb.py

```

<br>

### Viewing tags

| Operation                     | Syntax           | Explanation |
| ----------------------------- | ---------------- | ----------- |
| View All tags in repo         | `git tag`        |             |
| View a specific tagged commit | `git show <tag>` |

> Check documentation to create an annotated tag!

<br>
<br>
