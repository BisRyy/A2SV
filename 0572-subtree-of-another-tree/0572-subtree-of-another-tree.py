# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return root
        
        def check(root1, root2):
            if not root1 and not root2:
                return True
                
            if (not root1 and root2) or (root1 and not root2):
                return False
            
            if root1.val != root2.val:
                return False
                
            return check(root1.left, root2.left) and check(root1.right, root2.right)

        def preorderTraversal(root, ans):
            if not root:
                return ans
            
            preorderTraversal(root.left, ans)

            if root.val == subRoot.val:
                ans.append(check(root, subRoot))

            preorderTraversal(root.right, ans)
            
        ans = []

        preorderTraversal(root, ans)
    
        return True if True in ans else False
            
            
        
