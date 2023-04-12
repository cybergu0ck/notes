# Git syntax

| Syntax | Example | 
|---------|----|
| `git <command> <--flags> <arguments>` | `git status --short` |
| | `git add file.txt` (Here file.txt is an argument) |

flags are also known as options or switches

<br/>
<br/>

# Getting help

```
git help <command>
```
<br/>
<br/>

# Configuration

```
git config [--local | --global | --system] <key> [<value>]
```

- `--local` flag or no flag applies only to the current repository
- `--global` flag applies to every repo that one uses on his computer
- `--system` flag applies to every repo for all users on the comouter


<br/>

| Operation | Syntax | Explanation | 
|----------|----------|----|
| 1. Set up username  | `git config --global user.name <username>`  |    |
| 2. Set up email  | `git config --global user.email <email>`  |    |
| 3. Read/ Check credentials | `git config user.name (or user.email)` | 

  
<br/>
<br/>


# Git locations 


## Remote Repository

- A repo generally hosted on the cloud or a datacenter.
- Hosted options : Bitbucket, GitHub
- On-premise options : Bitbucket server, Github enterprise
- Remote repo's generally donot have working tree and staging area
- Remote repo's end with .git 

<br/>



<br/>
<br/>


# Git Commits


| Operation | Syntax | Explanation | 
|----------|----------|----|
| 1. View file status | `git status` | view the status of the files in the working tree and staging area. |
| 2. Stage contents| `git add <file-or-dir>` | Add the untracked or modified files to the staging Area| 
| 3. Commit content   |  `git commit -m <message>`  |  Adds staged content to the local repository as a commit, (commit is a snapshot of the project)  |
| 4. View the commit history | `git log` | View the commit history | 


<br/>
<br/>



# Pushing to Remote Repo

To push to a remote repo, we have to make sure that there is a remote repo associated with a local repo.

- If there is no remote repo associated with a local repo,
    - We can clone a remote repo to create a new local repo.
    - We can add a remote repo to get associated with an existing local repo.

<br/>

## 1A Cloning a remote repo

`git clone` is used to create a local copy of a remote repo. i.e. if we donot have a local repo then cloning a remote repo will create a local repo that is associated with the remote repo.

<br/>

| Operation | Syntax | Explanation | 
|----------|----------|----|
|1. Clone a remote repo | `git clone <url> [localprojectname]` |  creates a local repo from a remote repo <br/> if localprojectname is specified, local repo will be named that | 
|2. Get Info on remote repo | `git remote --verbose`| Displays info (url) about remote repo associated with local repo |

<br/>

## 1B Adding a remote repo

`git remote add` adds the remote repo to the current existing local repo.

| Operation | Syntax | Explanation | 
|----------|----------|----|
|1. Add a remote repo | `git remote add <name> <url>` |  Adds the remote repo to the local repo so that they can be made in sync <br/> `<name>` is the alias given to the remote repo, so that we can refer to the remote repo using the alias instead of the url! <br/> `origin` is the general alias name | 
|2. Get Info on remote repo | `git remote --verbose`| Displays info (url) about remote repo associated with local repo |

## 2 Pushing 

`git push` writes commits for a branch from the local repo to the associated remote repo.

```shell
git push [-u] [<repository>] [<branch>]
```

<br/>
<br/>

# Branches

- all commits belong to a branch
- by default there is a single branch called ***master***


1. Creating a Local Repo

    ```bash
    git init -b main
    ```

 
2. Staging all modfications and commiting

    ```bash
    git add . && git commit -m "first commit"
    ```


3. Create a Remote Repo on github and get the remote URL

    ```bash
    git remote add origin <REMOTE_URL>    # Sets the new remote

    git remote -v # Verifies the new remote URL
    ```


4. Push it to the remote repo

    ```bash
    git branch -M main

    git push -u origin main
    ```

<br/>
<br/>

# Pulling the Remote Repo to Local Repo

```bash
git pull origin main
```

<br/>
<br/>

