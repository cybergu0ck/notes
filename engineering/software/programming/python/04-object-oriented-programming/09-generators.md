[Generators](https://docs.python.org/3/glossary.html#term-generator) are a simple and powerful tool for creating iterators. They are written like regular functions but use the [`yield`](https://docs.python.org/3/reference/simple_stmts.html#yield) statement whenever they want to return data. Each time [`next()`](https://docs.python.org/3/library/functions.html#next "next") is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed).

```python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


print(type(reverse))

my_generator_obj = reverse('abc')

print(type(my_generator_obj))

for iterable in my_generator_obj:
    print(iterable)

#><class 'function'>
#><class 'generator'>
#>c
#>b
#>a
```

> Anything that can be done with generators can also be done with class-based iterators as described in the previous section. What makes generators so compact is that the `__iter__()` and [`__next__()`](https://docs.python.org/3/reference/expressions.html#generator.__next__ "generator.__next__") methods are created automatically.

- Another key feature is that the local variables and execution state are automatically saved between calls. This made the function easier to write and much more clear than an approach using instance variables like `self._index` and `self.data`. (See `class Reverse` in [[08-iterators]] )

- In addition to automatic method creation and saving program state, when generators terminate, they automatically raise [`StopIteration`](https://docs.python.org/3/library/exceptions.html#StopIteration "StopIteration").