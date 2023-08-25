# heapq

The heapq module provides functions to create and manipulate heaps, making it easy to manage collections of elements with varying priorities.

<br>
<br>
<br>

# Useful Functions

## `heapify(iterable)`

- Transform list x into a heap, in-place, in linear time O(n).
- It takes in any iterable.
- Note that this function doesn't sort the list but just ensures that the first element is always the smallest element!

<br>
<br>

## `heappush(heap, item)`

- This function adds an element to the heap while maintaining the heap property. The element is inserted at the appropriate position to maintain the heap structure.
- The time complexity is O(logn)

<br>
<br>

## `heappop(heap)`

- This function removes and returns the **_smallest_** element from the heap, while ensuring that the heap property is preserved.
- The time complexity is O(logn)

<br>
<br>

## Illustatration

- Here we can see that heapify() converts the list to a min heap. heappop() retrives the smallest value every time.

  ```py
  import heapq

  my_iterables = [100,5,10,20,1]
  min_heap = my_iterables   #personally I think this is good as I can refer to the original list as min_heap

  heapq.heapify(min_heap)

  popped_items = []

  while min_heap:
      popped_items.append(heapq.heappop(min_heap))

  print(popped_items)

  #>[1, 5, 10, 20, 100]
  ```

- Making a max-heap implementation using min heaps.

  ```py
  import heapq

  my_iterables = [100,5,10,20,1]
  min_heap = my_iterables

  max_heap = [ -val for val in min_heap]    #clever

  heapq.heapify(max_heap)

  popped_items = []

  while max_heap:
      popped_items.append(heapq.heappop(max_heap))

  print([-val for val in popped_items])

  #>[100, 20, 10, 5, 1]
  ```

* heaps can store lists aswell, in this case it'll use the first item for heapifying!

  ```py
  import heapq

  my_iterables = [[20,'a'], [1, 'z'], [10, 'a']]
  min_heap = my_iterables
  heapq.heapify(min_heap)
  popped_items = []

  while min_heap:
      popped_items.append(heapq.heappop(min_heap))

  print(popped_items)

  #>[[1, 'z'], [10, 'a'], [20, 'a']]
  ```
