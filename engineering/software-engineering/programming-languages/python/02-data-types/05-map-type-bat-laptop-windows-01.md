# Python dict

- Dicts are mutable
- Dictionaries are used to store data values in key:value pairs
- Dictionaries cannot have duplicate keys and the keys must be immutable.
  - Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key.

## Creating Dictionaries

- Using {}

  ```python
  my_dict = {'Dave': '001', 'Ava' : '002', 'Joe': '003' }
  print(my_dict)

  #>{'Dave': '001', 'Ava': '002', 'Joe': '003'}
  ```

- The dict() constructor builds dictionaries directly from sequences of key-value pairs:

  ```python
  my_dict = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
  print(my_dict)

  #>{'sape': 4139, 'guido': 4127, 'jack': 4098}
  ```

- When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:

  ```python
  my_dict = dict(Dave = 100, Ava = 60)
  print(my_dict)

  #>{'Dave': 100, 'Ava': 60}
  ```

- dict comphrehensions can be used from arbitrary key-value pairs:

  ```python
  squares = {x:x*x for x in (1,2,3,4,5)}
  print(squares)

  #>{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
  ```

- Nested dictionaries (dictionaries containing dictionaries) can also be created

      ```python
      emp_details = {'Employee': {'Dave': {'ID': '001','Salary': 2000, 'Designation':'Python Developer'},
                                  'Ava': {'ID':'002','Salary': 2300,'Designation': 'Java Developer' },
                                  'Joe': {'ID': '003','Salary': 1843, 'Designation': 'Hadoop Developer'}}}

      print(emp_details)

      #> {'Employee': {'Dave': {'ID': '001', 'Salary': 2000,  'Designation': 'Python Developer'},
      #   'Ava': {'ID': '002', 'Salary': 2300, 'Designation': 'Java Developer'},
      #  'Joe': {'ID': '003', 'Salary': 1843, 'Designation': 'Hadoop Developer'}}}
      ```

  <br/>

# Inserting items

```python
my_dict={'Dave' : '001' , 'Ava': '002' , 'Joe': '003'}
my_dict['Jack'] = '007'
print(my_dict)

#>{'Dave': '001', 'Ava': '002', 'Joe': '003', 'Jack': '007'}
```

# Accessing Items, keys and values

1.  Accesing items in the dictionary

    ```python
    my_dict={'Dave' : '001' , 'Ava': '002' , 'Joe': '003'}
    print(type(my_dict.items()))
    print(my_dict.items())

    #><class 'dict_items'>
    #>dict_items([('Dave', '001'), ('Ava', '002'), ('Joe', '003')])
    ```

    Although it might look like `items()` gives us a `list` object, It is not the case and hence they can't be indexed, They are actually `dict_items` object. To be indexable, we can type cast them into list.

    ```python
    my_dict={'Dave' : '001' , 'Ava': '002' , 'Joe': '003'}
    list(my_dict.items())[0]

    #>('Dave', '001')
    ```

2.  Accesing keys in the dictionary

    ```python
    my_dict={'Dave' : '001' , 'Ava': '002' , 'Joe': '003'}
    print(type(my_dict.keys()))
    print(my_dict.keys())

    #><class 'dict_keys'>
    #>dict_keys(['Dave', 'Ava', 'Joe'])
    ```

3.  Accesing values

        ```python
        # Accesing all the values
        my_dict={'Dave' : '001' , 'Ava': '002' , 'Joe': '003'}
        print(type(my_dict.values()))
        print(my_dict.values())

        #> <class 'dict_values'>
        #> dict_values(['001', '002', '003'])
        ```

        ```python
        # Accesing specific value using a key
        my_dict={'Dave' : '001' , 'Ava': '002' , 'Joe': '003'}
        someValue = my_dict['Dave']
        print(someValue)

        #>'001'
        ```

        ```python
        # Accesing specific value using get() method
        my_dict={'Dave' : '001' , 'Ava': '002' , 'Joe': '003'}
        my_dict.get('Dave')

        #>'001'
        ```

    <br/>

