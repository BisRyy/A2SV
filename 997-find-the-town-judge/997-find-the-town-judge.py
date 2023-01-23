class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        t = defaultdict(set)
        s = [0]*(n+1)
        a = []
        
        if len(t)==0 and n == 1:
            return 1
        for i in trust:
            t[i[1]].add(i[0])
            s[i[0]]+=1
            
        for j in t:
            if len(t[j]) == n-1 and s[j]==0:
                a.append(j)
                
        if len(a)== 1 and len(t[a[0]]) == n-1 and s[a[0]]==0:
            return a[0]
        
        
        return -1