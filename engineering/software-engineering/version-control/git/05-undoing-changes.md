# Undoing changes in git

## Unstaging files

- Files that are staged but not yet committed can be unstaged using:

  ```
  git reset <file>
  ```

<br>
<br>

## Ammend Commit

The following command allows us to make changes to the commit message. add or remove changes only from the most recent commit (HEAD~1).

- Follow these steps to change only the commit messge:

  1. The following command will open the text editor set in git config.

  ```
  git commit --amend
  ```

  2. The editor will show the commit message of the previous commit. Make changes, save and close the editor.

<br>

- Follow these steps to make changes in the previous commit:

1. Make changes in the working directory (changes with intention to replace the previous commit's update).
1. Stage those files
1. Use the command, opens the editor, give new commit message and save.

   ```
   git commit --amend
   ```

<br>
<br>

## Soft Reset

It is a process where git moves the branch pointer (ex: HEAD) to a different commit while keeping the changes intact (working directory and staging area).

![soft](./_assets/softreset.gif)

```
git reset --soft <hash>
```

- The branch pointer is moved to the mentioned hash.
- Any changes made after the soft reset that need to be recorded must be done via a new commit. This new commit will advance the HEAD with a new hash.

<br>
<br>

## Hard Reset

It is a process where git moves the branch pointer (ex: HEAD) to a different commit while discarding all the changes in working directory and staging area.

![hard](./_assets/hardreset.gif)

```
git reset --hard <hash>
```

- The branch pointer is moved to the mentioned hash.
- Similar to soft reset, Any changes made after the hard reset that need to be recorded must be done via a new commit. This new commit will advance the HEAD with a new hash.

<br>
<br>

## Revert

Reverting is a process of undoing changes done in a previous commit without modifying the history of the branch. Unlike resetting, revert adds a new commit containing the updated changes without moving the branch pointer.

![revert](./_assets/revert.gif)

```
git revert <hash>
```

- In the above gif illustrates a case where the index.js file that was introduced in the commit hash ec5be wasn't needed, Hence `git revert ec5be` is used, index.js is deleted and this change is staged and commited.
- This is particularly useful when working in a collaborative environment where you want to keep a record of why and when certain changes were reverted.
