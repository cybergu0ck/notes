# Pip

<br>
<br>

## requirements.txt

_requirements.txt is a file listing all the dependencies for a specific python project._

<br>

### Creating a requirements.txt file manually

- requirements.txt file can be created manually by listing the packages and the versions.

  ```txt
  package1==1.0.0
  package2>=2.1.0
  ```

<br>

### Generating a requirements.txt file from a virtual environment

1. Activate the virtual environment.
2. Run the following command to genereate the file.

   ```bash
   pip freeze > requirements.txt
   ```

<br>

### Installing the packages from requirements.txt

```zsh
pip install -r <path-to-requirements.txt>
```
