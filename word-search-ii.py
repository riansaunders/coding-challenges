class TrieNode():
    def __init__(self):
        self.characters = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.characters:
                cur.characters[c] = TrieNode()
            cur = cur.characters[c]
        cur.isEnd = True
        return cur 

def ws2(board ,words):
    rows, cols = len(board), len(board[0])
    path = set()
    res = set()
    trie = Trie()
    for w in words:
        trie.insert(w)

    def dfs(row, col, trie, word):
        if row < 0 or col < 0 or row >= rows or col >= cols:
            return
        if (row, col) in path:
            return
        if board[row][col] not in trie.characters:
            return
        letter = board[row][col]
        node = trie.characters[letter]
        if node.isEnd:
            res.add(word + letter)
            return

        path.add((row, col))
        dfs(row + 1, col, node, word + letter)
        dfs(row - 1, col, node, word + letter)
        dfs(row, col + 1, node, word + letter)
        dfs(row, col - 1, node, word + letter)
        path.remove((row, col))
        
    for r in range(rows):
        for c in range(cols):
                dfs(r, c, trie.root, "")

    return list(res)
   
print(ws2([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath", "pea", "eat", "rain"]))