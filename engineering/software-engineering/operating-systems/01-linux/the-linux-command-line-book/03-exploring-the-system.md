# ls command

## Options and Arguments

* Commands are often followed by one or more options that modify their behavior and, further, by one or more arguments, the items upon which the command acts

    ```command -options arguments```

* Many commmands also support long options with syntax:

    ```command --longOptions arguments```

* Many commands allow multiple short options to be strung together. example:

    ```bash
    ls -la
    ```

<br/>

![image](./ImageRefs/lsOptions.png)

<br/>

## A Longer Look at Long Format

![image](./ImageRefs/ls-l.png)

* The meaning of each terms :

    ![image](./ImageRefs/ls-lMeaning.png)

<br/>
<br/>

# Determining a File’s Type with `file`

* `file` command to print a breif description of the file contents.
* Syntax: ```file <filename>```
* Note that while a filename like picture.jpg would normally be expected to contain a JPEG compressed image, it is not required to in 
Linux.
* In fact, one of the common ideas in Unix like operating systems such as Linux is that “everything is a file."

<br/>
<br/>

# Viewing File Contents with `less`

* `less` command is used to view text files. 
* Syntax : ```less <filename>```
* Many of the system files, config files and scripts are stored in human readable texts, hence less command is ideal.
* Once the less program starts, *we can view the contents of the file. If the  file is longer than one page, we can scroll up and down. To exit less, press the Q key*

<br/>
<br/>

# Directories Found on Linux Systems 

![image](./ImageRefs/dir1.png)
![image](./ImageRefs/dir2.png)
![image](./ImageRefs/dir3.png)
![image](./ImageRefs/dir4.png)
![image](./ImageRefs/dir5.png)
![image](./ImageRefs/dir6.png)


<br/>
<br/>

## Symbolic Links
---



