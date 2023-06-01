# References

* A reference in C++ is a special type of variable that cannot be assigned a new value. It can only refer to an existing object. 
* References are declared using the & symbol.
* Reference cannot be null.


<br>
<br>

# References as Alias

* Reference can an alias for a variable.
    ```cpp
    int main()
    {
        int num{ 10 };
        int& my_num{ num };
        my_num = 100;
        cout << num << endl;  //100
    }
    ```

<br>
<br>

# Reference to avoid copying objects

* References are typically used to avoid copying objects. For example, if you have a function that takes an object as a parameter, you can use a reference to avoid copying the object. This can improve performance, especially if the object is large.
* In a range based for loop, the variable is a copy of the orginal iterable, hence we get the following reult: 

    ```cpp
    int main()
    {
        vector<string> stooges{ "larry", "moe","curly" };

        for (auto name : stooges) {
            name = "funny";
        }

        for (auto name : stooges) {
            cout << name << endl;
        }
    }

    //larry 
    //moe
    //curly
    ```
* When we use references (see inside range based for loop)

    ```cpp
    int main()
    {
        vector<string> stooges{ "larry", "moe","curly" };

        for (auto &name : stooges) {
            name = "funny";
        }

        for (auto name : stooges) {
            cout << name << endl;
        }
    }
    //funny
    //funny
    //funny
    ```

<br>
<br>

# l-value 

* An l-value is an object that occupies location in memory and is addressable.
* objects are addressable when they can be used on the left hand side of an assignment statement.

    ```cpp
    int main()
    {
        int num;
        num = 100; //num is a lvalue
    }
    ```

<br>
<br>

# r-value

* Anything that is not an lvalue is an rvalue, hence rvalues are non addressable and non assignable.
* Usually,
    * rvalues are on the right hand side of the assignment
    * literals are rvalues
    * ravlues can be temporary (inteneded to be non modifiable)

* rvalues can be assigned to lvalues explicitely

    ```cpp
    int main()
    {
        int x{ 1 }, y{ 0 };
        y = 100; // r-value 100 is assigned to l-value y
        x = x + y;  // r-value (x+y) is assigned to l-value x; here r-value is a temporary that is non-modifiable!
    }
    ```

<br>
<br>

# references as l-value

* Initial value of a reference must be an lvalue.
    ```cpp
    int main()
    {
        int x;
        int& ref1 = x;      //ok: ref1 is a reference of an lvalue (x)
        int& ref2 = 100;    //error: 100 is an rvalue
    }
    ```
* The same concept applies to functions with references

    ```cpp
    void foo(int& num);

    int main()
    {
        int x;
        foo(x);		//ok
        foo(10);	//error: 100 is a rvalue	 
    }

    void foo(int& num) {
        cout << "does nothing" << endl;
    }
    ```