# Permissions

The first letter tells us if it is a directory or a file,

- If the first letter is 'd' then it is referring to a directory.
- If it is '-' then it is referring to a file.
- If it is 'l' then it is referring to links.

```syntax
drwxrwxr-x  2  batpi  batpi 4096 Feb 15 16:41 dir1
|           |    |      |     |    |      |     |
|           |    |      |     |    |      |     Name of the directory/file
|           |    |      |          Date   Time
|           |    |      Group
|           |    User
|
|
--premission string
```

The first string in every line is the permission string. Understanding it more,

```
d rwx   rwx   r-x
  |     |     |
  |     |     Permission for others
  |     |
  |      Permission for Group
  |
  Permission for User
```

- 'r' means Read the contents of the directory or a file
- 'w' means Write
- 'x' means Execute
  - If it were a file, 'x' means it can be be executed.
  - If it were a directory, 'x' means we can go into that directory.

<br/>
<br/>
<br/>

## Chmod command

Used to change permissions.

```bash
chmod  <entity>   <add or remove>  <permission type>  <file/directory>
```

- entity can be
  - 'u' for user
  - 'g' for group
  - 'o' for others
- add or remove:
  - '+' for add
  - '-' for remove
- permission type:
  - 'r' for Read
  - 'w' for Write
  - 'x' for Execute

<br/>

Few examples to make it concrete,

- Giving user the permission to execute the file called testfile.txt
  ```bash
  chmod u+x testfile.txt
  ```
- Removing user's permission to enter into a directory called dangerous-dir
  ```bash
  chmod u-x dangerous-dir
  ```
- Giving user full permissions and removing all permissions for groups and others
  ```bash
  chmod go-rwx file1.txt
  ```

<br/>

### Permissions in the form of bits

rwx can be referred to 2^2 , 2^1, 2^0 i.e. 4,2,1 respectively.

- 7 means rwx
- 4 means r--
- 2 means -w-
- 1 means --x
- 5 means r-x
- 3 means -wx
- 6 means rw-
- 0 means ---

<br/>
<br/>
<br/>

## Chown command

Change ownership using chown.

```bash
sudo chown <new_owner> <file/directory>
```

- change ownership of file nuke-code from current owner (has sudo previlledges) to user called batman
  ```bash
  sudo chown batman nuke-code
  ```
- We can recursively do
  ```bash
  sudo chown -R batman nuke-dir
  ```
