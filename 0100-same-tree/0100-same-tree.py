# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def isSameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        if (not root1 and root2) or (not root2 and root1): return False
        if not root2 and not root1:  return True
        if root2 and root1:
            if root1.val == root2.val:
                if self.isSameTree(root1.left, root2.left):
                    if self.isSameTree(root1.right, root2.right):
                        return True
        return False