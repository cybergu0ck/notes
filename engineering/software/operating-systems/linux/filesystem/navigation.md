# Navigation

<br>
<br>
<br>

## Ls command

<br>
<br>

### Filtered list

To find files with substring of the full file name.

```bash
ls | grep "<substring?"
```

<br>
<br>

### List number of files

To list the number of files in the current directory.

```bash
ls | wc -l
```

<br>
<br>
<br>

## Cd command

```bash
cd ~/.      # cd into Home Directory (home directory is always fixed)
cd ..       # cd one directory up in the file structure
cd ./       # cd to current working directory (basically doesn't change directories)
cd ./..     # cd one directory up in the file structure
cd ./../..  # cd two directories up in the file structure
```
