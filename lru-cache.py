

class LRUNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.cache =  {}
        self.left = LRUNode(None, None)
        self.right = LRUNode(None, None)

        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node: LRUNode):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def insert(self, node: LRUNode):
        prev, right = self.right.prev, self.right

        prev.next = right.prev = node

        node.next, node.prev = right, prev 


    def get(self, key):

        if key in self.cache:
            node: LRUNode = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key, val):
        if key in self.cache:
            node: LRUNode = self.cache[key]
            self.remove(node)

        node = LRUNode(key, val)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key] 

 

cache = LRUCache(2)

cache.put(2,1)
cache.put(1,1)
cache.put(2,3)
cache.put(4,1)
print(cache.get(1))
print(cache.get(2))