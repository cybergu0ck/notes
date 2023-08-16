# STL Stack

- stacks is a "last in first out" data structure.
- It is an adaptor class and hence we can choose what underlying container we want to use for the stack (vector, list, deque)

  ```cpp
  #include <iostream>
  #include <stack>
  #include <vector>
  #include <deque>

  int main() {
      std::stack <int, std::vector<int>> my_stack;	//using vector
      //std::stack <int, std::list<int>> my_stack;	//using list
      //std::stack <int, std::deque<int>> my_stack;	//using deque
      //std::stack <int> my_stack;  //uses deque by default

      my_stack.push(10);
      my_stack.push(10);
      std::cout << my_stack.size() << std::endl;	//2
  }
  ```

<br>
<br>
<br>

# Useful Functions

## push()

- Used to insert elements to the stack.

  ```cpp
  #include <iostream>
  #include <stack>

  int main() {
      std::stack <int> my_stack;
      my_stack.push(10);
      my_stack.push(20);
      my_stack.pop();
      std::cout << my_stack.size() << std::endl;	//1
      my_stack.push(25);
      std::cout << my_stack.size() << std::endl;	//2
  }
  ```

<br>
<br>

## pop()

- Remove the top most element in the stack.

<br>
<br>

## top()

- Returns the reference to the top most element in the stack.

<br>
<br>

## size()

- Returns the number of elements of the stack.

<br>
<br>

## empty()

- Returns true if the stack is empty else returns false.
