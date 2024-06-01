# Heap

_Heap is a [Complete Binary Tree](./trees/binary-tree.md#complete-binary-tree) in which the parent nodes have values greater or lesser than the values of the children, based on wether it is max or min heap respectively._

<br/>
<br/>
<br/>

# Max Heap

_Max Heap is a [Complete Binary Tree](./trees/binary-tree.md#complete-binary-tree) in which the value of each node is greater than or equal to the values of its children._

- In a max heap, the value of the root node is the largest among all nodes in the heap.
- When represented as an array: for any node i in the heap,
  - its left child is located at 2i + 1.
  - its right child is located at 2i + 2.
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

## Max Heap Property

The value of any node in the heap must be greater than or equal to the values of the children nodes.

<br/>
<br/>

## Implementaion

Heaps are commonly implemented with an array. Any binary tree can be stored in an array, but because a binary heap is always a complete binary tree, it can be stored compactly. No space is required for pointers; instead, the parent and children of each node can be found by arithmetic on array indices.

```python
class MaxHeap:
    def __init__(self, array: list = None):
        self.heap = []

        if array:
            self.build_max_heap(array)

    def left_child_index(self, parent_index):
        return 2 * parent_index + 1

    def right_child_index(self, parent_index):
        return 2 * parent_index + 2

    def parent_index(self, child_index):
        return child_index // 2

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

    def build_max_heap(self, array: list = None) -> None:
        if array:
            self.heap = array

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

    def insert(self, value: float) -> None:
        self.heap.append(value)
        self.build_max_heap(self.heap)
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

<br/>

### build_max_heap Algorithm

`build_max_heap` ensures that the entire binary tree obey's the [max heap property](#max-heap-property) by calling `max_heapify` on each non-leaf node from the bottom up.

```py
def build_max_heap(self, array: list = None) -> None:
    if array:
        self.heap = array
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.max_heapify(i)
```

- `build_max_heap` algorithm will fix the entire tree.

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

<br>

### Inserting a Value

The algorithm to insert a new value to the max heap employee's the `build_max_heap` algorithm to maintain the [max heap property](#max-heap-property).

```python
def insert(self, value: float) -> None:
    self.heap.append(value)
    self.build_max_heap(self.heap)
```

<br/>
<br/>

## Complexity

The asymptotic worst-case complexities are considered here.

- For a Binary Search Tree with a linear chain of 'n' nodes,
  | Operation | Time Complexity | Space Complexity |
  | --------- | --------------- | ---------------- |
  | Search | O(n) | |
  | Insertion | O(n) | |
  | Deletion | O(n) | |

- For a Complete Binary Search Tree with "n" nodes,
  | Operation | Time Complexity | Space Complexity |
  | --------- | --------------- | ---------------- |
  | Search | O(log(n)) | |
  | Insertion | O(log(n)) | |
  | Deletion | O(log(n)) | |

//TODO - Fill up the above table

<br>
<br>
<br>

# Min Heap

A min heap is a complete binary tree in which the value of each node is lesser than or equal to the values of its children.

- Min heaps are quite similar to Max heaps except for the main difference.

<br>
<br>
<br>

# Heap Sort

//TODO - Add the heap sort algorithm

<br>
<br>
<br>
