## cat

### Displaying the Contents of a File

```bash
cat <file>
```

- The following command will display the contents in the exisiting file, `greeting.txt`.

  ```bash
  cat greeting.txt
  ```

<br>

### Concatenating Multiple Files

```bash
cat <file1> <file2>
```

- The following command will display the contents in the exisiting file, `file.md` and then consequetively display the contents of `newfile.txt`.

  ```bash
  cat file.md newfile.txt
  ```

<br>

### Creating a New File

```bash
cat <newfile>
```

<br>

### Appending to a File

```bash
cat >> <filename>
```

- Example :

  ```bash
  cat >> greeting.txt
  Hey there!
  Good to see you
  (Ctrl + D)
  ```

<br>

### Overwriting a File

```bash
cat > <filename>
```

- Example :

  ```bash
  cat > greeting.txt
  Hey there!
  Good to see you
  (Ctrl + D)
  ```

<br>

### Printing the number of files in a directory

```bash
ls -1 | wc -l
```

<br>

### Combining Existing Files into another File

- To combine files and append to another file.

  ```bash
  cat <file1> <file2> >> <file>
  ```

- To combine files and overwrite to Another file.

  ```bash
  cat <file1> <file2> > <file>
  ```

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

## Modifying default directory paths

```bash
nano ~/.config/user-dirs.dirs
```
