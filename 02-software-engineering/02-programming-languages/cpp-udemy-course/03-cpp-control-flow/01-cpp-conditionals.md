# if statement

```cpp
if (expr){
    //code
}
```

- variables inside if block has block level scope and is accessible only inside that block.

  ```cpp
  int main()
  {
      if (true) {
          int num { 10 };
      }
      cout << num; //error
      return 0;
  }
  ```

  <br>
  <br>

# if else construct

```cpp
if (expr){
    //code
}
else {
    //code
}
```

<br>
<br>

# if - else if - else contruct

```cpp

if (expr){
    //code
}
else if (expr){
    //code
}
else{
    //code here is executed if none of the above blocks are executed.
}
```
