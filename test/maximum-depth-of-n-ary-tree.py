"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        ans = 1
        
        for child in root.children:
            ans = max(self.maxDepth(child) + 1, ans)
            
        return ans