# Implementation

In the below implementation Node.nodes will have all the instances of the Node. i.e. list of all nodes that are created.

```python
class Node:
    nodes = []
    def __init__(self, val = 0, neighbours = None):
        self.val = val
        self.neighbours = neighbours if neighbours is not None else []
        self.nodes.append(self)
```


- Graphs can be created using Node objects, dict objects representing directed graphs or list objects representing un-directed graphs. 

- The following implementation requires `get_directed_graph` method in case of undirected graphs are used for instantiation.

```python
class Graph:
    def __init__(self, nodes = Node.nodes):
        if nodes == None:
            nodes = Node.nodes
            self.directed_graph = {}
            for node in nodes:
                self.directed_graph[node.val] = node.neighbours
                
        elif type(nodes) == dict:
            #means a directed graph
            self.directed_graph = nodes

        elif type(nodes) == list:
            #means an undirected graph, got to convert to a directed graph.
            self.undirected_graph = nodes
            self.directed_graph = self.get_directed_graph(nodes)



    def get_directed_graph(self, undirected_graph):
        from collections import defaultdict             #this is convinient.

        directed_graph = defaultdict(list)

        for i in undirected_graph:
            directed_graph[i[0]].append(i[1])
            directed_graph[i[1]].append(i[0])
        
        return directed_graph
```

<br/>

## 1.Instantiating from `Node` objects:

```python

# Create nodes with values and it's neighbors, if any.
node1 = Node(3)
node2 = Node(4, [6])
node3 = Node(6, [4,5,7,8])
node4 = Node(8, [6])
node5 = Node(7, [6])
node6 = Node(5, [6])
node7 = Node(1, [2])
node8 = Node(2, [1])

#Instantiate Graph with zero arguments!
my_graph = Graph()

print(my_graph.directed_graph)

#> {3: [], 4: [6], 6: [4, 5, 7, 8], 8: [6], 7: [6], 5: [6], 1: [2], 2: [1]}
```

The output directed graph is as shown below :
```
{
    3: [],
    4: [6],
    6: [4, 5, 7, 8],
    8: [6],
    7: [6],
    5: [6],
    1: [2],
    2: [1],
}

```

<br/>

## 2.Instantiating from dict objects that represent directed graphs:

```python
graph = {
    3 : [],
    4 : [6],
    6 : [4,5,7,8],
    8 : [6],
    7 : [6],
    5 : [6],
    1 : [2],
    2 : [1] 
}


#Instantiate Graph with dict object as a parameter
my_graph = Graph(graph)

print(my_graph.directed_graph)

#> {3: [], 4: [6], 6: [4, 5, 7, 8], 8: [6], 7: [6], 5: [6], 1: [2], 2: [1]}
```

<br/>

## 3.Instantiating from list objects that represent un-directed graphs:

```python
undirected_graph = [ ['i', 'j'], ['k', 'i'], ['m', 'k'], ['k','l'],['o','n']]

#Instantiate Graph with list object as a parameter
my_graph = Graph(undirected_graph)

print(my_graph.directed_graph)

#>defaultdict(<class 'list'>, {'i': ['j', 'k'], 'j': ['i'], 'k': ['i', 'm', 'l'], 'm': ['k'], 'l': ['k'], 'o': ['n'], 'n': ['o']})
```

<br/>
<br/>

# Traversals

Consider the following graphs, `graph1` contains no cycles but `graph2` contains cycles!

```python
graph1 = {
         'a' : ['b', 'c'],
         'b' : ['d'],
         'c' : ['e','g'],
         'd' : ['f'],
         'e' : [],
         'f' : [],
         'g' : []
}

graph2 = {
    4 : [6],
    6 : [4,5,7,8],
    8 : [6],
    7 : [6],
    5 : [6],
    1 : [2],
    2 : [1],
    3 : [],
}


graph_with_no_cycle = Graph(graph1)
graph_with_cycle = Graph(graph2)
```

<br/>


## Breadth First Search

> Add BFS image!


- BFS uses Queues.
- BFS cannot be implemented recursively (I Think)

