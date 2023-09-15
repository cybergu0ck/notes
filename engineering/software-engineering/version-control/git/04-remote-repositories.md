# Remote Repo

<br>
<br>

## Connecting to remote repo

- Connecting a local git repo to a remote repo provides lot of benefits.
- A git repo that is cloned is connected by default.
- A git repo that is initialised locally can be connected to a remote one.

- We can do this by using

  ```
  git remote add <name> <remote-repo-url>
  ```

  - `name` is the alias given to the remote repo, so that we can refer to the remote repo using the alias instead of the url! origin is the general alias name.
  - `remote-repo-url` must be found from the PaaS (GitHub).

<br>
<br>

## Viewing the associated remote repo

Once a remote repo is connected to the local repo, it's details can be checked using

```
git remote --verbose
```

<br>
<br>

## Fetching updates from the remote repo

git fetch updates the local references to the remote branches without making changes to the working directory and moving the HEAD.

![fetch](./_assets/fetch.gif)

<br>
<br>

## Pulling the updates from the remote repo

git pull fetches and merges the updates from the remote repo.

![pull](./_assets/pull.gif)

<br>
<br>

## Working with remote branches

- To list the remote branches, use:

  ```
  git branch -r
  ```

- To create a local branch that tracks remote branch, use:

  ```bash
  git checkout -b <local-branch-name> <remote_name>/<remote-branch-name> # git checkout -b bugfix1.2 origin/bugfix1.2
  ```

  - Note that the name of the local branch and the remote branch in the above case must be same, else a new branch will be created in remote repo when the changes are pushed.

- To push update to the remote branch

  ```bash
  git push <remote-name> <local-branch-name> #git push origin bugfix1.2
  ```

- To pull updates for the remote branch.

  ```bash
  git pull <remote-name> <local-branch-name> #git pull origin bugfix1.2
  ```

- To delete a remote branch on the remote repo, use:

  ```bash
  git push <remote-name> --delete <branch-name> #git push origin --delete bugfix1.2
  ```

<br>

### pull options

| Option         | Description                                      |
| -------------- | ------------------------------------------------ |
| --ff (default) | fast forward if possible otherwise merge commit. |
| --no--ff       | always merge commit                              |
| --ff--only     | cancel instead of doing merge commit             |
| --rebase       | \<see rebase docs\>                              |

<br>
<br>
