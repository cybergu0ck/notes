A function is a block of code with a name.

```cpp
int fact(int val){
    int res = 1;
    while (val >1){
        res *= val--;
    }
    return res;
}
```

The above function computes the factorial of a given number, Our function is named _fact_. It takes _one int parameter_ and _returns an int value._

#### Calling the function

```cpp
int main(){
    int factorial = fact(5);
    cout << "The factorial of 5 is " << factorial <<endl;
    
    return 0;
}
```


<br/>

#### Arguments and parameters

Arguments are the initializers for a function’s parameters.

<br/>

#### Function Parameter List

- A parameter list typically consists of a comma-separated list of parameters, each of which looks like a declaration with a single declarator. Even when the types of two parameters are the same, the type must be repeated:
	```cpp
	int f3(int v1, v2) { /* ... */ } // error
	int f4(int v1, int v2) { /* ... */ } // ok
	```

- Parameter names are optional. However, there is no way to use an unnamed parameter. Therefore, parameters ordinarily have names.


## Local Objects

In C++, names have scopes and objects have lifetimes.

- ___The scope of a name is the part of the program’s text in which that name is visible.___
- ___The lifetime of an object is the time during the program’s execution that the object exists.___

Objects defined outside any function exist throughout the program’s execution. Such objects are created when the program starts and are not destroyed until the program ends. The lifetime of a local variable depends on how it is defined.

<br/>

### Automatic Objects

- Objects that exist only while a block is executing are known as automatic objects
- After execution exits a block, the value of the automatic objects created in that block are undefined.
- Parameters are automatic objects.

<br/>

### Local `static` Objects

- It can be useful to have a local variable whose lifetime continues across calls to the function. 
- We obtain such objects by defining a local variable as `static`. 
- Each local static object is initialized before the first time execution passes through the object’s definition.
- Local statics are not destroyed when a function ends; they are destroyed when the program terminates.

```cpp
#include <iostream>
using namespace std;

int print_for(){
    static int num =0;   //Here the local object num is not destroyed after the end of fucntion call.
    return ++num; 
}

int main(){
    for (int i =0; i != 10; i++){
        cout << print_for() <<endl;
    }
    
    return 0;
}
```

- If a local static has no explicit initializer, it is value initialized (§ 3.3.1, p. 98), meaning that local statics of built-in type are initialized to zero.


## Function Declarations

- Like any other name, the name of a function must be declared before we can use it.
- As with variables, a function may be defined only once but may be declared multiple times. (with one exception)
- A function declaration is just like a function definition except that a declaration has no function body. In a declaration, a semicolon replaces the function body
- Because a function declaration has no body, there is no need for parameter names. Hence, parameter names are often omitted in a declaration.
- Function declarations are also known as the __function prototype__.

```
return_type   function_name  parameter_list ;
```

```cpp
void print(vector::const_iterator beg, vector::const_iterator end);
```

<br/>

### Function Declarations Go in Header Files

Recall that variables are declared in header files and defined in source files. For the same reasons, functions should be declared in header files and defined in source files.


## Missing notes (refer 6.1.3 of textbook)

<br/>
<br/>

# Argument Passing

If the parameter is a reference, then the parameter is bound to its argument. Otherwise, the argument’s value is copied.

- When a parameter is a reference, we say that its corresponding argument is __“passed by reference”__ or that the function is __“called by reference.”__ As with any other reference, a reference parameter is an alias for the object to which it is bound; that is, the parameter is an alias for its corresponding argument.

- When the argument value is copied, the parameter and argument are independent objects. We say such arguments are __“passed by value”__ or alternatively that the function is __“called by value.”__'

<br/>

## 6.2.1 Passing Arguments by Value

Here, nothing the function does to the parameter can affect the argument. 

In the above example code for the function printing factorial, Although fact changes the value of the parameter `val`, that change has no effect on the argument passed to `fact`. Calling `fact(i)` doesn't change the value of `i`.


<br/>

### Pointer Parameters

When we copy a pointer, the value of the pointer is copied. After the copy, the two pointers are distinct. However, a pointer also gives us indirect access to the object to which that pointer points. We can change the value of that object by assigning through the pointer.

```cpp
int n=0, i=41;  
int *p = &n , *q = &i; // p points to n; q points to i
*p = 42;               // value in n is changed; p is unchanged
p = q;                 // value in n is changed; p is unchanged
```

