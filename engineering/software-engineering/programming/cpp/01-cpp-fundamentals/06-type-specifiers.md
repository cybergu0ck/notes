# Type Specifiers

<br>
<br>

## Type Alias

*A type alias is a name that is a synonym for another type.*

```cpp
#include <iostream>
#include <vector>

typedef std::vector<std::string> strings;   //Old standard using typedef
using strings = std::vector<std::string>;   //Modern standard using alias declaration

int main()
{
	strings names{ "James", "Bond" };
	for (auto name : names)
	{
		std::cout << name << "\t";
	}
}

//James Bond
```
- When using type alias with pointers and const. Note the non-intuitive interpretation.

    ```cpp
    using ptr_num = int *;	//typedef int* ptr_num;

    const ptr_num huge; 
    const int* huge; //pointer to a constant int   //Wrong Interpretation
    int* const huge; //constant pointer to an int  //Right Interpretation

    const ptr_num *huge_ptr;
    const int* *huge; //pointer to a pointer to a constant int      //Wrong Interpretation
    int* const *huge; //pointer to a constant pointer to an int     //Right Interpretation
    ```




    ```cpp  
    #include <iostream>

    using ptr_num = int *;	//typedef int* ptr_num;

    int main()
    {
        int num{ 1000 };
        int another{ 70 };
        const ptr_num huge = &num; //huge is a constant pointerand not a pointer to a const int 
        huge = &another;	//Error
    }
    ```

<br>
<br>

## Auto Type Specifier


*`auto` type secifier lets the compiler deduce the type of the variable from it's initialiser.*

- By Implication, the variable with type auto must have an initialiser.

<br>
<br>

## Decltype Type Specifier