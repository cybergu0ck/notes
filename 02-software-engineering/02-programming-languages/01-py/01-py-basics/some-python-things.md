# A thing about interpretor 

The code written in a single line occurs simulataneosly. I don't know what is this called but observe the following behaviour.


```python
listed = [1,2,3]

def swap(i,j):
    listed[i] = listed[j]
    listed[j] = listed[i]
swap(1,2)

print(listed)

#>[1, 3, 3]
```


```python
listed = [1,2,3]

def swap(i,j):
    listed[i],listed[j] = listed[j],listed[i]
      
swap(1,2)

print(listed)

#>[1, 3, 2]
```