The same behavior applies to pointer parameters:

```cpp
void reset(int *ip){
	*ip =50;  // changes the value of the object to which ip points
	ip =0;   // changes only the local copy of ip; the argument is unchanged
}
```
After a call to reset, the object to which the argument points will be 50, but the pointer argument itself is unchanged:

```cpp
int main(){
    int num = 100;
    int *num_ptr = &num;
    reset(num_ptr);
    cout << num << endl;
    return 0;
}

//>50
```

<br/>

## 6.2.2 Passing Arguments by Reference

Recall that operations on a reference are actually operations on the object to which the reference refers

```cpp
int n=0, i =42;
int &r = n;  // r is bound to n (i.e., r is another name for n)
r =42;       // n is now 42
r = i;       // n now has the same value as i (n = 42)
i =r;        // i has the same value as n (i = 42)
```

Reference parameters exploit this behavior. They are often used to allow a function to change the value of one or more of its arguments.

```cpp
void reset(int &i){   // i is just another name for the object passed to reset
	i = 50;           // changes the value of the object to which i refers

int main(){
    int n=100;
    reset(n);        //See here that the argument doesn't need to be a reference!
    cout << n <<endl; 
    return 0;
}

//> 50
```

<br/>

### Using References to Avoid Copies

It can be inefficient to copy objects of large class types or large containers. Moreover, some class types (including the IO types) cannot be copied. Functions must use reference parameters to operate on objects of a type that cannot be copied.

- For instance, lets say we want to write a function to compare the length of two strings. copying long strings is inefficient, hence we use parameter reference. further as comparing strings don't involve change, we use `const` reference.
```cpp
bool compare( const string &s1, const string &s2){
    return s1.size() > s2.size();
}

int main(){
    string my_name = "HITASHI";
    string your_name = "TRUMP";
    bool is_longer = compare(my_name, your_name);
    cout << is_longer  <<endl;
    return 0;
}

//> 1         //Here 1 means True!
```

> Reference parameters that are not changed inside a function should be references to const.


### Using Reference Parameters to Return Additional Information

Notes not made for this. Refer textbook

<br/>

## 6.2.3 `const` Parameters and Arguments

Notes not made for this. Refer textbook

<br/>

## 6.2.4 Array Parameters

Arrays have two special properties that affect how we define and use functions that operate on arrays: 
- We cannot copy an array, Hence we cannot pass an array by value.
- when we use an array it is (usually) converted to a pointer , Therefore when we pass an array to a function, we are actually passing a pointer to the array’s first element.

Even though we cannot pass an array by value, we can write a parameter that looks like an array:
```cpp
// despite appearances, these three declarations of print are equivalent
// each function has a single parameter of type const int*
void print(const int*);
void print(const int[]);   // shows the intent that the function takes an array
void print(const int[10]); // dimension for documentation purposes (at best)
```

```cpp
void foo(int *p){         //foo(int *p) :: foo(int p[]) :: foo(int p[2])
    cout << *p <<endl;
    
}
int main(){
    int arr[2] = {169,2};
    foo(arr);            //We are actually passing the pointer which points to the first element of the array and not the entire array
    return 0;
}

//>169
```

However the below code has error and i do-not know why exactly,
```cpp
void foo(int *p){
    cout << *p <<endl;
    
}
int main(){
    int arr[2] = {169,2};
    foo(&arr);         //Error Here 
    return 0;
}

//cannot convert 'int (*)[2]' to 'int*' for argument '1' to 'void foo(int*)'
```

<br/>

Because arrays are passed as pointers, functions ordinarily don’t know the size of the array they are given. They must rely on additional information provided by the caller. There are three common techniques used to manage pointer parameters.

### Using a Marker to Specify the Extent of an Array

Something about C-style characters, refer the textbook.

<br/>

### Using the Standard Library Conventions

A second technique used to manage array arguments is to pass pointers to the first and one past the last element in the array.

```cpp
void print(const int *beg, const int *end){
	while (beg != end)
		cout << *beg++ << " ";
}

int main(){
    int arr[5] = {1,2,3,4,5};
    print(begin(arr), end(arr));   //begin() and end() are functions.
    return 0;
}

//>1 2 3 4 5
```

<br/>

### Explicitly Passing a Size Parameter
A third approach for array arguments, which is common in C programs and older C++ programs, is to define a second parameter that indicates the size of the array.