# Trees

A tree is a nonlinear hierarchial data structure that consists of nodes connected by edges. 

![image](./_assets/tree-parts.jpg)

- ***Node*** : Entity that contains a value and pointers to it's children nodes.
- ***Edge*** : Link between nodes.
- ***Root*** : Top most node of a tree.
- ***Leaf/Terminal Node*** : A node without children 
- ***Height*** (h) of the tree is the distance (edge count) between the farthest leaf to the root.
    - Height is measured from the bottom
    - A has a height of 3
    - I has a height of 0
- ***Depth*** or level of a node is the distance between the root and the node in question.
    - Depth is measured from the top
    - H has a depth of 2
    - B has a depth of 1

<br/>
<br/>

# Types of Trees

1. Binary Trees
    1. Full Binary Trees
    1. Complete Binary Trees
    1. Perfect Binary Trees

1. Binary Search Trees (BST)
1. AVL Trees
1. B-Tree
<br/>
<br/>


# Binary Tress
When a tree has at the most two children, then it’s called ***binary tree***.


1. Full Binary Tree : Each node has exactly 0 or 2 children (but never 1).
1. Complete binary tree :  When all levels except the last one are full with nodes.
1. Perfect binary tree : When all the levels (including the last one) are full of nodes.
    - Perfect binary trees have precisely (2^k) - 1 nodes, where k is the last level of the tree (starting with 1).

<br/>

![image](./_assets/full-complete-perfect-binary-tree.jpg)

<br/>

These properties are not always mutually exclusive. You can have more than one:

- A perfect tree is always complete and full.
- A complete tree is not always full. (It's a complete tree even if the grapy node is present)
- A full tree is not always complete and perfect.


<br/>
<br/>

# Binary Search Tree (BST)

BST has at most two nodes (like all binary trees). However, the values are so that the left children value must be less than the parent, and the right children must be higher.

- Duplicates: Some BST doesn’t allow duplicates while others add the same values as a right child. Other implementations might keep a count on a case of duplicity.


## Implementation 

```python
class Node:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree:
    "Binary Search Tree (BST) is a Binary tree where the value of the left children is less than the parent and right child."
    
    def __init__(self):
        self.root = Node()


```
<br/>
<br/>

## Node Insertion

```python
class BinarySearchTree:
    "Binary Search Tree (BST) is a Binary tree where the value of the left children is less than the parent and right child."
    
    def __init__(self):
        self.root = Node()

    def insert(self,new_data):
        new_node = Node(new_data)
        cur = self.root

        if cur.val == None:
            self.root = new_node
            cur = self.root

        else:
            while cur:
                if new_data < cur.val:
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = new_node
                        cur = cur.left.left     #This line is not intuitive (Done to exit out of while)
                elif new_data > cur.val:
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = new_node
                        cur = cur.right.right   #same
                else:
                    print("No duplicates")

```
<br/>
<br/>

## Node Deletion

<br/>
<br/>

## Binary Tree Traversals

<br/>

### In-Order Traversal


```python
def in_order(self, root):
        "DFS, left -> root -> right"
        cur = root
        res = []
        stack = []

        while True:
            if cur:
                stack.append(cur)
                cur = cur.left

            elif stack:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
            else:
                break
        return res
```
<br/>

### Post-Order Traversal

<br/>

### Pre- Order Traversal

<br/>

### Level-Order Traversal (BFS)


<br/>
<br/>

## Balanced vs UnBalanced Trees

















# Reference

https://adrianmejia.com/data-structures-for-beginners-trees-binary-search-tree-tutorial/#.W0_QE_GXQ10.reddit