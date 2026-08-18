[← Back to oops](./contents)

# Contents

- [Generators](#generators)
  - [Generator expressions](#generator-expressions)

<br>
<br>
<br>




# Generators

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

<br>
<br>
<br>

## Generator expressions

Some simple generators can be coded succinctly as expressions using a syntax similar to list comprehensions but with parentheses instead of square brackets. These expressions are designed for situations where the generator is used right away by an enclosing function. Generator expressions are more compact but less versatile than full generator definitions and tend to be more memory friendly than equivalent list comprehensions.

`sum()` is a builtin function which outputs the sun of the iterable that is giving as an input

```python
#example code for sum()

print(sum([1,2,3]))

#>6
```

<br/>

Now we can use generator expressions,

```python
print( sum(  i for i in range(1,4) ))

#>6
```

Note that the above code is different from `print(sum([i for i in range(1,4)]))`, this is list comprehension

<br/>

```python
print(i for i in range(1,4))

#><generator object <genexpr> at 0x00000247187125E0>
```

```python
my_generator_obj = (i for i in range(1,4))
print(next(my_generator_obj))
#we can continuing iterating
#
#>1
```

<br/>

- "Use list compressions when time is important and generators when memory is important." https://stackoverflow.com/a/47792/4518341
- Refer https://peps.python.org/pep-0289/ for full details on generator expressions
