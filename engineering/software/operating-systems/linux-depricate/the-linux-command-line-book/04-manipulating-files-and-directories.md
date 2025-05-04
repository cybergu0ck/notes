
# Wildcards

* Using wildcards (which is also known as ***globbing***) allow you to select filenames based on patterns of characters.
<br>

* Table 4-1, Wildcards 
	| Wildcard | Meaning |
	|---|--|
	| * | Matches any character |
	| ? | Matches a single character |
	| \[characters] | Matches any character that is a member of the set *characters* |
	| \[! characters] | Matches any character that is not a member of the set characters |
	| \[\[:class:]] | Matches any character that is a member of the specified class |

<br>

* Table 4-2, commonly used character classes
	| Character class | Meaning |
	|---| ---|
	| \[:alhanum:] | Matches any alphanumeric character |
	| \[:alpha:] | Matches any alphabetic character |
	| \[:digit:] | Matches any numeral |
	| \[:lower:] | Matches any lowercase letter |
	| \[:upper:] | Matches any uppercase letter |

*  Using wildcards makes it possible to construct very sophisticated selection criteria for filenames.

<br>


* Wildcard examples
	| Pattern | Matches |
	| ---| ---|
	|  g* |  Any files beginning with "g"   |
	|  b*.txt  |   Any files beginning with b, followed by any characters and ending with .txt   |
	| Data???    |  Any file beginning with "Data" and followed by exactly 3 characters |
	|   \[abc]*     |  Any file beginning with a "a" or "b" or "c"   |
	|    BACKUP.\[0-9]\[0-9]\[0-9]     |      Any file beginning with “BACKUP.” followed by exactly three numerals         |
	|    \[\[:upper:]]*     |           Any file beginning with an uppercase letter    | 
	|     \[!\[:digit:]]*    |         Any file not beginning with a numeral      |
	|     \*\[\[:lower:]123]    |      Any file ending with a lowercase letter or the numerals “1”, “2”, or “3”         | 

<br>
<br>

# Creating directories using `mkdir`

```
mkdir <directory...>
```

* When three periods follow an argument in description of a command, it means the argument can be repeated!

* Creating a single directory,
	```shell
	mkdir dir1
	```

* Creating three directories,
	```shell
	mkdir dir2 dir3 dir4
	```

<br>
<br>

# Copying files and directories using `cp`

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

* Table 4-4, cp options
	| option | Meaning |
	|---|---|
	|  -a, --archive   | Copy the files and directories and all of their attributes, including ownerships and permissions. Normally, copies take on the default attributes of the user performing the copy.    |
	| -i, --interactive    |  Before overwriting an existing file, prompt the user for confirmation. If this option is not specified, cp will silently overwrite files.   |
	|  -r, --recursive   |  Recursively copy directories and their contents. This option (or the -a option) is required when copying directories.   |
	|  -u, --update   | When copying files from one directory to another, only copy files that either don't exist, or are newer than the existing corresponding files, in the destination directory.    |
	|  -v, --verbose   | Display informative messages as the copy is performed.    |

<br>

