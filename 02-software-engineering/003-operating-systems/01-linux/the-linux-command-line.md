
# 4 Manipulating Files and Directories
---

## Wildcards
---
Using wildcards (which is also known as ***globbing***) allow you to select filenames based on patterns of characters.

Table 4-1, Wildcards 
| Wildcard | Meaning |
|---|--|
| * | Matches any character |
| ? | Matches a single character |
| \[characters] | Matches any character that is a member of the set *characters* |
| \[! characters] | Matches any character that is not a member of the set characters |
| \[\[:class:]] | Matches any character that is a member of the specified class |

Table 4-2, commonly used character classes
| Character class | Meaning |
|---| ---|
| \[:alhanum:] | Matches any alphanumeric character |
| \[:alpha:] | Matches any alphabetic character |
| \[:digit:] | Matches any numeral |
| \[:lower:] | Matches any lowercase letter |
| \[:upper:] | Matches any uppercase letter |

> Using wildcards makes it possible to construct very sophisticated selection criteria for filenames.


Wildcard examples
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


# Creating directories using `mkdir`
---
```syntax
mkdir directory...
```

When three periods follow an argument in description of a command, it means the argument can be repeated!

Creating a single directory,
```shell
mkdir dir1
```

Creating three directories,
```shell
mkdir dir2 dir3 dir4
```



# Copying files and directories using `cp`
---
This command can be used in two ways 

1. to copy the single file or directory “item1” to file or directory “item2” 
```syntax
cp item1 item2
```

2. to copy multiple items (either files or directories) into a directory
```syntax
cp item... directory
```

Table 4-4, cp options
| option | Meaning |
|---|---|
|  -a, --archive   | Copy the files and directories and all of their attributes, including ownerships and permissions. Normally, copies take on the default attributes of the user performing the copy.    |
| -i, --interactive    |  Before overwriting an existing file, prompt the user for confirmation. If this option is not specified, cp will silently overwrite files.   |
|  -r, --recursive   |  Recursively copy directories and their contents. This option (or the -a option) is required when copying directories.   |
|  -u, --update   | When copying files from one directory to another, only copy files that either don't exist, or are newer than the existing corresponding files, in the destination directory.    |
|  -v, --verbose   | Display informative messages as the copy is performed.    |

Table 4-5 cp examples

* Copy file1 to file2,
	* If file2 exists, contents of file2 is overwritten by contents of file1
	* If file2 doesn't exist, it is created.

```sh
cp file1 file2
```

* Same as above, but user is prompted before overwriting.
```sh
cp -i file1 file2
```

* Copy file1 and file2 to dir1, dir1 must exist for the following command to work
```sh
cp file1 file2 dir1
```

* Copy all files in dir1 to dir2 using wildcard, dir2 must exist!
```sh
cp dir1/* dir2
```


