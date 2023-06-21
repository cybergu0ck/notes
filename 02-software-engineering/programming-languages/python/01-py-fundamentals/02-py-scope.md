```python

#Change the name of the fucntion here
def passBy(data):
    data = 1000
    print("value of data inside the function scope: ", data)

data = 1
print("value of data initially: ", data)

passBy(data)
print("value of data finally: ", data)

"""
Output :
value of data initially: 1 
value of data inside the function scope: 1000 
value of data finally: 1

"""
```