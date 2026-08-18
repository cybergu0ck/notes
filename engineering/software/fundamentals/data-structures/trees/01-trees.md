# Tree

_Tree is a nonlinear hierarchial data structure that consists of nodes connected by edges._

<br>
<br>
<br>

## Basics of Tree

![image](./_assets/tree-parts.jpg)

<br>
<br>

### Elements of Tree

1. **_Node_** : Entity that contains a value and pointers to it's children nodes.

1. **_Edge_** : Link between nodes.

1. **_Root_** : Top most node of a tree.

1. **_Leaf/Terminal Node_** : A node without children

<br>
<br>

### Features of Tree

1. **_Height_** of a node is the number of edges from the node to the deepest leaf.

   - Height is measured from the bottom.
   - Height of the tree is the number of edges from the root to the deepest leaf.
   - In the above image, the height of node J is 0, node D is 2 and the height of the entire tree is 3.

1. **_Depth_** of a node is the number of edges from the node to the root.

   - Depth is measured from the top.
   - Depth of the tree is the number of edges from the root to the deepest leaf. (For the tree, height and depth are same in magnitude)
   - In the above image, the depth of node A is 0, of node H is 2 and node J is 3

1. Level of a tree is same as the depth.
   - Level starts from zero in these notes.
   - Zeroth level has depth = 0.
   - First level has depth = 1 and so on.

- Some might consider the nodes (instead of edges) for depth and level. In that case, the depth (and level) starts from 1 instead of 0. All the formula in these notes need to be adjusted for this.

<br>
<br>
<br>

## Types of Trees

1. Binary Trees
   <ol type="1">
   <li>Full Binary Trees</li>
   <li>Complete Binary Trees</li>
   <li>Perfect Binary Trees</li>
   </ol>

1. Binary Search Trees (BST)
1. AVL Trees
1. B-Tree

<br/>
<br/>
<br/>

## Equations

The maximum number of nodes in a tree with depth of $n$ and each node having $k$ branches is

$$\frac{k^{(n+1)} - 1}{k - 1}$$

<br/>
<br/>
<br/>

## Reference

https://adrianmejia.com/data-structures-for-beginners-trees-binary-search-tree-tutorial/#.W0_QE_GXQ10.reddit
