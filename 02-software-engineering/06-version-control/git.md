# Git Basics 

Git is a distributed version control system (VCS) that is widely used for software development and collaboration.

> git is a distributed VCS while github is a PaaS for VCS.

<br/>

## Configuring git

```
git config [--local | --global | --system] <key> [<value>]
```

- `--local` flag or no flag applies only to the current repository
- `--global` flag applies to every repo that one uses on his computer
- `--system` flag applies to every repo for all users on the comouter



| Operation | Syntax | Explanation | 
|----------|----------|----|
| 1. Set up username  | `git config --global user.name <username>`  |    |
| 2. Set up email  | `git config --global user.email <email>`  |    |
| 3. Read/ Check credentials | `git config user.name (or user.email)` | 

  
<br/>
