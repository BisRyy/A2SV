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
        
        d = {}
        
        for e in em:
            d[e.id] = [e.importance, e.subordinates]
        
        ans = 0
        
        def dfs(id):
            nonlocal ans
            ans += d[id][0]
            if len(d[id][1]) == 0:
                return
            
            for i in d[id][1]:
                dfs(i)
                
            
        dfs(id)
        return ans
    
    