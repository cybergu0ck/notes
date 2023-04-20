From here on, everything will be explained using practical illustration! 

- Consider the project of movie rating website (kinda like IMDB).
- The project directory is MovieDB

<br>
<br>

# Initialising a git Repo

```bash
git init
```
```
$ git init
Initialized empty Git repository in /home/coder/moviedb/.git/
```

<br>
<br>

# Checking the status of files

```
git status
```

```
$ git status
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

Now, lets create a movie.py file which contains our code. After creating the file and running `git status`

```
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        moviedb.py

nothing added to commit but untracked files present (use "git add" to track)
```

<br>
<br>

# Adding to staging Area

```
git add <file/ folder ...>
```

After running `git add .` and then checking the status

```
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   moviedb.py
```

<br>
<br>

# Commit

```
git commit -m <message>
```

```bash
$ git commit -m "created moviedb.py"
[master (root-commit) f9a6285] created moviedb.py
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 moviedb.py
```

<br>
<br>

# View Log

The project's commit history can be viewed using 

```
git log --oneline --graph
```
```
$ git log --oneline 
f9a6285 (HEAD -> master) created moviedb.py
```

In the above output, 
- the first string is the partial SHA-1 hash [Refer Git ID](../01-git-fundamentals.md##git-id/-sha-1-/-hash-/-object-id-/-checksum)
- the HEAD and master in the paranthesis is the reference [Refer References]()

>Check backlinks for github 