
# Basic Operations of a data structure

1. **Access**   : Retrieving a value from the data structure.
1. **Search** : Finding whether a value exists in the data structure.
1. **Insertion** : Adding a new value to the data structure.
1. **Append** : Adding a new value at the end of a data structure.
1. **Delete** : Removing a value from the data structure.
1. **Pop** : Removing a value from the end of a datastructure.
1. **Find Min (or Max)** :
1. **Delete Min (or Max)** :

<br/>
<br/>

# Comaprision of datastructures based on time complexity

| Data Structure     | Access  | Search   | Insert     |Append     |Delete     | Pop        |Find Min    |Delete Min |
|----------------    |   ----  | ----     |   ----     |   ----    |----       | ----       |  ----      | ----      |
| Unsorted Array     | O(1)    | O(N)     |O(N)        |O(1)       |   O(N)    | O(1)       | O(N)       | O(N)      |
| Sorted Array       | O(1)    |O(logN)*1 |O(N)        |O(1)       |  O(N)     |  O(1)      | O(1)       | O(N)      |
| Stack              |         |  O(N)    |     -      |O(1)       |           |  O(1) *2   |            |           |
| Queue              |         |  O(N)    |            |O(1)       |           |  O(1) *3   |            |           |
| Hash Map           | O(1)    |          | O(N)       |           | O(N)      |            |            |           |
| Singly Linked List | O(N)    | O(N)     | O(1) *4    |           | O(N)      |            | O(N)       |  O(N)     |
| Doubly Linked List |         |          |            |           |           |            |            |           |
| Tree               |         |          |            |           |           |            |            |           |
| Binary Tree        |         |          |            |           |           |            |            |           |
| Binary Search Tree |         | O(N) *5  |  O(N) *5   |           |  O(N) *5  |            |            |           |
| Min Heap           |         | O(N)     |  O(logN)   |           |           |            |  O(1)      |  O(logN)  |
| Max Heap           |         |          |            |           |           |            |            |           |


4. The insertion operation takes O(1) but finding the index at which we want to insert takes O(N)
5. In the worst case, BST is a linked list! and will number of nodes = number of levels = N.
