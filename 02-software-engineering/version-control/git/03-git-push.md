- To push the commits to a remote repo, we have to make sure that there is a remote repo associated with the current local repo.

- There can be 2 scenarios

    1. We already have a local repo on our local machine.
    2. We donot have a local repo but there's a remote repo which we want to copy to our local machine.

<br>
<br>

# Remote Add 

`git remote add` associates the remote repo with the current existing local repo.

<br>

| Operation | Syntax | Explanation | 
|----------|----------|----|
|1. Add a remote repo | `git remote add <name> <url>` |  `<name>` is the alias given to the remote repo, so that we can refer to the remote repo using the alias instead of the url!  `origin` is the general alias name <br> `<url` is the remote url found from the PaaS ex: github| 
|2. Get Info on remote repo | `git remote --verbose`| Displays info (url) about remote repo associated with local repo |

<br/>
<br/>

# Clone 

`git clone` is used to create a local copy of a remote repo. i.e. if we donot have a local repo then cloning a remote repo will create a local repo that is associated with the remote repo.

<br/>

| Operation | Syntax | Explanation | 
|----------|----------|----|
|1. Clone a remote repo | `git clone <url> [localprojectname]` |  creates a local repo from a remote repo <br/> if localprojectname is specified, local repo will be named that | 
|2. Get Info on remote repo | `git remote --verbose`| Displays info (url) about remote repo associated with local repo |

<br/>
<br/>

# Push

Once we are sure that a remote repo is associated with the local repo then we can push the commits to the remote repo.

```
git push -u <remote> <branch>
```

- `<remote>` can be alias or the url of the remote repo.
- -u is set to track the current branch (--set-upstream).