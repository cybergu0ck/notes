
### tree command
---

To show only directories
```cmd
tree 
```

```output
E:.
├───10StandardLibrary1
├───11StandardLibrary2
├───12VirtualEnvironment&Packages
├───2Interpreter
├───3Introduction
├───4ControlFlow
├───5Datatructures
│   └───__pycache__
├───6Modules
│   ├───Numpy
│   ├───OS
│   │   ├───Folder1
│   │   │   └───Folder11
│   │   └───Folder2
│   └───Pip
├───7Input&Output
├───8Error&Exceptions
├───9Classes
├───RandomConcepts
└───_assets
```


To show directories and files
```cmd
tree /f
```

```output
E:.
├───10StandardLibrary1
├───11StandardLibrary2
├───12VirtualEnvironment&Packages
│       Venv.md
│
├───2Interpreter
├───3Introduction
│       Dictionaries.ipynb
│       Lists.ipynb
│       Python Dictionaries.md
│       Sets.ipynb
│       Strings.ipynb
│       Tuples.ipynb
│
├───4ControlFlow
│       ForLoop.ipynb
│       Functions.md
│       generators.ipynb
│       IfElse.ipynb
│       isinstance.ipynb
│       property.ipynb
│       PythonDecorator.py
│
├───5Datatructures
│   │   1. Stacks.ipynb
│   │   2. Queues.ipynb
│   │   BigO.ipynb
│   │   binaryTree.py
│   │   LinkedLists.py
│   │   Trees.ipynb
│   │
│   └───__pycache__
│           queue.cpython-39.pyc
│
├───6Modules
│   │   Regex.ipynb
│   │
│   ├───Numpy
│   ├───OS
│   │   │   osModule.ipynb
│   │   │
│   │   ├───Folder1
│   │   │   │   file1.txt
│   │   │   │   image.png
│   │   │   │
│   │   │   └───Folder11
│   │   └───Folder2
│   │           code.py
│   │
│   └───Pip
│           Pip.md
│
├───7Input&Output
├───8Error&Exceptions
├───9Classes
│       Inheretence.py
│       OOPS.ipynb
│
├───RandomConcepts
│       Fixes.md
│       RandomConcepts.ipynb
│
└───_assets
        confirmvenv.png
        passByRefpassByVal.png
        pipfreeze.png
```


To show everything
```cmd
tree /f /a
```

 