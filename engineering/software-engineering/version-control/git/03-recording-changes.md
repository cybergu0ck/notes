# Git Recording changes

# The status

The status of the repo can be checked by checking the state of the files. A file can be in different state in VCS.

1. Untracked : An untracked file is a file that is not yet recognized by Git. It means Git is not monitoring changes to this file. Untracked files are typically new files that haven't been added to the staging area or committed yet.
1. Tracked: A tracked file is a file that is recognized by git.
   1. Staged : A staged file is a modified file that has been marked for inclusion in the next commit. These changes are in the staging area.
   1. Modified : A modified file is a file that was previously committed but has been changed since the last commit.
   1. Deleted : A deleted file is a file that existed in the previous commit but has been deleted from the working directory.
1. Ignored : Ignored files are files that match patterns specified in a .gitignore file.

<br>
<br>

## Checking the status

```
git status
```

<br>
<br>
<br>

# Staging the changes

- Staging refers to the process of adding the changes in the working directory to the staging area, to include these updates in the next commit.
- The following command is used

  ```
  git add <file/directory>
  ```

<br>
<br>
<br>

# Commiting the changes

```
git commit -m "commit message goes here"
```

<br>
<br>

## Ammending previous commits

- Use the following command, make changes in the commit message and close the file. See undoing changes file to ammend commit itself.
  ```bash
  git commit --amend
  ```

<br>
<br>
<br>

# Tag

- A tag is a reference/label attached to a specific commit.
- There are 2 types of tags:
  1. Lightweight : A simple reference to a commit
  2. Annoted tag : A full git object that references a commit
- Like other references we can use tags instead of SHA-1 values in git commands.

<br>
<br>

## Creating a light weight tag

```
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
<br>

## Viewing tags

| Operation                     | Syntax           | Explanation |
| ----------------------------- | ---------------- | ----------- |
| View All tags in repo         | `git tag`        |             |
| View a specific tagged commit | `git show <tag>` |

> Check documentation to create an annotated tag!

<br>
<br>
<br>
