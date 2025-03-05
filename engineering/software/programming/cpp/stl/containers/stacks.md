# Stacks

A std::stack is a container adapter that provides stack functionality.

- It's not a fundamental container like std::vector or std::list; rather, it wraps an existing container to provide a specific interface.

- a stack is a fundamental data structure that follows the Last-In-First-Out (LIFO) principle. This means that the last element added to the stack is the first one to be removed.

<br>
<br>
<br>

## Initialisation

- Different kinds of initialisation :

```cpp
#include <stack>

//default initialisation
std::stack<int> stack1;

//Initialization with a Container (Vector, Deque, List)
std::vector<int> myVector = {1, 2, 3, 4, 5};
std::stack<int, std::vector<int>> stack2(myVector); // Initialize with a vector
std::deque<int> myDeque = {6, 7, 8};
std::stack<int, std::deque<int>> stack3(myDeque); // Initialize with a deque
std::list<int> myList = {9, 10};
std::stack<int, std::list<int>> stack4(myList); //Initialize with a list


//uniform initialisation is NOT supported!
std::stack <int> test_score{98,88,60,30};
std::stack <char> vowels = {'a','e', 'i','o','u'}; //using an initaliser list
```

- Note that stacks cannot be initialised using initialiser list or braces initialisation!

<br>
<br>
<br>

## Methods

<br>
<br>

### Access

1. `T& top();`

   - Returns a non-constant reference to the top element of the stack.
   - Has $O(1)$ time complexity.

<br>
<br>

### Search

<br>
<br>

### Insertion

1. `void push(const T& value);`

   - Insert value at the top of the stack.
   - Has amortised $O(1)$ time complexity, average is $O(1)$ and is $O(n)$ in case of relocation.

<br>
<br>

### Deletion

1. `void pop();`

   - Removes the top element from the stack.
   - Has $O(1)$ time complexity.

<br>
<br>

### Modification

<br>
<br>

### Miscallaneous

1. `bool empty() const;`

   - Returns true if the stack is empty.
   - Has $O(1)$ time complexity.

<br>
<br>
