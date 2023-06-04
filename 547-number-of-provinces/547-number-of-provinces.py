class Solution:
    def findCircleNum(self, c: List[List[int]]) -> int:
        
        d = {}
        n = len(c)
        ans = list(range(n))
        for i in range(n):
            d[i] = [False, []]
            for j in range(n):
                if c[i][j] ==1 and i != j:
                    d[i][1].append(j)
        ans = 0
        def dfs(i):
            nonlocal ans
            if not d[i][0]:
                d[i][0] = True
                for j in d[i][1]:
                    dfs(j)
        for i in d:
            if not d[i][0]:
                dfs(i)
                ans += 1
            
        return ans
        