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

<br/>

## 2 Pushing 

`git push` writes commits for a branch from the local repo to the associated remote repo.

```shell
git push [-u] [<repository>] [<branch>]
```

- `<repository>` can be alias or the url of the remote repo.
- -u is set to track the current branch (--set-upstream).

<br/>
<br/>


# Flow

| Operation | Syntax | Explanation | 
|----------|----------|----|
| 1. Make sure you are in the local repo | `git status` | If not initialise a local repo or clone a remote repo|
| 2. Stage all the files | `git add` | |
| 3. Commit | `git commit` || 
| 4. Make sure a remote repo is associated with the local repo | `git remote -v` | If not, add the remote repo|
| 5. Push | `git push` || 


<br/>
<br/>

# Pulling the Remote Repo to Local Repo

```bash
git pull origin main
```

<br/>
<br/>

# Git's DAG (Directed Acyclic Graph)

- Git models the relationship of commits with a DAG.
- A DAG is a directed graph (graph with edges having directions) with no cycles.
- The edge points at a commit's parent.

- A ***branch*** occurs if a commit has more than one child.
    ![dag-branch](./_assets/dag-branch.jpg)
- A ***merge*** occurs when a commit has more than one parent.
    ![dag-branch](./_assets/dag-merge.jpg)


- Use the `git log --graph` shows the DAG

<br/>
<br/>


# Git ID's

- Internally git uses objects to store 4 types of things:
    1. **Commit object** : A small text file contating commit user info, commit message, a reference to commit's parent('s) and a reference to the root tree of the project.

    2. **Annotated tag** : A reference to a specific commit

    3. **Tree**: Directories and filenames in the project

    4. **Blob**: The content of a file in the project.



- git objects are named with a 40 character hex string
- These strings are called as ***git id*** or ***object id*** or ***SHA-1*** or ***hash*** or ***checksum***.
    - SHA-1 means Secure Hash Algorithm-1   
    - Every change in file results in a different SHA-1 value.
    - Statistically no two unique files have same SHA-1 value.
    - SHA-1 is designed to Avalanche, meaning a small change in file content results in drastic change in SHA-1


<br/>
<br/>

# References

- A reference is a userfriendly name that points to:
    1. A commit SHA-1 hash
    2. another reference ( refernce becomes a symbolic reference) 

    <br/>

    - Illustration :
    - Assume we have a local repo and we have 3 commits as shown by `git log --oneline`

        ```bash
        4e68221 (HEAD -> master) deleted file.txt
        cad2070 modified file.txt
        cf0715f added file.txt
        ```
    - Here the first string is the partial SHA-1 hash and the remaining strings are the comment messages.
    - Here the `HEAD` is a reference pointing to another reference `master`, hence `HEAD` is a symbolicreference.

<br/>

- We can use the reference instead of the SHA-1 hash in git commands
- ~ or ~1 is used to refer the parent of current commit. ~~ or ~2 refers to the parent's parent of the current commit

    - Illustration
    - using `git show --no-patch --oneline HEAD` displays where the HEAD is currently pointing. As shown below:
    - the flags --no-patch and --oneline displays the info cleaner. we can use `git show HEAD` also

        ```bash
        4e68221 (HEAD -> master) deleted file.txt
        ```

    - using ~1 in `git show --no-patch --oneline HEAD~1` shows the parent commit of the current HEAD.

        ```bash
        cad2070 modified file.txt
        ```

    - similarly we can go on ~2, ~3...

- In case of merges, ^ or ^1 is used to refer the first parent of the current commit and ^^ or ^2 refers the second parent and so on.

<br/>
<br/>

# Tag

- A tag is a reference/label attached to a specific commit.
- There are 2 types of tags:
    1. Lightweight : A simple reference to a commit
    2. Annoted tag : A full git object that references a commit
- Like other references we can use tags instead of SHA-1 values in git commands.

<br/>

## Creating a light weight tag

```bash
git tag <tagname> [<commit>]
```
If we don't specify the commit then the commit that HEAD points to will be tagged.

<br/>

## View tags 

| Operation | Syntax | Explanation | 
|----------|----------|----|
| View All tags in repo | `git tag` | |
| View a specific tagged commit | `git show <tag>` |

<br/>

### Illustration

- Consider the repo with 3 commits as shown
    ```bash
    4e68221 (HEAD -> master) deleted file.txt
    cad2070 modified file.txt
    cf0715f added file.txt
    ```

