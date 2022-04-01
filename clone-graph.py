class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

def clone(node):

    output = {}

    def dfs(node):
        if node in output:
            return output[node]

        output[node] = Node(val=node.val)
        for nei in node.neighbors:
            output[node].neighbors.append(dfs(nei))

        return output[node]

    return dfs(node) if node else None