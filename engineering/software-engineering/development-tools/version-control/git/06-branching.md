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

  - Commits in branch2 that are not in branch1.
    ```bash
    git log branch1..branch2
    ```
  - Commits in branch1 that are not in branch2.
    ```bash
    git log branch2..branch1
    ```

- To check the differences between two git branches.

  - Changes in branch2 that are not in branch1.
    ```bash
    git diff branch1..branch2
    ```
  - Changes in branch1 that are not in branch2.
    ```bash
    git diff branch2..branch1
    ```
