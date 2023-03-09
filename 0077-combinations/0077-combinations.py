class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def combine(s,k,c):
            if k == 0:
                r.append(c)
            
            for i in range(s,n+1):
                combine(i+1, k-1, c+[i])
                
        r = []
        combine(1,k,[])
        return r