# Git Repositories

**_A Git repository is a directory or folder that contains a collection of files and their revision history, managed using Git._**

<br>
<br>

## Types of repos

<br>

### Local Repo

**_Local Repo is the Git Repo on the local machine._**

- There are 3 areas in a git version controlled project directory.

  1. Working Tree (Working Directory)

     - The working tree is the directory on the local machine where the project files are located.
     - When we checkout to a differnt commit (access a different commit), the working tree will be updated i.e. the project files will modify according to that commit.

  2. Staging Area

     - The staging area holds a list of files that will be included in the next commit.
     - It is present in the .git directory

  3. Local Repository

     - local repository conatins all the commits of the project and is present in the .git directory.
     - This is different from the Local Repo that refers to the Git Repo on the local machine.
     - It is common to call both of these as Local Repo. However, it doesn't change how git works under the hood!

<br/>

### Remote Repository

**_Remote Repo is the Git Repo on the server._**

- It is a copy of the local repo that is stored on a remote server, facilitated by code hosting services like GitHub, GitLab, or Bitbucket.
- A remote repository generally doesn't have staging area and working tree as .git directory is not present.

<br/>
<br/>

## Creating Repositories

Git repo's can be created in many ways.

<br>

### Initialising a Git Repo

**_Initializing a Git repo is the process of setting up a new directory to be tracked by Git._**

- A git repo can be initialised on the locally (local machine) aswell as remotely (GitHub etc)
- Once it is initialised, it keeps track of all the current files (if present) and all the future files (as and when we modify) in that directory
- To initialise a git repo locally,

  ```bash
  git init
  ```

<br>

### Clone an existing remote repo

**_Cloning is a process of creating a git repo locally from an existing remote repo._**

```bash
git clone <remote repo url> <directory>
```

<br>

### Forking an existing remote repo

- It refers to the process of creating a copy of a repository, known as the "_fork_," from one user's account or organization to another user's account or organization.
- It is used extensively in open source development. Contributors can fork a project, make improvements or fixes in their forked repository, and then submit PRs (Pull Requests) to the original project to have their changes reviewed and potentially merged.
- Once a fork is created, It is exactly same as a remote repo under our account. One can clone it to the local machine, make changes, and push those changes back to the forked repository.

<br>

> <br>
> Fork is not a git command (or concept). it's a concept and a feature provided by Git hosting platforms like GitHub, GitLab, and Bitbucket. These platforms offer a web-based interface for managing Git repositories and collaboration, and one of the key features they provide is the ability to fork repositories. <br>
> <br>

<br>
<br>
