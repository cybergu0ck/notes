# Binary Tree

_When a tree has at the most two children, then it’s called ***binary tree***._

<br>
<br>

## Types of Binary Tree

1. Full Binary Tree : Each node has exactly 0 or 2 children (but never 1).
1. Complete binary tree : A complete binary tree is a binary tree in which every level of the tree is completely filled, except possibly the last level. In the last level, all nodes are as far left as possible.
   - In the below image if the right most gray node in complete binary tree image is considered then It would not be a complete binary tree (as it is not left when possible)
1. Perfect binary tree : When all the levels (including the last one) are full of nodes.
   - Perfect binary trees have precisely (2^k) - 1 nodes, where k is the last level of the tree (starting with 1).

<br/>

![image](../assets/full-complete-perfect-binary-tree.jpg)

<br/>

These properties are not always mutually exclusive. You can have more than one:

- A perfect binary tree is always complete binary tree.
- A complete tree is not always perfect tree.
- A full tree is not always complete and perfect.

<br>
<br>

## Equations related to Binary Tree

<br>

### Maximum number of nodes for a given height

The maximum number of nodes at a given height is $2^h$. The maximum number of nodes at a given height can be calculated by summing up all the nodes at previous height's i.e $ 2^h + 2^{h-1} + 2^{h-2} + ... + 1 $. This is a geometric series and the sum of a geometric series is given by the formula:

$$ S = a \left( \frac{1- r^n }{1- r } \right)$$

In our case, $ a = 2^h$, $r = 1/2$ and $n = h+1$. Therefore,

$$ S = 2^{h+1} -1 $$

Hence, For a tree with height $h$,

$$ \text{The maximum number of nodes in the tree} = N = 2^{h+1} -1 $$

<br>

### Height of the tree for number of nodes

If $N$ is the maximum number of nodes and $h$ is the height of the tree, from [proof](#maximum-number-of-nodes-for-a-given-height) we know that:

$$ N = 2^{h+1} -1 $$

Solving for h in the above equation,

$$ h = \log_2{(N+1)}-1 $$

Hence, For a tree with $N$ nodes,

$$ \text{The height of the tree = h =} floor(log_2(N))$$

<br/>

### Indices when represented as an array

When the tree is represented as an array, for node at index $i$,

$$ \text{Index of left child} = 2\times{i}+1 $$
  $$ \text{Index of right child} = 2\times{i} +2$$
$$ \text{Index of parent} = floor((i-1)/2)$$

<br/>
<br/>

## Binary Tree Traversals

<br/>

### In-Order Traversal

- This is Depth First Search (DFS) approach and Traversal occurs left -> root -> right

  ```python
  #This is a method of class BinarySearchTree
  def in_order(self, root = None, must_return = "values"):
      "in order is DFS hence use a stack, left -> root ->right"
      #---------------------------------------------------------------------------------
      #consider self.root as defualt parameter
      if root == None:
          cur = self.root
      else:
          cur = root
      #---------------------------------------------------------------------------------
      #in-order traversal of an empty tree is []
      if cur == None:
          return []
      #---------------------------------------------------------------------------------
      #logic
      nodes = []                  #nodes is a list of Nodeobjects
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
      #---------------------------------------------------------------------------------
      #returning nodes
      if must_return == "nodes":
          return nodes
      #---------------------------------------------------------------------------------
      #returning values
      elif must_return == "values":
          values = []                     #values is a listof Node values
          for node in nodes:
              values.append(node.val)
          return values
      #---------------------------------------------------------------------------------
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
          "post order is a DFS hence use a stack; left ->right -> root"
          #---------------------------------------------------------------------------------
          #consider self.root as defualt parameter
          if root == None:
              cur = self.root
          else:
              cur = root
          #---------------------------------------------------------------------------------
          #postOrder traversal of empty tree is []
          if cur == None:
              return []
          #---------------------------------------------------------------------------------
          #logic
          stack = [cur]
          nodes = []
          while stack:
              cur = stack.pop()
              nodes.append(cur)
              if cur.left:
                  stack.append(cur.left)          #Leftchild must be added first!
              if cur.right:
                  stack.append(cur.right)
          nodes = nodes[::-1]                     #what wewant is actually the reverse!
          #---------------------------------------------------------------------------------
          #returning nodes
          if must_return == "nodes":
              return nodes
          #---------------------------------------------------------------------------------
          #returning values
          elif must_return == "values":
              values = []
              for node in nodes:
                  values.append(node.val)
              return values
          #---------------------------------------------------------------------------------
  ```

<br/>

### Level-Order Traversal (BFS)

- This is Breadth First Search (BFS) approach and traversal occurs level wise.

  ```py
  # This is a method of class BinarySearchTree


  def level_order(self, root=None, must_return="values", return_type="list(list)"):
      """level order is a BFS hence use queue."""
      # ----------------------------------------------------------------------------------
      if root == None:
          cur = self.root  # consider self.root as defualt parameter
      else:
          cur = root
      # ----------------------------------------------------------------------------------
      if cur == None:
          return []  # level order for an empty tree is []
      # ----------------------------------------------------------------------------------
      # logic
      q = [cur]
      multi_nodes = []  # multi_nodes is a list of list of Node objects
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
      # ----------------------------------------------------------------------------------
      # list(list) means [[], [], [], ...]
      if return_type == "list(list)":
          if must_return == "nodes":
              return multi_nodes
          elif must_return == "values":
              multi_values = []  # multi_values is a list of list of Node values.
              for node_list in multi_nodes:  # nodes is of the type [[]]
                  values_list = []
                  for node in node_list:
                      values_list.append(node.val)
                  multi_values.append(values_list)
              return multi_values
      # ----------------------------------------------------------------------------------
      # list means []
      elif return_type == "list":
          nodes = []  # nodes is a list of Node objects
          for node_list in multi_nodes:
              for node in node_list:
                  nodes.append(node)
          if must_return == "nodes":
              return nodes
          elif must_return == "values":
              values = []  # values is a list of Node values.
              for node in nodes:
                  values.append(node.val)
              return values
      # ----------------------------------------------------------------------------------
  ```

<br/>
<br/>
