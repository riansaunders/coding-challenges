class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def has_path(root, targ):

    res =[]
    def dfs(root, cs):
        if not root:
            return
        cs.append(root.val)

        if sum(cs) == targ and not root.left and not root.right:
            res.append(cs.copy())
        else:
            dfs(root.left, cs)
            dfs(root.right, cs) 
        cs.pop()

    dfs(root, [])
    
    return res

def main():

  root = TreeNode(1)
  root.left = TreeNode(7)
  root.right = TreeNode(9)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)
  root.right.left = TreeNode(2)
  root.right.right = TreeNode(7)
  print("Tree has path: ", has_path(root, 12))
  print("Tree has path: ", has_path(root,17))


main()
