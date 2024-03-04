
#### os.walk( ) was not recursing through all folders when all the foldernames were modified
---
Exact problem as [python - Renaming folders and files while os.walk()ing them missed some files after change of the directory name - Stack Overflow](https://stackoverflow.com/questions/53123867/renaming-folders-and-files-while-os-walking-them-missed-some-files-after-chang)

Fix : use topdown parameter in walk() and make it False.