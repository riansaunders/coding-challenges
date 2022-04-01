class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def count_paths(root, S):
 
	def dfs(root, ts): 
		if not root:
			return 0 

		res = 1 if root.val == ts else 0
		res += dfs(root.left, ts - root.val) + dfs(root.right, ts - root.val) 
		return res

	return dfs(root, S) + dfs(root.left, S) + dfs(root.right, S)

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has paths: " + str(count_paths(root, 11)))


main()