# Files

Note on file names in linux,

- Filenames that begin with a period character are hidden. This only means that ls will not list them unless you say `ls -a`.
- Filenames and commands in Linux, as in Unix, are case sensitive. The filenames _File1_ and _file1_ refer to different files
- Linux has no concept of a “file extension” like some other operating systems.
- Though Linux supports long filenames that may contain embedded spaces and punctuation characters, limit the punctuation characters in the names of files you create to period, dash (hyphen), and underscore. Most importantly, **_do not embed spaces in filenames._**

<br/>
<br/>
<br/>

## File command

- `file` command to print a breif description of the file contents.
- Syntax: `file <filename>`
- Note that while a filename like picture.jpg would normally be expected to contain a JPEG compressed image, it is not required to in
  Linux.
- In fact, one of the common ideas in Unix like operating systems such as Linux is that “everything is a file."

<br/>
<br/>
<br/>

## Less command

- `less` command is used to view text files.
- Syntax : `less <filename>`
- Many of the system files, config files and scripts are stored in human readable texts, hence less command is ideal.
- Once the less program starts, _we can view the contents of the file. If the file is longer than one page, we can scroll up and down. To exit less, press the Q key_

<br/>
<br/>

## Links

A link in UNIX is a pointer to a file.

<br>
<br>

### Hard links

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
<br/>

### Symbolic links

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

<br>
<br>

### Ln command

<br/>
<br/>
<br/>

## Wildcards

- Using wildcards (which is also known as **_globbing_**) allow you to select filenames based on patterns of characters.
  <br>

- Table 4-1, Wildcards
  | Wildcard | Meaning |
  |---|--|
  | * | Matches any character |
  | ? | Matches a single character |
  | \[characters] | Matches any character that is a member of the set *characters\* |
  | \[! characters] | Matches any character that is not a member of the set characters |
  | \[\[:class:]] | Matches any character that is a member of the specified class |

<br>

- Table 4-2, commonly used character classes
  | Character class | Meaning |
  |---| ---|
  | \[:alhanum:] | Matches any alphanumeric character |
  | \[:alpha:] | Matches any alphabetic character |
  | \[:digit:] | Matches any numeral |
  | \[:lower:] | Matches any lowercase letter |
  | \[:upper:] | Matches any uppercase letter |

- Using wildcards makes it possible to construct very sophisticated selection criteria for filenames.

<br>

- Wildcard examples
  | Pattern | Matches |
  | ---| ---|
  | g* | Any files beginning with "g" |
  | b*.txt | Any files beginning with b, followed by any characters and ending with .txt |
  | Data??? | Any file beginning with "Data" and followed by exactly 3 characters |
  | \[abc]_ | Any file beginning with a "a" or "b" or "c" |
  | BACKUP.\[0-9]\[0-9]\[0-9] | Any file beginning with “BACKUP.” followed by exactly three numerals |
  | \[\[:upper:]]_ | Any file beginning with an uppercase letter |
  | \[!\[:digit:]]\* | Any file not beginning with a numeral |
  | \*\[\[:lower:]123] | Any file ending with a lowercase letter or the numerals “1”, “2”, or “3” |

<br>
<br>
<br>
