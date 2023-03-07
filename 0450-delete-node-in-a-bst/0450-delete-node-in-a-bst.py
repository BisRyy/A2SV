# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def minValueNode(node):
            current = node
            while(current.right):
                current = current.right
            return current
        
        if not root:
            return root
        
        if root.val == key:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            root.val = minValueNode(root.left).val
            root.left = self.deleteNode(root.left, root.val)

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        
        return root
    
    
    