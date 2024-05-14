# Heap

A heap is a [complete binary tree](./trees/binary-tree.md####complete-binary-tree)  in which the parent nodes have values greater or lesser than the values of the children, based on wether it is max or min heap respectively.

<br/>
<br/>

# Max Heap

A max heap is a complete binary tree in which the value of each node is greater than or equal to the values of its children.

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

<br/>
<br/>

### Implementaion of max heap

```python
class MaxHeap:
    def __init__(self):
        self.heap = []

    def left_child_index(self, parent_index):
        return 2*parent_index + 1

    def right_child_index(self, parent_index):
        return 2*parent_index + 2

    def parent_index(self, child_index):
        return child_index//2
```

<br/>

### `insert` method

Add a new node to the heap while maintaining max-heap property. Requires the `max_heapify` method

```python
def insert(self, new_value):
    self.heap.append(new_value)
    self.max_heapify()
```

<br/>

## `max_heapify` method

Given a heap (i.e. A complete binary tree), this fucntion rearranges the values to satisfy max-heap property.

```python
def swap(self,i,j):
        self.heap[i],self.heap[j] = self.heap[j],self.heap[i]

def max_heapify_logic(self, index):
    last_index = len(self.heap
    left_index = self.left_child_index(index)
    right_index = self.right_child_index(index)
    largest_index = in
    if left_index <= last_index and self.heap[left_index] > self.heap[index]:
        largest_index = left_in
    if right_index <= last_index and self.heap[right_index] > self.heap[largest_index]:
        largest_index = right_in
    if largest_index != index:
        self.swap(index,largest_index)
        self.max_heapify_logic(largest_index)

def max_heapify(self):
    for i in range(len(self.heap)-1,-1,-1):
        self.max_heapify_logic(i)

```

<br/>

## `extract_max` method

This method pop's the max value (i.e. the root value) from the heap and maintains the max-heap property.

```python
def extract_max(self):
    if not self.heap:
        return None
    max_val = self.heap.pop(0)          #root has the max value
    last_node_val = self.heap.pop()     #remove the last node and insert it as root
    self.heap.insert(0, last_node_val)
    self.max_heapify()                   #max_heapify to restore max-heap property
    return max_val
```

<br>

## Heapify for an array

```py
def heapify(arr):
    size_arr = len(arr)

    def heapify_algo(arr, i):
        largest = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < size_arr and arr[left_child] > arr[largest]:
            largest = left_child

        if right_child < size_arr and arr[right_child] > arr[largest]:
            largest = right_child

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify_algo(arr, largest)

    for i in range(size_arr // 2 - 1, -1, -1):
        heapify_algo(arr, i)


my_list = [10, 5, 15, 3, 7, 1, 100]
print("Original list:", my_list)
heapify(my_list)
print("Heapified list:", my_list)

# Original list: [10, 5, 15, 3, 7, 1, 100]
# Heapified list: [100, 7, 15, 3, 5, 1, 10]
```

<br/>
<br/>

# Min Heap

A min heap is a complete binary tree in which the value of each node is lesser than or equal to the values of its children.

- Min heaps are quite similar to Max heaps except for the main difference.
