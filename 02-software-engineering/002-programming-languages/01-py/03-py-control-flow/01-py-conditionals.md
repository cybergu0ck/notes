# If Else-If Else 


```python
x = int(input("Please enter an integer: "))
if x<0 :
	print("number is negative")
elif x==0:
	print('x is zero')
elif x == 1:
	print('x is one')
else:
	print('x is more')
```
<br>

## One liner
---

```python
num = 10
is_even = True if num%2 ==0 else False
print(is_even)

#>True
```

<br>
<br>

# pass statements

* The [`pass`](https://docs.python.org/3/reference/simple_stmts.html#pass) statement does nothing. It can be used when a statement is required syntactically but the program requires no action.

	```py
	num = 10

	if num:
		pass
	else:
		print("entered else block")
	
	#>
	```
<br>
<br>


# Switch case statements

> Add notes