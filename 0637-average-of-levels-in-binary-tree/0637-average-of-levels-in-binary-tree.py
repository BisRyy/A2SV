# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        q = deque([root])
        s = set([root])
        
#         def bfs(root):
        
#             q.append(root.left)
#             q.append(root.right)
        ans = [root.val/1]
        while q:
            total = 0
            for i in range(len(q)):
                poped = q.popleft()

                if poped.left:
                    q.append(poped.left)
                    total += poped.left.val
                if poped.right:
                    q.append(poped.right)
                    total += poped.right.val
            if q:
                ans.append(total / len(q))
            
        return ans