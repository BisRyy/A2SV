# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def maxDepth(root):
            if not root:
                return 0    
            return max(maxDepth(root.left), maxDepth(root.right)) + 1
        depth = maxDepth(root)
        
        def goRight(root, level):
            if not root:
                return
            if level == 0:
                return root.val
            
            ans = goRight(root.right, level-1)
            if ans != None :
                return ans
            else:
                return goRight(root.left, level-1)
                    
        ans = []
        
        for i in range(depth):
            
            ans.append(goRight(root, i))
            
        return ans