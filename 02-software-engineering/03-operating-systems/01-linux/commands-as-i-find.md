
# Tee

The _tee command_ reads standard input (stdin) and writes it to both standard output (stdout) and one or more files.

To write ".obsidian" into .gitignore file,
```bash
echo ".obsidian" |tee .gitignore
```

<br/>

# `cd `

```bash
cd ~/.      # cd into Home Directory (home directory is always fixed)
cd ..       # cd one directory up in the file structure
cd ./       # cd to current working directory (basically doesn't change directories) 
cd ./..     # cd one directory up in the file structure
cd ./../..  # cd two directories up in the file structure 
```

