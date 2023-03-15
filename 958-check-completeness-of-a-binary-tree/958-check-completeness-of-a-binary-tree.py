# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        last_level = 0 
        level = 0
        q = [(root,1)]
        while q:
            if len(q) != 2**level:
                last_level += 1
            if last_level > 1:
                return False
            new_level= []
            for node in q:
                if node[0].left:
                    new_level.append((node[0].left,2*node[1]-1))
                if node[0].right:
                    new_level.append((node[0].right,2*node[1]))
            if new_level:
                if new_level[0][1] != 1:
                    return False 
            for i in range(len(new_level)-1):
                if new_level[i+1][1] - new_level[i][1] != 1:
                    return False
            q = new_level
            level += 1
        return True 