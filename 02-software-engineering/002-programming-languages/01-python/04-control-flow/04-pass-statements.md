The [`pass`](https://docs.python.org/3/reference/simple_stmts.html#pass) statement does nothing. It can be used when a statement is required syntactically but the program requires no action. For example:

This is commonly used for creating minimal classes:
```python
class MyEmptyClass:
    pass
```

Another place [`pass`](https://docs.python.org/3/reference/simple_stmts.html#pass) can be used is as a place-holder for a function or conditional body when you are working on new code, allowing you to keep thinking at a more abstract level. The `pass` is silently ignored:
```python
def initlog(*args):
    pass   # Remember to implement this!
```
