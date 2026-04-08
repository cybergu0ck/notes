# Stacks

A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner.

<br>
<br>

## Implementation

- Stacks can be implemented using lists.

  ```py
  stack = []

  stack.append(1)
  stack.append(2)
  stack.append(3)
  print(f'stack before popping :{stack}')

  stack.pop()  # ONLY pop() must be used!

  print(f'stack after popping :{stack}')

  #>stack before popping :[1, 2, 3]
  #>stack after popping :[1, 2]
  ```

* Stack can be implemented using `collections.deque` (deque is pronounced as 'deck'!)

  ```py
  from collections import deque

  stack = deque()
  stack.append(100)
  stack.append(200)
  stack.append(300)

  print(f'stack before popping :{stack}')

  stack.pop()

  print(f'stack after popping :{stack}')

  #>Queue before popping :deque([100, 200, 300])
  #>Queue after popping :deque([100, 200])
  ```

<br>
<br>