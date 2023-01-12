
## Pass by Reference and Pass by value in Python
---
The problem comes from a misunderstanding of what variables are in Python. If you're used to most traditional languages, you have a mental model of what happens in the following sequence:

```python
a = 1
a = 2
```

- You believe that `a` is a memory location that stores the value `1`, then is updated to store the value `2`. That's not how things work in Python. Rather, `a` starts as a reference to an object with the value `1`, then gets reassigned as a reference to an object with the value `2`. Those two objects may continue to coexist even though `a` doesn't refer to the first one anymore; in fact they may be shared by any number of other references within the program. 
- When you call a function with a parameter, a new reference is created that refers to the object passed in. This is separate from the reference that was used in the function call, so there's no way to update that reference and make it refer to a new object.

> use built in function ___id()___ which gives the identity of the object.


```kotlin
a = 1
print(id(a))

a = 2
print(id(a))

/*Output :
2481719961904 
2481719961936
*/
```
In the above code we see that id's are different which means they are referring to different objects.

```kotlin
a = 1
print(id(a))

b = 1
print(id(b))

/*Output :
2481719961904 
2481719961904
*/
```
In the above code we see that even if the variables are different, they are actually referring to the same object.


Refer this for more information [python - How do I pass a variable by reference? - Stack Overflow](https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference)



Remember this simplified version on how the way Python treats variables and parameters.
![[Pasted image 20230112211817.png]]


```kotlin
def passBy(data):
    data = 1000
    print("value of data inside the function scope: ", data)

data = 1
print("value of data initially: ", data)

passBy(data)
print("value of data finally: ", data)

/*
Output:
value of data initially: 1 
value of data inside the function scope: 1000 
value of data finally: 1

*/
```

```kotlin
def passBy(data):
    data = [1000]
    print("value of data inside the function scope: ", data)

data = [1]
print("value of data initially: ", data)

passBy(data)
print("value of data finally: ", data)


/*
Output:
value of data initially: [1] 
value of data inside the function scope: [1000] 
value of data finally: [1]

*/
```

```kotlin
def passBy(data):
    data.append(1000)    #Inplace
    print("value of data inside the function scope: ", data)

data = [1]
print("value of data initially: ", data)

passBy(data)
print("value of data finally: ", data)

/*
Output:
value of data initially: [1] 
value of data inside the function scope: [1, 1000] 
value of data finally: [1, 1000]

*/

```

