
class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def find_path(root, seq):
	def dfs(root, i):
		if i == len(seq):
			return False
		if not root or seq[i] != root.val:
			return len(seq) == 0
		if not root.left and not root.right and i == len(seq) - 1:
			return True
		return dfs(root.left, i +1) or dfs(root.right, i +1)

	return dfs(root, 0)

def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()