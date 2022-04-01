class TrieNode():
    def __init__(self) -> None:
        self.characters = {}
        self.isEnd = False



class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if not c in node.characters:
                node.characters[c] = TrieNode()
            node = node.characters[c]

        node.isEnd = True

    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
            if c in node.characters:
                node = node.characters[c]
            else:
                return False
        return True

    def search(self, word):
        node = self.root
        for c in word:
            if c in node.characters:
                node = node.characters[c]
            else:
                return False
        return node.isEnd

trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))