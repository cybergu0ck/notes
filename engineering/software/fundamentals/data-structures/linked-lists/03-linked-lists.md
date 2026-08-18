# Singly Linked List

_A linked list is a data structure consisting of nodes where each node contains a value and a reference (or link) to the next node in the sequence._

- Singly linked list are used because of it's advantages:
  - Insertion and Deletion at the begining of the list is O(1).
  - They are memory efficient as they don't need contigous memory like arrays.

<br>
<br>

## Complexity

The asymptotic worst-case complexities are considered here.

| Operation | Time Complexity |Space Complexity |
| --------- | --------------- |---------------- |
| Search    | O(n)            |                 |
| Insertion | O(n)            |                 |
| Deletion  | O(n)            |                 |

<br>
<br>

## Implementation

```py
class Node:
    def __init__(self, value = None, next = None):
        self.val = value
        self.next = next

class LinkedList:
    def __init__(self, root = Node()):
        self.root = root

    def printList(self):
        cur = self.root
        res = []
        while cur:
            res.append(cur.val)
            cur = cur.next
        print(res)

    def appendNode(self, node):
        cur = self.root
        while cur.next:
            cur = cur.next
        cur.next = node

    def removeNode(self, node):
        cur = self.root
        if cur == node:
            self.root = node.next
        while cur:
            if(cur.next == node):
                cur.next = node.next
            cur = cur.next

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
ll = LinkedList(n1)
ll.appendNode(n2)
ll.appendNode(n3)
ll.appendNode(n4)
ll.removeNode(n3)
ll.printList()
```

<br>
<br>

## The Runner Technique

This technique uses two pointers, often called as "fast" and "slow" pointers to accomplish many applications in linked lists.

* Finding the middle node in a linked list