- Tagging the commit with SHA-1 cad2070 as v1.0, note we donot need to specify full SHA-1:
    ```bash
    git tag v1.0 cad2
    ```

- Now see the log:

    ```bash
    4e68221 (HEAD -> master) deleted file.txt
    cad2070 (tag: v1.0) modified for the first time
    cf0715f added file.txt
    ```
- We can show a particular commit using the tag using `git show --no-patch --oneline v1.0`

    ```bash
    cad2070 (tag: v1.0) modified for the first time
    ```


<br/>

> Check documentation to create an annotated tag!

<br/>
<br/>

# Branches

- A branch is a set of commits that trace back to the project's first commit.
- all commits belong to a branch
- by default there is a single branch called ***master*** 
- Creating a branch is fast and easy as it creates one single file for the reference!

- Uses of branches :
    - Enable experimentation
    - enable team development
    - support multiple versions

- Branches can be short lived or ***Topic***, It's a branch for a feature, a bug fix, a hotfix, config change etc.
- Branches can be ***long-lived***, example : master, dev, release, prod branches

<br/>

![branch](./_assets/branch-1.jpg)

In the above case, dev branch contains commits A, B, E and F while featureX branch contains commits  C, D, E and F. Note that commits can belong to multiple branches!


<br/>

## Viewing branches

Use `git branch` to see a list of branches. The current branch will be color highlighted.

<br/>

## Creating branches

```
git branch <name>
```

The above command is used to create branch, creating a branch will simply creates a new branch label reference and we still remain on the original branch! (i.e the HEAD doesn't change)

<br/>

- ![](./_assets/SmartSelect_20230412_152355_Coursera.jpg)
    

- Creating a branch called ***newfilesystem*** in our repo:

    ```bash
    git branch newfilesystem
    ```
- We can notice that our head hasn't changed using `git log --oneline --graph`

    ```bash
    * 4e68221 (HEAD -> master, newfilesystem) deleted file.txt
    * cad2070 (tag: v1.0) modified file.txt
    * cf0715f added file.txt
    ```

<br/>

## Checkout

Checkout does 2 things:
1. Updates the HEAD reference from current commit to the checkedout branch label
2. Updates the working tree with the commit's files

```bash
git checkout <branch or commit> 
```

- Switching to newfilesystem branch using `git checkout newfilesystem`
- Checking the current branch using `git branch` (The green color branch is the current branch)

<br/>

![](./_assets/next-commit.jpg)







<br/>

## Creating and Checking out together

```bash
git checkout -b <name>
```

<br/>

## Deleting a branch

deleting a branch is basically deleting the branch label!

```bash
git branch -d <name>
```
<br/>

## Dangling Commits

dangling commits are those commits present in a branch that was deleted before merging.

> Add Image 

<br/>

## Undoing an accidental branch delete

- `git reflog` displays a local list of recent HEAD commits.
- Find the SHA-1 of the dangling commit from that list
- create the branch and checkout i.e. `git checkout -b <name>`


<br/>


<br/>
<br/>

# Merging

- Base branch is the primary branch. example: master
- Topic branch is the secondary branch. example: feature branch

- There are 4 types of merges:
    1. fast forward merge
    2. merge commit
    3. squash commit
    4. rebase

<br/>

## 1 Fast forward merge 

- Moves the base branch label to the tip of the topic branch.
- This type of merge is possible only if no other commits have been made to the base branch since branching. i.e. git will not allow this merge if the condition is not satisfied.

- git automatically assumes fast-forward merge if it is possible.


> Add Image


### Performing the fast forward merge

```bash
git checkout <basebranch>
git merge <topicbranch>
git branch -d <topicbranch>
```
<br/>


## 2 Merge Commit

- merge commit combines the commits at the tips of the merged branches and places the result in the merge commit.
- git automatically assumes merge commit if fast-forward merge is not possible.

>Add Image

<br/>

### Performing the fast forward merge

It is exactly same as performing fast-forward merge as git takes care of it!

```bash
git checkout <basebranch>
git merge <topicbranch>
git branch -d <topicbranch>
```
<br/>


### Forcing merge commits

In a scenario where fast-forward merge is possible but we want merge commit, we can force it:

```bash
git checkout <basebranch>
git merge --no-ff <topicbranch>
git branch -d <topicbranch>
```



<br/>
<br/>