# Deleting items from a dictionary

items can be deleted using `del()`, `pop()`, `popitem()`, `clear()`

```python
my_dict={'Dave': '004', 'Ava': '002', 'Joe': '003', 'Chris': '005'}
del my_dict['Dave']  #removes key-value pair of 'Dave'
my_dict.pop('Ava')   #removes the value of 'Ava'
my_dict.popitem()    #removes the last inserted item
print(my_dict)

#>{'Joe':'003'}
```

<br/>

# Sorting dicts

1. Sorting dicts by keys

   ```python
   newdict = {'a':1000, 'z':26, 't':500, 'y':25}
   newdict = dict(sorted(newdict.items()))
   print(newdict)

   #> {'a':1000, 't':500, 'y':25, 'z':26}
   ```

2. Sorting dicts by values

   ```python
   newdict = {'a':1000, 'z':26, 't':500, 'y':25}
   newdict = dict(sorted(newdict.items(),key = lambda items: items[1]))
   print(newdict)

   #>{'y': 25, 'z': 26, 't': 500, 'a': 1000}
   ```

### Difference between sorted() and sort()

- sorted() is a function and it expects parameters to be passed to it. It creates a new object and must be stored in a variable.
- sort() is a method and has to be called by an object. It is called in-place.

<br/>

# Default Dict

- Must be imported from the collections package.
- A defaultdict works exactly like a normal dict, but it is initialized with a function (“default factory”) that takes no arguments and provides the default value for a nonexistent key. A defaultdict will never raise a KeyError. Any key that does not exist gets the value returned by the default factory.

Say we want to prepare a dictonary that gives the frequency of items of a list.

```python
my_list = [100,60,100,99,100]
freq_dict = {}

for item in my_list:
    if item not in freq_dict :
        freq_dict[item] = 1
    else:
        freq_dict[item] +=1

print(freq_dict)

#>{100: 3, 60: 1, 99: 1}
```

Instead we can simplify the above code by using `defaultdict()` :

```python
from collections import defaultdict

my_list = [100,60,100,99,100]
freq_dict = defaultdict(int)

for item in my_list:
    freq_dict[item] += 1

print(freq_dict)

#>defaultdict(<class 'int'>, {100: 3, 60: 1, 99: 1})
```

- We can pass a lambda function inside `defaultdict()`

  ```python
  from collections import defaultdict

  myList = [1,1,2,4]

  myDict = defaultdict(lambda:2)   #Now the default value will be 2

  for i in myList:
      myDict[i] += 1

  print(myDict)

  #Observe the output, frequency values are incremented by 2 because the default was set as 2.

  #>defaultdict(<function __main__.<lambda>()>, {1: 4, 2: 3, 4: 3})
  ```

- We can make a defaultdict(list) too!

  ```python
  from collections import defaultdict

  spoken_language = [('Annie', 'German'), ('Dan', 'English'), ('Annie', 'English'), ('Gwen', 'Spanish'), ('Gwen','Kannada')]

  result = defaultdict(list)

  for item in spoken_language:
      result[item[0]].append(item[1])

  print(result)

  #>defaultdict(<class 'list'>, {'Annie': ['German', 'English'], 'Dan': ['English'], 'Gwen': ['Spanish', 'Kannada']})
  ```

# Dict methods

## `setdefault()`

---

If the key is present in the dict, then setdefault() will return the value of that key, if not present it will return the default value (if provided) else returns None.

```python
myDict = {'a':1000, 'z':26}

isPresent = myDict.setdefault('a')
print(isPresent)

#>1000
```

```python
myDict = {'a':1000, 'z':26}

isPresent = myDict.setdefault('x', 69)
print(isPresent)

#>69
```

```python
myDict = {'a':1000, 'z':26}

isPresent = myDict.setdefault('y')
print(isPresent)

#>None
```
