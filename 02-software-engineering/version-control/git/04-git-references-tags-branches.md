# Theory 

- Git history is stored in the form of Directed Acyclic Graph (DAG) where commits are represented as nodes and edges point to the parent commit
- A DAG is a directed graph (edges have directions) with no cycles!
- New commits get chained to the previous commits!

- `git log --graph` displays the DAG using * and lines


<br>
<br>

# Reference

- A reference is a userfriendly name that points to either a commit SHA-1 hash or another reference.
- The reference is called a symbolic reference it points to another reference.

- In the output of the `git log --oneline`, the **HEAD** and the **master** are references.

    ```
    $ git log --oneline 
    f9a6285 (HEAD -> master) created moviedb.py
    ```
- We can use the reference instead of the current SHA-1 hash in all git commands.
- "HEAD" refers to a symbolic reference that points to the currently checked-out commit in a repository.
-  ~ or ~1 is used to refer the parent of current commit. ~~ or ~2 refers to the parent's parent of the current commit

<br>
<br>

# Tag

- A tag is a reference/label attached to a specific commit.
- There are 2 types of tags:
    1. Lightweight : A simple reference to a commit
    2. Annoted tag : A full git object that references a commit
- Like other references we can use tags instead of SHA-1 values in git commands.

<br>

## Creating a light weight tag

```
git tag <tagname> [commit]
```
Setting a tag called header for the commit where we defined a module level header and then viewing the log

```
$ git tag header HEAD

$ git log --oneline
1edd0b1 (HEAD -> master, tag: header) Added module header
f9a6285 created moviedb.py

```

<br>

## View tags 

| Operation | Syntax | Explanation | 
|----------|----------|----|
| View All tags in repo | `git tag` | |
| View a specific tagged commit | `git show <tag>` |

> Check documentation to create an annotated tag!

<br>
<br>















