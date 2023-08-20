# OS Module

## walk() function

- `os.walk` returns a generator, that creates a tuple of values (current_path, directories in current_path, files in current_path).
- Every time the generator is called it will follow each directory recursively until no further sub-directories are available from the initial directory that walk was called upon.

```py
obj = os.walk('D:\PC\ProgramFiles\VSCode\Python\PyLearning\Modules\os Module')
type(obj)

#>generator
```

Given the folder structure

```
-> os Module
        -> Folder1
            -> Folder 1.1 (empty)
            - file.txt
            - image.png
        -> Folder2
            - code.py
        - osModule.ipynb

```

```py
for obj in os.walk('D:\PC\ProgramFiles\VSCode\Python\PyLearning\Modules\os Module'):
    print(obj)
    print('\n')


"""
('D:\\PC\\ProgramFiles\\VSCode\\Python\\PyLearning\\Modules\\os Module', ['Folder1', 'Folder2'], ['osModule.ipynb'])

('D:\\PC\\ProgramFiles\\VSCode\\Python\\PyLearning\\Modules\\os Module\\Folder1', ['Folder1.1'], ['file1.txt', 'image.png'])

('D:\\PC\\ProgramFiles\\VSCode\\Python\\PyLearning\\Modules\\os Module\\Folder1\\Folder1.1', [], [])

('D:\\PC\\ProgramFiles\\VSCode\\Python\\PyLearning\\Modules\\os Module\\Folder2', [], ['code.py'])
"""
```

```py
for item in os.walk('D:\PC\ProgramFiles\VSCode\Python\PyLearning\Modules\os Module'):
    print(type(item),'\n')
    print(f"""The type of first item in the tuple is {type(item[0])} \n
The type of second item in the tuple is {type(item[1])} \n
The type of third item in the tuple is {type(item[2])} \n
    """)
    break


"""
<class 'tuple'>
The type of first item in the tuple is <class 'str'>
The type of second item in the tuple is <class 'list'>
The type of third item in the tuple is <class 'list'>
"""
```

```py
for path, subdir, file in os.walk('D:\PC\ProgramFiles\VSCode\Python\PyLearning\Modules\os Module'):
    print(path)
    print(subdir)
    print(file)
    print('\n')

"""
D:\PC\ProgramFiles\VSCode\Python\PyLearning\Modules\os Module
['Folder1', 'Folder2']
['osModule.ipynb']

D:\PC\ProgramFiles\VSCode\Python\PyLearning\Modules\os Module\Folder1
['Folder1.1']
['file1.txt', 'image.png']

D:\PC\ProgramFiles\VSCode\Python\PyLearning\Modules\os Module\Folder1\Folder1.1
[]
[]

D:\PC\ProgramFiles\VSCode\Python\PyLearning\Modules\os Module\Folder2
[]
['code.py']
"""
```
