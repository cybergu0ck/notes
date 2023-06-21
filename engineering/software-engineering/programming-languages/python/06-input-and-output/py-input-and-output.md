# Reading from files

* When you want to work with the information in a text file, the first step is to read the file into memory. You can read the entire contents of a file, or you can work through the file one line at a time.

    ```
    #pi.txt

    3.1415926535 
    8979323846 
    2643383279
    ```

    ```python
    with open('pi.txt') as file_object:
        contents = file_object.read()
        print(contents)

    """o/p

    3.1415926535 
    8979323846 
    2643383279
    
    """
    ```

* we can `open()` and `close()` the files explicitly but improperly closed files can cause data to be lost or corrupted. hence, it is always ideal to use `with open() as` statement where it'll automatically close the file after use.
* The only difference between the output and the original file is the extra blank line at the end of the output. The blank line appears because read() returns an empty string when it reaches the end of the file; this empty string shows up as a blank line. use `rstrip()` to remove all whitespaces from the right side of the string.

<br/>
<br/>

# File Paths

* Consider the directory tree as shown
    ```
    Code
    |
    └───try.py 
    │
    └───text-folder
            pi.txt
    ```

* Using Relative file path
    ```python
    with open('text-folder\pi.txt') as obj:
        contents = obj.read()
        print(contents)

    # We can use wither \ or \\ in the file path string.

    """o/p
    3.1415926535 
    8979323846 
    2643383279
    """
    ```

* Using Absolute file path
    ```python
    with open('D:\\Code\\text-folder\\pi.txt') as obj:
        contents = obj.read()
        print(contents)

    #Make sure to use \\ when using absolute paths.

    """o/p
    3.1415926535 
    8979323846 
    2643383279
    """
    ```

<br>
<br>

# Reading line by line

```python
with open('D:\\Code\\text-folder\\pi.txt') as obj:
    for line in obj:
        print(line)    #Here line is not a keyword!

"""o/p
 3.1415926535 
 8979323846 
 2643383279
"""
```

* These blank lines appear because an invisible newline character is at the end of each line in the text file. The print statement adds its own newline every time.

    ```python
    # fix using rstrip()
    with open('D:\\Code\\text-folder\\pi.txt') as obj:
        for line in obj:
            print(line.rstrip())    #Here line is not a keyword!

    """o/p
    3.1415926535 
    8979323846 
    2643383279
    """
    ```