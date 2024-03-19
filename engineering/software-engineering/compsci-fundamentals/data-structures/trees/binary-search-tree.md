## Binary Search Tree (BST)

BST has at most two nodes (like all binary trees). However, the values are so that the left children value must be less than the parent, and the right children must be higher.

- Duplicates: Some BST doesn’t allow duplicates while others add the same values as a right child. Other implementations might keep a count on a case of duplicity.

### Implementation

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

### Node Insertion

```python
#This is a method of class BinarySearchTree.

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
                    print("No duplicates")      #raise exceptions here!

```

<br/>
<br/>

### Node Deletion

```python
#This is a method of class BinarySearchTree
#This requires treversal methods (pre_order)

def delete(self, value):
        cur = self.root
        to_be_deleted = None
        prev_node = None    #prev_node contains the node who's child is to be deleted.
        flag = None         #flag enables us to decide whether to delete left or right child.

        while cur:
            if value < cur.val:
                if cur.left:
                    prev_node = cur
                    flag = "left"
                    cur = cur.left

            elif value > cur.val:
                if cur.right:
                    prev_node = cur
                    flag = "right"
                    cur = cur.right

            elif value == cur.val :
                to_be_deleted = cur
                if flag == "left":
                    prev_node.left = None
                if flag == "right" :
                    prev_node.right = None
                if flag == None:
                    #Meaning we are deleting self.root
                    self.root = Node()
                break

        nodes_after_deleted_node = self.pre_order(to_be_deleted, must_return = "values")
        nodes_after_deleted_node.pop(0)
        for value in nodes_after_deleted_node:
            self.insert(value)

```

<br/>
<br/>
