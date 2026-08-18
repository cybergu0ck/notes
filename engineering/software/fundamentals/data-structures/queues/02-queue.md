# Queue

Queue follows the First In First Out (FIFO) rule - the item that goes in first is the item that comes out first.

<br>
<br>

## Implementation

- Queues can be implemented using lists

  ```py
  queue = []

  queue.append(1)
  queue.append(2)
  queue.append(3)
  print(f'Queue before popping :{queue}')

  queue.pop(0)  # ONLY pop(0) must be used!

  print(f'Queue after popping :{queue}')

  #>Queue before popping :[1, 2, 3]
  #>Queue after popping :[2, 3]
  ```

* Queues can be implemented using `collections.deque` using `append()` and `popleft()`.

  ```py
  from collections import deque

  queue = deque()
  queue.append(100)
  queue.append(200)
  queue.append(300)

  print(f'Queue before popping :{queue}')

  queue.popleft()

  print(f'Queue after popping :{queue}')

  #>Queue before popping :deque([100, 200, 300])
  #>Queue after popping :deque([200, 300])
  ```

<br>
<br>