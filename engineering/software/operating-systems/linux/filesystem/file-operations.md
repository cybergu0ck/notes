# File operations

<br>
<br>
<br>

## Cat command

<br>
<br>

### Displaying the Contents of a File

```bash
cat <file>
```

<br>
<br>

### Concatenating Multiple Files

```bash
cat <file1> <file2>
```

<br>
<br>

### Creating a New File

```bash
cat <newfile>
```

<br>
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
