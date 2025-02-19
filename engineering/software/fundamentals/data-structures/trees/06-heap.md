# Heap

_Heap is an array based datasructure visualised as a [complete binary tree](./trees/binary-tree.md#complete-binary-tree) in which the parent nodes have values greater or lesser than the values of the children, based on wether it is max or min heap respectively._

- As heaps are binary trees (specifically complete binary tree), the positions of the children given the root's position are same as that of [binary trees](02-binary-tree.md#indices-when-represented-as-an-array)

<br/>
<br/>

## Max Heap

_Max Heap an array based datasructure visualised as a [complete binary tree](./trees/binary-tree.md#complete-binary-tree) in which the value of each node is greater than or equal to the values of its children._

- In a max heap, the value of the root node is the largest among all nodes in the heap.
- Max heaps are often used to implement priority queues, where the element with the highest priority (i.e., the largest key) is always at the front of the queue and can be efficiently accessed and removed.

- Example :

  ```
            20
          /    \
        18      12
       / \     /  \
      9   7   5    4

  ```

<br>
<br>

## Min Heap

A min heap is a complete binary tree in which the value of each node is lesser than or equal to the values of its children.

- Min heaps are quite similar to Max heaps except for the main difference.

<br>
<br>

## Implementation

```python
class MaxHeap:
    def __init__(self, array: list = None):
        self.heap = [] if array is None else array
        self.build_max_heap()

    def left_child_index(self, parent_index):
        return 2 * parent_index + 1

    def right_child_index(self, parent_index):
        return 2 * parent_index + 2

    def parent_index(self, child_index):
        return (child_index - 1) // 2

    def max_heapify(self, index: int = 0) -> None:
        left_index = self.left_child_index(index)
        right_index = self.right_child_index(index)
        largest = index
        if left_index < len(self.heap) and self.heap[left_index] > self.heap[index]:
            largest = left_index
        if right_index < len(self.heap) and self.heap[right_index] > self.heap[largest]:
            largest = right_index
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.max_heapify(largest)

    def build_max_heap(self) -> None:
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.max_heapify(i)

    def extract_max(self) -> float:
        res = None
        if self.heap:
            max = self.heap[0]
            res = max
            last = self.heap.pop()
            self.heap[0] = last
            self.max_heapify()
        return max

    def push(self, value: float) -> None:
        self.heap.append(value)
        self.build_max_heap()
```

<br/>

### max_heapify Algorithm

`max_heapify` assumes that the binary tree rooted at the the left and right children of a given index are max heaps and ensures that the max heap property is satisfied if the value of the index doesn't satisfy it by "floating" it down.

```py
def max_heapify(self, index: int = 0) -> None:
    left_index = self.left_child_index(index)
    right_index = self.right_child_index(index)
    largest = index
    if left_index < len(self.heap) and self.heap[left_index] > self.heap[index]:
        largest = left_index
    if right_index < len(self.heap) and self.heap[right_index] > self.heap[largest]:
        largest = right_index
    if largest != index:
        self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
        self.max_heapify(largest)
```

- `max_heapify` algorithm will not fix the entire tree as the assumption that it inherently makes is not always true.
- `max_heapify` has $O(log(N))$ time complexity, as it'll run as many times as the height of the binary tree.

<br/>

### build_max_heap Algorithm

`build_max_heap` ensures that the entire binary tree obey's the [max heap property](#max-heap-property) by calling `max_heapify` on each non-leaf node from the bottom up.

```py
def build_max_heap(self) -> None:
    for i in range(len(self.heap) // 2 - 1, -1, -1):
        self.max_heapify(i)
```

- Note that the last non-leaf node's index is given by $(N//2)-1$, where N is the total number of nodes in the heap.
- `build_max_heap` algorithm will fix the entire tree.
- `build_max_heap` has $O(n*log(N))$ time complexity, a tighter asymptotic bound would be $O(n)$. The intutive explnation is that when max_heapify is called on leaf nodes it runs only once, and one level above it may run twice....only the root node will run $log(N)$ (Mathematical proof can be found in the textbook).

<br/>

### extract_max Algorithm

`extract_max` algorithm returns the maximum value by popping it from the max heap without voilating [max heap property](#max-heap-property).

```python
def extract_max(self) -> float:
    res = None
    if self.heap:
        max = self.heap[0]
        res = max
        last = self.heap.pop()
        self.heap[0] = last
        self.max_heapify()
    return max
```

- The `extract_max` algorithm has $O(log(N))$ time complexity.

<br>

### Pushing a Value

The algorithm to insert a new value to the max heap employee's the `build_max_heap` algorithm to maintain the [max heap property](#max-heap-property).

```python
def push(self, value: float) -> None:
    self.heap.append(value)
    self.build_max_heap()
```

- The time complexity of the above code is $O(log(N))$.

<br/>
<br/>

## Python's Heapq Module

_heapq is a python module that has implmentation for "min" heaps._

- `heapq.heapify` function transforms a list to a min heap in $O(n)$.

  ```py
  import heapq

  input = [4, 1, 3, 2, 16, 9]
  heapq.heapify(input)
  print(input)

  # [1, 2, 3, 4, 16, 9]
  ```

- `heapq.heappop` returns the minimum element from a min heap in $O(log(N))$ while mainting the min heap property.

  ```py
  import heapq

  input = [4, 1, 3, 2, 16, 9]
  heapq.heapify(input)  # It is important to heapify first
  min = heapq.heappop(input)
  print(min)
  print(input)

  # 1
  # [2, 4, 3, 9, 16]
  ```

- `heapq.heappush` adds the new element into the array and tranforms the array to a min heap in $O(log(n))$.

  ```py
  import heapq
  input = [4, 1, 3, 2, 16, 9]
  heapq.heapify(input)  # It is important to heapify first
  heapq.heappush(input, 5)
  print(input)
  # [1, 2, 3, 4, 16, 9, 5]
  ```

<br>

### Using heapq module for max heap

- Heapifying to get a max heap.

  ```py
  import heapq

  input = [4, 1, 3, 2, 16, 9]
  input = [-(num) for num in input]
  heapq.heapify(input)
  print([-num for num in input])

  # [16, 4, 9, 2, 1, 3]
  ```

- Popping the maximum element from a max heap.

  ```py
  import heapq

  input = [4, 1, 3, 2, 16, 9]
  input = [-(num) for num in input]
  heapq.heapify(input)  # It is important to heapify first
  max = -heapq.heappop(input)
  print(max)
  input = [-(num) for num in input]
  print(input)

  # 16
  # [9, 4, 3, 2, 1]
  ```

- Pushing an element to a max heap.

  ```py
  import heapq

  input = [4, 1, 3, 2, 16, 9]
  input = [-num for num in input]
  heapq.heapify(input)  # It is important to heapify first
  heapq.heappush(input, -5)
  input = [-num for num in input]
  print(input)
  #[16, 4, 9, 2, 1, 3, 5]
  ```

<br/>
<br/>

## Complexity

- The asymptotic worst-case complexities for implementation of heap.

  | Operation     | Time Complexity      | Space Complexity |
  | ------------- | -------------------- | ---------------- |
  | Heapify       | O(log(n))            | O(1)             |
  | Build Heap    | O(n\*log(n)) => O(n) | O(1)             |
  | Push          | O(log(n))            | O(1)             |
  | Extract (Pop) | O(log(n))            | O(1)             |

- The asymptotic worst-case complexities of heap using heapq module.

  | Operation | Time Complexity | Space Complexity |
  | --------- | --------------- | ---------------- |
  | heapify   | O(n)            | O(1)             |
  | heappush  | O(log(n))       | O(1)             |
  | heappop   | O(log(n))       | O(1)             |

<br>
<br>

## References

- Checkout [heap sort](../../algorithms/sorting-algorithms.md#heap-sort).
