# Venv

_The venv module supports creating lightweight “virtual environments”, each with their own independent set of Python packages installed._

<br>
<br>

##  Creating the virtual environment

- Use the following commmand to create the virtual environment, `<path>` is optional.

  ```bash
  python -m venv <environment_name> <path>
  ```

- Some pointers about venv:

  - The version of python used to create the virtual environment will be the version of python installed in the newly created environment.
  - If diff version of python is to be installed, use virtual_env !

  - The internal directories of the created venv will be based on the type of shell used (bash, cmd, powershell etc)

<br>
<br>

## Activate the virtual environment

- Use the following command for a venv created using a bash/zsh shell:

  ```zsh
  source env/bin/activate
  ```

- Use the following command for a venv created using a cmd:

  ```zsh
  env\Scripts\actiavte
  ```

- Use the following command for a venv created using a powershell:

  ```zsh
  env\Scripts\activate.bat
  ```

<br>
<br>
  
## Deactivate the virtual environment

```cmd
deactivate
```

<br>
<br>

## Delete the virtual environment

- Basically delete the environment directory and it’s subdirectories.

<br>
<br>

## requirements.txt

Refer [requirements.txt](../../../tools-and-technology/pip/pip.md#requirementstxt)

<br>
<br>

## Good Practice

1.  It is ideal  to keep the environment folder free of other files because an environment is something which can be created and destroyed.

    - Avoid the following directory structure for projects:

      ```
      my-project
        - my-proj-env
          - code
          - assets
          - documentation
      ```

    - Follow the following directory structure:

      ```
      my-project
        - my-proj-env
        - code
        - assets
        - documentation
      ```

2.  Donot use source control (git) on environment folder. if you want to share, send the requirement.txt file and ask your peer to reproduce the results by creating his own environment.

<br>
<br>

## References

[venv — Creation of virtual environments — Python 3.11.1 documentation](https://docs.python.org/3/library/venv.html)
