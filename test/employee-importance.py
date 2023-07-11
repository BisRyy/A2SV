"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, em: List['Employee'], id: int) -> int:
        
        d = {e.id : [e.importance, e.subordinates] for e in em}
        
        ans = 0
        
        def dfs(id):
            nonlocal ans
            ans += d[id][0]
            for i in d[id][1]:
                dfs(i)
                
        dfs(id)
        return ans
    
    