```python
#This is a method of class Graph

def breadth_first_search(self, source):
        res = []
        q = [source]
        visited = set()             #sets are memory efficient, look up is O(1)

        while q:
            cur = q.pop()           # items are removed from last!

            while cur in visited:   #This while block takes care of cycles, if present in the graph!
                if q:
                    cur = q.pop()
                else:
                    break
            else:                   #the code in this else block is executed if the break in above while is not hit! 
                visited.add(cur)
                res.append(cur)
                if self.directed_graph[cur] :
                    for node in self.directed_graph[cur]:
                        q.insert(0,node)           #items are added from first!
        
        return res
```

```python
print(graph_with_no_cycle.breadth_first_search('a'))
print(graph_with_cycle.breadth_first_search(4))

#>['a', 'b', 'c', 'd', 'e', 'g', 'f']
#>[4, 6, 5, 7, 8]
```
<br/>

## Depth First Search 

> Add DFS image

- DFS uses stacks.
- DFS can be implemented iteratively and recursively.

```python
# Iterative

def depth_first_search(self, source):
        res = []
        stack = [source]
        visited = set()  
        
        while stack:
            cur = stack.pop()       # Remove item from the back of the stack!
            
            while cur in visited:   #This while block takes care of cycles, if present in the graph!
                if stack:
                    cur = stack.pop()
                else:
                    break
            else:
                visited.add(cur)
                res.append(cur)
                if self.directed_graph[cur]:
                    for node in self.directed_graph[cur]:
                        stack.append(node)          # Adding item to the back of the stack!
        return res
```

```python
print(graph_with_no_cycle.depth_first_search('a'))
print(graph_with_cycle.depth_first_search(4))

#>['a', 'c', 'g', 'e', 'b', 'd', 'f']
#>[4, 6, 8, 7, 5]
```

<br/>

```python
#recursive
#not written for graphs with cycles! can work on this method!
res = []
def recursivedepthfirstsearch(graph, source):
    res.append(source)

    for i in graph[source]:
        recursivedepthfirstsearch(graph, i)
    
    return res
```


<br/>
<br/>


# `has_path` function


- BFS or DFS can be used, I prefer BFS!!
- Better to avoid recursive implementations as it will complicate coding up for cyclic graphs!

```python
# this is a method of class Graph

def has_path(self, source, destination):
        #Using BFS
        q = [source]
        visited = set()
        while q:
            cur = q.pop()

            if cur == destination:
                return True
            else:
                for node in self.directed_graph[cur]:
                    if node not in visited:
                        visited.add(node)
                        q.insert(0, node)
        return False
```

```python
print(graph_with_cycle.has_path(1,2))
print(graph_with_cycle.has_path(1,1))
print(graph_with_cycle.has_path(4,8))
print(graph_with_cycle.has_path(4,1))

#>True
#>True
#>True
#>False
```

<br/>
<br/>

# Finding number of connected components in a graph

```python
# this is a method of class Graph

def number_of_components(self):
        components = 0
        visited = set()

        for node in self.directed_graph:
            if node not in visited:
                res = self.breadth_first_search(node)
                for item in res:
                    if item not in visited:
                        visited.add(item)
                components += 1
               
            elif node in visited:
                continue
        
        return components
```

```python
print(graph_with_cycle.number_of_components())

#>3
```

<br/>
<br/>

# Finding the longest connected component in the graph


```python
# this is a method of class Graph

# type = None or 'length' returns int
# type = 'subtree' returns the list of longest_component

def longest_component(self, type = None):
        components = 0
        max_len = 0
        max_subtree = []
        visited = set()

        for node in self.directed_graph:
            if node not in visited:
                res = self.breadth_first_search(node)
                for item in res:
                    if item not in visited:
                        visited.add(item)
                components += 1
                max_len = max(max_len, len(res))
                if max_len == len(res):
                    max_subtree = res
            elif node in visited:
                continue
        
        if type == None or type == 'length':
            #return max_len by default
            return max_len

        elif type == 'subtree':
            return max_subtree
```

```python
print(graph_with_cycle.longest_component())
print(graph_with_cycle.longest_component('subtree'))

#>5
#>[4, 6, 5, 7, 8]

```
