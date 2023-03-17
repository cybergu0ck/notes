# Heap

A heap is a complete binary tree in which the parent nodes have values greater or lesser (based on wether it is max or min heap respectively) than the values of the children.



### Concept Clarity:

- Look up the definition of a complete binary tree.
- This is a complete binary tree.
    ```
              20
            /    \
          18      12
         / \       
        9   7       

    ```
- This is a complete binary tree.
    ```
              20
            /    \
          18      12
         / \     / 
        9   7   1   

    ```
- This is a complete binary tree.
    ```
              20
            /    \
          18      12
         / \     /  \
        9   7   1    2

    ```
- This is NOT a complete binary tree. As it is not left leaning when possible.
    ```
              20
            /    \
          18      12
         / \        \
        9   7        1

    ```

<br/>
<br/>

# Max Heap

A max heap is a complete binary tree in which the value of each node is greater than or equal to the values of its children.

- In a max heap, the value of the root node is the largest among all nodes in the heap. 
- When represented as an array: for any node i in the heap, 
    - its left child is located at 2i.
    - its right child is located at 2i + 1.
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


# Min Heap

A min heap is a complete binary tree in which the value of each node is lesser than or equal to the values of its children.
