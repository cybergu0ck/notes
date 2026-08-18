# Navigation

- Like Windows, a Unix-like operating system such as Linux organizes its files in what is called a hierarchical directory structure (Tree like patterns)
  - The first directory in the filesystem is called the root directory.
  - The root directory contains files and subdirectories, which contain more files and subdirectories, and so on
- Note that unlike Windows, which has a separate filesystem tree for each storage device, Unix-like systems such as Linux always have a single filesystem tree, regardless of how many drives or storage devices are attached to the computer.
- Storage devices are attached (or more correctly, mounted) at various points on the tree according to the whims of the system administrator.

<br>
<br>
<br>

## Pathname

<br>
<br>

### Absolute Pathnames

An absolute pathname begins with the root directory and follows the tree branch by branch until the path to the desired directory or file is completed.

<br/>
<br/>

### Relative Pathnames

A relative pathname starts from the working directory.

- The . or ./ symbol refers to the working directory.
- The .. or ../ symbol refers to the working directory’s parent directory

* In almost all cases, you can omit the ./ because it is implied. Hence `cd bin` will give the same results as `cd ./bin`.

<br>
<br>
<br>

## Pwd command

Check the current working directory using `pwd`

- `pwd` command is used to display the current working directory.
- When we first log in to our system, our current working directory is set to our home directory.
- Each user account is given its own home directory, which is the only place the user is allowed to write files when operating as a regular user.

<br>
<br>
<br>

## Ls command

`ls` command is used to list the files and directories in the current working directory.

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

`cd` command is used to change the current working directory.

```bash
cd ~/.      # cd into Home Directory (home directory is always fixed)
cd ..       # cd one directory up in the file structure
cd ./       # cd to current working directory (basically doesn't change directories)
cd ./..     # cd one directory up in the file structure
cd ./../..  # cd two directories up in the file structure
```

| command          | Description                                                      |
| ---------------- | ---------------------------------------------------------------- |
| `cd ./`          |                                                                  |
| `cd ../`         |                                                                  |
| `cd -`           | changes the working directory to the previous working directory. |
| `cd ~<username>` | changes the working directory to the home directory of username. |

- A pathname is the route we take along the branches of the tree to get to the directory we want.
- Pathnames can be specified in one of two ways, as absolute pathnames or as relative pathnames.
