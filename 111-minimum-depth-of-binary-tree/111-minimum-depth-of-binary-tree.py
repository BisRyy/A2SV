# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        ans = float('inf')
        def dfs(root, count=1):
            nonlocal ans
            if root.left == root.right == None:
                ans = min(ans, count)
                return 
            if root.left:
                dfs(root.left, count+1)
            if root.right:
                dfs(root.right, count+1)
        if root:
            dfs(root)
        else:
            return 0
        return ans