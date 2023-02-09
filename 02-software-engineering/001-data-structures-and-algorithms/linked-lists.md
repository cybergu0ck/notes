

```python
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.root = Node()
```

<br/>

## Appending

```python
def append(self, new_data):
        cur_node = self.root
        new_node = Node(new_data)

        if cur_node.data == None:
            self.root = new_node
            cur_node = self.root
        
        else:
            while(cur_node):
                if cur_node.next != None:
                    cur_node = cur_node.next
                else:
                    cur_node.next = new_node
                    break
```

<br/>

## Show the linked list

```python
def show(self):
        cur_node = self.root
        res = []
        while cur_node:
            if cur_node.next != None:
                res.append(cur_node.data)
                cur_node = cur_node.next
            else:
                res.append(cur_node.data)
                break
        return res
```

<br/>

## Inserting

```python
def insert(self, new_data, index):
        cur_node = self.root
        cur_index = 0
        new_node = Node(new_data)

        if cur_index == index:
            #inserting as first node in the list
            self.root = new_node
            self.root.next = cur_node

        else:
            while cur_index < index-1:
                if cur_node.next != None:
                    cur_node = cur_node.next
                    cur_index += 1
                else:
                    print("error")
                    break

            temp = cur_node.next
            cur_node.next = new_node
            new_node.next = temp

```

<br/>

## Poping

```python
def pop(self):
        cur_node = self.root
        prev_node = None

        while cur_node.next:
            prev_node = cur_node
            cur_node = cur_node.next

        prev_node.next = None
```

<br/>

## remove

```python
def remove(self, index):
        cur_node = self.root
        prev_node = None
        cur_index = 0

        if cur_index == index:
            if cur_node.next:
                self.root = cur_node.next
                cur_node = self.root
            else:
                print("error")
        else:
            while cur_index != index:
                if cur_node:
                    prev_node = cur_node
                    cur_node = cur_node.next
                    cur_index += 1
                else:
                    print("error")
                    break
            temp = cur_node.next
            prev_node.next = temp
```