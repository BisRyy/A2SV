# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        d = defaultdict(int)
        
        def preorderTraversal(root):
            if not root:
                return

            d[root.val]+=1
            preorderTraversal(root.left)
            preorderTraversal(root.right)
            
            return
        preorderTraversal(root)
        top = 0
        ans = []
        for i in d:
            if d[i] > top:
                ans = [i]
                top = d[i]
            elif d[i] == top:
                ans.append(i)
        return ans
        