* Table 4-5 cp examples

	| Command | Results |
	|---|---|
	|cp file1 file2 |Copy file1 to file2. If file2 exists, it is overwritten with the contents of file1. If file2 does not exist, it  is created. |
	| cp -i file1 file2|Same as above, except that if file2 exists, the user is prompted before it is overwritten. |
	|cp file1 file2 dir1 | Copy file1 and file2 into directory dir1. dir1 must already exist.|
	| cp dir1/* dir2|Using a wildcard, all the files in dir1 are copied into dir2. dir2 must already exist|
	|cp -r dir1 dir2 |Copy the contents of directory dir1 to directory dir2. If directory dir2 does not exist, it is created and, after the copy, will contain the same contents as directory dir1. <br> If directory dir2 does exist, then directory dir1 (andits contents) will be copied into dir2.  |

<br>
<br>

# Moving/Renaming items using `mv`

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

* Table 4-6: mv Options

	| Option | Meaning |
	|---|---|
	|-i, --interactive |Before overwriting an existing file, prompt the user for confirmation. If this option is not specified, mv will silently overwrite files. |
	| -u, --update |When moving files from one directory to another, only  move files that either don't exist, or are newer than the existing corresponding files in the destination directory. |
	|-v, --verbose | Display informative messages as the move is performed.|

<br>

* Table 4-7: mv Examples

	| Command | Results |
	|---|---|
	| mv file1 file2| Move file1 to file2. If file2 exists, it is overwritten with the contents of file1. If file2 does not exist, it is created. In either case, file1 ceases to exist.|
	| mv -i file1 file2| Same as above, except that if file2 exists, the user is prompted before it is overwritten.|
	| mv file1 file2 dir1 | Move file1 and file2 into directory dir1. dir1 must already exist|
	|mv dir1 dir2 | If directory dir2 does not exist, create directory dir2 and move the contents of directory dir1 into  dir2 and delete directory dir1. If directory dir2 does exist, move directory dir1 (and its contents) into directory dir2.|



<br/>
<br/>

# Removing items using `rm`

* The `rm` command is used to remove (delete) files and directories,

    ```bash
    rm <item...>
    ```
<br>

* Table 4-8: rm Options

	| Option | Meaning |
	|---|---|
	|-i, --interactive  |Before deleting an existing file, prompt the user for confirmation. If this option is not specified, rm will silently delete files.|
	|-r, --recursive | Recursively delete directories. This means that if a  directory being deleted has subdirectories, delete them too. To delete a directory, this option must be specified.|
	| -f, --force| Ignore nonexistent files and do not prompt. This overrides the --interactive option. |
	|-v, --verbose | Display informative messages as the deletion is performed.|

<br>

* Table 4-9: rm Examples

	| Command | Results |
	|---|---|
	|rm file1 | Delete file1 silently. |
	|rm -i file1| Same as above, except that the user is prompted for confirmation before the deletion is performed. |
	| rm -r file1 dir1 | Delete file1 and dir1 and its contents. |
	| rm -rf file1 dir1 | Same as above, except that if either file1 or dir1 do not exist, rm will continue silently. |


<br>

> CAUTION: Once an item is deleted in linux it's permanently gone!
    Be particularly careful with wildcards. Consider this classic example. Let’s say you want to delete just the HTML files in a directory. To do this, you type:
    `rm *.html`
    which is correct, but if you accidentally place a space between the * and the .html like so:
    `rm * .html`
    the rm command will delete all the files in the directory and then complain that there is no file called .html.

> TIP: Whenever you use wildcards with `rm` (besides carefully 
checking your typing!), test the wildcard first with `ls`. This will let you see the 
files that will be deleted. Then press the up arrow key to recall the command 
and replace the `ls` with `rm`



<br/>
<br/>

# Creating links using `ln`

A link in UNIX is a pointer to a file.

<br/>

## Hard links 

- Command to create a hard link is: 
    ```bash
    ln <original_file_name>  <link_name>
    ```
- Each hard linked file is assigned the same Inode value as the original, therefore they reference the same physical file location.
- If original file is removed then the link will still show the content of the file.
- We cannot create a hard link for a directory to avoid recursive loops. 
- Even if we change the filename of the original file then also the hard links properly work.
- ls -l command shows all the links with the link column shows number of links.
- Links have actual file contents
- Removing any link, just reduces the link count, but doesn’t affect other links.
- The size of any of the hard link file is same as the original file and if we change the content in any of the hard links then size of all hard link files are updated.
- The disadvantage of hard links is that it cannot be created for files on different file systems (disk partitions) and it cannot be created for special files or directories.

<br/>

## Symbolic links

A soft link is similar to the file shortcut feature which is used in Windows Operating systems. 

- Command to create a Soft link is: 
    ```bash
    ln -s <original_file_name>  <link_name>
    ```

- Each soft linked file contains a separate Inode value that points to the original file. 
- As similar to hard links, any changes to the data in either file is reflected in the other. 
- Soft links can be linked across different file systems, although if the original file is deleted or moved, the soft linked file will not work correctly (called hanging link).
- ls -l command shows all links with first column value l? and the link points to original file.
- Soft Link contains the path for original file and not the contents.
- Removing soft link doesn’t affect anything but removing original file, the link becomes “dangling” link which points to nonexistent file.
- A soft link can link to a directory.
- The size of the soft link is equal to the length of the path of the original file we gave. E.g if we link a file like ln -s /tmp/hello.txt /tmp/link.txt then the size of the file will be 14bytes which is equal to the length of the “/tmp/hello.txt”.
- If we change the name of the original file then all the soft links for that file become dangling i.e. they are worthless now.


