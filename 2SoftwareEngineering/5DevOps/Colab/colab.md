

```python 
from psutil import *

cpu_count()
```


```python
#cpu model and speed
!lscpu |grep 'Model name'
```

```python
#gpu type
!nvidea-smi -L
```

```python
!nvidea-smi
```


### Importing a library that is not in Colaboratory
---
To import a library that's not in Colaboratory by default, you can use `!pip install` or `!apt-get install`.