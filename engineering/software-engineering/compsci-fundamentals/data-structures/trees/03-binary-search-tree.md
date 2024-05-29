# Binary Search Tree

_Binary Search Tree is a Binary Tree where at any given node, the value in the left subtree is less than the node and the value in the right subtree is greater than the node._

- Duplicates: Some BST doesn’t allow duplicates while others add the same values as a right child. Other implementations might keep a count on a case of duplicity.

<br>
<br>

## Binary Search Tree Property

Given that $x$ is a node in a binary search tree,

- If $y$ is a node in the left subtree of $x$, then $y.value$ <= $x.value$.
- If $y$ is a node in the right subtree of $x$, then $y.value$ >= $x.value$.

<br>
<br>

## Implementation

```python
class Node:
    def __init__(self, value: float = None, left: "Node" = None, right: "Node" = None):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = Node()

    def insert_node(self, value: float) -> None:
        new_node = Node(value)
        cur = self.root

        if not cur.value:
            self.root = new_node
        else:
            while cur:
                if value < cur.value:
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = new_node
                        break
                elif value > cur.value:
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = new_node
                        break
                else:
                    print("duplicates are ignored")
                    break


    def search_node(self, value: float, root: Node = None) -> Node:
        res = None
        cur = self.root if not root else root
        while cur:
            if cur.value == value:
                res = cur
                break
            elif value < cur.value:
                cur = cur.left
            elif value > cur.value:
                cur = cur.right
        return res

    def get_min_node(self, root: Node = None) -> Node:
        cur = self.root if not root else root
        while cur.left:
            cur = cur.left
        return cur

    def get_max_node(self, root: Node = None) -> Node:
        cur = self.root if not root else root
        while cur.right:
            cur = cur.right
        return cur

    def get_successor_node(self, node: Node) -> Node:
        res = None
        if node:
            cur = node

            if cur.right:
                res = self.get_min_node(cur.right)
            else:
                cur = self.root

                while cur:
                    if node.value < cur.value:
                        res = cur
                        cur = cur.left
                    elif node.value > cur.value:
                        cur = cur.right
                    else:
                        break
        return res

    def get_predecessor_node(self, node: Node) -> Node:
        res = None
        if node:
            cur = node

            if cur.left:
                res = self.get_max_node(cur.left)
            else:
                cur = self.root

                while cur:
                    if node.value < cur.value:
                        cur = cur.left
                    elif node.value > cur.value:
                        res = cur
                        cur = cur.right
                    else:
                        break
        return res

    def get_parent_node(self, node: Node) -> Node:
        res = None
        if node and node.value != self.root.value:
            cur = self.root
            while cur:
                if cur.left == node or cur.right == node:
                    res = cur
                    break
                elif node.value < cur.value:
                    cur = cur.left
                else:
                    cur = cur.right
        return res

    def delete_node(self, value: float) -> None:
        to_delete = self.search_node(value)
        if to_delete:
            if to_delete.left and to_delete.right:
                suc = self.get_successor_node(to_delete)
                if suc == to_delete.right:
                    to_delete.value = suc.value
                    to_delete.right = suc.right

                else:
                    to_delete.value = suc.value
                    if suc.right:
                        suc.value = suc.right.value
                        if suc.right.right:
                            suc.right = suc.right.right
                        if suc.right.left:
                            suc.left = suc.right.left

            elif to_delete.left:
                to_delete_parent = self.get_parent_node(to_delete)
                to_delete_parent.left = to_delete.left

            elif to_delete.right:
                to_delete_parent = self.get_parent_node(to_delete)
                to_delete_parent.right = to_delete.right

            else:
                to_delete_parent = self.get_parent_node(to_delete)
                if to_delete_parent.left == to_delete:
                    to_delete_parent.left = None
                else:
                    to_delete_parent.right = None

    def in_order_traversal(self, root: Node = None) -> list[float]:
        res = []
        cur = self.root if not root else root
        stack = []

        while True:
            if cur:
                stack.append(cur)
                cur = cur.left
            elif stack:
                cur = stack.pop()
                res.append(cur.value)
                cur = cur.right
            else:
                break
        return res

    def pre_order_traversal(self, root: Node = None) -> list[float]:
        res = []
        cur = self.root if not root else root
        stack = [cur]

        while stack:
            cur = stack.pop()
            res.append(cur.value)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res

    def post_order_traversal(self, root: Node = None) -> list[float]:
        res = []
        cur = self.root if not root else root
        stack = [cur]

        while stack:
            cur = stack.pop()
            res.append(cur.value)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return res[::-1]

    def level_order_traversal(self, root: Node = None) -> list[float]:
        res = []
        cur = self.root if not root else root
        q = [cur]

        while q:
            cur = q.pop(0)
            res.append(cur.value)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return res

    def level_order_traversal_diff(self, root: Node = None) -> list[list[Node]]:
        res = []
        cur = self.root if not root else root
        q = [cur]

        while q:
            level = []
            for i in range(len(q)):
                cur = q.pop(0)
                level.append(cur.value)

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(level)

        return res
```

<br/>

