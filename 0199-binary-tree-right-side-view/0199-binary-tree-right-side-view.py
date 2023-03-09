# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        result=[]
        
        def func(root,level):
            if root is None:
                return 
            if len(result)==level:
                result.append(root.val)
            func(root.right,level+1)
            func(root.left,level+1)

        
        func(root,0)
        
        return result