# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        
        def dfs(root):
            if not root:
                return 0
            nonlocal diameter
            leftDiameter = dfs(root.left)
            rightDiameter = dfs(root.right)

            diameter = max(leftDiameter + rightDiameter, diameter)
            
            return 1 + max(leftDiameter, rightDiameter)
        
        dfs(root)
        return diameter