### Insertion of a Node

The algorithm to insert a node to a binary search tree uses the [binary search tree property](#binary-search-tree-property). The algorithm can be different based on what is done for the case of duplicates. In the following algorithm we ignore the duplicates.

```python
#This is a method of class BinarySearchTree.
def insert_node(self, value: float) -> None:
    new_node = Node(value)
    cur = self.root
    if not cur.value:
        self.root = new_node
    else:
        while cur:
            if value < cur.value:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = new_node
                    break
            elif value > cur.value:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = new_node
                    break
            else:
                print("duplicates are ignored")
                break
```

<br/>

### Searching of a Node

The algorithm to get an existing node from a binary search tree uses the [binary search tree property](#binary-search-tree-property).

```py
def search_node(self, value: float, root: Node = None) -> Node:
    res = None
    cur = self.root if not root else root
    while cur:
        if cur.value == value:
            res = cur
            break
        elif value < cur.value:
            cur = cur.left
        elif value > cur.value:
            cur = cur.right
    return res
```

<br/>

### Node with the Minimum Value

The algorithm to find the node with the least value exploits the fact that the left most node in the binary search tree holds the least value.

```py
def get_min_node(self, root: Node = None) -> Node:
    cur = self.root if not root else root
    while cur.left:
        cur = cur.left
    return cur
```

<br/>

### Node with the Maximum Value

The algorithm to find the node with the largest value exploits the fact that the right most node in the binary search tree holds the largest value.

```py
def get_max_node(self, root: Node = None) -> Node:
    cur = self.root if not root else root
    while cur.right:
        cur = cur.right
    return cur
```

<br/>

### Successor of a Node

_Successor of a node in a binary search tree is the node with the smallest value that is larger than the value of the given node._

```py
def get_successor_node(self, node: Node) -> Node:
    res = None
    if node:
        cur = node
        if cur.right:
            res = self.get_min_node(cur.right)
        else:
            cur = self.root
            while cur:
                if node.value < cur.value:
                    res = cur
                    cur = cur.left
                elif node.value > cur.value:
                    cur = cur.right
                else:
                    break
    return res
```

- In terms of in-order traversal, The successor of a node is the next node that will be traversed.

<br/>

### Predecessor of a Node

_Predecessor of a node in a binary search tree is the node with the largest value that is smaller than the value of the given node._

```py
def get_predecessor_node(self, node: Node) -> Node:
    res = None
    if node:
        cur = node
        if cur.left:
            res = self.get_max_node(cur.left)
        else:
            cur = self.root
            while cur:
                if node.value < cur.value:
                    cur = cur.left
                elif node.value > cur.value:
                    res = cur
                    cur = cur.right
                else:
                    break
    return res
```

- In terms of in-order traversal, The predecessor of a node is the previous node that was traversed.

<br/>

### Parent of a Node

The algorithm to find the parent of a node in a binary search tree uses the [binary search tree property](#binary-search-tree-property).

```py
def get_parent_node(self, node: Node) -> Node:
    res = None
    if node and node.value != self.root.value:
        cur = self.root
        while cur:
            if cur.left == node or cur.right == node:
                res = cur
                break
            elif node.value < cur.value:
                cur = cur.left
            else:
                cur = cur.right
    return res
```

<br/>

### Deletion of a Node

The algorithm to delete a node is slightly intensive,

```py
def delete_node(self, value: float) -> None:
    to_delete = self.search_node(value)
    if to_delete:
        if to_delete.left and to_delete.right:
            suc = self.get_successor_node(to_delete)
            if suc == to_delete.right:
                to_delete.value = suc.value
                to_delete.right = suc.right
            else:
                to_delete.value = suc.value
                if suc.right:
                    suc.value = suc.right.value
                    if suc.right.right:
                        suc.right = suc.right.right
                    if suc.right.left:
                        suc.left = suc.right.left
        elif to_delete.left:
            to_delete_parent = self.get_parent_node(to_delete)
            to_delete_parent.left = to_delete.left
        elif to_delete.right:
            to_delete_parent = self.get_parent_node(to_delete)
            to_delete_parent.right = to_delete.right
        else:
            to_delete_parent = self.get_parent_node(to_delete)
            if to_delete_parent.left == to_delete:
                to_delete_parent.left = None
            else:
                to_delete_parent.right = None
```

1. Get the node to be deleted.
1. If the node to be deleted exisits in the binary search tree, then there would be 3 cases:
   1. If the node to be deleted has both left and right children, then get the successor node,
      1. If the successor node is the right child of the node to be deleted, replace the value and the right pointer of the node to be deleted with the successor node.
      2. If the successor node is not the right child, replace the value of the node to be deleted with the value of the successor node and the replace the successor node with it's right child (as it won't have a left child)
   2. If the node to be deleted has only one of left or right child, replace the node to be deleted with it's child.
   3. If the node to be deleted has no children, then just delete it's reference.

<br/>

### Traversal Algorithms

The traversal algorithms for the binary search tree is same as that of the [binary tree](./02-binary-tree.md#tree-traversal-algorithms).

<br>
<br>

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
