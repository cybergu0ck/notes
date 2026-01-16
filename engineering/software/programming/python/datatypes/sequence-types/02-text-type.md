# printing a float with specified number of digits after decimal point

```python
pi = 3.141592653
print(f'pi upto 3 decimal digits is {pi:.4}')

#>pi upto 3 decimal digits is 3.142
```

you can pass in both a field width and a precision. The format is {value:width.precision}. Let’s format pi (3.1415926) to two decimal places - we’ll set the width to 1 because we don’t need padding, and the precision to 3, giving us the one number to the left of the decimal and the two numbers to the right:

```python
print(f"Pi to two decimal places is {3.1415926:1.3}")

value = 3.1415926
width = 1
precision = 3
print(f"Pi to two decimal places is: {value:{width}.{precision}}")

value = 3.1415926
width = 10
precision = 3
print(f"Pi to two decimal places is: {value:{width}.{precision}}")

#>Pi to two decimal places is 3.14
#>Pi to two decimal places is: 3.14
#>Pi to two decimal places is:       3.14
```

<br/>

# string methods

## `title()` or `capitalize()` converts the first character of the string to upper case.

```python
word = 'john'
print(word.capitalize())

#>John
```

## `lower() `/ `upper()` converts the string to lower case or upper case respectively.

```python
word = 'HELLO'
lowerCaseWord = word.lower()
print(lowerCaseWord)

#>hello
```

## `islower()` / `isupper()` returns true if the string characters are in lower case or uppercase respectively.

```python
word = 'HeY'
print(word.isupper())

#>False
```

## `isalpha()` returns True if all characters in the string are in the alphabet

```python
print('hey Hello'.isalpha())

#>False
```

## `isdigit()` returns True if all characters in the string are digits

```python
print('333'.isdigit())

#>True
```

- `isnumeric()` is similar to `isdigit()`
- The main difference between both the functions is: The `isdigit()` method accepts only decimals, subscripts, and superscripts. The `isnumeric()` function supports Digits, Vulgar Fractions, Subscripts, Superscripts, Roman Numerals, and Currency Numerators.

## `lstrip()` removes any leading characters

- `lstrip()` by default removes any leading (left-hand side) whitespace characters from a string.
- It can have an optional parameter, which is basically a set of characters to remove as leading characters.
- `rstrip()` is similar.

```python
initial_message = '    Hey   Hello'
final_message = initial_message.lstrip()  #Removes all whitespaces at the begining
print(final_message)

#>Hey   Hello
```

```python
initial_message = '$$$Asap@Rocky'
final_message = initial_message.lstrip('$A')  #If $ or A is present in the starting left side, it removes it
print(final_message)

#>sap@Rocky
```

```python
initial_message = '$$$Asap@Rocky'
final_message = initial_message.lstrip('s')   #No change as 's' is not present in the leading left
print(final_message)

#>$$$Asap@Rocky
```

## `count()` method returns the number of times a specified value appears in the string

syntax:

```
string.count(value, start, end)
```

- value: Required. A String. The string to value to search for.

- start: Optional. An Integer. The position to start the search. Default is 0

- end : Optional. An Integer. The position to end the search. Default is the end of the string. (seems to be exclusive)

```python
word = 'Baad'
print(word.count('a'))

#>2

```

```python
word = '12341'
print(word.count('1',0,4 ))

#>1
```

## `endswith()` method returns True if the string ends with the specified value, otherwise False.

syntax:

```
string.endswith(value, start, end)
```

```python
txt = 'hey there how are you doing'
print(txt.endswith('how are you doing'))

#>True
```

```python
txt = 'Date : 24/12/2022'
txt.endswith('24',0,9)

#>True
```

## `find()` method finds the first occurrence of the specified value.

syntax :

```
string.find(value, start, end)
```

- The `find()` method returns -1 if the value is not found.
- The `find()` method is almost the same as the `index()` method, the only difference is that the `index()` method raises an exception if the value is not found.

```python
txt = "Hello, welcome to my world."
x = txt.find("e")
print(x)

#>1
```

<br>
<br>

## Character encoding

<br>
<br>

### `ord()`

ord() returns the ASCII value of the parameter

```python
ord('A')

#>65
```

<br/>
<br/>

### `chr()`

chr() returns the character for the given ASCII number

```python
chr(65)

#>'A'
```

<!-- TODO - Refactor this entire notes -->
