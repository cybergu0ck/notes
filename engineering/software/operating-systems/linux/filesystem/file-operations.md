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

## Tee command

The *tee command* reads standard input (stdin) and writes it to both standard output (stdout) and one or more files.

- To write ".obsidian" into .gitignore file,

  ```bash
  echo ".obsidian" |tee .gitignore
  ```

<br>
<br>
<br>

## Cp command

This command can be used in two ways

1. to copy the single file or directory “item1” to file or directory “item2”

   ```syntax
   cp item1 item2
   ```

2. to copy multiple items (either files or directories) into a directory

   ```syntax
   cp item... directory
   ```

<br>

- Table 4-4, cp options
  | option | Meaning |
  |---|---|
  | -a, --archive | Copy the files and directories and all of their attributes, including ownerships and permissions. Normally, copies take on the default attributes of the user performing the copy. |
  | -i, --interactive | Before overwriting an existing file, prompt the user for confirmation. If this option is not specified, cp will silently overwrite files. |
  | -r, --recursive | Recursively copy directories and their contents. This option (or the -a option) is required when copying directories. |
  | -u, --update | When copying files from one directory to another, only copy files that either don't exist, or are newer than the existing corresponding files, in the destination directory. |
  | -v, --verbose | Display informative messages as the copy is performed. |

<br>

- Table 4-5 cp examples

  | Command             | Results                                                                                                                                                                                                                                                                          |
  | ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | cp file1 file2      | Copy file1 to file2. If file2 exists, it is overwritten with the contents of file1. If file2 does not exist, it is created.                                                                                                                                                      |
  | cp -i file1 file2   | Same as above, except that if file2 exists, the user is prompted before it is overwritten.                                                                                                                                                                                       |
  | cp file1 file2 dir1 | Copy file1 and file2 into directory dir1. dir1 must already exist.                                                                                                                                                                                                               |
  | cp dir1/\* dir2     | Using a wildcard, all the files in dir1 are copied into dir2. dir2 must already exist                                                                                                                                                                                            |
  | cp -r dir1 dir2     | Copy the contents of directory dir1 to directory dir2. If directory dir2 does not exist, it is created and, after the copy, will contain the same contents as directory dir1. <br> If directory dir2 does exist, then directory dir1 (andits contents) will be copied into dir2. |

<br>
<br>
<br>

## Mv command

The mv command performs both file moving and file renaming, depending on how it is used,

- To move or rename a file/ directory
  ```bash
  mv <file/dir> <file/dir>
  ```
- To move one or more items from one direcory to another
  ```bash
    mv <file/dir...> <dir>
  ```

<br>

- Table 4-6: mv Options

  | Option            | Meaning                                                                                                                                                                    |
  | ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | -i, --interactive | Before overwriting an existing file, prompt the user for confirmation. If this option is not specified, mv will silently overwrite files.                                  |
  | -u, --update      | When moving files from one directory to another, only move files that either don't exist, or are newer than the existing corresponding files in the destination directory. |
  | -v, --verbose     | Display informative messages as the move is performed.                                                                                                                     |

<br>

- Table 4-7: mv Examples

  | Command             | Results                                                                                                                                                                                                                        |
  | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  | mv file1 file2      | Move file1 to file2. If file2 exists, it is overwritten with the contents of file1. If file2 does not exist, it is created. In either case, file1 ceases to exist.                                                             |
  | mv -i file1 file2   | Same as above, except that if file2 exists, the user is prompted before it is overwritten.                                                                                                                                     |
  | mv file1 file2 dir1 | Move file1 and file2 into directory dir1. dir1 must already exist                                                                                                                                                              |
  | mv dir1 dir2        | If directory dir2 does not exist, create directory dir2 and move the contents of directory dir1 into dir2 and delete directory dir1. If directory dir2 does exist, move directory dir1 (and its contents) into directory dir2. |

<br/>
<br/>
<br/>

## Mkdir command

Creating directories using `mkdir`

```
mkdir <directory...>
```

- When three periods follow an argument in description of a command, it means the argument can be repeated!

- Creating a single directory,

  ```shell
  mkdir dir1
  ```

- Creating three directories,
  ```shell
  mkdir dir2 dir3 dir4
  ```

<br>
<br>
<br>

## Rm command

Removing items using `rm`

```bash
rm <item...>
```

<br>

- Table 4-8: rm Options

  | Option            | Meaning                                                                                                                                                                 |
  | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | -i, --interactive | Before deleting an existing file, prompt the user for confirmation. If this option is not specified, rm will silently delete files.                                     |
  | -r, --recursive   | Recursively delete directories. This means that if a directory being deleted has subdirectories, delete them too. To delete a directory, this option must be specified. |
  | -f, --force       | Ignore nonexistent files and do not prompt. This overrides the --interactive option.                                                                                    |
  | -v, --verbose     | Display informative messages as the deletion is performed.                                                                                                              |

<br>

- Table 4-9: rm Examples

  | Command           | Results                                                                                            |
  | ----------------- | -------------------------------------------------------------------------------------------------- |
  | rm file1          | Delete file1 silently.                                                                             |
  | rm -i file1       | Same as above, except that the user is prompted for confirmation before the deletion is performed. |
  | rm -r file1 dir1  | Delete file1 and dir1 and its contents.                                                            |
  | rm -rf file1 dir1 | Same as above, except that if either file1 or dir1 do not exist, rm will continue silently.        |

<br>

- CAUTION: Once an item is deleted in linux it's permanently gone!

  - Be particularly careful with wildcards. Consider this classic example. Let’s say you want to delete just the HTML files in a directory. To do this, you type: `rm *.html` which is correct, but if you accidentally place a space between the _ and the .html like so: `rm _ .html` the rm command will delete all the files in the directory and then complain that there is no file called .html.

* TIP: Whenever you use wildcards with `rm` (besides carefully
* checking your typing!), test the wildcard first with `ls`. This will let you see the
* files that will be deleted. Then press the up arrow key to recall the command
* and replace the `ls` with `rm`

<br/>
<br/>
<br/>
