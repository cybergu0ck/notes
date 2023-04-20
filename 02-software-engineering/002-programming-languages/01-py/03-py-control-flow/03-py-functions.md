# Function definiton and call

```py
#function definiton
def foo(para1, para2):
    #code

#function call
foo('some', 'thing')
```

* Here *para1* and *para2* are parameters defined in the function definition.
* 'some' and 'thing' are arguments that we pass in the function call.
* It is important to pass exactly the right number of arguments that the function needs.

<br>
<br>

# Simplified version of how python treats variables and parameters

![image](../_assets/passByRefpassByVal.png)

* It doesn't matter if A is mutable or not. If you assign something different to B, _A doesn't change_. example: 

    ```py
    def makeItEasy(numbers):
        numbers = [100,200,300]  #Assignment, Hence the original variable won't change

    my_numbers = [1,2,3]
    makeItEasy(my_numbers)

    print(my_numbers)

    #>[1,2,3]
    ```

* If B is modified in-place, then *A will change*, example:
    ```py
    def makeItEasy(numbers):
        numbers.extend([100,200,300])  #In-place modification, Hence the original variable will change

    my_numbers = [1,2,3]
    makeItEasy(my_numbers)

    print(my_numbers)

    #>[1, 2, 3, 100, 200, 300]
    ```

* Assignment using subscription is considered as in-place modification.

    ```py
    def makeItEasy(numbers):
        numbers[0] = 100  #In-place modification, Hence the original variable will change
        numbers[1] = 200
        numbers[2] = 300

    my_numbers = [1,2,3]
    makeItEasy(my_numbers)

    print(my_numbers)

    #>[100, 200, 300]
    ```
*  Refer this for more information [python - How do I pass a variable by reference? - Stack Overflow](https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference)  
* Refer [Martijn Pieters's comment in Zenadix's answer in this url](https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference)

<br>
<br>

# Parameters

Remember! Parameters show up in function definiton.

<br>

## Default parameters

* default values are considered if arguments are not passed for that parameter.
    ```python
    def greet(name, msg="Good morning!"):
        print("Hello", name + ', ' + msg)

    greet("Kate")
    greet("Bruce", "How do you do?")

    #>Hello Kate, Good morning! 
    #>Hello Bruce, How do you do?
    ```

* The default values are evaluated at the point of function definition in the _defining_ scope, so that
    ```python
    i = 5

    def f(arg=i):
        print(arg)

    i = 6
    f()

    #> 5
    ```

* The default value is evaluated only once. This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes. For example, the following function accumulates the arguments passed to it on subsequent calls:

    ```python
    def f(a, L=[]):
        L.append(a)
        return L

    print(f(1))
    print(f(2))
    print(f(3))

    #>[1]
    #>[1, 2]
    #>[1, 2, 3]
    ```

<br>
<br>

# Arguments 

* Remember! arguments appear in function call.
* arguments are of 3 types: positional, keyword and arbitrary.

<br>

## 1. Positional Arguments

* When the things (objects) themselves are passed as arguments, they are positional arguments.
* Order matters as parameter are considered based on the posi

    ```py
    def printName(firstName, lastName):
        print(firstName + lastName)

    printName('John', 'Dough')

    #>John Dough
    ```
<br>

## 2. Keyword Arguments

* When arguments are passed in the form of `key = value`, those are keyword arguments.

    ```python
    def greet(name, msg):
        print (f'Hello, {name} says {msg}')

    greet(msg = 'Get outta here', name = 'Ryan') #Order doesn't matter

    #>Hello, Ryan says Get outta here
    ```
* We can mix positional arguments with keyword arguments during a function call. ___In a function call, keyword arguments must follow positional arguments.___


    ```python
    def greet(name, msg, department):
        print (f'Hello, {name} from {department} says {msg}')

    greet("Bob", department= 'Systems', msg = "It's working") #Positional Arguments first, Then comes the keyword arguments!

    #This should be kept in mind while creating the function definition, order the parameters such that keyword arguments come last. See next code

    #>Hello, Bob from Systems says It's working
    ```

<br>

## Convention

* The following convention must be followed for readability and clean code.


    ```
    def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
        -----------    ----------     ----------
            |             |                  |
            |        Positional or keyword   |
            |                                - Keyword only
            -- Positional only
    ```

    ```python
    def func(pos1, pos2,/,pos_or_key,*,kwd1, kwd2):
        pass

    func(1,2,pos_or_key=2,kwd1=1,kwd2=10) # or func(1,2,2,kwd=1,kwd=10)
    ```

>As guidance:
>
>* Use positional-only if you want the name of the parameters to not be available to the user. This is useful when parameter names have no real meaning, if you want to enforce the order of the arguments when the function is called or if you need to take some positional parameters and arbitrary keywords.
>
>* Use keyword-only when names have meaning and the function definition is more understandable by being explicit with names or you want to prevent users relying on the position of the argument being passed.
>
>* For an API, use positional-only to prevent breaking API changes if the parameter’s name is modified in the future.

<br>
<br>

## 3. Arbitrary Argument Lists (\*args  and \**kwargs)

