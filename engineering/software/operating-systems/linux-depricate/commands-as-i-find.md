<br>

### Printing the number of files in a directory

```bash
ls -1 | wc -l
```

<br>

<br>
<br>
<br>

## Tee

The *tee command* reads standard input (stdin) and writes it to both standard output (stdout) and one or more files.

To write ".obsidian" into .gitignore file,

```bash
echo ".obsidian" |tee .gitignore
```

<br/>
<br/>
<br/>

## `cd `

```bash
cd ~/.      # cd into Home Directory (home directory is always fixed)
cd ..       # cd one directory up in the file structure
cd ./       # cd to current working directory (basically doesn't change directories)
cd ./..     # cd one directory up in the file structure
cd ./../..  # cd two directories up in the file structure
```

<br>
<br>
<br>

## grep along with ls

- To find files with substring of the full file name.

  ```bash
  ls | grep "<substring?"
  ```

<br>
<br>
<br>

## Print the number of files in the directory

```bash
ls | wc -l
```

<br>
<br>
<br>
