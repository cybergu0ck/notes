[← Back to trees](./contents.md)

# Contents

- [Heap](#heap)
  - [Max Heap](#max-heap)
  - [Min Heap](#min-heap)
  - [Implementation](#implementation)
    - [Sift up algorithm](#sift-up-algorithm)
    - [Sift down algorithm](#sift-down-algorithm)
    - [Floyds construction algorithm](#floyds-construction-algorithm)
  - [Python's Heapq Module](#pythons-heapq-module)
    - [Using heapq module for max heap](#using-heapq-module-for-max-heap)
  - [Complexity](#complexity)
  - [References](#references)

<br>
<br>
<br>




# Contents

- [Heap](#heap)
  - [Max Heap](#max-heap)
  - [Min Heap](#min-heap)
  - [Implementation](#implementation)
    - [Sift up algorithm](#sift-up-algorithm)
    - [Sift down algorithm](#sift-down-algorithm)
    - [Floyds construction algorithm](#floyds-construction-algorithm)
  - [Python's Heapq Module](#pythons-heapq-module)
    - [Using heapq module for max heap](#using-heapq-module-for-max-heap)
  - [Complexity](#complexity)
  - [References](#references)

<br>
<br>
<br>




# Contents

- [Heap](#heap)
  - [Max Heap](#max-heap)
  - [Min Heap](#min-heap)
  - [Implementation](#implementation)
    - [Sift up algorithm](#sift-up-algorithm)
    - [Sift down algorithm](#sift-down-algorithm)
    - [Floyds construction algorithm](#floyds-construction-algorithm)
  - [Python's Heapq Module](#pythons-heapq-module)
    - [Using heapq module for max heap](#using-heapq-module-for-max-heap)
  - [Complexity](#complexity)
  - [References](#references)

<br>
<br>
<br>




# Contents

- [Heap](#heap)
  - [Max Heap](#max-heap)
  - [Min Heap](#min-heap)
  - [Implementation](#implementation)
    - [Sift up algorithm](#sift-up-algorithm)
    - [Sift down algorithm](#sift-down-algorithm)
    - [Floyds construction algorithm](#floyds-construction-algorithm)
  - [Python's Heapq Module](#pythons-heapq-module)
    - [Using heapq module for max heap](#using-heapq-module-for-max-heap)
  - [Complexity](#complexity)
  - [References](#references)

<br>
<br>
<br>




[← Back to trees](./contents.md)

# Heap

_Heap is an array based datasructure visualised as a [complete binary tree](./binary-tree.md#complete-binary-tree) in which the parent nodes have values greater or lesser than the values of the children, based on wether it is max or min heap respectively._

- As heaps are binary trees (specifically complete binary tree), the positions of the children given the root's position are same as that of [binary trees](binary-tree.md#indices-when-represented-as-an-array)

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

```py
class MaxHeap:
    def __init__(self, array = []):
        self.heap = []
        if array:
            self.heap = array
            self._build_heap()

    def _left(self, i):
        return 2*i + 1

    def _right(self, i):
        return 2*i + 2

    def _parent(self, i):
        return (i-1)//2

    def _sift_up(self, i):
        # O(log(N))
        while i>0:
            parent = self._parent(i)
            if self.heap[parent] >= self.heap[i]:
                break
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            i = parent

    def _sift_down(self, i):
        # O(log(N))
        largest = i
        left = self._left(i)
        right = self._right(i)
        if left < len(self.heap) and self.heap[left] > self.heap[i]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._sift_down(largest)

    def _build_heap(self):
        # O(N)
        for i in range(len(self.heap)//2 - 1, -1, -1):
            self._sift_down(i)

    def push(self, value):
        # O(log(N))
        self.heap.append(value)
        self._sift_up(len(self.heap)-1)

    def peek(self):
        if not self.heap:
            raise IndexError("heap is empty")
        return self.heap[0]

    def pop(self):
        # O(log(N))
        if not self.heap:
            raise IndexError("heap is empty")
        res = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._sift_down(0)
        return res
```

<br/>
<br/>

### Sift up algorithm

- Moves the node up the heap (swapping with parents) until the max-heap property holds.
- This algorithm is called while pushing a new value to the heap. The new value is added at the bottom of the heap and then sifted up.
- This is also known as "Bubble up"
- Note that calling this algorithm (ex: on the root node) will not make the heap satisfy the heap-property!

<br>
<br>

### Sift down algorithm

- Moves the node down the heap (swapping with the larger child) until the max-heap property holds.
- This algorithm is called while building a heap from an array of values.
- This is also known as "Bubble down" or "Heapify".
- Note that calling this algorithm (ex: on the root node) will not make the heap satisfy the heap-property!

<br/>
<br/>

### Floyds construction algorithm

This is building a heap by calling `_sift_down` on each non leaf node from the bottom up.

- It is the `_build_heap` method.
- Note that the last non-leaf node's index is given by $(N//2)-1$, where N is the total number of nodes in the heap.
- Note that calling this algorithm will make the heap satisfy the heap-property!
- `_build_heap` has $O(n*log(N))$ time complexity, a tighter asymptotic bound would be $O(n)$.
  - The intutive explnation is that when max_heapify is called on leaf nodes it runs only once, and one level above it may run twice....only the root node will run $log(N)$.
  - Mathematical proof is difficult to illustrate and can be found in textbook.

<br/>
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

  | Operation           | Time Complexity      | Space Complexity |
  | ------------------- | -------------------- | ---------------- |
  | Sift up             | O(log(n))            | O(1)             |
  | Sift down / Heapify | O(log(n))            | O(1)             |
  | Build Heap          | O(n\*log(n)) => O(n) | O(1)             |
  | Push                | O(log(n))            | O(1)             |
  | Pop                 | O(log(n))            | O(1)             |

- The asymptotic worst-case complexities of heap using heapq module.

  | Operation | Time Complexity | Space Complexity |
  | --------- | --------------- | ---------------- |
  | heapify   | O(n)            | O(1)             |
  | heappush  | O(log(n))       | O(1)             |
  | heappop   | O(log(n))       | O(1)             |

<br>
<br>
<br>

## References

- Checkout [heap sort](../../algorithms/sorting-algorithms.md#heap-sort).
