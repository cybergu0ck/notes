# Git Branching

Branching allows multiple lines of development to coexist independently, making it easier to work on new features, fix bugs, and collaborate on projects without disrupting the main codebase.

- Each branch is a lightweight pointer to a specific commit (a snapshot of the codebase at a certain point in time).

<br>
<br>

## Creating branch

```bash
git branch <branch-name>
```

<br>
<br>

## Viewing branches

- To view the list of all branches.
  ```bash
  git branch
  ```
- In the context of remote repo, the above command only shows only the local branches. To show all the branches (including the branches in the remote repo), use:

  ```bash
  git branch --all
  ```

* The default branch (master or main) will be shown only after the first commit is made.

<br>
<br>

## Switch branch

- To switch to branch, use the following command with the name of the branch to be switched to.

  ```bash
  git switch <branch-name-to-switch-to>
  ```

- Create and switch to that new branch using one command.

  ```bash
  git switch -c <branch-name>
  ```

<br>
<br>

## Renaming branches

```bash
git branch -m <old-branch-name> <new-branch-name>
```

<br>
<br>

## Deleting branches

- Local branches can be deleted using:

  ```bash
  git branch -d <branch-name>
  ```

- Remote branches can be deleted using:

  ```bash
  git push <remote-name> --delete <branch-name> #git push origin --delete bugfix1.2
  ```

<br>
<br>

## Undoing a branch delete

View [in undoing changes notes](06-undoing-changes.md#undoing-a-branch-delete)

<br>
<br>

## Working with remote branches

View [in remote repositories notes](04-remote-repositories.md#working-with-remote-branches)

<br>
<br>

## Cherrypicking

**_Cherrypicking refers to selecting and applying specific commits from one branch to another._**

![cherry](./_assets/cherrypick.gif)

<br>
<br>

## Comparing branches

- To compare the commits between two branches.

  - The following command shows all the commits exclusive to branch2 when compared with branch1. i,e, commits in branch2 that are not in branch1.
    ```bash
    git log branch1..branch2
    ```
  - The following command shows all the commits exclusive to branch1 when compared with branch2. i,e, commits in branch1 that are not in branch2.
    ```bash
    git log branch2..branch1
    ```

- To check the differences between two git branches.

  - The following command shows the difference the differance in branch2 when compared with branch1.
    ```bash
    git diff branch1..branch2
    ```
  - The following command shows the difference the differance in branch1 when compared with branch2.
    ```bash
    git diff branch2..branch1
    ```

<br>

### Illustration

- Assume branch1 has one commit (b60d22, "added text in file.txt in branch1") and the contents of file.txt is as follows:

  ```txt
  This is change made in branch1
  ```

- Assume branch2 has one commit (e149c1, "added text in file.txt in branch2") and the contents of file.txt is as follows:

  ```txt
  This is change made in branch2
  ```

- The result of the versions of the above command is as shown:

  ```bash
  git log branch1..branch2
  ```

  ```
  e149c1, "added text in file.txt in branch2"
  ```

  <br>
  <br>

  ```bash
  git log branch2..branch1
  ```

  ```
  b60d22, "added text in file.txt in branch1"
  ```

  <br>
  <br>

  ```bash
  git diff branch1..branch2
  ```

  ```
  <metadata>
  - This is change made in branch1
  + This is change made in branch2
  ```

  <br>
  <br>

  ```bash
  git diff branch2..branch1
  ```

  ```
  <metadata>
  - This is change made in branch2
  + This is change made in branch1
  ```
