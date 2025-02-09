
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



