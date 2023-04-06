class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        d = {}
        for l in edges:
            if l[0] in d:
                return l[0]
            else:
                d[l[0]]=1
                
            if l[1] in d:
                return l[1]
            else:
                d[l[1]]=1
        
        return 0