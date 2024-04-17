# Singly Linked List

_A singly linked list is a linear data structure consisting of a sequence of elements called nodes._

- Uses of Singly Linked Lists are as follows:
  - Insertion and Deletion at the begining of the list is O(1).
  - They are memory efficient as they don't need contigous memory like arrays.

<br>
<br>

## Complexity

| Operation | Time Complexity |
| --------- | --------------- |
| Insertion | O(n)            |
| Deletion  | O(n)            |
| Search    | O(n)            |

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
