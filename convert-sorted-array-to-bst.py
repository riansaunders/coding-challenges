class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def convert(nums):

    if not nums:
        return None

    pivot = len(nums)//2 
    head = TreeNode(val=nums[pivot])

    head.left = convert(nums[:pivot])
    head.right = convert(nums[pivot + 1:])
    return head
    
print(convert([-10,-3,0,5,9]).val)