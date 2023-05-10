# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        def grandTotal(node):
            total = 0
            if node.left:
                if node.left.left:
                    total += node.left.left.val
                if node.left.right:
                    total += node.left.right.val
                    
            if node.right:
                if node.right.left:
                    total += node.right.left.val
                if node.right.right:
                    total += node.right.right.val
            return total

        def preorderTraversal(root, ans):
            if not root:
                return ans
            preorderTraversal(root.left, ans)
            if root.val % 2 == 0:
                ans.append(grandTotal(root))
            preorderTraversal(root.right, ans)
            
            return ans
        
        return sum(preorderTraversal(root, []))
    
    
    
    
    
    
    