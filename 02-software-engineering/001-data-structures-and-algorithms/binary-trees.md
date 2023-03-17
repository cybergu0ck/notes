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


- When represented as an array, for any node i in the tree, 
    - its left child is present at 2*i +1.
    - its right child is present at 2*i +2.
     
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
1. Complete binary tree :  A complete binary tree is a binary tree in which every level of the tree is completely filled, except possibly the last level. In the last level, all nodes are as far left as possible. 
    - In the below image if the right most gray node in complete binary tree image is considered then It would not be a complete binary tree (as it is not left when possible)
3. Perfect binary tree : When all the levels (including the last one) are full of nodes.
    - Perfect binary trees have precisely (2^k) - 1 nodes, where k is the last level of the tree (starting with 1).

<br/>

![image](./_assets/full-complete-perfect-binary-tree.jpg)

<br/>

These properties are not always mutually exclusive. You can have more than one:

- A perfect binary tree is always complete binary tree.
- A complete tree is not always perfect tree.
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

## Node Deletion

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

## Binary Tree Traversals

<br/>

### In-Order Traversal

- This is Depth First Search (DFS) approach and Traversal occurs left -> root -> right

    ```python
    #This is a method of class BinarySearchTree

    def in_order(self, root = None, must_return = "values"):
        "in order is DFS hence use a stack, left -> root -> right"
        #----------------------------------------------------------------------------------
        #consider self.root as defualt parameter
        if root == None:
            cur = self.root         
        else:
            cur = root
        #----------------------------------------------------------------------------------
        #in-order traversal of an empty tree is [] 
        if cur == None:
            return []               
        
        #----------------------------------------------------------------------------------
        #logic
        nodes = []                  #nodes is a list of Node objects
        stack = []
        while True:
            if cur:
                stack.append(cur)
                cur = cur.left
            elif stack:
                cur = stack.pop()
                nodes.append(cur)
                cur = cur.right
            else:
                break
        
        #----------------------------------------------------------------------------------
        #returning nodes
        if must_return == "nodes":
            return nodes
        
        #----------------------------------------------------------------------------------
        #returning values 
        elif must_return == "values":
            values = []                     #values is a list of Node values
            for node in nodes:
                values.append(node.val)
            return values
        #----------------------------------------------------------------------------------
    ```
<br/>

### Pre- Order Traversal

- This is Depth First Search (DFS) approach and Traversal occurs root -> left -> right 

    ```python
    #This is a method of class BinarySearchTree

    def pre_order(self,root = None, must_return = "values"):
            "pre order is DFS, root -> left -> right"
            #----------------------------------------------------------------------------------
            #consider self.root as defualt parameter

            if root == None:
                cur = self.root                  
            else:
                cur = root

            #----------------------------------------------------------------------------------
            #preOrder traversal of empty tree is []
            if cur == None:
                return []        
                        
            #----------------------------------------------------------------------------------
            #logic
            stack = [cur]
            nodes = []                          #nodes is a list of Node objects
            while stack:
                cur = stack.pop()
                nodes.append(cur)               #we are appending the Node objects itself.
                if cur.right:
                    stack.append(cur.right)     #Right child must be appended first!
                if cur.left:
                    stack.append(cur.left)

            #----------------------------------------------------------------------------------
            #returning nodes

            if must_return == "nodes":
                return nodes                    #Return based on the must_return parameter.
            
            #----------------------------------------------------------------------------------
            #returning values

            if must_return == "values":
                values =[]                          #values is a list of Node values
                for node in nodes:
                    values.append(node.val)

                return values
            #----------------------------------------------------------------------------------
    ```

<br/>

### Post-Order Traversal

- This is Depth First Search (DFS) approach and Traversal occurs left -> right -> root

    ```python
    #This is a method of class BinarySearchTree

    def post_order(self, root = None, must_return = "values"):
            "post order is a DFS hence use a stack; left -> right -> root"
            #----------------------------------------------------------------------------------
            #consider self.root as defualt parameter
            if root == None:
                cur = self.root
            else:
                cur = root
            
            #----------------------------------------------------------------------------------
            #postOrder traversal of empty tree is []
            if cur == None:
                return []
            
            #----------------------------------------------------------------------------------
            #logic 

            stack = [cur]
            nodes = []

            while stack:
                cur = stack.pop()
                nodes.append(cur)
                if cur.left:
                    stack.append(cur.left)          #Left child must be added first!
                if cur.right:
                    stack.append(cur.right)
                

            nodes = nodes[::-1]                     #what we want is actually the reverse!

            #----------------------------------------------------------------------------------
            #returning nodes 
            if must_return == "nodes":
                return nodes

            #----------------------------------------------------------------------------------
            #returning values 
            elif must_return == "values":
                values = []
                for node in nodes:
                    values.append(node.val)
                return values

            #----------------------------------------------------------------------------------
    ```
<br/>

### Level-Order Traversal (BFS)

- This is Breadth First Search (BFS) approach and traversal occurs level wise.

    ```python
    #This is a method of class BinarySearchTree

    def level_order(self, root = None, must_return = "values", return_type = "list(list)"):
            """level order is a BFS hence use queue."""
            #----------------------------------------------------------------------------------
            if root == None:
                cur = self.root                 #consider self.root as defualt parameter
            else:
                cur = root
            #----------------------------------------------------------------------------------
            if cur == None:
                return []                       #level order for an empty tree is []

            #----------------------------------------------------------------------------------
            #logic
            q = [cur]
            multi_nodes = []                          #multi_nodes is a list of list of Node objects
            
            while q:
                levels = []
                for node in q.copy():
                    levels.append(node)
                    q.pop(0)
                multi_nodes.append(levels)
                for node in multi_nodes[-1]:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            #----------------------------------------------------------------------------------
            #list(list) means [[], [], [], ...]
            if return_type == "list(list)":

                if must_return == "nodes":
                    return multi_nodes
                
                elif must_return == "values":
                    multi_values = []                             #multi_values is a list of list of Node values.
                    
                    for node_list in multi_nodes:                 #nodes is of the type [[]]
                        values_list = []
                        for node in node_list:
                            values_list.append(node.val)
                        multi_values.append(values_list)
                    return multi_values
            #----------------------------------------------------------------------------------
            #list means []
            elif return_type == "list":

                nodes =[]                         #nodes is a list of Node objects
                for node_list in multi_nodes:
                    for node in node_list:
                        nodes.append(node)

                if must_return == "nodes":
                    return nodes
                elif must_return == "values":
                    values = []                 #values is a list of Node values.
                    for node in nodes:
                        values.append(node.val)
                    return values
            #----------------------------------------------------------------------------------
    ```

<br/>
<br/>

## Balanced vs UnBalanced Trees

>Make Notes!

<br/>
<br/>













# Reference

https://adrianmejia.com/data-structures-for-beginners-trees-binary-search-tree-tutorial/#.W0_QE_GXQ10.reddit
