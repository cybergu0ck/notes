# Undoing changes in git

<br>
<br>

## Discarding changes in working directory

The changes in this context are unstaged. Follow these steps:

1. Discard the changes in working directory for all tracked files. It will revert the working directory to match the previous commit.

   ```bash
   git checkout .
   ```

1. The above command will not delete the changes, it will make them untracked. To delete them use :

   ```bash
   git clean -f
   ```

   <br>

> Ideally use VS code and discard all the changes in GUI.

<br>
<br>

## Unstaging files

- Unstaging individual staged (but not yet commited) files:

  ```bash
  git reset <file>
  ```

- Unstaging all staged (but not yet commited) files:

  ```bash
  git reset
  ```

<br>
<br>

## Ammend Commit

The following command allows us to make changes to the commit message. add or remove changes only from the most recent commit (HEAD~1).

- Follow these steps to change only the commit messge:

  1. The following command will open the text editor set in git config.

  ```bash
  git commit --amend
  ```

  2. The editor will show the commit message of the previous commit. Make changes, save and close the editor.

<br>

- Follow these steps to make changes in the previous commit:

1. Make changes in the working directory (changes with intention to replace the previous commit's update).
1. Stage those files
1. Use the command, opens the editor, give new commit message and save.

   ```bash
   git commit --amend
   ```

<br>
<br>

## Reset

**_Reset commands faciliate undoing of changes by rewriting (modifying) history especially when working alone_**

- Reset commands should not be used when working with remote repos. In such cases, Revert command is suggested.

<br>

### Soft Reset

It is a process where git moves the branch pointer (ex: HEAD) to a different commit while keeping the changes intact (working directory and staging area).

![soft](./_assets/softreset.gif)

```bash
git reset --soft <hash>
```

- The branch pointer is moved to the mentioned hash.
- Any changes made after the soft reset that need to be recorded must be done via a new commit. This new commit will advance the HEAD with a new hash.

<br>

### Hard Reset

It is a process where git moves the branch pointer (ex: HEAD) to a different commit while discarding all the changes in working directory and staging area.

![hard](./_assets/hardreset.gif)

```bash
git reset --hard <hash>
```

- The branch pointer is moved to the mentioned hash.
- Similar to soft reset, Any changes made after the hard reset that need to be recorded must be done via a new commit. This new commit will advance the HEAD with a new hash.

<br>
<br>

## Revert

**_Revert command facilitates undoing of changes without rewriting (modifying) the history._**

- Unlike resetting, revert adds a new commit containing the updated changes (that undo's the changes).

  ![revert](./_assets/revert.gif)

  ```bash
  git revert <hash>
  ```

- In the above gif illustrates a case where the index.js file that was introduced in the commit hash ec5be wasn't needed, Hence `git revert ec5be` is used, index.js is deleted and this change is staged and commited.
- This is particularly useful when working in a collaborative environment where you want to keep a record of why and when certain changes were reverted.

<br>
<br>

## Undoing a branch delete

Follow these steps:

1. Get the hash of the deleted branch's last commit. It will be shown when we delete a branch using `git branch -D <branch-name>`, else use:

   ```bash
   git reflog
   ```

1. Checkout to that hash, the HEAD will now be in detached state.

   ```bash
   git checkout <hash>
   ```

1. Create a new branch (with the old name) at that hash

   ```bash
   git checkout -b <branch-name>
   ```

<br>
<br>

## Undoing a merge

Follow these steps:

1. Find the commit hash before the merge, use `git log` or `git reflog`.

1. Use the reset command.

   ```bash
   git reset --merge <hash>
   ```

<br>

### Undoing a merge pushed in remote

If the merge is pushed into the remote repo and there are commits done in the remote repo after that merge, we cannot force push (`git push -f`) the undone merge from local as it will delete all the remote commits. Ideal way to resolve this is to follow these steps:

1. Pull the latest changes of that branch.

   ```bash
   git pull <remote-name><branch-name>
   ```

1. Create a new branch to undo the merge

   ```bash
   git switch -c <new-branch-name>
   ```

1. Use either show or difftool (compare the hash before merge and after merge) and get the changes that were introduced in the merge.

1. Use the revert command and revert to a hash before the commit.

   ```bash
   git revert <hash-before-merge>
   ```

1. If there is any merge conflict, resolve it by remove the changes introduced by the merge.
1. Complete the revert by committing, use appropritate commit message always.

   ```bash
   git commit -m "reverted the change introduced by merge"
   ```

1. Push this branch to remote

   ```bash
   git push <remote-name><new-branch-name>
   ```

1. Create a pull request or merge request in the remote repo to merge _new-branch-name_ to _branch-name_.

<br>
<br>
