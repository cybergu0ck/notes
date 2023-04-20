Consider a for-loop

```python
for element in [1, 2, 3]:
    print(element)

#>1
#>2
#>3
```
<br/>

The use of iterators pervades and unifies Python. Behind the scenes, the [`for`](https://docs.python.org/3/reference/compound_stmts.html#for) statement calls [`iter()`](https://docs.python.org/3/library/functions.html#iter "iter") on the container object. The function returns an iterator object that defines the method [`__next__()`](https://docs.python.org/3/library/stdtypes.html#iterator.__next__ "iterator.__next__") which accesses elements in the container one at a time. When there are no more elements, [`__next__()`](https://docs.python.org/3/library/stdtypes.html#iterator.__next__ "iterator.__next__") raises a [`StopIteration`](https://docs.python.org/3/library/exceptions.html#StopIteration "StopIteration") exception which tells the `for` loop to terminate. You can call the [`__next__()`](https://docs.python.org/3/library/stdtypes.html#iterator.__next__ "iterator.__next__") method using the [`next()`](https://docs.python.org/3/library/functions.html#next "next") built-in function; this example shows how it all works:

```python
some_string = 'abc'
my_iterator = iter(some_string)       # iter() method is used to create iterators from iterable objects
print(my_iterator)

#><str_iterator object at 0x000001C31312AE30>
```

```python
some_string = 'abc'
my_iterator = iter(some_string)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))  # This line raises the error


#>a
#>b
#>c
#> Traceback (most recent call last):
#  File "d:\PC\Code\Other\Try\TryPy\Try.py", line 6, in <module>
#   print(next(my_iterator))
# StopIteration
```


<br/>

> Having seen the mechanics behind the iterator protocol, it is easy to add iterator behavior to your classes. Define an __iter__() method which returns an object with a __next__() method. If the class defines __next__(), then __iter__() can just return self:

```python
class Reverse:
    def __init__(self, string_data):
        self.string_data = string_data
        self._index = len(string_data)

    def __itr__(self):
        return self

    def __next__(self):
        if self._index == 0:
            raise StopIteration
        self._index -= 1
        return self.string_data[self._index]

obj = Reverse('abc')
print(next(obj))
print(next(obj))
print(next(obj))

# Or we can also use `for char in obj: print char`


#>c
#>b
#>a
```