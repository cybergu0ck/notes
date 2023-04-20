class Node:
    """ This class will be used internally inside LinkedList class only """
    def __init__(self,data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()
    
    def append(self, newData):
        currHead = self.head
        if currHead.data is None:
            currHead.data = newData
        else:
            newNode = Node(newData) 
            while currHead.next is not None:
                currHead = currHead.next
            currHead.next = newNode
    
    def showList(self):
        linklist = []
        currHead = self.head
        while currHead is not None:
            linklist.append(currHead.data)
            currHead = currHead.next
        return linklist

    

myList = LinkedList()    #Notice how we donot create Node() externally
myList.append(1)
myList.append('seconf')
myList.append(3)
print(myList.showList())


