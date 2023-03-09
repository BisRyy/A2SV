# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def maxDepth(root):
            if not root:
                return 0    
            return max(maxDepth(root.left), maxDepth(root.right)) + 1
        
        
        def getThem(root, n):
            if not root:
                return root
            if n == 0:
                res.append(root.val)
            
            getThem(root.left, n-1)
            getThem(root.right, n-1)
        
        
        depth = maxDepth(root)
        
        ans = []
        
        for i in range(depth):
            res = []
            getThem(root, i)
            ans.append(res)
        
        return ans