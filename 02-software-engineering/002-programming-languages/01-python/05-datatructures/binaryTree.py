class Node:
    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = Node()

    def insert(self, newData):
        if self.root.data is None:
            self.root.data = newData
        else:
            self._insert(newData,self.root)
    
    def _insert(self,newData, currRoot):
        if newData < currRoot.data:
            if currRoot.left is None:
                currRoot.left = Node(newData)
            else:
                self._insert(newData,currRoot.left)
    
        elif newData > currRoot.data:
            if currRoot.right is None:
                currRoot.right = Node(newData)
            else:
                self._insert(newData,currRoot.right)

        """ else:
            currRoot.data = newData """           #This is the case for newData == currRoot.data
        
    def printTree(self):
        self._printTree(self.root)
        print('None')

    def _printTree(self,currRoot):
        if currRoot.left:
            self._printTree(currRoot.left)
        print(currRoot.data, end = ' --> ')
        if currRoot.right:
            self._printTree(currRoot.right)
    
    
    """ def inOrder(self):
        trav = self._inOrder(self.root)
        print(trav)
        return trav

    def _inOrder(self, currRoot):
        _trav = []
        if currRoot.left:
            _trav.extend(self._inOrder(currRoot.left))

        _trav.append(self.root.data)

        if currRoot.right:
            _trav.extend(self._inOrder(currRoot.right))
        return _trav """
    


myTree = Tree()
myTree.insert(10)
myTree.insert(9)
myTree.insert(18)
myTree.insert(12)
myTree.insert(17)
myTree.printTree()
