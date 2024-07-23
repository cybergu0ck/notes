# Git Versions

<br>
<br>

## Viewing Git History

The term "Git history" refers to the chronological record of changes and commits made to a Git repository.

<br>

### `git log`

It is used to view the commit history of a git repo.

- Use the following command.

  ```bash
  git log
  ```

* By default git log shows the logs for the current branch. Viweing the logs for a specific branch can be done using,

  ```bash
  git log <branch-name>
  ```

* Viewing the history of a specific file

  ```bash
  git log <file-path>
  ```

* Some common flags used along with this command are

  ```bash
  git log --oneline --graph --all
  ```

* To view the commits made by a specific author,

  ```bash
  git log --author="<username>"
  ```

* To filter the commit log based on the commit messages,

  ```bash
  git log --grep=<text>
  ```

<br>

### `git show`

It is used to view the detailed information about a specific git object (commit, tag, tree, blob etc)

- To view details of a commit

  ```bash
  git show <commit-hash>
  ```

- To list all the files that were touched in a commit

  ```bash
  git show --pretty="" --name-only <commit-hash>
  ```

- To output all commits in the range.

  ```bash
  git show <commit-hash-1>...<commit-hash-2>
  ```

- To view the details of a tag

  ```bash
  git show tag
  ```

<br>

### `git reflog`

It is used to list the chronological record of all the updates(merges, resets, reverts, commits etc) to Git references (branches and tags) in a repository.

![reflog](./_assets/reflog.gif)

- Reflog stands for "Reference Logs".
- This information is particularly useful for recovering lost commits, branches, or other changes that may have been accidentally deleted or overwritten.

- To see reflog of current branch, use:

  ```bash
  git reflog
  ```

- To see reflog for a particular branch, use:

  ```bash
  git reflog <branch-name>
  ```

<br>
<br>

## Inspecting changes

- Using an external difftool is ideal. VS code as difftool is nice. Check customizations file to set it up.
- The following commands will work without difftool by using the command `diff` instead of `difftool`.

- To see the changes between the working directory and the last commit, use the following command. This will open VS code as a new tab accoriding to config file.

  ```bash
  git difftool -y
  ```

- To see the changes between the staging area and the last commit, use:

  ```bash
  git difftool --staged -y
  ```

- To see the changes in `commit-hash-2` compared to `commit-hash-1`.

  ```bash
  git difftool <commit-hash-1> <commit-hash-2>
  ```

- To see the changes of a particular file among the modified files.

  ```
  git difftool <file(path)>
  ```

<br>
<br>
