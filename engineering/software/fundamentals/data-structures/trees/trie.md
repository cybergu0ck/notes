[← Back to trees](./contents.md)

# Contents

- [Trie](#trie)
  - [Implementation](#implementation)
  - [Complexity](#complexity)

<br>
<br>
<br>




[← Back to trees](./contents.md)

# Trie

Trie is a specialized search tree data structure used to store and retrieve strings.

- Trie is also known as 'preffix tree' or 'digital tree'
- Trie is super useful for fast string storage and retrieval, preffix matching.

<br>
<br>
<br>

## Implementation

```py
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isEnd = False
```

```py
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for ch in word:
            cur = cur.children[ch]
        cur.isEnd = True

    def search(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.childre[ch]
        return cur.isEnd

    def startsWith(self, preffix):
        cur = self.root
        for ch in preffix:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return True
```

<br>
<br>
<br>

## Complexity

- The asymptotic worst-case time complexities for implementation of Trie.

  | Operation  | Time Complexity |
  | ---------- | --------------- |
  | Insert     | O(n)            |
  | Search     | O(n)            |
  | StartsWith | O(n)            |
  - Here $n$ is the length of the word.

- The space complexity of the Trie datastructure is $O(w*l)$, where $w$ is the number of words and $l$ is the average length of the word.
  - The number of TrieNodes determines the space complexity. In the worst case, a TrieNode is required for all the letters of all the words.
