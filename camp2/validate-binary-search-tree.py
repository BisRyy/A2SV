# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def traverse(root):
            if not root:
                return []
            ans = traverse(root.left)
            ans.append(root.val)
            ans += traverse(root.right)
            return ans
        return traverse(root) == sorted(traverse(root)) == sorted(list(set(traverse(root))))
        
        