<br>

## \*args

* __\*args__ are arbitrary number of non-keyword arguments (positional)
* Note that args in not a keyword hence any valid identifier can be used in its place.

    ```python
    def adder(*args):
        sum = 0
        for n in args:
            sum = sum + n
        print("Sum:",sum)

    adder(3,5)
    adder(4,5,6,7)
    adder(1,2,3,5,6)

    #>Sum: 8  
    #>Sum: 22
    #>Sum: 17
    ```

* \*args are taken as Tuple in python
    ```python
    def foo(*args):
        print("\nData type of argument:",type(args))
        print(args)

    foo(1,2,3,100)

    #>Data type of argument: <class 'tuple'> 
    #>(1, 2, 3, 100)
    ```

* Passing \*\*args from one function/Class to another (same applies to [[#* *kwargs]])
    ```python
    class Demo:
        def __init__(self):
            pass

        def foo(self, **kwds):
            print(kwds)
            temp = Sub(**kwds)    # the keyword arg's are being passed as parameter for another class
            self.bla(**kwds)    #the keyword arg's are passed as parameters for another function

        def bla(self, **new):
            print(new)

    class Sub:
        def __init__(self, **kwds):
            print(kwds)

    obj = Demo()
    obj.foo(key1 = 1, key2 = 2)

    #>{'key1': 1, 'key2': 2} 
    #>{'key1': 1, 'key2': 2} 
    #>{'key1': 1, 'key2': 2}
    ```

<br>

## \*\*kwargs

* \*\*kwargs are arbitary number of keyword arguments.
* Note that kwargs in not a keyword hence any valid identifier can be used in its place.

    ```python
    def intro(**data):
        for key, value in data.items():
            print("{} is {}".format(key,value))

    intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)


    #> Firstname is Sita 
    #> Lastname is Sharma 
    #> Age is 22 
    #> Phone is 1234567890
    ```

* \*\*kwargs are taken as Dictionaries in pyhton
    ```python
    def foo(**kwargs):
        print("\nData type of argument:",type(kwargs))
        print(kwargs)

    foo(key1 = 1, key2 = 100, key3 = 18)

    #>Data type of argument: <class 'dict'> 
    #>{'key1': 1, 'key2': 100, 'key3': 18}
    ```

<br>
<br>

# Scope

* Check for a markdown in 01-py-basics file.

<br>
<br>

# Lambda Expressions

* Small anonymous functions can be created with the [`lambda`](https://docs.python.org/3/reference/expressions.html#lambda) keyword.
* They are syntactically restricted to a single expression.
* Lambda functions can be used wherever function objects are required.
* Like nested function definitions, lambda functions can reference variables from the containing scope.

* The syntax of lambda expressions are
    ```
    lambda arguments : expression
    ```
* Illustration :
    ```python
    # Traditional approach

    def get_longer(collection1, collection2):
        if len(collection1) > len(collection2):
            return collection1
        else:
            return collection2

    print(get_longer([1,2],[1,2,3,4]))

    #>[1,2,3,4]
    ```

    ```python
    #Using lambdas
    get_longer = lambda collection1, collention2: collection1 if len(collection1) > len(collention2) else collention2
    print(get_longer([1,2],[1,2,3,4]))

    #>[1,2,3,4]
    ```
* Another example:

    ```python
    pairs = [(2, 'two'), (3, 'three'),(1, 'one'),  (4, 'four')]
    pairs.sort(key = lambda pair:pair[0])
    print(pairs)

    #>[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
    ```

<br>
<br>


# Functions using match statements


```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

            
print(http_error(400))

#>Bad request
```

<br>
<br>



# Docstrings

Here are some conventions about the content and formatting of documentation strings.

* This line should begin with a capital letter and end with a period.
* If there are more lines in the documentation string, the second line should be blank, visually separating the summary from the rest of the description. The following lines should be one or more paragraphs describing the object’s calling conventions, its side effects, etc.
* the first line is generally adjacent to the string’s opening quotes

    ```python
    def my_function():
        """Do nothing, but document it.
        No, really, it doesn't do anything.
        """
        pass

    print(my_function.__doc__)


    > Do nothing, but document it.
        No, really, it doesn't do anything.
    ```

Observe the indentation in the output, to know how it works checkout [4. More Control Flow Tools — Python 3.11.1 documentation](https://docs.python.org/3/tutorial/controlflow.html#documentation-strings)

<br>
<br>

# Function Annotations

- [Function annotations](https://docs.python.org/3/reference/compound_stmts.html#function) are completely optional metadata information about the types used by user-defined functions (see [**PEP 3107**](https://peps.python.org/pep-3107/) and [**PEP 484**](https://peps.python.org/pep-0484/) for more information).
	
-  [Annotations](https://docs.python.org/3/glossary.html#term-function-annotation) are stored in the `__annotations__` attribute of the function as a dictionary and have no effect on any other part of the function.

    ```python
    def is_present(nums:list[int], target:int) -> bool :
        """Return True if target present in nums."""

        if target in nums:
            return True
        else:
            return False

    print(is_present([1,2,3],0))

    #>False
    ``` 