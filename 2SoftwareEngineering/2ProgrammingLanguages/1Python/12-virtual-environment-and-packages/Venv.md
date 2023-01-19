The `venv` module supports creating lightweight “virtual environments”, each with their own independent set of Python packages installed.

[official documentation]([venv — Creation of virtual environments — Python 3.11.1 documentation](https://docs.python.org/3/library/venv.html))


###  Creating a new virtual environment

---
```cmd
python -m venv test_env
```

- my_env is the name of the python virtual environment.
- The above command creates the virtual environment in the directory in which the command is run.
- 
```cmd
python -m venv test_env D:\PC\Code\My_Project
```

- The above command show's how to use path for the virtual environment.


> The version of python used to create the virtual environment will be the version of python installed in the newly created environment.

> If diff version of python is to be installed, use virtual_env !

  

### Check the Virtual environment using **dir**
---
![image](./_assets/confirmvenv.png)
We can see that test_env directory is formed!

### To activate the environment
---
```cmd
test_env\Scripts\activate.bat
```

  
### To deactivate the environment
---
```cmd
deactivate
```

### To delete the enironment
---
```cmd
rmdir test_env /s
```

- Basically delete the environment directory and it’s subdirectories.


### Creating Requirements.txt File
---
requirements.txt is **a file listing all the dependencies for a specific Python project**.

- To get the list of all dependencies in the virtual environment, use the following command and copy the contents to a txt file and name it requirements.txt

```cmd
pip freeze
```


![image](./_assets/pipfreeze.png)


### Installing packages using requirements.txt
---
```cmd
pip install -r <path of requirements.txt>
```


### Good Practice
---

> It is ideal  to keep the environment folder free of other files because an environment is something which can be created and destroyed.
 
Avoid the following directory structure for projects:


- ->MyProject

        -> MyProject_env1

            -> Code

            -> Assets

            -> Documentation

  

Follow the following directory structure:

  

- -> MyProject

        -> MyProject_env1

        -> Code Base

        -> Assets

        -> Documentation

  

> Donot use source control (git) on environment folder. if you want to share, send the requirement.txt file and ask your peer to reproduce the results by creating his own environment.