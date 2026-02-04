# Depth first search

DFS explores as far as possible along each branch before backtracking.

- A golden rule for DFS is to never visit the same node twice (to avoid infinite loops).
- DFS algorithm can be implemented either [recursively](#recursive-dfs) or [iteratively](#iterative-dfs).
  - Recursion uses call stack and if the graph is extremely deep, there is always a chance of "StackflowError".
  - Iterative approach is the best one.

- DFS algorithm can be used to solve:
  1. Path finding : "Source to target" or "Find all paths"
  1. Cycle detection
  1. Connected components (islands)
  1. Topological sort

<br>
<br>
<br>

## General template

<br>
<br>

### Recursive DFS

```py
def dfs_recursive(node, visited):
    # base case
    if node in visited:
        return

    # process the node and mark it visited
    print(node) #or any other op
    visited.add(node)

    # traverse neighbours; datastructure would mostly be in the form of matrix i.e. graph[node]
    for neighbour in datastructure:
        dfs_recursive(neighbour)
```

- A general template of recursive DFS algorithm would look like the above, this works for 90% of dfs approaches.
- The algorithm uses a set type of datastructure to keep track of visited nodes. The backtracking happens naturally because of recursion. Note that there is no use of stack!
- Time complexity : $O(n)$, where $n$ is the number of nodes as each node is visited only once.
- Space complexity : $O(n)$ because of the recursion stack.

<br>
<br>

### Iterative DFS

```py
def dfs_iterative(start_node, graph):
    visited = set()

    # Initialize stack with the starting point
    stack = [start_node]

    while stack:
        node = stack.pop()

        if node not in visited:
            # process the node and mark it visited
            print(node)
            visited.add(node)

            # Add neighbors to the stack, Reversing neighbors keeps the same order as recursive DFS
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
```

- A general template of iterative DFS algorithm would look like the above.
- The algorithm uses a set type of datastructure to keep track of visited nodes. The backtracking happens manually using a stack!
- Time complexity : $O(n)$, where $n$ is the number of nodes as each node is visited only once.
- Space complexity : $O(n)$ for the stack, example: A skewed graph (like a linked list)

<br>
<br>

## DFS on a 2d matrix

```py
def dfs(r, c, grid, visited):
    # Boundary and Base Cases
    if (r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or (r, c) in visited or grid[r][c] == "0"):
        return

    visited.add((r, c))

    # Standard 4-directional moves
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for dr, dc in directions:
        dfs(r + dr, c + dc, grid, visited)
```
